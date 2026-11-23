"""Torch-free query encoder for bge-small-en-v1.5, used by the deployed API.

The index was built with sentence-transformers (PyTorch). At serving time only the query needs
embedding, so the API runs BAAI's official ONNX export of the same model with onnxruntime:
CLS pooling + L2 normalisation, exactly as the model's sentence-transformers config says.
tests/test_onnx_parity.py checks both encoders give the same vectors and the same rankings.

Model files: scripts/fetch_onnx.py downloads them (pinned revision) into ONNX_DIR.
"""
from __future__ import annotations

import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ONNX_DIR = Path(os.getenv("ONNX_DIR", ROOT / ".cache" / "bge-onnx"))
MAX_LEN = 512


class OnnxEncoder:
    def __init__(self, model_dir: Path = ONNX_DIR):
        import onnxruntime as ort
        from tokenizers import Tokenizer

        self.tok = Tokenizer.from_file(str(model_dir / "tokenizer.json"))
        self.tok.enable_truncation(MAX_LEN)
        self.tok.enable_padding()
        opts = ort.SessionOptions()
        opts.intra_op_num_threads = int(os.getenv("ORT_THREADS", "1"))  # small free hosts: 1 vCPU
        self.sess = ort.InferenceSession(str(model_dir / "model.onnx"), opts, providers=["CPUExecutionProvider"])
        self.inputs = {i.name for i in self.sess.get_inputs()}

    def encode(self, texts: list[str], normalize_embeddings: bool = True, **_) -> np.ndarray:
        enc = self.tok.encode_batch(texts)
        feed = {
            "input_ids": np.array([e.ids for e in enc], dtype=np.int64),
            "attention_mask": np.array([e.attention_mask for e in enc], dtype=np.int64),
            "token_type_ids": np.array([e.type_ids for e in enc], dtype=np.int64),
        }
        hidden = self.sess.run(None, {k: v for k, v in feed.items() if k in self.inputs})[0]
        emb = hidden[:, 0]  # CLS token
        if normalize_embeddings:
            emb = emb / np.linalg.norm(emb, axis=1, keepdims=True)
        return emb.astype(np.float32)

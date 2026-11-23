"""The deployed API embeds queries with ONNX; the index and all reported results used
sentence-transformers. This checks the two give the same vectors and the same top-8 rankings
on all 76 evaluation questions. Needs both backends installed (skipped in the slim CI job)."""
import json
import os

import numpy as np
import pytest

from retrieve import ROOT, Retriever

pytest.importorskip("sentence_transformers")
pytest.importorskip("onnxruntime")
from onnx_embed import ONNX_DIR, OnnxEncoder  # noqa: E402

if not (ONNX_DIR / "model.onnx").exists():
    pytest.skip("ONNX model not downloaded (python scripts/fetch_onnx.py)", allow_module_level=True)

QUESTIONS = [json.loads(l)["question"] for l in (ROOT / "eval" / "questions.jsonl").open(encoding="utf-8")]


@pytest.fixture(scope="module")
def pair():
    os.environ.pop("EMBED_BACKEND", None)
    st = Retriever()
    ox = Retriever()
    ox.__dict__["model"] = OnnxEncoder()  # same index, other query encoder
    return st, ox


def test_same_vectors(pair):
    st, ox = pair
    q = [st.query_prefix + x for x in QUESTIONS]
    a = st.model.encode(q, normalize_embeddings=True)
    b = ox.model.encode(q, normalize_embeddings=True)
    cos = (a * b).sum(axis=1)
    assert cos.min() > 0.9999, cos.min()


def test_same_rankings(pair):
    st, ox = pair
    for q in QUESTIONS:
        assert st.rank_dense(q, 8) == ox.rank_dense(q, 8), q


def test_passages_match_index(pair):
    """ONNX also reproduces the stored passage vectors (same model, not just same queries)."""
    st, ox = pair
    from retrieve import passage_text
    idx = list(range(0, len(st.chunks), 97))
    b = ox.model.encode([passage_text(st.chunks[i]) for i in idx], normalize_embeddings=True)
    cos = (st.embeddings[idx] * b).sum(axis=1)
    assert cos.min() > 0.999, cos.min()

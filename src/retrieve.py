"""Retrieval over the AI Act + GDPR chunks.

Modes (so the evaluation can compare them on the same questions):
  - "bm25"     : keyword search (rank-bm25)
  - "dense"    : sentence embeddings + cosine similarity
  - "hybrid"   : reciprocal rank fusion (RRF) of bm25 and dense
  - "weighted" : weighted fusion of min-max normalised bm25 and dense scores (alpha = dense weight)
  - "rerank"   : dense top-N candidates re-scored by a cross-encoder

Knobs (constructor arguments, all evaluated on the dev split):
  embed_model     : any sentence-transformers model; each gets its own index directory
  recital_penalty : subtracted from the dense cosine of recital chunks, so binding articles
                    win ties against the recitals that explain them
  reranker        : cross-encoder model name used by "rerank"

Build an embedding index once per model:  python src/retrieve.py --build [--embed MODEL]
Try a query:                              python src/retrieve.py "Is emotion recognition at work allowed?"
"""
from __future__ import annotations

import argparse
import json
import re
from functools import cached_property
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "data" / "processed" / "chunks.jsonl"
INDEX = ROOT / "data" / "index"

EMBED_MODEL = "BAAI/bge-small-en-v1.5"
RERANK_MODEL = "BAAI/bge-reranker-base"
BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
RRF_K = 60  # standard RRF constant
# Chosen on the dev split (eval/experiments.py): 0.05 is the smallest value on the plateau
# (R@5 72% -> 83%), kept small so recitals can still surface when they are the best match.
RECITAL_PENALTY = 0.05
KEEP_ORIGINAL = 4  # with rewrites: top results of the plain question that are always kept
MODES = ("bm25", "dense", "hybrid", "weighted", "rerank")

TOKEN = re.compile(r"[a-z0-9]+")
STOP = set("the a an of to in and or for on by with is are be as that this which at from "
           "shall may any its their such other where".split())


def tokenize(text: str) -> list[str]:
    return [t for t in TOKEN.findall(text.lower()) if t not in STOP]


def passage_text(c: dict) -> str:
    """What gets indexed: citation + chapter + body, so headings help both retrievers."""
    return f"{c['heading']}. {c['chapter']}. {c['text']}"


def minmax(x: np.ndarray) -> np.ndarray:
    span = x.max() - x.min()
    return (x - x.min()) / span if span > 0 else np.zeros_like(x)


class Retriever:
    def __init__(self, chunks_path: Path = CHUNKS, index_root: Path = INDEX,
                 embed_model: str = EMBED_MODEL, recital_penalty: float = RECITAL_PENALTY,
                 reranker: str = RERANK_MODEL, rerank_depth: int = 30, alpha: float = 0.7,
                 rerank_recital_penalty: float = 0.0):
        self.chunks = [json.loads(l) for l in chunks_path.open(encoding="utf-8")]
        self.embed_model = embed_model
        self.index_dir = index_root / embed_model.split("/")[-1]
        self.recital_penalty = recital_penalty
        self.reranker_name = reranker
        self.rerank_depth = rerank_depth
        self.alpha = alpha
        self.rerank_recital_penalty = rerank_recital_penalty
        self.keep_original = KEEP_ORIGINAL
        self.bm25 = BM25Okapi([tokenize(passage_text(c)) for c in self.chunks])
        self.is_recital = np.array([c["kind"] == "recital" for c in self.chunks])

    @cached_property
    def model(self):
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(self.embed_model)

    @cached_property
    def cross_encoder(self):
        from sentence_transformers import CrossEncoder
        return CrossEncoder(self.reranker_name)

    @property
    def query_prefix(self) -> str:
        return BGE_QUERY_PREFIX if "bge-" in self.embed_model and "-en-" in self.embed_model else ""

    @cached_property
    def embeddings(self) -> np.ndarray:
        path = self.index_dir / "embeddings.npy"
        if not path.exists():
            raise FileNotFoundError(f"No index for {self.embed_model}: run "
                                    f"`python src/retrieve.py --build --embed {self.embed_model}`")
        ids = json.loads((self.index_dir / "ids.json").read_text(encoding="utf-8"))
        if ids != [c["id"] for c in self.chunks]:
            raise RuntimeError("Index is stale (chunks changed): rebuild with --build")
        return np.load(path)

    def build(self) -> None:
        self.index_dir.mkdir(parents=True, exist_ok=True)
        emb = self.model.encode([passage_text(c) for c in self.chunks], batch_size=32,
                                normalize_embeddings=True, show_progress_bar=True)
        np.save(self.index_dir / "embeddings.npy", emb.astype(np.float32))
        (self.index_dir / "ids.json").write_text(json.dumps([c["id"] for c in self.chunks]), encoding="utf-8")
        print(f"indexed {len(self.chunks)} chunks with {self.embed_model} -> {emb.shape}")

    # --- scores over all chunks -----------------------------------------------------------
    def bm25_scores(self, query: str) -> np.ndarray:
        return self.bm25.get_scores(tokenize(query))

    def dense_scores(self, query: str) -> np.ndarray:
        q = self.model.encode([self.query_prefix + query], normalize_embeddings=True)[0]
        return self.embeddings @ q - self.recital_penalty * self.is_recital

    # --- rankings: lists of chunk indices, best first -------------------------------------
    def rank_bm25(self, query: str, n: int) -> list[int]:
        return list(np.argsort(-self.bm25_scores(query))[:n])

    def rank_dense(self, query: str, n: int) -> list[int]:
        return list(np.argsort(-self.dense_scores(query))[:n])

    def rank_hybrid(self, query: str, n: int, depth: int = 50) -> list[int]:
        fused: dict[int, float] = {}
        for ranking in (self.rank_bm25(query, depth), self.rank_dense(query, depth)):
            for r, i in enumerate(ranking):
                fused[i] = fused.get(i, 0.0) + 1.0 / (RRF_K + r + 1)
        return sorted(fused, key=fused.get, reverse=True)[:n]

    def rank_weighted(self, query: str, n: int) -> list[int]:
        s = self.alpha * minmax(self.dense_scores(query)) + (1 - self.alpha) * minmax(self.bm25_scores(query))
        return list(np.argsort(-s)[:n])

    def rank_rerank(self, query: str, n: int) -> list[int]:
        cands = self.rank_dense(query, max(n, self.rerank_depth))
        scores = np.asarray(self.cross_encoder.predict([(query, passage_text(self.chunks[i])) for i in cands]))
        scores = scores - self.rerank_recital_penalty * self.is_recital[cands]
        return [cands[j] for j in np.argsort(-scores)[:n]]

    def rank_multi(self, queries: list[str], n: int, depth: int = 50) -> list[int]:
        """RRF over dense rankings of several phrasings (original question + LLM rewrites)."""
        fused: dict[int, float] = {}
        for q in queries:
            for r, i in enumerate(self.rank_dense(q, depth)):
                fused[i] = fused.get(i, 0.0) + 1.0 / (RRF_K + r + 1)
        return sorted(fused, key=fused.get, reverse=True)[:n]

    def search(self, query: str, k: int = 5, mode: str = "dense", rewrites: list[str] | None = None) -> list[dict]:
        if rewrites:
            # The original question's top `keep` results are always kept, so a bad rewrite can
            # only add candidates, never push out what the plain question found.
            keep = self.rank_dense(query, min(self.keep_original, k))
            fused = [i for i in self.rank_multi([query, *rewrites], 2 * k) if i not in keep]
            return [self.chunks[i] for i in (keep + fused)[:k]]
        rank = getattr(self, f"rank_{mode}")
        return [self.chunks[i] for i in rank(query, k)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--embed", default=EMBED_MODEL)
    ap.add_argument("--mode", default="dense", choices=MODES)
    ap.add_argument("-k", type=int, default=5)
    args = ap.parse_args()
    r = Retriever(embed_model=args.embed)
    if args.build:
        r.build()
    if args.query:
        for c in r.search(args.query, args.k, args.mode):
            print(f"- {c['heading']}\n  {c['text'][:160]}...")


if __name__ == "__main__":
    main()

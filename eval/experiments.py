"""Retrieval experiments on the DEV split only (the test split stays untouched until the end).

Each config = (name, mode, Retriever kwargs). Results are appended to eval/results/experiments.jsonl
so the README can show the full ablation history, not just the winner.

python eval/experiments.py                 # run every config
python eval/experiments.py penalty rerank  # only configs whose name contains one of these words
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "eval"))
from eval_retrieval import KS, evaluate, load_questions, validate  # noqa: E402
from retrieve import Retriever  # noqa: E402

SMALL, BASE = "BAAI/bge-small-en-v1.5", "BAAI/bge-base-en-v1.5"
CONFIGS = [
    ("dense-small (baseline)", "dense", dict(embed_model=SMALL)),
    ("dense-small penalty=0.01", "dense", dict(embed_model=SMALL, recital_penalty=0.01)),
    ("dense-small penalty=0.02", "dense", dict(embed_model=SMALL, recital_penalty=0.02)),
    ("dense-small penalty=0.03", "dense", dict(embed_model=SMALL, recital_penalty=0.03)),
    ("dense-small penalty=0.05", "dense", dict(embed_model=SMALL, recital_penalty=0.05)),
    ("dense-small penalty=0.07", "dense", dict(embed_model=SMALL, recital_penalty=0.07)),
    ("dense-small penalty=0.10", "dense", dict(embed_model=SMALL, recital_penalty=0.10)),
    ("weighted-small alpha=0.8", "weighted", dict(embed_model=SMALL, alpha=0.8)),
    ("weighted-small alpha=0.9", "weighted", dict(embed_model=SMALL, alpha=0.9)),
    ("dense-base", "dense", dict(embed_model=BASE)),
    ("dense-base penalty=0.03", "dense", dict(embed_model=BASE, recital_penalty=0.03)),
    ("dense-base penalty=0.05", "dense", dict(embed_model=BASE, recital_penalty=0.05)),
    ("dense-base penalty=0.07", "dense", dict(embed_model=BASE, recital_penalty=0.07)),
    ("dense-base penalty=0.10", "dense", dict(embed_model=BASE, recital_penalty=0.10)),
    ("rerank-small", "rerank", dict(embed_model=SMALL)),
    ("rerank-base", "rerank", dict(embed_model=BASE)),
    ("rerank-base penalty=0.05+0.2", "rerank", dict(embed_model=BASE, recital_penalty=0.05, rerank_recital_penalty=0.2)),
]
OUT = ROOT / "eval" / "results" / "experiments.jsonl"


def main() -> None:
    words = sys.argv[1:]
    configs = [c for c in CONFIGS if not words or any(w in c[0] for w in words)]
    qs = load_questions()
    dev = [q for q in qs if q["gold"] and q["split"] == "dev"]
    retrievers: dict[str, Retriever] = {}  # one per embedding model; knobs are reset per config
    defaults = dict(recital_penalty=0.0, rerank_recital_penalty=0.0, alpha=0.7)
    OUT.parent.mkdir(exist_ok=True)

    print(f"{len(dev)} dev questions\n")
    print(f"{'config':28s} " + " ".join(f"{'R@' + str(k):>6s}" for k in KS) + "  MRR@10   s/q  misses@5")
    for name, mode, kw in configs:
        if kw["embed_model"] not in retrievers:
            retrievers[kw["embed_model"]] = Retriever(embed_model=kw["embed_model"])
            validate(qs, {c["id"] for c in retrievers[kw["embed_model"]].chunks})
        r = retrievers[kw["embed_model"]]
        for key, val in {**defaults, **kw}.items():
            if key != "embed_model":
                setattr(r, key, val)
        if mode == "rerank":  # load the cross-encoder once and share it across embedding models
            shared = next((x.__dict__["cross_encoder"] for x in retrievers.values() if "cross_encoder" in x.__dict__), None)
            if shared is not None:
                r.__dict__["cross_encoder"] = shared
        t = time.perf_counter()
        res = evaluate(r, dev, mode)
        per_q = (time.perf_counter() - t) / len(dev)
        misses = [row["id"] for row in res["rows"] if not row["rank"] or row["rank"] > 5]
        print(f"{name:28s} " + " ".join(f"{res[f'R@{k}']:6.1%}" for k in KS)
              + f"  {res['MRR@10']:6.3f} {per_q:5.2f}  {' '.join(misses)}", flush=True)
        with OUT.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"config": name, "mode": mode, **kw, "split": "dev",
                                **{k: v for k, v in res.items() if k != "rows"},
                                "sec_per_query": round(per_q, 3), "misses@5": misses}) + "\n")


if __name__ == "__main__":
    main()

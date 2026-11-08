"""Does LLM query rewriting help retrieval? DEV split only.

Variants: original question / rewrite only / original + rewrite fused with RRF.
Rewrites are cached in eval/results/rewrites_<model>.jsonl so re-runs cost no API calls.

python eval/eval_rewrite.py [--model openai/gpt-oss-20b]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "eval"))
import generate  # noqa: E402
from eval_retrieval import KS, first_hit_rank, load_questions, summarise  # noqa: E402
from generate import Generator  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--model", default=generate.REWRITE_MODEL)
a = ap.parse_args()
generate.REWRITE_MODEL = a.model

g = Generator()
r = g.retriever
dev = [q for q in load_questions() if q["gold"] and q["split"] == "dev"]
cache_path = ROOT / "eval" / "results" / f"rewrites_{a.model.split('/')[-1]}.jsonl"
cache_path.parent.mkdir(exist_ok=True)
cache = {}
if cache_path.exists():
    cache = {d["id"]: d["rewrite"] for d in map(json.loads, cache_path.open(encoding="utf-8"))}
with cache_path.open("a", encoding="utf-8") as f:
    for q in dev:
        if q["id"] not in cache:
            cache[q["id"]] = g.rewrite(q["question"])
            f.write(json.dumps({"id": q["id"], "question": q["question"], "rewrite": cache[q["id"]]}) + "\n")

variants = {
    "original": lambda q: r.search(q["question"], 10),
    "rewrite only": lambda q: r.search(cache[q["id"]], 10),
    "original+rewrite": lambda q: r.search(q["question"], 10, rewrites=[cache[q["id"]]]),
}
print(f"{len(dev)} dev questions, rewriter {a.model}\n")
print(f"{'variant':18s} " + " ".join(f"{'R@' + str(k):>6s}" for k in KS) + "  MRR@10  misses@5")
for name, fn in variants.items():
    rows = [{"id": q["id"], "type": q["type"],
             "rank": first_hit_rank([c["id"] for c in fn(q)], set(q["gold"]))} for q in dev]
    s = summarise(rows)
    misses = [x["id"] for x in rows if not x["rank"] or x["rank"] > 5]
    print(f"{name:18s} " + " ".join(f"{s[f'R@{k}']:6.1%}" for k in KS) + f"  {s['MRR@10']:6.3f}  {' '.join(misses)}")
    with (ROOT / "eval" / "results" / "experiments.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({"config": f"rewrite[{a.model}] {name}", "split": "dev",
                            **s, "misses@5": misses}) + "\n")

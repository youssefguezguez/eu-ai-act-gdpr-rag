"""Retrieval evaluation: Recall@k and MRR for each retrieval mode, on the dev or test split.

The split is fixed and stratified by question type (alternate items within each type), so dev
and test have the same mix. Tune on dev; report test only for final numbers.
Unanswerable questions have no gold chunks and are excluded from retrieval metrics
(they are used later to test whether the generator declines).

python eval/eval_retrieval.py --split dev
python eval/eval_retrieval.py --split test --modes bm25 dense hybrid
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from retrieve import Retriever  # noqa: E402

QUESTIONS = ROOT / "eval" / "questions.jsonl"
KS = (1, 3, 5, 10)


def load_questions() -> list[dict]:
    qs = [json.loads(l) for l in QUESTIONS.open(encoding="utf-8") if l.strip()]
    by_type: dict[str, int] = defaultdict(int)
    for q in qs:
        q["split"] = "dev" if by_type[q["type"]] % 2 == 0 else "test"
        by_type[q["type"]] += 1
    return qs


def validate(qs: list[dict], chunk_ids: set[str]) -> None:
    ids = [q["id"] for q in qs]
    assert len(ids) == len(set(ids)), "duplicate question ids"
    bad = [(q["id"], g) for q in qs for g in q["gold"] if g not in chunk_ids]
    if bad:
        raise SystemExit(f"unknown gold chunk ids: {bad}")


def first_hit_rank(ranked_ids: list[str], gold: set[str]) -> int | None:
    for r, cid in enumerate(ranked_ids, 1):
        if cid in gold:
            return r
    return None


def evaluate(retriever: Retriever, qs: list[dict], mode: str) -> dict:
    rows = []
    for q in qs:
        ranked = [c["id"] for c in retriever.search(q["question"], max(KS), mode)]
        rows.append({"id": q["id"], "type": q["type"], "rank": first_hit_rank(ranked, set(q["gold"]))})
    return {"rows": rows, **summarise(rows)}


def summarise(rows: list[dict]) -> dict:
    n = len(rows)
    out = {f"R@{k}": sum(1 for r in rows if r["rank"] and r["rank"] <= k) / n for k in KS}
    out["MRR@10"] = sum(1 / r["rank"] for r in rows if r["rank"]) / n
    out["n"] = n
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="dev", choices=["dev", "test", "all"])
    ap.add_argument("--modes", nargs="+", default=["bm25", "dense", "hybrid"])
    ap.add_argument("--save", help="write per-question results to this JSON file")
    args = ap.parse_args()

    retriever = Retriever()
    qs = load_questions()
    validate(qs, {c["id"] for c in retriever.chunks})
    qs = [q for q in qs if q["gold"] and (args.split == "all" or q["split"] == args.split)]
    print(f"{len(qs)} answerable questions on split '{args.split}'\n")

    header = f"{'mode':8s} " + " ".join(f"{m:>7s}" for m in [f'R@{k}' for k in KS] + ["MRR@10"])
    print(header)
    results = {}
    for mode in args.modes:
        res = evaluate(retriever, qs, mode)
        results[mode] = res
        print(f"{mode:8s} " + " ".join(f"{res[f'R@{k}']:7.1%}" for k in KS) + f" {res['MRR@10']:7.3f}")

    print("\nR@5 by question type:")
    types = sorted({q["type"] for q in qs})
    print(f"{'mode':8s} " + " ".join(f"{t:>9s}" for t in types))
    for mode, res in results.items():
        cells = []
        for t in types:
            sub = [r for r in res["rows"] if r["type"] == t]
            cells.append(f"{summarise(sub)['R@5']:6.0%}({len(sub)})")
        print(f"{mode:8s} " + " ".join(f"{c:>9s}" for c in cells))

    misses = {mode: [r["id"] for r in res["rows"] if not r["rank"] or r["rank"] > 5] for mode, res in results.items()}
    print("\nmissed at k=5:", json.dumps(misses))
    if args.save:
        Path(args.save).write_text(json.dumps(results, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()

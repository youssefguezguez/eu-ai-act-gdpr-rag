"""Show the top-k retrieved chunks next to the gold ids for chosen questions.

python scripts/diagnose.py q027 q030 --penalty 0.05 --embed BAAI/bge-small-en-v1.5
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "eval"))
from eval_retrieval import load_questions  # noqa: E402
from retrieve import EMBED_MODEL, Retriever  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("ids", nargs="*")
ap.add_argument("--penalty", type=float, default=0.05)
ap.add_argument("--embed", default=EMBED_MODEL)
ap.add_argument("--mode", default="dense")
ap.add_argument("-k", type=int, default=5)
ap.add_argument("--recital-gold", action="store_true", help="all questions whose gold includes a recital")
a = ap.parse_args()

r = Retriever(embed_model=a.embed, recital_penalty=a.penalty)
qs = {q["id"]: q for q in load_questions()}
sel = [q for q in qs.values() if q["id"] in a.ids
       or (a.recital_gold and any("recital" in g for g in q["gold"]))]
for q in sel:
    print(f"\n{q['id']} [{q['type']}/{q['split']}] {q['question']}")
    print(f"  gold: {q['gold']}")
    for i, c in enumerate(r.search(q["question"], a.k, a.mode), 1):
        mark = "*" if c["id"] in q["gold"] else " "
        print(f"  {mark}{i}. {c['id']:28s} {c['text'][:90]!r}")

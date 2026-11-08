"""Re-parse citations in saved generation results after a parser fix (no API calls).

python scripts/rescore_citations.py eval/results/generation_dev.jsonl eval/results/generation_test.jsonl
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from generate import CITE, normalise_citations  # noqa: E402

for path in map(Path, sys.argv[1:]):
    rows = [json.loads(l) for l in path.open(encoding="utf-8")]
    changed = 0
    for r in rows:
        text = normalise_citations(r["answer"])
        n = len(r["sources"])
        nums = sorted({int(x) for x in CITE.findall(text) if 1 <= int(x) <= n})
        cited = [r["sources"][k - 1]["id"] for k in nums]
        changed += cited != r["cited_ids"]
        r["answer"], r["cited_ids"] = text, cited
        r["invalid_citations"] = sorted({int(x) for x in CITE.findall(text)} - set(range(1, n + 1)))
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    print(f"{path.name}: {changed} rows updated")

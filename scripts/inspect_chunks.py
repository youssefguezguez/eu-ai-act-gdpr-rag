"""Quick sanity checks on data/processed/chunks.jsonl."""
import json
from pathlib import Path

chunks = [json.loads(l) for l in (Path(__file__).resolve().parents[1] / "data/processed/chunks.jsonl").open(encoding="utf-8")]
long = [c for c in chunks if len(c["text"]) > 1500]
print(f"{len(long)} chunks over 1500 chars:")
for c in sorted(long, key=lambda c: -len(c["text"]))[:10]:
    print(f"  {len(c['text']):5d}  {c['heading'][:90]}")
for cid in ["AIAct-article-5-1", "AIAct-article-3", "GDPR-article-6-1", "AIAct-annex-III", "GDPR-recital-26"]:
    c = next((c for c in chunks if c["id"] == cid), None)
    print("\n==", cid, "->", c["heading"] if c else "MISSING")
    if c:
        print(c["chapter"][:100])
        print(c["text"][:500])

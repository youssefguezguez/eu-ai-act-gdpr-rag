"""Find chunks whose text matches a regex, optionally restricted to an article.

python scripts/find.py "AIAct:5:emotion" "GDPR:6:" "GDPR::seventy-two hours"
Each spec is REG:ARTICLE:REGEX (ARTICLE or REGEX may be empty). Prints id + match context.
"""
import json
import re
import sys
from pathlib import Path

chunks = [json.loads(l) for l in (Path(__file__).resolve().parents[1] / "data/processed/chunks.jsonl").open(encoding="utf-8")]
for spec in sys.argv[1:]:
    reg, art, pat = (spec.split(":", 2) + ["", ""])[:3]
    print(f"\n### {spec}")
    for c in chunks:
        if reg and not c["id"].startswith(reg + "-"):
            continue
        if art and not (c["kind"] == "article" and c["number"] == art) and not (art.startswith("A") and c["kind"] == "annex" and c["number"] == art[1:]):
            continue
        if pat:
            m = re.search(pat, c["text"], re.I)
            if not m:
                continue
            s = max(0, m.start() - 60)
            ctx = c["text"][s:m.end() + 90]
        else:
            ctx = c["text"][:110]
        print(f"  {c['id']:28s} {ctx}")

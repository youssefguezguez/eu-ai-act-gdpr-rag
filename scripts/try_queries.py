"""Compare the three retrieval modes on a few hand-picked questions (top-3 headings)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from retrieve import Retriever  # noqa: E402

QUESTIONS = [
    "Is emotion recognition in the workplace allowed?",          # AI Act Art. 5(1)(f)
    "What are the lawful bases for processing personal data?",   # GDPR Art. 6(1)
    "When must a company carry out a data protection impact assessment?",  # GDPR Art. 35
    "What fines apply for using a prohibited AI practice?",       # AI Act Art. 99(3)
]

r = Retriever()
for q in QUESTIONS:
    print(f"\nQ: {q}")
    for mode in ("bm25", "dense", "hybrid"):
        heads = [c["heading"][:70] for c in r.search(q, 3, mode)]
        print(f"  {mode:6s} | " + "\n         | ".join(heads))

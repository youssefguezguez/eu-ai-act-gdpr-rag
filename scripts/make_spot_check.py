"""Write a self-contained human spot-check sheet: the judge's 5 flagged answers + 5 it passed.

Everything needed to grade is on the page: the reference answer, the full text of the gold
(correct) passages, the assistant's answer, and the text of each source it cited.

python scripts/make_spot_check.py --split dev
"""
import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--split", default="dev")
ap.add_argument("--passed", type=int, default=5)
a = ap.parse_args()

chunks = {c["id"]: c for c in map(json.loads, (ROOT / "data/processed/chunks.jsonl").open(encoding="utf-8"))}
rows = [json.loads(l) for l in (ROOT / f"eval/results/generation_{a.split}.jsonl").open(encoding="utf-8")]
rows = [r for r in rows if r["gold"]]
flagged = [r for r in rows if r["judge"].get("correct") == "no" or r["judge"].get("faithful") is False]
passed = [r for r in rows if r not in flagged and r["judge"].get("correct") == "yes"]
random.Random(0).shuffle(passed)
sample = sorted(flagged + passed[: a.passed], key=lambda r: r["id"])
random.Random(1).shuffle(sample)  # mixed order, so you don't know which ones the judge failed

L = ["# Spot-check: grade 10 answers", "",
     "For each question: read the REFERENCE and the CORRECT ARTICLE TEXT, then the ANSWER.",
     "Write two verdicts at the bottom of each question:",
     "- **Correct**: yes (gets the key point right) / partial (some of it, or vague) / no (wrong, or refuses)",
     "- **Faithful**: yes / no. Look at each sentence's [n] number and check that the cited source",
     "  (printed below the answer) really says that. If one claim isn't in its source, write no.",
     "", "The judge's verdicts are in a separate file (spot_check_judge_key.md). Open it only after you finish.", ""]
key = ["# Judge verdicts (open after grading)", ""]
for i, r in enumerate(sample, 1):
    L += ["---", "", f"## {i}. {r['question']}", "", f"**REFERENCE:** {r['answer_note']}", "",
          "**CORRECT ARTICLE TEXT:**", ""]
    for g in r["gold"]:
        L += [f"> **{chunks[g]['heading']}**", ">", f"> {chunks[g]['text']}", ""]
    L += ["**ANSWER:**", "", r["answer"], "", "**SOURCES THE ANSWER CITED:**", ""]
    cited = [s for s in r["sources"] if s["id"] in r["cited_ids"]]
    for s in cited:
        L += [f"> **[{s['n']}] {s['heading']}**", ">", f"> {s['text']}", ""]
    if not cited:
        L += ["(none)", ""]
    L += ["**Your verdict:** Correct = ______   Faithful = ______", ""]
    j = r["judge"]
    key += [f"{i}. ({r['id']}) correct={j.get('correct')}, faithful={j.get('faithful')}: {j.get('reason', '')}"]

out = ROOT / "eval/results"
(out / f"spot_check_{a.split}.md").write_text("\n".join(L), encoding="utf-8")
(out / "spot_check_judge_key.md").write_text("\n".join(key) + "\n", encoding="utf-8")
print(f"{len(sample)} questions -> {out / f'spot_check_{a.split}.md'}")

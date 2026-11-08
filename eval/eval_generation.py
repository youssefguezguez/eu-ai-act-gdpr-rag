"""End-to-end evaluation of generated answers (DEV split unless --split test).

Per question it records the answer, citations and two LLM-judge verdicts:
  - faithful : every factual claim is supported by the sources it cites (hallucination check)
  - correct  : the answer agrees with the reference note written with the gold set
The judge is a different model family (Qwen) from the generator (gpt-oss) to limit
self-preference. A human spot-check file is written so the judge itself can be audited.

Results are appended per question to eval/results/generation_<split>.jsonl; re-running
resumes where it stopped (useful with free-tier rate limits).

python eval/eval_generation.py --split dev
python eval/eval_generation.py --split dev --report   # summary only, no API calls
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "eval"))
from eval_retrieval import load_questions  # noqa: E402

JUDGE_MODEL = "qwen/qwen3.8-27b"
SEEN_TEST = {"q065", "q069"}  # test items displayed during development; reported separately

JUDGE_SYSTEM = """You grade answers produced by a legal question-answering assistant about the EU AI Act
and the GDPR. You receive the question, a reference note written by an expert, the assistant's
answer, and the numbered sources the assistant was given.

Judge two things:
1. faithful: is EVERY factual claim in the answer supported by the source(s) it cites? A claim
   with no citation, or citing a source that does not say it, makes the answer unfaithful.
   Paraphrase is fine. Ignore style.
2. correct: compared with the reference note, is the answer "yes" (states the key point and
   nothing contradicting it), "partial" (some of the key point, or vague), or "no" (misses or
   contradicts it, or wrongly declines)?

Reply with JSON only:
{"faithful": true|false, "unsupported": ["claim ...", ...], "correct": "yes"|"partial"|"no", "reason": "one sentence"}"""


def parse_json(text: str) -> dict:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S)
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError(f"judge returned no JSON: {text[:200]}")
    return json.loads(m.group(0))


def judge(gen, q: dict, out: dict) -> dict:
    sources = "\n\n".join(f"[{s['n']}] {s['heading']}\n{s['text']}" for s in out["sources"])
    msg = (f"Question: {q['question']}\n\nReference note: {q['answer_note']}\n\n"
           f"Assistant answer:\n{out['answer']}\n\nSources:\n\n{sources}")
    for attempt in range(3):
        try:
            return parse_json(gen.chat([{"role": "system", "content": JUDGE_SYSTEM},
                                        {"role": "user", "content": msg}],
                                       model=JUDGE_MODEL, max_tokens=1500))
        except (ValueError, json.JSONDecodeError):
            if attempt == 2:
                return {"faithful": None, "correct": None, "reason": "judge output unparseable"}
    return {}


def report(rows: list[dict]) -> None:
    ans = [r for r in rows if r["gold"]]
    una = [r for r in rows if not r["gold"]]
    clean = [r for r in ans if r["id"] not in SEEN_TEST]
    pct = lambda xs, f: f"{sum(1 for x in xs if f(x)) / len(xs):.1%}" if xs else "n/a"  # noqa: E731
    print(f"answerable: {len(ans)}   unanswerable: {len(una)}")
    print(f"  correctly declined (unanswerable)   {pct(una, lambda r: r['declined'])}")
    print(f"  wrongly declined (answerable)       {pct(ans, lambda r: r['declined'])}")
    print(f"  cites >=1 gold chunk                {pct(ans, lambda r: set(r['cited_ids']) & set(r['gold']))}")
    print(f"  gold chunk among the sources given  {pct(ans, lambda r: {s['id'] for s in r['sources']} & set(r['gold']))}")
    print(f"  answers with invalid citation nos.  {pct(ans, lambda r: r['invalid_citations'])}")
    print(f"  faithful (judge)                    {pct([r for r in ans if not r['declined']], lambda r: r['judge'].get('faithful') is True)}")
    print(f"  correct = yes (judge)               {pct(ans, lambda r: r['judge'].get('correct') == 'yes')}")
    print(f"  correct = yes or partial (judge)    {pct(ans, lambda r: r['judge'].get('correct') in ('yes', 'partial'))}")
    print(f"  mean seconds per answer             {sum(r['seconds'] for r in rows) / len(rows):.1f}")
    if len(clean) != len(ans):
        print(f"  correct = yes, excluding seen items {pct(clean, lambda r: r['judge'].get('correct') == 'yes')} (n={len(clean)})")
    bad = [r["id"] for r in ans if r["judge"].get("correct") == "no" or r["judge"].get("faithful") is False]
    print(f"  to inspect (not correct or not faithful): {' '.join(bad)}")


def spot_check(rows: list[dict], path: Path) -> None:
    lines = ["# Human spot-check of generated answers", "",
             "For each answer, mark **Correct** (yes / partial / no) and **Faithful** (yes / no),",
             "then compare with the judge's verdict below it.", ""]
    for r in rows:
        lines += [f"## {r['id']} ({r['type']}) {r['question']}", "",
                  f"**Reference:** {r['answer_note']}", "", f"**Answer:** {r['answer']}", "",
                  "**Sources cited:** " + (", ".join(f"[{s['n']}] {s['heading']}" for s in r['sources']
                                                       if s['id'] in r['cited_ids']) or "none"), "",
                  f"**Judge:** correct={r['judge'].get('correct')}, faithful={r['judge'].get('faithful')}"
                  f" ({r['judge'].get('reason', '')})", "",
                  "**Your verdict:** Correct = ___ · Faithful = ___", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", default="dev", choices=["dev", "test"])
    ap.add_argument("--report", action="store_true", help="summarise existing results only")
    ap.add_argument("--limit", type=int, help="only the first N questions (smoke test)")
    a = ap.parse_args()

    out_path = ROOT / "eval" / "results" / f"generation_{a.split}.jsonl"
    out_path.parent.mkdir(exist_ok=True)
    done = {}
    if out_path.exists():
        done = {d["id"]: d for d in map(json.loads, out_path.open(encoding="utf-8"))}
    qs = [q for q in load_questions() if q["split"] == a.split][: a.limit]

    if not a.report:
        from generate import Generator
        gen = Generator(max_wait=3600)  # the eval may wait out the daily token limit
        todo = [q for q in qs if q["id"] not in done]
        for i, q in enumerate(todo, 1):
            out = gen.answer(q["question"])
            row = {**{k: q[k] for k in ("id", "type", "question", "gold", "answer_note")}, **out}
            row["judge"] = judge(gen, q, out) if q["gold"] else {}
            done[q["id"]] = row
            with out_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"[{i}/{len(todo)}] {q['id']} declined={out['declined']} cited={out['cited_ids']} "
                  f"judge={row['judge'].get('correct')}/{row['judge'].get('faithful')}", flush=True)

    rows = [done[q["id"]] for q in qs if q["id"] in done]
    report(rows)
    spot_check(rows, ROOT / "eval" / "results" / f"spot_check_{a.split}.md")


if __name__ == "__main__":
    main()

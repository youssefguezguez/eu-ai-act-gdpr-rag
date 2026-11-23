"""Answer questions on the EU AI Act + GDPR from retrieved passages, with citations.

The LLM sees k numbered sources and must cite them as [1], [2], ... after each claim.
Citations are mapped back to chunk ids so the evaluation can check them against gold.
If the sources do not answer the question, the model must start with DECLINE (a fixed
sentence), so declining is detected exactly rather than guessed from wording.

python src/generate.py "Is emotion recognition in the workplace allowed?"
"""
from __future__ import annotations

import argparse
import os
import re
import time
from functools import cached_property
from pathlib import Path

from dotenv import load_dotenv

from retrieve import Retriever

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

GEN_MODEL = "openai/gpt-oss-120b"  # open weights (Apache 2.0), served free by Groq
REWRITE_MODEL = "openai/gpt-oss-120b"  # beat gpt-oss-20b as rewriter on dev (R@8 91.7% vs 88.9%)
# Chosen on dev (eval/eval_rewrite.py): original + gpt-oss-120b rewrite fused, 8 sources -> R@8 91.7%
# vs 83.3% without rewriting (more sources alone did not help).
TOP_K = 8
DECLINE = "The AI Act and GDPR texts I have do not answer this question."

SYSTEM = f"""You answer questions about two EU laws: the AI Act (Regulation 2024/1689) and the
GDPR (Regulation 2016/679), using ONLY the numbered sources provided.

Rules:
- Every factual sentence ends with the source number(s) it relies on, like [2] or [1][3].
- Use only what the sources say. Do not add outside knowledge, dates, figures or case law.
- Name the article when you rely on it (e.g. "Article 5(1)(f) of the AI Act prohibits ... [1]").
- If the sources do not contain the answer (the topic is outside these two laws, or the question
  asks about facts, news, prices or other jurisdictions), reply with exactly this sentence and
  nothing else: "{DECLINE}"
- If the sources answer only part of the question, answer that part and say what is not covered.
- Be concise: 2-6 sentences, plain English, no headings. This is information, not legal advice."""

REWRITE_SYSTEM = """Rewrite the user's question as a search query for the legal text of the EU AI Act
and the GDPR. Everyday words rarely match legal drafting, so translate the question into the
formal terms a regulation would use for the same situation, and name the legal concepts the
answer depends on (roles, obligations, rights, scope, exceptions). Do not answer the question
and do not guess article numbers. Output one line, at most 40 words, nothing else."""

CITE = re.compile(r"\[(\d+)\]")


def normalise_citations(text: str) -> str:
    """gpt-oss sometimes cites in its native 【8】 / 【1†L3】 style: rewrite to [8]."""
    return re.sub(r"【(\d+)[^】]*】", lambda m: f"[{m.group(1)}]", text)


def format_sources(chunks: list[dict]) -> str:
    return "\n\n".join(f"[{i}] {c['heading']}\n{c['text']}" for i, c in enumerate(chunks, 1))


class Generator:
    def __init__(self, retriever: Retriever | None = None, model: str = GEN_MODEL, k: int = TOP_K,
                 reasoning_effort: str = "low", max_wait: float = 60, rewrite_model: str | None = None):
        self.retriever = retriever or Retriever()
        self.model = model
        self.rewrite_model = rewrite_model or REWRITE_MODEL
        self.k = k
        self.reasoning_effort = reasoning_effort
        self.max_wait = max_wait  # longest rate-limit wait to accept (the demo keeps this short)

    @cached_property
    def client(self):
        from groq import Groq
        if not os.getenv("GROQ_API_KEY"):
            raise RuntimeError("GROQ_API_KEY missing: put it in .env")
        return Groq()

    def chat(self, messages: list[dict], model: str | None = None, max_tokens: int = 1200,
             usage: dict | None = None, **kw) -> str:
        model = model or self.model
        if model.startswith("openai/gpt-oss"):
            kw.setdefault("reasoning_effort", self.reasoning_effort)
        for attempt in range(6):
            try:
                r = self.client.chat.completions.create(model=model, messages=messages, temperature=0,
                                                        max_tokens=max_tokens, **kw)
                if usage is not None and getattr(r, "usage", None):  # tokens per answer, for the API log
                    usage["tokens"] = usage.get("tokens", 0) + (r.usage.total_tokens or 0)
                return (r.choices[0].message.content or "").strip()
            except Exception as e:  # rate limits on the free tier: wait as told, then retry
                if "429" not in str(e) and "rate" not in str(e).lower() or attempt == 5:
                    raise
                hint = re.search(r"try again in (?:(\d+)m)?([\d.]+)s", str(e))
                wait = int(hint.group(1) or 0) * 60 + float(hint.group(2)) + 2 if hint else 5 * 2 ** attempt
                if wait > self.max_wait:
                    raise
                time.sleep(wait)
        raise RuntimeError("unreachable")

    def rewrite(self, question: str, usage: dict | None = None) -> str:
        return self.chat([{"role": "system", "content": REWRITE_SYSTEM},
                          {"role": "user", "content": question}], model=self.rewrite_model, max_tokens=600,
                         usage=usage)

    def answer(self, question: str, rewrite: bool = True) -> dict:
        t = time.perf_counter()
        usage: dict = {}
        rewrites = [self.rewrite(question, usage)] if rewrite else []
        chunks = self.retriever.search(question, self.k, rewrites=rewrites)
        text = self.chat([
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Sources:\n\n{format_sources(chunks)}\n\nQuestion: {question}"},
        ], usage=usage)
        text = normalise_citations(text)
        declined = text.startswith(DECLINE[:40])
        nums = sorted({int(n) for n in CITE.findall(text) if 1 <= int(n) <= len(chunks)})
        return {
            "question": question,
            "answer": text,
            "declined": declined,
            "cited_ids": [chunks[n - 1]["id"] for n in nums],
            "invalid_citations": sorted({int(n) for n in CITE.findall(text)} - set(range(1, len(chunks) + 1))),
            "sources": [{"n": i, "id": c["id"], "heading": c["heading"], "url": c["url"], "text": c["text"]}
                        for i, c in enumerate(chunks, 1)],
            "rewrites": rewrites,
            "model": self.model,
            "seconds": round(time.perf_counter() - t, 2),
            "tokens": usage.get("tokens", 0),
        }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("-k", type=int, default=TOP_K)
    a = ap.parse_args()
    out = Generator(k=a.k).answer(a.question)
    print(out["answer"], "\n")
    for s in out["sources"]:
        mark = "*" if s["id"] in out["cited_ids"] else " "
        print(f" {mark}[{s['n']}] {s['heading']}")
    print(f"\n{out['seconds']} s, cited: {out['cited_ids']}")


if __name__ == "__main__":
    main()

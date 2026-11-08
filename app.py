"""Gradio demo: ask a question about the EU AI Act or the GDPR, get a cited answer.

Local:   python app.py            (needs GROQ_API_KEY in .env)
Spaces:  set GROQ_API_KEY as a Space secret; this file is the entry point.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

import gradio as gr

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from generate import Generator  # noqa: E402

gen = Generator(max_wait=20)
gen.retriever.embeddings  # load the index at startup, not on the first question
gen.retriever.model
# The free tier caps each model at a daily token budget. When gpt-oss-120b's is used up,
# fall back to gpt-oss-20b (separate budget); the footer shows which model answered.
FALLBACK = "openai/gpt-oss-20b"
fallback = Generator(retriever=gen.retriever, model=FALLBACK, rewrite_model=FALLBACK, max_wait=20)

EXAMPLES = [
    "Can my employer use AI to read my emotions during video calls?",
    "We sell a CV-screening tool. Is it high-risk under the AI Act?",
    "How quickly must a company report a personal data breach?",
    "What must a chatbot tell users about being an AI?",
    "Can we use ethnicity data to detect bias in our model?",
    "What is the VAT rate on AI software in Germany?",
]

INTRO = """# EU AI Act & GDPR assistant
Answers come **only** from the official texts of the
[AI Act (Regulation 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) and the
[GDPR (Regulation 2016/679)](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Every claim cites
the article it relies on; if the texts don't cover a question, the assistant says so.
*Information, not legal advice.* Free-tier model: if it is busy, wait a minute and retry."""


def link_citations(answer: str, sources: list[dict]) -> str:
    by_n = {s["n"]: s for s in sources}

    def repl(m: re.Match) -> str:
        s = by_n.get(int(m.group(1)))
        return f"[[{m.group(1)}]]({s['url']} \"{html.escape(s['heading'])}\")" if s else m.group(0)
    return re.sub(r"\[(\d+)\]", repl, answer)


def format_sources(out: dict) -> str:
    lines = []
    for s in out["sources"]:
        cited = s["id"] in out["cited_ids"]
        lines.append(f"**[{s['n']}] [{s['heading']}]({s['url']})**" + (" · *cited*" if cited else ""))
        text = s["text"] if len(s["text"]) < 700 else s["text"][:700] + " …"
        lines.append(f"> {text}\n")
    if out.get("rewrites"):
        lines.append(f"*Search also used this legal rephrasing of your question:* {out['rewrites'][0]}")
    return "\n".join(lines)


def ask(question: str):
    question = (question or "").strip()
    if not question:
        return "Type a question first.", ""
    if len(question) > 500:
        return "Please keep questions under 500 characters.", ""
    try:
        try:
            out = gen.answer(question)
        except Exception as e:
            if "429" not in str(e):
                raise
            out = fallback.answer(question)
            out["model"] += " (fallback: main model's free daily quota used up)"
    except Exception as e:  # free-tier rate limit or provider outage
        msg = "The free model is busy (rate limit). Please retry in a minute." if "429" in str(e) or "rate" in str(e).lower() \
            else "The model provider returned an error. Please retry in a minute."
        return msg, ""
    answer = out["answer"] if out["declined"] else link_citations(out["answer"], out["sources"])
    footer = f"\n\n<sub>{out['seconds']} s · {out['model']} · {len(out['cited_ids'])} source(s) cited</sub>"
    return answer + footer, format_sources(out)


with gr.Blocks(title="EU AI Act & GDPR assistant") as demo:
    gr.Markdown(INTRO)
    q = gr.Textbox(label="Your question", placeholder="e.g. Is emotion recognition at work allowed?", lines=2)
    btn = gr.Button("Ask", variant="primary")
    answer = gr.Markdown(label="Answer")
    with gr.Accordion("Sources retrieved", open=False):
        sources = gr.Markdown()
    gr.Examples(EXAMPLES, inputs=q)
    gr.Markdown("Code, evaluation set and results: "
                "[github.com/youssefguezguez/eu-ai-act-gdpr-rag](https://github.com/youssefguezguez/eu-ai-act-gdpr-rag)")
    btn.click(ask, q, [answer, sources], concurrency_limit=2)
    q.submit(ask, q, [answer, sources], concurrency_limit=2)

if __name__ == "__main__":
    demo.queue(max_size=20).launch()

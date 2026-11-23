"""FastAPI service: the deployed version of the assistant (web page + JSON API).

  GET  /         the web page (web/index.html)
  GET  /health   liveness + index size
  POST /ask      {"question": "..."} -> cited answer, sources, model, latency, tokens

Run locally:  EMBED_BACKEND=onnx uvicorn api:app --port 8000   (needs GROQ_API_KEY)
The Gradio app (app.py) stays for local use; this service is lighter (no torch) for free hosts.

Abuse limits, because the service spends a free-tier API key: questions <= 500 characters,
per-IP rate limit, at most 2 answers generated at once. Logs keep latency, tokens and outcome,
never the question text.
"""
from __future__ import annotations

import json
import logging
import os
import sys
import threading
import time
from collections import defaultdict, deque
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("EMBED_BACKEND", "onnx")
from generate import Generator  # noqa: E402

FALLBACK = "openai/gpt-oss-20b"  # own daily budget on the free tier
PER_MINUTE = int(os.getenv("RATE_PER_MINUTE", "4"))
PER_DAY = int(os.getenv("RATE_PER_DAY", "40"))
MAX_CONCURRENT = 2

log = logging.getLogger("rag")
logging.basicConfig(level=logging.INFO, format="%(message)s")


class Ask(BaseModel):
    question: str = Field(min_length=1, max_length=500)


class RateLimiter:
    def __init__(self, per_minute: int, per_day: int):
        self.limits = ((60, per_minute), (86400, per_day))
        self.hits: dict[str, deque] = defaultdict(deque)
        self.lock = threading.Lock()

    def allow(self, key: str, now: float | None = None) -> bool:
        now = time.time() if now is None else now
        with self.lock:
            q = self.hits[key]
            while q and now - q[0] > 86400:
                q.popleft()
            for window, limit in self.limits:
                if sum(1 for t in q if now - t <= window) >= limit:
                    return False
            q.append(now)
            return True


def build_generators() -> tuple[Generator, Generator]:
    gen = Generator(max_wait=20)
    fb = Generator(retriever=gen.retriever, model=FALLBACK, rewrite_model=FALLBACK, max_wait=20)
    return gen, fb


@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.getenv("SKIP_WARMUP"):
        gen, _ = generators()
        gen.retriever.embeddings  # load index + encoder now, not on the first question
        gen.retriever.model
    yield


app = FastAPI(title="EU AI Act & GDPR assistant", version="1.0", lifespan=lifespan)
app.state.limiter = RateLimiter(PER_MINUTE, PER_DAY)
app.state.slots = threading.BoundedSemaphore(MAX_CONCURRENT)
app.state.gen = None


def generators() -> tuple[Generator, Generator]:
    if app.state.gen is None:
        app.state.gen = build_generators()
    return app.state.gen


def client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")  # set by the host's proxy (Render)
    return fwd.split(",")[0].strip() if fwd else (request.client.host if request.client else "?")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(ROOT / "web" / "index.html")


@app.get("/health")
def health() -> dict:
    gen, _ = generators()
    return {"status": "ok", "chunks": len(gen.retriever.chunks)}


@app.post("/ask")
def ask(body: Ask, request: Request) -> dict:
    question = body.question.strip()
    if not question:
        raise HTTPException(422, "Empty question.")
    if not app.state.limiter.allow(client_ip(request)):
        raise HTTPException(429, f"Rate limit: {PER_MINUTE} questions per minute, {PER_DAY} per day.")
    if not app.state.slots.acquire(timeout=30):
        raise HTTPException(503, "Busy: please retry in a minute.")
    gen, fb = generators()
    try:
        try:
            out = gen.answer(question)
        except Exception as e:
            if "429" not in str(e):
                raise
            out = fb.answer(question)
            out["model"] += " (fallback: main model's free daily quota used up)"
    except Exception as e:
        log.info(json.dumps({"event": "error", "kind": type(e).__name__, "rate_limited": "429" in str(e)}))
        if "429" in str(e) or "rate" in str(e).lower():
            raise HTTPException(503, "The free model is busy (rate limit). Please retry in a minute.")
        raise HTTPException(502, "The model provider returned an error. Please retry in a minute.")
    finally:
        app.state.slots.release()
    log.info(json.dumps({"event": "answer", "seconds": out["seconds"], "tokens": out.get("tokens", 0),
                         "model": out["model"], "declined": out["declined"], "cited": len(out["cited_ids"]),
                         "q_chars": len(question)}))
    return {k: out[k] for k in ("answer", "declined", "cited_ids", "sources", "rewrites", "model", "seconds", "tokens")}

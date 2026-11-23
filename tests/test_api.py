"""API contract tests with the generator stubbed (no LLM calls, no model download)."""
import os

import pytest

os.environ["SKIP_WARMUP"] = "1"
from fastapi.testclient import TestClient  # noqa: E402

import api  # noqa: E402

ANSWER = {
    "question": "q", "answer": "Prohibited [1].", "declined": False, "cited_ids": ["AIAct-article-5-1.part3"],
    "invalid_citations": [], "rewrites": ["r"], "model": "stub", "seconds": 0.1, "tokens": 42,
    "sources": [{"n": 1, "id": "AIAct-article-5-1.part3", "heading": "Article 5(1)", "url": "https://x", "text": "t"}],
}


class StubRetriever:
    chunks = [{}] * 1461


class StubGen:
    def __init__(self, fail_with=None):
        self.retriever = StubRetriever()
        self.fail_with = fail_with

    def answer(self, question):
        if self.fail_with:
            raise RuntimeError(self.fail_with)
        return dict(ANSWER, question=question)


@pytest.fixture
def client():
    api.app.state.gen = (StubGen(), StubGen())
    api.app.state.limiter = api.RateLimiter(per_minute=3, per_day=100)
    return TestClient(api.app)


def test_health(client):
    assert client.get("/health").json() == {"status": "ok", "chunks": 1461}


def test_page(client):
    r = client.get("/")
    assert r.status_code == 200 and "EU AI Act" in r.text


def test_ask(client):
    r = client.post("/ask", json={"question": "Is emotion recognition at work allowed?"})
    assert r.status_code == 200
    d = r.json()
    assert d["cited_ids"] == ["AIAct-article-5-1.part3"] and d["tokens"] == 42
    assert "question" not in d  # the API does not echo or store questions


@pytest.mark.parametrize("q", ["", "x" * 501])
def test_rejects_bad_questions(client, q):
    assert client.post("/ask", json={"question": q}).status_code == 422


def test_rate_limit_per_ip(client):
    h = {"x-forwarded-for": "1.2.3.4"}
    codes = [client.post("/ask", json={"question": "q"}, headers=h).status_code for _ in range(4)]
    assert codes == [200, 200, 200, 429]
    assert client.post("/ask", json={"question": "q"}, headers={"x-forwarded-for": "5.6.7.8"}).status_code == 200


def test_fallback_on_quota(client):
    api.app.state.gen = (StubGen(fail_with="Error code: 429 tokens per day"), StubGen())
    d = client.post("/ask", json={"question": "q"}).json()
    assert "fallback" in d["model"]


def test_provider_error_is_502(client):
    api.app.state.gen = (StubGen(fail_with="boom"), StubGen())
    assert client.post("/ask", json={"question": "q"}).status_code == 502


def test_rate_limiter_windows():
    rl = api.RateLimiter(per_minute=2, per_day=3)
    assert [rl.allow("a", t) for t in (0, 1, 2)] == [True, True, False]
    assert rl.allow("a", 100) is True       # minute window passed
    assert rl.allow("a", 200) is False      # day cap of 3 reached
    assert rl.allow("a", 90000) is True     # next day

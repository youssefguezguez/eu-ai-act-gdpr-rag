"""Fast tests: no network, no model download. The LLM is replaced by a stub."""
import json

import pytest

from generate import DECLINE, Generator, normalise_citations
from retrieve import CHUNKS, INDEX, EMBED_MODEL, Retriever, tokenize


@pytest.fixture(scope="module")
def retriever():
    return Retriever()


def test_chunks_cover_both_laws(retriever):
    ids = [c["id"] for c in retriever.chunks]
    assert len(ids) == len(set(ids)) == 1461
    assert any(i.startswith("AIAct-article-5") for i in ids)
    assert any(i.startswith("GDPR-article-33") for i in ids)


def test_index_matches_chunks():
    ids = json.loads((INDEX / EMBED_MODEL.split("/")[-1] / "ids.json").read_text(encoding="utf-8"))
    assert ids == [json.loads(l)["id"] for l in CHUNKS.open(encoding="utf-8")]


def test_tokenize_drops_stopwords():
    assert tokenize("The right to erasure of the data") == ["right", "erasure", "data"]


def test_bm25_finds_breach_notification(retriever):
    top = retriever.search("notify the supervisory authority of a personal data breach 72 hours", 5, mode="bm25")
    assert any(c["id"].startswith("GDPR-article-33") for c in top)


def test_normalise_citations():
    assert normalise_citations("Banned 【1†L3】 and 【8】.") == "Banned [1] and [8]."


class StubRetriever:
    def __init__(self, chunks):
        self.chunks = chunks

    def search(self, query, k, rewrites=None):
        return self.chunks[:k]


def make_gen(retriever, replies):
    g = Generator(retriever=StubRetriever(retriever.chunks[:8]))
    calls = iter(replies)
    g.chat = lambda messages, model=None, max_tokens=1200, usage=None, **kw: next(calls)
    return g


def test_answer_maps_citations(retriever):
    g = make_gen(retriever, ["rewritten query", "It is covered [2]. Also [9] and 【1】."])
    out = g.answer("question?")
    assert not out["declined"]
    assert out["cited_ids"] == [retriever.chunks[0]["id"], retriever.chunks[1]["id"]]
    assert out["invalid_citations"] == [9]
    assert out["rewrites"] == ["rewritten query"]


def test_answer_detects_decline(retriever):
    g = make_gen(retriever, ["q", DECLINE])
    out = g.answer("What is the VAT rate in Germany?")
    assert out["declined"] and out["cited_ids"] == []

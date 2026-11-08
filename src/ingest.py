"""Parse the official EUR-Lex HTML of the EU AI Act and the GDPR into structure-aware chunks.

Chunks follow the legal structure instead of fixed-size windows:
  - articles   -> one chunk per numbered paragraph (e.g. Article 5(1));
                  long unnumbered articles (e.g. AI Act Art. 3 definitions) are split by point
  - recitals   -> one chunk per recital
  - annexes    -> grouped by consecutive blocks, up to MAX_CHARS

Every chunk keeps its citation (regulation, article, paragraph) and a deep link to EUR-Lex,
so answers can cite their sources and the evaluation can check citations exactly.

Usage:  python src/ingest.py
Output: data/processed/chunks.jsonl
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import warnings

from bs4 import BeautifulSoup, Tag, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed" / "chunks.jsonl"

SOURCES = {
    "32024R1689": "AI Act",
    "32016R0679": "GDPR",
}
MAX_CHARS = 1500  # about 350-400 tokens: fits every common embedding model's window

PARA_ID = re.compile(r"^\d{3}\.\d{3}$")


def clean(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def units_of(container: Tag) -> list[str]:
    """Split a block into ordered text units: each direct <p> and each table (one point)."""
    units = []
    for child in container.find_all(["p", "table"], recursive=False):
        if child.name == "p" and "oj-note" in (child.get("class") or []):
            continue
        t = clean(child.get_text(" "))
        if t:
            units.append(t)
    if not units:  # fall back to the whole block
        t = clean(container.get_text(" "))
        if t:
            units.append(t)
    return units


def split_long(unit: str, max_chars: int = MAX_CHARS) -> list[str]:
    """Split one over-long unit (e.g. a long recital) at sentence boundaries."""
    if len(unit) <= max_chars:
        return [unit]
    sentences = re.split(r"(?<=[.;])\s+(?=[A-Z(‘'])", unit)
    parts, cur = [], ""
    for s in sentences:
        if cur and len(cur) + len(s) + 1 > max_chars:
            parts.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        parts.append(cur)
    return parts


def group(units: list[str], max_chars: int = MAX_CHARS) -> list[str]:
    """Group units into chunks <= max_chars. A lead-in ending with ':' is repeated as context."""
    units = [p for u in units for p in split_long(u, max_chars)]
    if sum(len(u) for u in units) <= max_chars:
        return [" ".join(units)]
    lead = units[0] if units[0].endswith(":") else ""
    chunks, cur = [], []
    for u in units:
        if cur and len(" ".join(cur)) + len(u) + 1 > max_chars:
            chunks.append(" ".join(cur))
            cur = [lead] if lead and lead != u else []
        cur.append(u)
    if cur and cur != [lead]:
        chunks.append(" ".join(cur))
    return chunks


def chapter_of(node: Tag) -> str:
    cpt = node.find_parent("div", id=re.compile(r"^cpt_[IVXLC]+$"))
    if not cpt:
        return ""
    ps = [clean(p.get_text(" ")) for p in cpt.find_all("p", limit=2)]
    return " - ".join(p for p in ps if p)


def parse(celex: str, reg: str) -> list[dict]:
    html = (RAW / f"{celex}.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")
    base = f"https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{celex}"
    chunks: list[dict] = []

    def add(kind, number, title, para, text, anchor, chapter=""):
        shown = re.sub(r"\.?part\d+$", "", para or "")  # "1.part3" -> "1", "part7" -> ""
        heading = {
            "article": f"{reg} Article {number}" + (f"({shown})" if shown else "") + f" - {title}",
            "recital": f"{reg} Recital {number}",
            "annex": f"{reg} Annex {number}" + (f" - {title}" if title else ""),
        }[kind]
        chunks.append({
            "id": f"{reg.replace(' ', '')}-{kind}-{number}" + (f"-{para}" if para else ""),
            "regulation": reg,
            "celex": celex,
            "kind": kind,
            "number": number,
            "paragraph": para,
            "title": title,
            "chapter": chapter,
            "heading": heading,
            "text": text,
            "url": f"{base}#{anchor}",
        })

    # Articles
    for art in soup.find_all("div", id=re.compile(r"^art_\d+$")):
        number = art["id"].split("_")[1]
        sti = art.find("p", class_="oj-sti-art")
        title = clean(sti.get_text(" ")) if sti else ""
        chapter = chapter_of(art)
        paras = [d for d in art.find_all("div", recursive=False) if PARA_ID.match(d.get("id", ""))]
        if paras:
            for d in paras:
                para = str(int(d["id"].split(".")[1]))
                for i, text in enumerate(group(units_of(d))):
                    pid = para if i == 0 else f"{para}.part{i + 1}"
                    add("article", number, title, pid, text, art["id"], chapter)
        else:
            body = [u for u in units_of(art)
                    if not u.startswith("Article ") and u != title]
            for i, text in enumerate(group(body)):
                add("article", number, title, "" if i == 0 else f"part{i + 1}", text, art["id"], chapter)

    # Recitals
    for rct in soup.find_all("div", id=re.compile(r"^rct_\d+$")):
        number = rct["id"].split("_")[1]
        text = clean(rct.get_text(" "))
        text = re.sub(rf"^\({number}\)\s*", "", text)
        for i, part in enumerate(group([text])):
            add("recital", number, "", "" if i == 0 else f"part{i + 1}", part, rct["id"])

    # Annexes
    for anx in soup.find_all("div", id=re.compile(r"^anx_[IVXLC]+$")):
        number = anx["id"].split("_")[1]
        ps = [clean(p.get_text(" ")) for p in anx.find_all("p")]
        ps = [p for p in ps if p]
        title = ps[1] if len(ps) > 1 else ""
        body = [p for p in ps[2:]]
        for i, text in enumerate(group(body)):
            add("annex", number, title, "" if i == 0 else f"part{i + 1}", text, anx["id"])

    return chunks


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    all_chunks = []
    for celex, reg in SOURCES.items():
        c = parse(celex, reg)
        kinds = {k: sum(1 for x in c if x["kind"] == k) for k in ("article", "recital", "annex")}
        arts = len({x["number"] for x in c if x["kind"] == "article"})
        print(f"{reg}: {len(c)} chunks, {arts} articles, {kinds}")
        all_chunks += c
    ids = [c["id"] for c in all_chunks]
    assert len(ids) == len(set(ids)), "duplicate chunk ids"
    with OUT.open("w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    lens = sorted(len(c["text"]) for c in all_chunks)
    print(f"total {len(all_chunks)} chunks; chars median {lens[len(lens)//2]}, max {lens[-1]}")


if __name__ == "__main__":
    main()

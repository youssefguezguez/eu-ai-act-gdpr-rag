"""Capture README screenshots of the running Gradio demo (python app.py must be running).

Uses the locally installed Microsoft Edge through Playwright (pip install playwright; no browser download).
python scripts/screenshots.py
"""
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs"
OUT.mkdir(exist_ok=True)
URL = "http://127.0.0.1:7860"
SHOTS = [
    ("answer.png", "Can my employer use AI to read my emotions during video calls?", True),
    ("decline.png", "What is the VAT rate on AI software in Germany?", False),
]

# wait for the server
import urllib.request
for _ in range(120):
    try:
        urllib.request.urlopen(URL, timeout=2)
        break
    except Exception:
        time.sleep(2)
else:
    sys.exit("demo not reachable on " + URL)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge")
    page = browser.new_page(viewport={"width": 1100, "height": 900}, device_scale_factor=1.5,
                            color_scheme="light", locale="en-US")
    for name, question, open_sources in SHOTS:
        page.goto(URL)
        page.get_by_label("Your question").fill(question)
        page.get_by_role("button", name="Ask").click()
        page.wait_for_function("document.body.innerText.includes(' s · ')", timeout=240_000)
        time.sleep(2)  # let the fade-in finish
        if open_sources:
            page.get_by_text("Sources retrieved").click()
            time.sleep(1)
        page.screenshot(path=str(OUT / name), full_page=True)
        print("saved", OUT / name)
    browser.close()

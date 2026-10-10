"""Polite one-time fetch of Dan's Editorial Checks public pages from checks.every.to.

Fetches the scoreboard, the JSON feed, and the run page behind every scoreboard cell,
saves the raw files to snapshot/raw/, and writes snapshot/benchmark.json.
Run: python3 fetch.py   (stdlib only, about 30 requests, 1 second apart)
"""
import json
import os
import re
import time
import urllib.request
from datetime import datetime, timezone

from checksignal.parse import BASE, parse_board, parse_run

SLUG = "dans-editorial-checks"
UA = "check-signal/0.1 (one-time public read; github.com/sivaratrisrinivas/check-signal)"
RAW = os.path.join("snapshot", "raw")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def norm(text):
    """Lowercase, drop apostrophes, collapse spaces: how a phrase list is usually matched."""
    text = text.lower().replace("\u2019", "").replace("'", "")
    return re.sub(r"\s+", " ", text)


def check_flagged_phrases(cell, page):
    """For a failing code check that names a phrase, download the public answer file
    and record whether that phrase appears in it. Plain string match, no AI."""
    for v in cell["verdicts"]:
        ev = v.get("evidence") or ""
        if v["kind"] != "code" or v["result"] != "fail" or "phrases:" not in ev:
            continue
        phrase = ev.split("phrases:", 1)[1].strip()
        v["flagged_phrase"] = phrase
        m = re.search(r'href="(/rails/active_storage/[^"]+?)"[^>]*>download', page)
        if not m:
            m = re.search(r'href="(/rails/active_storage/[^"]+?/ANSWER\.md\?disposition=attachment)"', page, re.I)
        if not m:
            v["answer_file_public"] = False
            continue
        time.sleep(1)
        answer = get(BASE + m.group(1).replace("&amp;", "&"))
        open(os.path.join(RAW, f"answer_{cell['run_id']}.md"), "w").write(answer)
        v["answer_file_public"] = True
        v["phrase_in_answer_file"] = norm(phrase) in norm(answer)


def main():
    os.makedirs(RAW, exist_ok=True)
    board_url = f"{BASE}/p/{SLUG}"
    board = get(board_url)
    open(os.path.join(RAW, "scoreboard.html"), "w").write(board)
    feed = json.loads(get(f"{board_url}/feed"))
    json.dump(feed, open(os.path.join(RAW, "feed.json"), "w"), indent=1)
    tasks, cells = parse_board(board)
    for c in cells:
        time.sleep(1)
        page = get(c["url"])
        open(os.path.join(RAW, f"run_{c['run_id']}.html"), "w").write(page)
        run = parse_run(page)
        c.update({k: run[k] for k in ("date", "tokens", "passed", "applicable", "verdicts")})
        check_flagged_phrases(c, page)
    snap = {
        "source": board_url,
        "feed_url": f"{board_url}/feed",
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "feed_generated_at": feed.get("generated_at"),
        "tasks": tasks,
        "models": [r["model"] for r in feed["runs"]],
        "feed": feed,
        "cells": cells,
    }
    json.dump(snap, open(os.path.join("snapshot", "benchmark.json"), "w"), indent=1, ensure_ascii=False)
    print(f"saved {len(cells)} cells, fetched_at {snap['fetched_at']}")


if __name__ == "__main__":
    main()

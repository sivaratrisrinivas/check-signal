# Check Signal

**Which checks on a personal AI benchmark actually decide the pick?**

Live: https://check-signal.onrender.com · 93 s video (voiced): https://check-signal.onrender.com/every-check-signal-demo.mp4 · [Memo](https://check-signal.onrender.com/memo.html)

**Why.** On release day you open your benchmark to decide whether to switch models. You see one score per model. You can't tell which of your own standards that score reflects, or whether a check can tell the models apart at all.

**What it found** on [Dan's Editorial Checks](https://checks.every.to/p/dans-editorial-checks), a public benchmark on [Checks](https://checks.every.to) by [Every](https://every.to) (5 models, 5 tasks, 25 runs, 34 checks, read 10 Oct 2026):

- **12 of 34 checks give every model the same result.** 11 always pass, 1 always fails. For each, a question: retire it, make it harder, reword it, or keep it on purpose?
- **The 80% five-way tie on the revision task isn't one.** 4 models miss R04; Sonnet 5.5 misses R01 instead.
- Counting only the 22 checks that decide, the ranking holds but the lead of GPT-6.1 Sol over GPT-6 Sol goes from 19 to 37 points.
- A few data oddities, shown as **questions, not bugs** (a shared phrase check that fails 4 of 5 models in one task only, missing token counts, one run per cell).
- Stretch: a **"Should I switch?"** card, check by check, with the judge's reason.

**How.** `fetch.py` reads the public scoreboard, JSON feed and the 25 run pages once (1 request per second). `checksignal/analyze.py` is plain rules. It first recomputes all 25 public scores from the run pages (25 of 25 match), then labels checks, finds ties and flags. `build.py` writes a static page. No AI calls.

```bash
git clone https://github.com/sivaratrisrinivas/check-signal && cd check-signal
python3 build.py && python3 -m http.server -d site 8000   # stdlib only; open localhost:8000
pip install -r requirements.txt && python3 -m pytest -q   # 12 plain tests, no eval set
python3 fetch.py && python3 build.py                      # optional: re-read the live pages
```

**Real vs not.** All numbers come from Every's public pages, snapshot in `snapshot/`. Nothing is simulated. The [v2 feed](site/feed-v2-example.json) is my proposal, generated from that data, not an Every format. I can't see Every's internals, so flags are questions.

Built by Srinivas Sivaratri as an independent prototype. Data credit: Every. Not affiliated with or endorsed by Every.

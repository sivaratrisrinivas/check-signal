"""Build the static Check Signal page from snapshot/benchmark.json. Stdlib only.
Run: python3 build.py   ->  site/index.html, site/memo.html, site/data.json, site/feed-v2-example.json
"""
import json
import os
from datetime import datetime, timedelta, timezone
from html import escape as e

from checksignal.analyze import (check_matrix, deciding_only_scores, flags, hidden_ties, label,
                                 rank, reconcile, spread, suggestion, summary, switch, task_scores)

SNAP = os.path.join("snapshot", "benchmark.json")
OUT = "site"
REPO = "https://github.com/sivaratrisrinivas/check-signal"
VIDEO = "every-check-signal-demo.mp4"
GUIDE = "https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark"

CSS = """
:root{--ink:#16181d;--ink2:#4a4f5a;--mute:#7b8190;--rule:#e4e2dc;--bg:#fbfaf7;--card:#fff;--pass:#1f7a4d;--fail:#b4442f;--same:#8a6d1f;--accent:#2b4fd8}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif}
main{max-width:1060px;margin:0 auto;padding:28px 24px 80px}
a{color:var(--accent)}h1{font-size:34px;line-height:1.15;margin:0 0 6px;letter-spacing:-.01em}h2{font-size:25px;margin:0 0 6px;letter-spacing:-.01em}h3{font-size:18px;margin:0 0 6px}
.sub{color:var(--ink2);margin:0 0 4px}.small{font-size:14px;color:var(--mute)}
section{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:24px 26px;margin:20px 0}
.lede{font-size:19px;color:var(--ink2);max-width:820px}
.big{display:flex;gap:14px;flex-wrap:wrap;margin:16px 0 6px}.stat{flex:1;min-width:150px;border:1px solid var(--rule);border-radius:10px;padding:12px 14px;background:#fff}
.stat b{display:block;font-size:30px;line-height:1.1}.stat span{font-size:14px;color:var(--ink2)}
.stat.hot{border-color:var(--same);background:#fffaf0}.stat.hot b{color:var(--same)}
.headline{font-size:28px;font-weight:700;margin:4px 0 2px;line-height:1.2}
.ok{display:inline-block;font-size:14px;background:#eef7f1;color:var(--pass);border-radius:999px;padding:3px 10px;margin-top:8px}
table{width:100%;border-collapse:collapse;font-size:15px}th,td{text-align:left;padding:8px 8px;border-bottom:1px solid var(--rule);vertical-align:top}th{font-size:13px;color:var(--mute);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.pill{display:inline-block;white-space:nowrap;border-radius:6px;padding:1px 8px;font-size:13px;font-weight:600}.p{background:#e8f4ed;color:var(--pass)}.f{background:#f8e9e5;color:var(--fail)}
.dots{white-space:nowrap}.dot{display:inline-block;width:14px;height:14px;border-radius:3px;margin-right:3px;vertical-align:-2px}.dot.p{background:var(--pass)}.dot.f{background:var(--fail)}
.q{font-weight:650;color:var(--same)}.task{font-size:13px;color:var(--mute)}
.tie{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}.chip{border:1px solid var(--rule);border-radius:10px;padding:10px 12px;min-width:150px;background:#fff}.chip b{font-size:24px;display:block}
.split{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px}.group{border:1px solid var(--rule);border-radius:10px;padding:14px 16px;background:#fff}.group.alt{border-color:var(--fail);background:#fff8f6}
.group h3{font-size:16px}details summary{cursor:pointer;color:var(--accent);font-size:14px;margin-top:6px}blockquote{margin:6px 0 0;padding-left:10px;border-left:3px solid var(--rule);color:var(--ink2);font-size:14.5px}
.flag{border-left:4px solid var(--same);padding:10px 14px;margin:12px 0;background:#fffcf3;border-radius:0 8px 8px 0}.flag ul{margin:6px 0;padding-left:20px;font-size:15px;color:var(--ink2)}
.bar{height:10px;background:#eceae4;border-radius:5px;overflow:hidden;min-width:120px}.bar i{display:block;height:100%;background:var(--ink2)}
select{font:inherit;padding:6px 8px;border-radius:8px;border:1px solid var(--rule);background:#fff}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:14px}.gain h3{color:var(--pass)}.loss h3{color:var(--fail)}
.gain li,.loss li{margin:6px 0;font-size:15px}.why{color:var(--ink2);font-size:14px}
nav{font-size:14px;margin:8px 0 0}nav a{margin-right:12px}
footer{font-size:14px;color:var(--mute);margin-top:30px}
code{background:#f1efe9;padding:1px 5px;border-radius:4px;font-size:14px}
"""


def dots(results, models):
    return "".join(f'<span class="dot {"p" if results.get(m) == "pass" else "f"}" title="{e(m)}: {results.get(m)}"></span>' for m in models)


def short_task(t):
    return t


def ist(utc_str):
    d = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) + timedelta(hours=5, minutes=30)
    return d.strftime("%-d %b %Y, %H:%M IST")


def build():
    snap = json.load(open(SNAP))
    models = list(dict.fromkeys(c["model"] for c in snap["cells"]))  # scoreboard order
    rows = check_matrix(snap)
    s = summary(snap)
    rec = reconcile(snap)
    _, overall = task_scores(snap)
    dtasks, doverall = deciding_only_scores(snap)
    ties = hidden_ties(snap)
    fl = flags(snap)
    same = [r for r in rows if label(r) != "decides"]
    decides = sorted([r for r in rows if label(r) == "decides"], key=lambda r: (-spread(r), r["task"]))
    src = snap["source"]
    fetched = ist(snap["fetched_at"])
    legend = " ".join(f"{i + 1}. {e(m)}" for i, m in enumerate(models))

    h = []
    h.append(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check Signal: which checks on Dan's Editorial Checks actually decide?</title><style>{CSS}</style></head><body><main>
<header id="top"><div class="small">Check Signal · a prototype by Srinivas Sivaratri · data: <a href="{src}">Dan's Editorial Checks</a> by <a href="https://every.to">Every</a>, public pages read {e(fetched)}</div>
<h1>Which checks actually decide the pick?</h1>
<p class="sub">A one-page read of one public Checks benchmark: {s['models']} models, {s['tasks']} tasks, {s['runs']} runs, {s['checks']} checks. Rules only, no AI calls.</p>
<nav><a href="#why">Why</a><a href="#tie">The 80% tie</a><a href="#same">Same-result checks</a><a href="#gaps">Scores</a><a href="#decide">Checks that decide</a><a href="#look">Worth a look</a><a href="#switch">Should I switch?</a><a href="memo.html">Memo</a><a href="{VIDEO}">Video</a><a href="{REPO}">Code</a></nav></header>""")

    # WHY
    h.append(f"""<section id="why"><h2>Release day</h2>
<p class="lede">A new model ships. You open your benchmark to decide whether to switch. You see one number per model. You can't see which of your own standards that number reflects, or whether a check can tell the models apart at all.</p>
<p class="headline">{s['same_result']} of {s['checks']} checks give every model the same result.</p>
<div class="big"><div class="stat hot"><b>{s['always_pass']}</b><span>always pass, for all {s['models']} models</span></div>
<div class="stat hot"><b>{s['always_fail']}</b><span>always fails, for all {s['models']} models</span></div>
<div class="stat"><b>{s['decides']}</b><span>actually separate the models</span></div>
<div class="stat"><b>{s['share_same_pct']}%</b><span>of checks can't help you pick</span></div></div>
<p class="small">They still count toward every score. That isn't wrong. Some are floors on purpose. But it's worth knowing which checks carry the decision.</p>
<span class="ok">Recomputed all {rec['cells_checked']} scoreboard cells and {len(models)} overall scores from the run pages: {rec['cells_checked'] - len(rec['cell_mismatches'])} of {rec['cells_checked']} match</span></section>""")

    # TIE
    if ties:
        t = ties[0]
        cells = {c["model"]: c for c in snap["cells"] if c["task"] == t["task"]}
        chips = "".join(f'<div class="chip"><span class="small">{e(m)}</span><b>{t["score"]}%</b></div>' for m in t["models"])
        groups = []
        for i, p in enumerate(t["patterns"]):
            quotes = "".join(f"<blockquote><b>{e(m)}</b> on <i>{e(ch)}</i>: {e(t['reasons'].get(m + '::' + ch) or '')}</blockquote>"
                             for m in p["models"] for ch in p["failed"])
            groups.append(f'<div class="group{" alt" if i else ""}"><h3>{len(p["models"])} model{"s" if len(p["models"]) > 1 else ""} missed: {e("; ".join(p["failed"]))}</h3>'
                          f'<div>{e(", ".join(p["models"]))}</div><details><summary>Judge\'s reasoning</summary>{quotes}</details></div>')
        others = "".join(f"<li><b>{e(x['task'])}</b>: {', '.join(e(m) for m in x['models'])} all score {x['score']}%, with {len(x['patterns'])} different sets of misses</li>" for x in ties[1:])
        h.append(f"""<section id="tie"><h2>A {t['score']}% tie that isn't one</h2>
<p class="lede">On <b>{e(t['task'])}</b>, all {len(t['models'])} models score {t['score']}%. Read as a scoreboard, they are the same. Open the checks and they fail in different ways.</p>
<div class="tie">{chips}</div><div class="split">{''.join(groups)}</div>
<p class="small" style="margin-top:12px">If the standard you care most about is the one only {e(", ".join(t['patterns'][-1]['models']))} misses, the tie hides your answer.</p>
<details><summary>Other ties with different misses ({len(ties) - 1})</summary><ul>{others}</ul></details></section>""")

    # SAME
    trs = []
    for r in sorted(same, key=lambda r: (label(r) != "always_fail", r["scope"] == "every task", r["task"])):
        q, why = suggestion(r)
        res = '<span class="pill p">all pass</span>' if label(r) == "always_pass" else '<span class="pill f">all fail</span>'
        trs.append(f'<tr><td><b>{e(r["check"])}</b><div class="task">{e(r["task"])} · {"code check" if r["kind"] == "code" else "LLM-judged"}{" · shared by every task" if r["scope"] == "every task" else ""}</div></td>'
                   f'<td>{res}</td><td><span class="q">{e(q)}</span><div class="why">{e(why)}</div></td></tr>')
    h.append(f"""<section id="same"><h2>{s['same_result']} checks that give everyone the same result</h2>
<p class="lede">For each one, a question for the benchmark owner. Retire it, make it harder, reword it, or keep it on purpose.</p>
<table><tr><th>Check</th><th>Result</th><th>Question</th></tr>{''.join(trs)}</table></section>""")

    # GAPS
    ro, rd = rank(overall), rank(doverall)
    lead = ro[0]
    gaps = "".join(f'<tr><td>{e(m)}</td><td>{round(overall[m])}%</td><td>{round(doverall[m])}%</td>'
                   f'<td><div class="bar"><i style="width:{doverall[m]:.0f}%"></i></div></td></tr>' for m in ro)
    second = ro[1]
    h.append(f"""<section id="gaps"><h2>What the score looks like with only the checks that decide</h2>
<p class="lede">Same formula as the scoreboard (checks passed over checks applicable, then the mean across tasks), counting only the {s['decides']} checks that separate models.</p>
<table><tr><th>Model</th><th>Public overall</th><th>Deciding checks only</th><th></th></tr>{gaps}</table>
<p class="small">The ranking {"stays the same" if ro == rd else "changes"}. The gaps move: {e(lead)} leads {e(second)} by {round(overall[lead] - overall[second])} points on the public score and by {round(doverall[lead] - doverall[second])} points on deciding checks. Same-result checks add the same points to everyone, which makes models look closer than they are.</p></section>""")

    # DECIDES
    drows = "".join(f'<tr><td><b>{e(r["check"])}</b><div class="task">{e(r["task"])}</div></td><td class="dots">{dots(r["results"], models)}</td>'
                    f'<td>{list(r["results"].values()).count("pass")} of {len(r["results"])} pass</td></tr>' for r in decides)
    h.append(f"""<section id="decide"><h2>{s['decides']} checks that decide</h2>
<p class="lede">Most even splits first. These are the standards that actually move the pick.</p>
<p class="small">Model order: {legend}. Green passed, red failed.</p>
<details open><summary>Show or hide the list</summary><table><tr><th>Check</th><th>Models</th><th>Split</th></tr>{drows}</table></details></section>""")

    # FLAGS
    fh = "".join(f'<div class="flag"><h3>{e(f["title"])}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in f["facts"])}</ul><div class="q">{e(f["question"])}</div></div>' for f in fl)
    h.append(f"""<section id="look"><h2>Worth a look</h2>
<p class="lede">Things in the public data that may have a simple explanation. Questions, not bugs. I can't see inside Every's system.</p>{fh}
<p class="small">The phrase check: I downloaded each failing run's public ANSWER.md and did a plain text match (case and apostrophes ignored).</p></section>""")

    # SWITCH
    opts = "".join(f"<option>{e(m)}</option>" for m in models)
    h.append(f"""<section id="switch"><h2>Should I switch?</h2>
<p class="lede">Pick the model you use now and the one you're considering. See which of your standards it newly clears and which it drops, with the judge's reason.</p>
<p>I use <select id="cur">{opts}</select> and I'm looking at <select id="cand">{opts}</select></p>
<div id="sw"></div></section>""")

    h.append(f"""<section id="memo-teaser"><h2>One platform idea</h2>
<p class="lede">The public <a href="{snap['feed_url']}">JSON feed</a> has task-level scores only. To build this page I had to read {s['runs']} HTML run pages. A check-level feed would let anyone build tools like this on Checks.</p>
<p><a href="memo.html">Read the one-page memo</a> · <a href="feed-v2-example.json">example check-level feed, generated from this data</a></p></section>""")

    h.append(f"""<footer>Data: <a href="{src}">Dan's Editorial Checks</a> on <a href="https://checks.every.to">Checks</a> by <a href="https://every.to">Every</a>, public scoreboard, feed and run pages, read {e(fetched)} (feed generated {e(ist(snap['feed_generated_at']))}). Built by Srinivas Sivaratri as an independent prototype. Not affiliated with or endorsed by Every. Rules only, no AI calls. <a href="{REPO}">Source</a>.</footer>""")

    sw_data = {"models": models, "rows": [{"task": r["task"], "check": r["check"], "results": r["results"],
               "why": {m: (r["reasons"].get(m) or r["evidence"].get(m)) for m in models}} for r in rows]}
    h.append("<script>const D=" + json.dumps(sw_data, ensure_ascii=False).replace("</", "<\\/") + ";\n" + r"""
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const cur=document.getElementById('cur'),cand=document.getElementById('cand');
const q=new URLSearchParams(location.search);cur.value=q.get('from')||'GPT-6 Sol';cand.value=q.get('to')||'GPT-6.1 Sol';
function render(){const a=cur.value,b=cand.value,g=[],l=[];let same=0,bothFail=0;
for(const r of D.rows){const x=r.results[a],y=r.results[b];if(!x||!y)continue;
if(x!=='pass'&&y==='pass')g.push(r);else if(x==='pass'&&y!=='pass')l.push(r);else if(x==='pass')same++;else bothFail++;}
const li=(r,m)=>`<li><b>${esc(r.check)}</b> <span class="task">${esc(r.task)}</span><div class="why">${esc(r.why[m])}</div></li>`;
document.getElementById('sw').innerHTML=a===b?'<p class="small">Pick two different models.</p>':
`<p class="headline" style="font-size:22px">${esc(b)} newly clears ${g.length} of your checks and drops ${l.length}.</p>
<div class="cols"><div class="gain"><h3>Newly clears (${g.length})</h3><ul>${g.map(r=>li(r,b)).join('')||'<li>None</li>'}</ul></div>
<div class="loss"><h3>Drops (${l.length})</h3><ul>${l.map(r=>li(r,b)).join('')||'<li>None</li>'}</ul></div></div>
<p class="small">${same} checks both pass, ${bothFail} both fail. One run per model, so a single flip could be noise. Judge reasons shown for ${esc(b)}.</p>`;}
cur.onchange=cand.onchange=render;render();
</script></main></body></html>""")
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "index.html"), "w").write("\n".join(h))

    # data + v2 feed example
    json.dump({"summary": s, "reconcile": rec, "flags": fl, "ties": ties,
               "deciding_only_overall": {m: round(v) for m, v in doverall.items()},
               "public_overall": {m: round(v) for m, v in overall.items()},
               "same_result_checks": [{"task": r["task"], "check": r["check"], "label": label(r), "question": suggestion(r)[0]} for r in same],
               "source": src, "fetched_at": snap["fetched_at"]},
              open(os.path.join(OUT, "data.json"), "w"), indent=1, ensure_ascii=False)
    v2 = {"schema": "every-benchmark-result/v2 (proposal, not an Every format)",
          "note": "Generated by Check Signal from public run pages, to show the shape. v1 fields kept; checks added per run.",
          "benchmark": snap["feed"]["benchmark"], "generated_at": snap["feed"]["generated_at"], "runs": []}
    by_model = {r["model"]: r for r in snap["feed"]["runs"]}
    for m in models:
        run = dict(by_model[m])
        run["cases"] = []
        for c in snap["cells"]:
            if c["model"] != m:
                continue
            run["cases"].append({"task": c["task"], "run_url": c["url"], "date": c["date"], "tokens": c["tokens"],
                                 "passed": c["passed"], "applicable": c["applicable"],
                                 "checks": [{"id": v["check"], "kind": v["kind"], "scope": v["scope"], "result": v["result"],
                                             "evidence": v.get("reason") or v.get("evidence")} for v in c["verdicts"]]})
        v2["runs"].append(run)
    json.dump(v2, open(os.path.join(OUT, "feed-v2-example.json"), "w"), indent=1, ensure_ascii=False)
    build_memo(snap, s, ties, fl)
    print(f"built site/: {s['same_result']} of {s['checks']} same-result checks; reconcile mismatches: {len(rec['cell_mismatches'])}")


def build_memo(snap, s, ties, fl):
    t = ties[0] if ties else None
    src = snap["source"]
    body = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Check Signal memo</title><style>{CSS} main{{max-width:760px}} li{{margin:6px 0}}</style></head><body><main>
<p class="small"><a href="index.html">Back to Check Signal</a></p>
<h1>Memo: check-level results in the public feed</h1>
<p class="sub">Srinivas Sivaratri · one page · data from <a href="{src}">Dan's Editorial Checks</a> by <a href="https://every.to">Every</a>, read {e(ist(snap['fetched_at']))}</p>
<section><h2>The user problem</h2>
<p>Someone picking a model sees one score per model. The score can't say which of their standards it reflects. On Dan's Editorial Checks, {s['same_result']} of {s['checks']} checks give every model the same result{f", and a {t['score']}% tie on {e(t['task'])} hides different misses" if t else ""}. The check-level data that shows this is public, but only in HTML run pages.</p></section>
<section><h2>The proposal</h2>
<p>Add check-level results to the JSON feed. Keep every v1 field. Under each run, list cases, and under each case, list checks with <code>id</code>, <code>kind</code> (code or model), <code>scope</code>, <code>result</code> and a short <code>evidence</code> string. <a href="feed-v2-example.json">Example generated from today's data</a>.</p>
<p>Why it matters for a platform: the role description talks about a platform people can build on (cases, checks, runs, results). Check-level data is what outside tools need: a release-day "should I switch?" card, a saturation alarm, a judge spot check.</p></section>
<section><h2>What I built, and what I cut</h2>
<ul><li>Built: a rules-only page that finds same-result checks, ties that hide different misses, and data oddities, plus a check-by-check "switch?" card. It reproduces every public scoreboard cell from the run pages.</li>
<li>Cut: LLM features, re-running models, auth, writing back to Checks. Rules answer these questions exactly, and saying so is part of the product call.</li>
<li>Limits: one run per cell, so variance is flagged, not measured. "Same result" is treated as a question, since some checks are floors on purpose.</li></ul></section>
<section><h2>Questions I would ask with internal data</h2>
<ul><li>Are the always-pass checks intentional floors? Is the always-fail check tracking a known gap, or is it stricter than intended?</li>
<li>Where does the flagged phrase on tend-feed-card-writing come from? It isn't in the public answer files I could download.</li>
<li>Are the low or missing token counts on some Opus 5.5 runs complete?</li>
<li>How long does a benchmark tuning review take today? That decides how much time this saves.</li></ul></section>
<section><h2>How I'd measure it in the product</h2>
<ul><li>Share of checks that separate models, per benchmark, over time.</li>
<li>Share of benchmarks where a flag is acted on within a week.</li>
<li>"Switch" decisions later reversed (the failure metric).</li></ul></section>
</main></body></html>"""
    open(os.path.join(OUT, "memo.html"), "w").write(body)


if __name__ == "__main__":
    build()

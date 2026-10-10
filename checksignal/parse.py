"""Parse public Checks pages (scoreboard + run pages) into plain dicts. Stdlib only."""
import html
import re

BASE = "https://checks.every.to"


def _text(fragment):
    t = re.sub(r"<[^>]+>", " ", fragment or "")
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def parse_board(page):
    """Return (tasks, cells) from the scoreboard. cells: {model, task, score, run_id, url}."""
    tasks = []
    thead = re.search(r"<thead.*?</thead>", page, re.S)
    if thead:
        for th in re.findall(r"<th[^>]*>(.*?)</th>", thead.group(0), re.S):
            name = _text(th)
            if name and name not in ("Model", "Overall"):
                tasks.append(name)
    cells = []
    for row in re.findall(r"<tr>(.*?)</tr>", page, re.S):
        head = re.search(r'class="rowhead"><a[^>]*>(.*?)</a>', row, re.S)
        if not head:
            continue
        model = _text(head.group(1))
        tds = re.findall(r'<td class="(?!overall)[^"]*">(.*?)</td>', row, re.S)
        for task, td in zip(tasks, tds):
            m = re.search(r'href="(/p/[^"]+/runs/(\d+))">\s*(\d+)%', td)
            if m:
                cells.append({"model": model, "task": task, "score": int(m.group(3)),
                              "run_id": int(m.group(2)), "url": BASE + m.group(1)})
    return tasks, cells


def parse_run(page):
    """Return run metadata and every verdict shown on one public run page."""
    body = _text(page)
    out = {"title": _text(re.search(r"<title>(.*?)</title>", page, re.S).group(1))}
    m = re.search(r"run (\d{1,2} \w{3} \d{4})", body)
    out["date"] = m.group(1) if m else None
    head = body.split("Instructions")[0]
    m = re.search(r"([\d,]+) tokens", head)
    out["tokens"] = int(m.group(1).replace(",", "")) if m else None
    m = re.search(r'<span class="score-lg">(\d+)/(\d+)</span>', page)
    out["passed"], out["applicable"] = (int(m.group(1)), int(m.group(2))) if m else (None, None)
    verdicts = []
    for b in re.split(r'<div class="verdict" id="verdict_\d+">', page)[1:]:
        b = re.split(r'<details class="disclosure passed|<h2 class="eyebrow', b)[0]
        pill = re.search(r'class="pill pill-(\w+)"', b)
        name = re.search(r'<p class="name">(.*?)<span class="chip[^"]*">(.*?)</span>', b, re.S)
        reason = re.search(r"Judge(?:&#39;|')s reasoning</p>.*?<p class=\"body\"[^>]*>(.*?)</p>", b, re.S)
        rubric = re.search(r"<summary>Rubric</summary><p[^>]*>(.*?)</p>", b, re.S)
        desc = re.search(r'<p class="desc">(.*?)</p>', b, re.S)
        evidence = re.search(r'<p class="mono[^"]*"[^>]*>(.*?)</p>', b, re.S)
        verdicts.append({
            "check": _text(name.group(1)) if name else None,
            "scope": _text(name.group(2)) if name else None,
            "result": pill.group(1) if pill else None,
            "kind": "model" if rubric or reason else "code",
            "reason": _text(reason.group(1)) if reason else None,
            "question": _text(rubric.group(1)).split(" Context:")[0][:300] if rubric else _text(desc.group(1)) if desc else None,
            "evidence": _text(evidence.group(1)) if evidence else None,
        })
    out["verdicts"] = verdicts
    return out

"""Rules-only analysis of a Checks benchmark snapshot. No AI calls, stdlib only.

Input: the dict written by fetch.py (snapshot/benchmark.json).
Every number the page shows comes from a function in this file.
"""
from collections import defaultdict
from statistics import median

SHARED_SCOPE = "every task"


def check_matrix(snap):
    """One row per (task, check): results per model plus metadata."""
    rows = {}
    for c in snap["cells"]:
        for v in c["verdicts"]:
            key = (c["task"], v["check"])
            row = rows.setdefault(key, {
                "task": c["task"], "check": v["check"], "kind": v["kind"],
                "scope": v["scope"], "question": v.get("question"),
                "results": {}, "reasons": {}, "evidence": {},
            })
            row["results"][c["model"]] = v["result"]
            row["reasons"][c["model"]] = v.get("reason")
            row["evidence"][c["model"]] = v.get("evidence")
    return list(rows.values())


def label(row):
    """'always_pass', 'always_fail' or 'decides'."""
    vals = set(row["results"].values())
    if vals == {"pass"}:
        return "always_pass"
    if vals == {"fail"}:
        return "always_fail"
    return "decides"


def suggestion(row):
    """A question-shaped suggestion for checks that give every model the same result."""
    lab = label(row)
    if lab == "always_pass" and row["scope"] == SHARED_SCOPE:
        return ("Keep as a floor, shown apart from the score?",
                "A shared floor every model clears. Useful as a guard, but it lifts every score by the same amount.")
    if lab == "always_pass":
        return ("Retire or make harder?",
                "Every model clears it, so it can't help pick one. If it still matters, a stricter version might.")
    if lab == "always_fail":
        return ("Reword, or keep as a known gap?",
                "No model clears it. Is that a real gap all models share, or could the wording be stricter than intended?")
    return ("Keep", "Models split on it, so it helps the pick.")


def spread(row):
    """How evenly models split: min(passes, fails). Higher means more decisive."""
    vals = list(row["results"].values())
    return min(vals.count("pass"), vals.count("fail"))


def summary(snap):
    rows = check_matrix(snap)
    same = [r for r in rows if label(r) != "decides"]
    model_rows = [r for r in rows if r["kind"] == "model"]
    return {
        "models": len(snap["models"]),
        "tasks": len(snap["tasks"]),
        "runs": len(snap["cells"]),
        "checks": len(rows),
        "same_result": len(same),
        "always_pass": sum(label(r) == "always_pass" for r in rows),
        "always_fail": sum(label(r) == "always_fail" for r in rows),
        "decides": len(rows) - len(same),
        "model_checks": len(model_rows),
        "model_checks_always_pass": sum(label(r) == "always_pass" for r in model_rows),
        "share_same_pct": round(100 * len(same) / len(rows)) if rows else 0,
    }


def task_scores(snap, keep=None):
    """Recompute task and overall scores the way the scoreboard describes them:
    a run is checks passed over checks applicable, Overall is the mean across tasks.
    keep: optional predicate on (task, check) to score only some checks."""
    scores = defaultdict(dict)
    for c in snap["cells"]:
        vs = [v for v in c["verdicts"] if keep is None or keep(c["task"], v["check"])]
        if not vs:
            continue
        scores[c["model"]][c["task"]] = 100 * sum(v["result"] == "pass" for v in vs) / len(vs)
    overall = {m: sum(t.values()) / len(t) for m, t in scores.items()}
    return dict(scores), overall


def reconcile(snap):
    """Do our parsed verdicts reproduce the public scoreboard cell by cell?"""
    mine, _ = task_scores(snap)
    bad = [(c["model"], c["task"], c["score"], round(mine[c["model"]][c["task"]]))
           for c in snap["cells"] if round(mine[c["model"]][c["task"]]) != c["score"]]
    feed_avg = {r["model"]: r["avg"] for r in snap["feed"]["runs"]}
    _, overall = task_scores(snap)
    bad_overall = [(m, feed_avg[m], round(o)) for m, o in overall.items() if round(o) != feed_avg.get(m)]
    return {"cells_checked": len(snap["cells"]), "cell_mismatches": bad, "overall_mismatches": bad_overall}


def deciding_only_scores(snap):
    """Scores if only checks that separate models were counted."""
    deciding = {(r["task"], r["check"]) for r in check_matrix(snap) if label(r) == "decides"}
    return task_scores(snap, keep=lambda t, ch: (t, ch) in deciding)


def rank(overall):
    return [m for m, _ in sorted(overall.items(), key=lambda kv: -kv[1])]


def hidden_ties(snap):
    """Tasks where 2+ models have the same score but failed different checks."""
    out = []
    by_task = defaultdict(list)
    for c in snap["cells"]:
        failed = tuple(sorted(v["check"] for v in c["verdicts"] if v["result"] != "pass"))
        by_task[c["task"]].append((c["score"], c["model"], failed, c))
    for task, items in by_task.items():
        groups = defaultdict(list)
        for score, model, failed, c in items:
            groups[score].append((model, failed, c))
        for score, members in groups.items():
            if len(members) < 2:
                continue
            patterns = defaultdict(list)
            for model, failed, c in members:
                patterns[failed].append(model)
            if len(patterns) > 1:
                reasons = {}
                for model, failed, c in members:
                    for v in c["verdicts"]:
                        if v["result"] != "pass":
                            reasons[(model, v["check"])] = v.get("reason") or v.get("evidence")
                out.append({
                    "task": task, "score": score, "models": [m for m, _, _ in members],
                    "patterns": [{"failed": list(f), "models": ms} for f, ms in
                                 sorted(patterns.items(), key=lambda kv: -len(kv[1]))],
                    "reasons": {f"{m}::{ch}": r for (m, ch), r in reasons.items()},
                })
    return sorted(out, key=lambda t: -len(t["models"]))


def _parse_date(s):
    from datetime import datetime
    return datetime.strptime(s, "%d %b %Y").date() if s else None


def flags(snap):
    """Data oddities, phrased as questions. Never called bugs."""
    out = []
    rows = check_matrix(snap)
    # 1. Shared check that fails only in one task, with the same evidence everywhere.
    for r in rows:
        if r["scope"] != SHARED_SCOPE or r["kind"] != "code":
            continue
        fails = [m for m, v in r["results"].items() if v == "fail"]
        if not fails:
            continue
        other_tasks_fail = any(o["check"] == r["check"] and o["task"] != r["task"]
                               and "fail" in o["results"].values() for o in rows)
        if other_tasks_fail:
            continue
        phrases = {r["evidence"][m] for m in fails}
        detail = []
        for c in snap["cells"]:
            if c["task"] != r["task"]:
                continue
            for v in c["verdicts"]:
                if v["check"] == r["check"] and "flagged_phrase" in v:
                    if not v.get("answer_file_public"):
                        detail.append(f"{c['model']}: no public answer file to compare")
                    else:
                        detail.append(f"{c['model']}: phrase {'found' if v['phrase_in_answer_file'] else 'not found'} in the public ANSWER.md")
        for c in snap["cells"]:
            if c["task"] == r["task"] and r["results"].get(c["model"]) == "pass":
                detail.append(f"{c['model']} passes; its run is dated {c['date']} and its evidence says \u201c{r['evidence'][c['model']]}\u201d")
        found_none = all("not found" in d or "no public" in d for d in detail if "passes;" not in d) and detail
        out.append({
            "id": "shared-check-one-task",
            "title": f"Shared check \u201c{r['check']}\u201d fails {len(fails)} of {len(r['results'])} models, only in {r['task']}",
            "facts": [f"Evidence on every failing run: \u201c{'; '.join(sorted(phrases))}\u201d",
                      f"Passes on all models in the other {len(snap['tasks']) - 1} tasks"] + detail,
            "question": ("Is the phrase coming from a file other than the answer, like an input the check also reads?"
                         if found_none else "Is this phrase really in all of these answers?"),
        })
    # 2. Token counts missing or far below the task median.
    by_task = defaultdict(list)
    for c in snap["cells"]:
        by_task[c["task"]].append(c)
    odd = []
    for task, cs in by_task.items():
        known = [c["tokens"] for c in cs if c["tokens"]]
        med = median(known) if known else 0
        for c in cs:
            if c["tokens"] is None:
                odd.append(f"{c['model']} on {task}: no token count shown")
            elif med and c["tokens"] < med / 5:
                odd.append(f"{c['model']} on {task}: {c['tokens']:,} tokens vs a task median of {int(med):,}")
    if odd:
        out.append({"id": "tokens", "title": f"{len(odd)} runs show missing or very low token counts",
                    "facts": odd,
                    "question": "Are these counts complete? A cost view built on them would favor these runs."})
    # 3. Run dates and one run per cell.
    dates = [_parse_date(c["date"]) for c in snap["cells"] if c["date"]]
    if dates:
        per_model = defaultdict(set)
        for c in snap["cells"]:
            per_model[c["model"]].add(c["date"])
        mixed = [m for m, d in per_model.items() if len(d) > 1]
        out.append({"id": "single-run", "title": f"Every cell is one run; runs span {min(dates):%-d %b} to {max(dates):%-d %b %Y}",
                    "facts": [f"{len(snap['cells'])} cells, 1 latest run each, so run-to-run variance isn't visible",
                              f"Models with runs on more than one date: {', '.join(mixed) or 'none'}"],
                    "question": "Would 3 runs per cell change any tie or gap of one check? Every\u2019s own guide suggests running a task three times."})
    # 4. Code check read different files for the same task.
    for task in snap["tasks"]:
        seen = defaultdict(list)
        for c in snap["cells"]:
            if c["task"] != task:
                continue
            for v in c["verdicts"]:
                ev = v.get("evidence") or ""
                if v["kind"] == "code" and ev.startswith("inspected"):
                    seen[ev].append(c["model"])
        if len(seen) > 1:
            out.append({"id": f"inspected-{task}", "title": f"The shared code check read different files on {task}",
                        "facts": [f"{', '.join(ms)}: {ev}" for ev, ms in seen.items()],
                        "question": "Should every model's answer be checked against the same set of files?"})
    return out


def switch(snap, current, candidate):
    """Check-by-check diff between two models."""
    gained, lost, both_pass, both_fail = [], [], [], []
    for r in check_matrix(snap):
        a, b = r["results"].get(current), r["results"].get(candidate)
        if a is None or b is None:
            continue
        item = {"task": r["task"], "check": r["check"], "why": r["reasons"].get(candidate) or r["evidence"].get(candidate),
                "why_current": r["reasons"].get(current) or r["evidence"].get(current)}
        if a != "pass" and b == "pass":
            gained.append(item)
        elif a == "pass" and b != "pass":
            lost.append(item)
        elif a == "pass":
            both_pass.append(item)
        else:
            both_fail.append(item)
    return {"current": current, "candidate": candidate, "gained": gained, "lost": lost,
            "both_pass": len(both_pass), "both_fail": len(both_fail)}

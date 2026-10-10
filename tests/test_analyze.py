"""Plain tests on a tiny hand-made benchmark. No eval set, no network."""
from checksignal.analyze import (check_matrix, deciding_only_scores, flags, hidden_ties, label,
                                 reconcile, suggestion, summary, switch)
from checksignal.parse import parse_board, parse_run


def v(check, result, kind="model", scope="this case", evidence=None, reason="quote"):
    return {"check": check, "result": result, "kind": kind, "scope": scope,
            "reason": reason if kind == "model" else None, "evidence": evidence, "question": check}


def cell(model, task, verdicts, date="1 Oct 2026", tokens=100000):
    p = sum(x["result"] == "pass" for x in verdicts)
    return {"model": model, "task": task, "verdicts": verdicts, "date": date, "tokens": tokens,
            "score": round(100 * p / len(verdicts)), "run_id": hash((model, task)) % 1000}


def fixture():
    floor = lambda r="pass", ev="inspected ANSWER.md": v("ai-wording", r, "code", "every task", ev)
    cells = [
        # task t1: "easy" always passes, "hard" always fails, "split" decides
        cell("A", "t1", [v("easy", "pass"), v("hard", "fail"), v("split", "pass"), floor()]),
        cell("B", "t1", [v("easy", "pass"), v("hard", "fail"), v("split", "fail"), floor()]),
        cell("C", "t1", [v("easy", "pass"), v("hard", "fail"), v("split", "fail"), floor()]),
        # task t2: all score 50 but miss different checks; floor fails here only
        cell("A", "t2", [v("x", "fail"), v("y", "pass"), floor("pass", "inspected answer.md")], tokens=None),
        cell("B", "t2", [v("x", "pass"), v("y", "fail"), floor("fail", "shared AI-tell phrases: zap")]),
        cell("C", "t2", [v("x", "fail"), v("y", "pass"), floor("fail", "shared AI-tell phrases: zap")], date="2 Oct 2026"),
    ]
    for c in cells:
        c["score"] = round(100 * sum(x["result"] == "pass" for x in c["verdicts"]) / len(c["verdicts"]))
    feed = {"runs": [{"model": m, "avg": None} for m in "ABC"]}
    snap = {"models": ["A", "B", "C"], "tasks": ["t1", "t2"], "cells": cells, "feed": feed}
    from checksignal.analyze import task_scores
    _, overall = task_scores(snap)
    for r in feed["runs"]:
        r["avg"] = round(overall[r["model"]])
    return snap


def row(snap, task, check):
    return next(r for r in check_matrix(snap) if r["task"] == task and r["check"] == check)


def test_saturated_and_floor_labels():
    s = fixture()
    assert label(row(s, "t1", "easy")) == "always_pass"
    assert label(row(s, "t1", "hard")) == "always_fail"
    assert label(row(s, "t1", "split")) == "decides"


def test_suggestions_are_questions():
    s = fixture()
    for r in check_matrix(s):
        if label(r) != "decides":
            assert suggestion(r)[0].endswith("?")
    assert suggestion(row(s, "t1", "ai-wording"))[0].startswith("Keep as a floor")
    assert suggestion(row(s, "t1", "easy"))[0] == "Retire or make harder?"
    assert suggestion(row(s, "t1", "hard"))[0].startswith("Reword")


def test_summary_counts():
    s = summary(fixture())
    assert (s["checks"], s["same_result"], s["always_pass"], s["always_fail"]) == (7, 3, 2, 1)


def test_tie_with_different_misses_is_found():
    ties = hidden_ties(fixture())
    t2 = next(t for t in ties if t["task"] == "t2")
    assert t2["score"] == 33 and t2["models"] == ["B", "C"] and len(t2["patterns"]) == 2


def test_shared_code_check_failing_in_one_task_is_flagged_as_question():
    fs = flags(fixture())
    f = next(f for f in fs if f["id"] == "shared-check-one-task")
    assert "t2" in f["title"] and f["question"].endswith("?")
    assert any("passes; its run is dated" in x for x in f["facts"])


def test_missing_tokens_and_single_run_flags():
    ids = {f["id"] for f in flags(fixture())}
    assert "tokens" in ids and "single-run" in ids
    assert "inspected-t2" not in ids  # failing runs show phrases, not file lists


def test_reconcile_matches_own_scores():
    r = reconcile(fixture())
    assert r["cell_mismatches"] == [] and r["overall_mismatches"] == []


def test_deciding_only_drops_same_result_checks():
    tasks, _ = deciding_only_scores(fixture())
    assert tasks["A"]["t1"] == 100 and tasks["B"]["t1"] == 0


def test_switch_diff():
    d = switch(fixture(), "B", "A")
    assert {g["check"] for g in d["gained"]} == {"split", "y", "ai-wording"}
    assert [g["check"] for g in d["lost"]] == ["x"]


BOARD = """<table><thead><tr><th>Model</th><th>Overall</th><th>t1</th></tr></thead>
<tr><th scope="row" class="rowhead"><a href="/p/b/A">A</a></th><td class="overall">50%</td>
<td class=""><a class="cell" href="/p/b/runs/7">50%</a></td></tr></table>"""

RUN = """<title>t1 · A · B</title> run 1 Oct 2026 1,234 tokens Instructions
<span class="score-lg">1/2</span>
<div class="verdict" id="verdict_1"><span class="pill pill-fail">fail</span>
<p class="name">Ask first<span class="chip ml-2">this case</span></p>
<p class="eyebrow mt-3">Judge's reasoning</p><p class="body" x>It says &quot;hi&quot;.</p>
<details class="disclosure mt-2"><summary>Rubric</summary><p>Does it ask?</p></details></div>
<details class="disclosure passed mt-2"><summary>1 passed</summary>
<div class="verdict" id="verdict_2"><span class="pill pill-pass">pass</span>
<p class="name"><span class="mono">ai-wording</span><span class="chip ml-2">every task</span></p>
<p class="desc">no tells</p><p class="mono text-[12px]">inspected ANSWER.md</p></div>"""


def test_parse_board_and_run():
    tasks, cells = parse_board(BOARD)
    assert tasks == ["t1"] and cells[0]["run_id"] == 7 and cells[0]["score"] == 50
    r = parse_run(RUN)
    assert (r["passed"], r["applicable"], r["tokens"], r["date"]) == (1, 2, 1234, "1 Oct 2026")
    assert r["verdicts"][0]["kind"] == "model" and r["verdicts"][0]["reason"] == 'It says "hi".'
    assert r["verdicts"][1]["kind"] == "code" and r["verdicts"][1]["evidence"] == "inspected ANSWER.md"

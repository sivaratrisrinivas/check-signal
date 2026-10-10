"""The committed snapshot must reproduce the public scoreboard exactly."""
import json
import os

from checksignal.analyze import reconcile

SNAP = os.path.join(os.path.dirname(__file__), "..", "snapshot", "benchmark.json")


def test_snapshot_reproduces_every_public_score():
    snap = json.load(open(SNAP))
    r = reconcile(snap)
    assert r["cells_checked"] == len(snap["cells"]) > 0
    assert r["cell_mismatches"] == [] and r["overall_mismatches"] == []


def test_audit_notes_on_snapshot():
    import json
    from checksignal.analyze import audit_notes
    a = audit_notes(json.load(open(SNAP)))
    assert a["heavy"] == "literary-analysis-follow-up" and a["heavy_checks"] == 3
    assert round(a["weight"][a["heavy"]], 2) == 6.67 and round(a["weight"][a["light"]], 2) == 1.67
    assert a["sole_decider"] == "No unearned praise" and round(a["sole_share"], 2) == 6.67
    assert round(a["pooled"]["Opus 5.5"]) == round(a["pooled"]["GPT-5.6"]) == 53
    assert set(a["harness"].values()) == {"codex", "claude"}

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

"""The page is built from the snapshot, and its headline matches the analysis."""
import json
import os

import build
from checksignal.analyze import summary


def test_build_writes_page_with_computed_headline(tmp_path, monkeypatch):
    monkeypatch.setattr(build, "OUT", str(tmp_path))
    build.build()
    page = (tmp_path / "index.html").read_text()
    s = summary(json.load(open(build.SNAP)))
    assert f"{s['same_result']} of {s['checks']} checks give every model the same result" in page
    assert "Not affiliated with or endorsed by Every" in page
    import re
    ours = re.sub(r"<blockquote>.*?</blockquote>|<script>.*?</script>|<li><b>.*?</li>", "", page, flags=re.S)
    assert "\u2014" not in ours  # no em dashes in our copy (quoted judge text kept verbatim)
    assert "\u2014" not in (tmp_path / "memo.html").read_text()
    v2 = json.loads((tmp_path / "feed-v2-example.json").read_text())
    assert v2["runs"] and v2["runs"][0]["cases"][0]["checks"]

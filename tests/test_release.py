import json
from pathlib import Path


def test_release_metadata():
    data = json.loads(Path("docs/release.json").read_text())
    assert data["release"] == "B9-238"
    assert data["version"] == "1.0.0"

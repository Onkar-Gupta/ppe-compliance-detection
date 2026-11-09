"""The replay exporter's pure helpers. The monitor itself needs weights and a clip, so it is not run here."""

from types import SimpleNamespace

from scripts.export_replay import build_replay, event
from src.monitor import Summary


def test_event_turns_an_alert_into_plain_json_values():
    alert = SimpleNamespace(track_id=7, missing_names="helmet", dwell=3.004)
    assert event(alert, 90, 3.0) == {
        "frame": 90,
        "seconds": 3.0,
        "track_id": 7,
        "missing": "helmet",
        "dwell_seconds": 3.0,
    }


def test_build_replay_carries_frames_alerts_latency_and_extras():
    summary = Summary()
    summary.latencies_ms = [10.0] * 20
    alert_row = {
        "frame": 90,
        "seconds": 3.0,
        "track_id": 7,
        "missing": "helmet",
        "dwell_seconds": 3.0,
    }
    replay = build_replay([{"i": 0}], [alert_row], summary, {"device": "cpu"})
    assert replay["alerts"] == [alert_row] and replay["frames"] == [{"i": 0}]
    assert replay["device"] == "cpu" and replay["latency"]["median_ms"] == 10.0

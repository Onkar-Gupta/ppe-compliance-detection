"""Export a saved replay of one real monitor run for the landing page.

    python -m scripts.export_replay --config configs/demo.yaml --out docs/replay
    python -m scripts.export_replay --config configs/demo.yaml --out docs/replay --device cpu --every 4

Drives ``src.monitor.iterate`` exactly as the command line and the dashboard do, so the replay
cannot disagree with the numbers the monitor reports. It writes every Nth annotated frame as a
WebP image and a ``replay.json`` with per-frame counts, the alert events, the latency summary
and, from a second pass with dwell and memory switched off, how many alerts the same clip
produces without them. Nothing here is simulated: every value comes from the run.
"""

import argparse
import dataclasses
import json
import platform
from pathlib import Path

import cv2

from src.monitor import DemoConfig, Summary, iterate


def event(alert, frame_index: int, seconds: float) -> dict:
    """One alert as a plain dict (alerts are dataclasses; JSON needs numbers and strings)."""
    return {
        "frame": frame_index,
        "seconds": round(seconds, 2),
        "track_id": alert.track_id,
        "missing": alert.missing_names,
        "dwell_seconds": round(alert.dwell, 2),
    }


def build_replay(frames: list[dict], events: list[dict], summary: Summary, extra: dict) -> dict:
    """Assemble the replay document from what the run recorded."""
    return {
        "frames": frames,
        "alerts": events,
        "latency": summary.stats(),
        "people_detections": summary.people_detections,
        **extra,
    }


def run_pass(config: DemoConfig, frames_dir: Path | None, every: int, width: int):
    """Run the monitor once. Saves every Nth frame when ``frames_dir`` is given."""
    summary = Summary()
    records, events = [], []
    if frames_dir is not None:
        frames_dir.mkdir(parents=True, exist_ok=True)
    for result in iterate(config, summary):
        for alert in result.alerts:
            events.append(event(alert, result.index, result.seconds))
        if frames_dir is not None and result.index % every == 0:
            image = result.annotated
            if width and image.shape[1] > width:
                scale = width / image.shape[1]
                image = cv2.resize(
                    image, (width, round(image.shape[0] * scale)), interpolation=cv2.INTER_AREA
                )
            name = f"f{result.index:05d}.webp"
            cv2.imwrite(str(frames_dir / name), image, [cv2.IMWRITE_WEBP_QUALITY, 78])
            records.append(
                {
                    "i": result.index,
                    "t": round(result.seconds, 2),
                    "img": name,
                    "people": result.people,
                    "breach": result.in_breach,
                    "alerts": len(result.alerts),
                    "ms": round(result.latency_ms, 1),
                }
            )
    return records, events, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("configs/demo.yaml"))
    parser.add_argument("--out", type=Path, default=Path("docs/replay"))
    parser.add_argument("--every", type=int, default=4, help="save every Nth frame")
    parser.add_argument("--width", type=int, default=800, help="saved frame width in pixels")
    parser.add_argument("--device", default=None, help='for example "cpu" or "0"')
    parser.add_argument("--weights", type=Path, default=None)
    parser.add_argument("--source", default=None)
    parser.add_argument("--zone", type=Path, default=None)
    args = parser.parse_args()

    config = DemoConfig.from_yaml(args.config)
    for name in ("weights", "source", "zone", "device"):
        value = getattr(args, name)
        if value is not None:
            setattr(config, name, value)
    config.display = False
    config.save_snapshots = False
    scratch = args.out.parent / "_replay_scratch"
    config.out = scratch

    records, events, summary = run_pass(config, args.out / "frames", args.every, args.width)

    # Second pass: the same clip with the on-delay and the hysteresis removed.
    raw = dataclasses.replace(config, dwell_seconds=0.0, memory_seconds=0.0)
    _, raw_events, _ = run_pass(raw, None, args.every, args.width)

    replay = build_replay(
        records,
        events,
        summary,
        {
            "source_name": Path(str(config.source)).name,
            "every": args.every,
            "frame_width": args.width,
            "settings": {
                "conf": config.conf,
                "association_threshold": config.association_threshold,
                "dwell_seconds": config.dwell_seconds,
                "memory_seconds": config.memory_seconds,
                "grace_seconds": config.grace_seconds,
                "required_ppe": list(config.required_ppe),
            },
            "alerts_without_dwell_or_memory": len(raw_events),
            "alerts_with_dwell_and_memory": len(events),
            "device": str(config.device or "default"),
            "machine": f"{platform.processor() or platform.machine()}, Python {platform.python_version()}",
        },
    )
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "replay.json").write_text(
        json.dumps(replay, indent=1), encoding="utf-8", newline="\n"
    )
    print(
        f"{len(records)} frames saved, {len(events)} alerts with dwell and memory, "
        f"{len(raw_events)} without, median {replay['latency'].get('median_ms')} ms"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Correlate process events using GUIDs, PIDs, and timestamps when available."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def parse_iso8601(value: str | None) -> datetime | None:
    if value is None:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_records(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    records: list[dict[str, Any]] = []
    if p.suffix.lower() == ".json":
        payload = json.loads(text)
        if isinstance(payload, dict):
            records = [payload]
        elif isinstance(payload, list):
            records = payload
        else:
            raise ValueError("JSON input must be object or array")
    elif p.suffix.lower() in {".jsonl", ".ndjson"}:
        for line in text.splitlines():
            if not line.strip():
                continue
            records.append(json.loads(line))
    else:
        raise ValueError("Unsupported file type: use .json or .jsonl")
    return records


def correlate_events(events: list[dict[str, Any]], window_seconds: int = 900) -> list[dict[str, Any]]:
    grouped: list[dict[str, Any]] = []
    for event in events:
        timestamp = parse_iso8601(str(event.get("timestamp")))
        process_name = str(event.get("process_name") or "")
        proc_guid = event.get("process_guid")
        pid = event.get("pid")
        parent_name = event.get("parent_process_name")
        if timestamp is None:
            continue

        cluster = {
            "process_name": process_name,
            "process_guid": proc_guid,
            "pid": pid,
            "parent_process_name": parent_name,
            "start": timestamp.isoformat(),
            "events": [event],
        }

        matched = False
        for existing in grouped:
            e_start = parse_iso8601(existing["start"])
            if e_start is None:
                continue
            delta = abs((timestamp - e_start).total_seconds())
            same_guid = bool(proc_guid) and bool(existing.get("process_guid")) and proc_guid == existing.get("process_guid")
            same_pid = pid is not None and existing.get("pid") is not None and pid == existing.get("pid") and delta <= window_seconds
            if same_guid or same_pid:
                existing["events"].append(event)
                existing["process_name"] = process_name or existing["process_name"]
                existing["parent_process_name"] = parent_name or existing["parent_process_name"]
                matched = True
                break
        if not matched:
            grouped.append(cluster)

    return grouped


def main() -> None:
    parser = argparse.ArgumentParser(description="Correlate process events by timestamp, PID, and process GUID.")
    parser.add_argument("--input", required=True, help="Path to a JSON or JSONL event file")
    parser.add_argument("--window-seconds", type=int, default=900, help="Time window for correlation")
    args = parser.parse_args()

    events = load_records(args.input)
    result = correlate_events(events, window_seconds=args.window_seconds)
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()

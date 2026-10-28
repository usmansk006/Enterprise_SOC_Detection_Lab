#!/usr/bin/env python3
"""Parse documented JSON or JSONL event input and normalize relevant fields."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

REQUIRED_FIELDS = {
    "timestamp",
    "event_id",
    "computer",
    "process_name",
    "pid",
}


def load_json_or_jsonl(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p}")

    text = p.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"Input file is empty: {p}")

    if p.suffix.lower() == ".json":
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Malformed JSON in {p}: {exc}") from exc
        if isinstance(payload, list):
            records = payload
        elif isinstance(payload, dict):
            records = [payload]
        else:
            raise ValueError(f"Unsupported JSON structure in {p}: expected object or list")
        return [normalize_event(record) for record in records]

    if p.suffix.lower() in {".jsonl", ".ndjson"}:
        records = []
        for idx, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Malformed JSONL at line {idx}: {exc}") from exc
            records.append(normalize_event(obj))
        return records

    raise ValueError(f"Unsupported file type for {p}. Use .json or .jsonl")


def normalize_event(event: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(event, dict):
        raise ValueError("Each event must be a JSON object")

    missing = sorted(field for field in REQUIRED_FIELDS if field not in event)
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    normalized = {
        "timestamp": event.get("timestamp"),
        "event_id": event.get("event_id"),
        "computer": event.get("computer"),
        "process_name": event.get("process_name"),
        "pid": event.get("pid"),
        "ppid": event.get("ppid"),
        "parent_process_name": event.get("parent_process_name"),
        "parent_process_path": event.get("parent_process_path"),
        "process_path": event.get("process_path"),
        "command_line": event.get("command_line"),
        "user": event.get("user"),
        "process_guid": event.get("process_guid"),
        "source": event.get("source", "unknown"),
        "notes": event.get("notes"),
    }
    return normalized


def parse_events(path: str | Path) -> list[dict[str, Any]]:
    return load_json_or_jsonl(path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse JSON or JSONL Windows event data.")
    parser.add_argument("--input", required=True, help="Path to a JSON or JSONL event file")
    args = parser.parse_args()

    records = parse_events(args.input)
    for record in records:
        print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()

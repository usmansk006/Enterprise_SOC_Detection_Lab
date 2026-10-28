#!/usr/bin/env python3
"""Validate supported YAML-like Sigma rule structure in a lightweight, dependency-safe way."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

REQUIRED_KEYS = {"title", "id", "status", "logsource", "detection"}


def read_rule_file(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"Rule file is empty: {p}")

    if yaml is not None:
        try:
            data = yaml.safe_load(text)
        except Exception as exc:  # pragma: no cover
            raise ValueError(f"YAML parsing failed for {p}: {exc}") from exc
        if not isinstance(data, dict):
            raise ValueError(f"Rule at {p} must parse to a YAML mapping")
        return data

    # Lightweight fallback for basic YAML field checks without external dependencies.
    simplified = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if re.match(r"^[A-Za-z0-9_-]+:\s*.*$", stripped):
            key, _, value = stripped.partition(":")
            simplified[key.strip()] = value.strip()
    if not simplified:
        raise ValueError(f"Could not parse YAML-like structure in {p}")
    return simplified


def validate_rule(rule: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    missing = sorted(key for key in REQUIRED_KEYS if key not in rule)
    if missing:
        errors.append(f"Missing required keys: {', '.join(missing)}")

    if "title" in rule and not str(rule["title"]).strip():
        errors.append("title must not be empty")
    if "id" in rule and not str(rule["id"]).strip():
        errors.append("id must not be empty")
    if "status" in rule and str(rule["status"]).strip() not in {"experimental", "test", "stable"}:
        errors.append("status should be 'experimental', 'test', or 'stable'")
    if "logsource" in rule and not isinstance(rule["logsource"], dict):
        errors.append("logsource must be a mapping")
    if "detection" in rule and not isinstance(rule["detection"], dict):
        errors.append("detection must be a mapping")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic validation for Sigma-style YAML structure.")
    parser.add_argument("--input", required=True, help="Path to a rule YAML file")
    args = parser.parse_args()

    try:
        rule = read_rule_file(args.input)
        errors = validate_rule(rule)
    except Exception as exc:
        print(f"ERROR: {exc}")
        raise SystemExit(1)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Rule validation passed: basic structure checks succeeded.")
    print("Note: full Sigma compatibility requires a dedicated Sigma parser or engine.")


if __name__ == "__main__":
    main()

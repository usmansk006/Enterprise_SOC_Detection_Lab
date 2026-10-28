# Regression tests

Regression tests ensure the logic remains stable across future edits.

## Example checks

- command-line parsing remains intact,
- rule validation still passes for supported YAML structure,
- process correlation still resolves valid GUID and timestamp relationships,
- malformed JSON or missing required fields are rejected safely.

## Scope

This repository contains automated Python test coverage for parsing, validation, and correlation logic. Full live telemetry regression remains pending authorized execution.

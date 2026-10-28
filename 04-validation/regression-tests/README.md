# Regression Tests

This folder documents stability checks and rule evolution guardrails.

## Example regression goals

- maintain detection logic readability after updates
- ensure file names and rule IDs remain consistent
- confirm parser and correlator handle malformed input gracefully
- review detection quality after new telemetry assumptions

## Notes

Regression tests should be executed only after rule or script changes that affect parser assumptions or detection logic.

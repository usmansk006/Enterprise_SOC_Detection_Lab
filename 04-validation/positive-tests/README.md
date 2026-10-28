# Positive Tests

This content documents suspicious activity and expected detection patterns.

## Included scenarios

- `mshta.exe` launched from a temp directory
- remote HTML content resolved via `http://` or `https://`
- `javascript:` or `vbscript:` embedded in command line
- HTA file created in user-writable directory and later executed
- network connection from the HTA process to an external host

## Scope

These are controlled test scenarios intended to validate detection logic and correlation behavior. They are not production telemetry.

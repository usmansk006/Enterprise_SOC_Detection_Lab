# Positive tests

This area is reserved for safe, authorized synthetic tests and validation examples. Positive tests are intended to represent suspicious or high-signal behavior, not confirmed malicious activity on real endpoints.

## Sample scenarios

- `mshta.exe` launched with a remote HTTP URL,
- `mshta.exe` executed from a temporary or user-writable path,
- process lineage from a shell to `mshta.exe`,
- file creation for `.hta`, `.js`, or `.vbs` artifacts,
- outbound network connection after HTA execution.

## Validation notes

These scenarios are synthetic by default and must not be represented as live Windows telemetry. They are useful for rule logic and Python validation exercises.

# Detection Engineering

This directory is the catalog for the HTA detection set. The content is intentionally local-first and does not require a SIEM to be operational.

Each detection includes a rule, telemetry requirements, rationale, false positive notes, and validation status.

## Detection set

- DET-001: mshta.exe execution baseline
- DET-002: remote HTA references
- DET-003: inline script patterns
- DET-004: suspicious parent process relationships
- DET-005: suspicious child process relationships
- DET-006: user-writable or temp path execution
- DET-007: relevant network activity
- DET-008: related file creation activity
- DET-009: suspicious command-line patterns and obfuscation
- DET-010: correlated multi-event HTA behavior

## Validation posture

These are detection hypotheses and must be interpreted with telemetry quality in mind. Normal software can legitimately use `mshta.exe`; therefore context matters.

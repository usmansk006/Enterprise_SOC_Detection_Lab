# HTA detection catalog

This section documents the core HTA-focused detection hypotheses for the repository. Each detection is treated as a testable hypothesis rather than a universal indicator of malicious behavior.

## Detection set

- DET-001: `mshta.exe` execution baseline
- DET-002: remote HTA reference or script fetch
- DET-003: suspicious inline script patterns
- DET-004: suspicious parent process relationships
- DET-005: suspicious child process relationships
- DET-006: execution from user-writable or temp paths
- DET-007: relevant network behavior
- DET-008: related file creation activity
- DET-009: suspicious command-line patterns and obfuscation
- DET-010: correlated multi-event HTA behavior

## Validation posture

Each detection should be evaluated with:

- relevant Sysmon process creation events,
- Windows Security process events where available,
- network and file creation telemetry,
- positive and negative test fixtures,
- and documented false-positive considerations.

## Documentation standard

Every detection directory contains a `README.md` and a rule or logic artifact describing:

- telemetry requirements,
- detection rationale,
- ATT&CK mapping,
- test cases,
- false positives,
- and validation state.

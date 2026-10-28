# Architecture overview

The repository architecture is designed around a local-first detection workflow: telemetry collection, event normalization, detection logic, validation, and investigation.

## Core flow

```text
Endpoint telemetry
    ↓
Sysmon + Windows Security logs
    ↓
Local parsing and correlation
    ↓
Detection logic and Sigma examples
    ↓
Investigation and hunting
    ↓
Documentation and reporting
```

## Design principles

- local-first and evidence-driven,
- SIEM-independent by default,
- practical for a detection engineering portfolio,
- and explicit about validation boundaries.

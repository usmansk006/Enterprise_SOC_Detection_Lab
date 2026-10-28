# DET-001: `mshta.exe` execution baseline

## Hypothesis

A process execution of `mshta.exe` is notable when combined with suspicious parent, command-line, remote reference, or child-process behavior. Baselining alone should not classify benign activity as malicious.

## Telemetry

- Sysmon Event ID 1 (`ProcessCreate`)
- Windows Security Event ID 4688
- `Image`
- `CommandLine`
- `ParentImage`
- `User`
- `ProcessGuid` when available

## Detection logic

Look for `mshta.exe` execution and review command-line context, parent image, and timing. This is often the starting point for a broader multi-event correlation workflow.

## Expected behavior

- positive: `mshta.exe` called with remote script or temporary file,
- negative: a known administrative HTA helper used in controlled internal testing.

## False positives

- internal admin scripts,
- legacy application support,
- legitimate help or automation packaging.

## Investigation steps

- confirm parent process,
- inspect command line and target file,
- review child-process creation,
- map to network connections and file creation,
- and assess whether the behavior matches an approved workflow.

## Validation status

Documented as an initial baseline hypothesis. Live validation is pending authorized lab execution.

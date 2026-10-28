# DET-008: Related file creation activity

## Hypothesis

HTA abuse often leaves related artifacts behind: downloaded `.hta`, `.js`, `.vbs`, or shell scripts written under temporary or user-writable directories. This behavior can be suspicious when related to `mshta.exe` execution.

## Telemetry

- Sysmon Event ID 11 (`FileCreate`)
- `TargetFilename`
- `ProcessGuid`
- process creation telemetry

## Detection logic

Correlate file creation with process creation to determine whether a dropped or staged script file is associated with `mshta.exe` or with a suspicious parent process.

## False positives

- legitimate user file creation,
- user-generated files,
- or internal application packaging.

## Validation status

Documented as a contextual, evidence-dependent detection with live validation pending.

# DET-009: Suspicious command-line patterns and obfuscation

## Hypothesis

`mshta.exe` execution with encoded or indirect script patterns is a strong signal when the command line references remote content, script protocols, or temporary file locations. Obfuscation may hide the actual script objective but not the execution context.

## Telemetry

- `CommandLine`
- `Image`
- `ParentImage`
- `ParentCommandLine`
- `ProcessGuid`

## Detection logic

Look for suspicious command-line values that contain `javascript:`, `vbscript:`, `about:`, remote URLs, or user-writable paths. Correlate with process and file creation to assess severity.

## False positives

- automation,
- approved help files,
- and custom enterprise wrappers.

## Validation status

This detection is documented as a high-signal hypothesis and should be tuned using lab telemetry.

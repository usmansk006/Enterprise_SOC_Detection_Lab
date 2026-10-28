# DET-003: Suspicious inline script patterns

## Hypothesis

HTA execution may be suspicious when it invokes inline script or scriptlet patterns instead of a local `.hta` file. Inline script invocation can be used to decrease file footprint and obfuscate execution intent.

## Telemetry

- `ProcessCreate`
- `CommandLine`
- `ParentImage`
- `ParentCommandLine`
- file creation and script artifacts where available

## Detection logic

Search for `mshta.exe` with `javascript:`, `vbscript:`, `script:`, or similar patterns in the command line. This should be correlated with a parent process and the target URL or file path.

## False positives

- internal administrative help pages,
- custom enterprise applications based on scriptlet wrappers,
- or legacy help and support tooling.

## Validation status

Rule documented and ready for environment-specific reproduction. No live validation claim.

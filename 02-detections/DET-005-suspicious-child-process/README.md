# DET-004: Suspicious parent process relationships

## Hypothesis

`mshta.exe` spawned by unexpected script or shell processes can indicate staging or execution of a remote or obfuscated payload.

## Telemetry

- `ParentImage`
- `ParentCommandLine`
- `Image`
- `CommandLine`
- `ProcessGuid`

## Detection logic

Correlate parent and child processes to identify when `mshta.exe` is launched directly from `powershell.exe`, `cmd.exe`, or other living script wrappers. This is most meaningful when combined with suspicious command-line patterns.

## False positives

- legacy admin workflows,
- endpoint management scripts,
- or user-run help automation.

## Validation status

Documented as a contextual detection hypothesis requiring verified telemetry and lab validation.

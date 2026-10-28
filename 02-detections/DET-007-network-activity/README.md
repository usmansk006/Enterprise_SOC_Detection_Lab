# DET-006: User-writable or temporary paths

## Hypothesis

When `mshta.exe` is used from writable user directories such as `%AppData%`, `%Temp%`, or Downloads, it may indicate script staging or user-driven execution. This is a contextual indicator rather than a direct malicious signature.

## Telemetry

- `CommandLine`
- `Image`
- file creation events,
- user context,
- `TargetFilename` when available

## Detection logic

Look for `mshta.exe` execution where the target file or script path resolves under a user-writable directory. Use additional process lineage and parent-process checks to reduce false positives.

## False positives

- local developer tools,
- user-generated support content,
- or internal testing with staged HTA files.

## Validation status

Documented as a practical contextual detection. Requires validation against actual lab telemetry.

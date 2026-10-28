# DET-002: Remote HTA reference

## Hypothesis

`mshta.exe` is often abused when it is launched with a remote script URL or an untrusted file reference. Remote execution is a meaningful indicator when combined with suspicious parent lineage or network activity.

## Telemetry

- Sysmon Event ID 1
- Windows Security Event ID 4688
- `CommandLine`
- `ParentImage`
- `DestinationIp` or network telemetry
- `Image` and `ProcessGuid`

## Detection logic

Review process creation where `mshta.exe` is invoked with HTTP/HTTPS or script-like URL patterns. Remote references are more suspicious when paired with unusual parent processes or temporary file creation.

## Investigation steps

- review the exact URL loaded,
- determine whether the parent was `powershell.exe`, `cmd.exe` or a browser,
- validate any public IP or external domain activity,
- and inspect whether a child process or script file was created.

## Validation status

Logic is documented and ready for synthetic or live validation. No production claim is made.

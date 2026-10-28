# DET-005: Suspicious child process relationships

## Hypothesis

A child process launched by `mshta.exe` may be an execution stage for further script abuse, payload staging, or evasion. This is particularly suspicious if the spawned process is a scripting host, shell, or system utility.

## Telemetry

- `ProcessCreate`
- `ParentImage`
- `ParentCommandLine`
- `Image`
- `CommandLine`
- `User`

## Detection logic

Monitor process creation where the parent is `mshta.exe` and the child is `powershell.exe`, `cmd.exe`, `rundll32.exe`, or `regsvr32.exe`.

## Investigation steps

- determine whether the child process executes scripts or remote content,
- assess command line and file path,
- correlate with network and file creation events,
- and check for suspicious persistence or user-writable artifacts.

## Validation status

Hypothesis documented; requires controlled validation in a Windows lab.

# Process Tree Analysis

Process tree analysis is essential when investigating HTA execution.

## Key questions

- What launched the HTA file?
- What parent process created the child chain?
- Did the process create a script or payload file?
- Did a child process such as `powershell.exe`, `cmd.exe`, or `rundll32.exe` launch afterwards?

## Requirements

The analyst needs reliable process GUIDs, event ordering, and host context. PID-only joins across a long time window are not robust.

# Correlation logic notes

Correlation should prioritize:

- `ProcessGuid` when available,
- `ProcessId` and `ParentProcessId` within a limited time window,
- `CommandLine` and `Image` consistency,
- and related file or network telemetry.

Do not rely on `PID` alone across long time windows, because process IDs may be reused and context can be misleading. Use the combination of `ProcessGuid`, timestamps, and correlated events when possible.

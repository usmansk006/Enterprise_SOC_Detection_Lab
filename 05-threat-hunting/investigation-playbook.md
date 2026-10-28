# Investigation playbook

## Triage criteria

Escalate or investigate further when:

- `mshta.exe` is executed from an unexpected parent,
- the command line includes remote URLs or script protocols,
- the process is located in `%Temp%`, `%AppData%`, or Downloads,
- or it spawns a suspicious child process or network connection.

## Evidence preservation

Preserve:

- event logs and exported Windows events,
- file hashes or parent artifact metadata,
- screenshots or timeline entries if captured in a controlled lab,
- and the exact timestamps around the event sequence.

## Investigation flow

1. Confirm `mshta.exe` execution.
2. Inspect the full command line.
3. Review the parent process and user context.
4. Examine child processes and file creation.
5. Correlate outbound network connections.
6. Assess whether behavior aligns with enterprise policy or a lab exercise.

## Analyst caveat

Observed execution alone does not prove malicious intent. Additional telemetry and evidence must support the conclusion.

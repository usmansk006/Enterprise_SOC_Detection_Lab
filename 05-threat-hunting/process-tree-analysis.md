# Process tree analysis

## Investigative model

Establish the process sequence from the user session or service context to the final `mshta.exe` execution and observe any related child processes.

## Key questions

- Which parent process launched the HTA?
- Did the parent create a temporary file or script?
- Did `mshta.exe` spawn `powershell.exe`, `cmd.exe`, or `rundll32.exe`?
- Did the process access the network or write to user-writable paths?

## Evidence handling

Review process lineage, command line, and timestamps in order. Document observed evidence before making an analyst inference about malicious intent.

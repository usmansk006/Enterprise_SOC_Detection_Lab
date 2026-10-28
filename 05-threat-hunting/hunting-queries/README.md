# Hunting Queries

This folder stores analyst-oriented queries and review patterns.

## Example query themes

- `mshta.exe` process creation
- command-line patterns with `http`, `javascript`, or `vbscript`
- child processes launched by `mshta.exe`
- network connections originating from HTA execution
- suspicious file creation near temp or user-writable paths

## Investigation guidance

Always review host, user context, timestamp ordering, and process lineage before concluding malicious activity.

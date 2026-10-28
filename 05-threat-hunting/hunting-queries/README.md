# Threat hunting guide

This section focuses on practical hunting for suspicious HTA execution behavior using local event data and process correlation.

## Core hunting questions

- Was `mshta.exe` launched by a suspicious parent?
- Was a remote HTA file or script reference used?
- Did the process spawn additional script hosts or system utilities?
- Was there related network activity or temporary file staging?
- Did the user context or path pattern align with malicious behavior?

## Event sources

- Sysmon process creation,
- Network connection telemetry,
- file creation events,
- Windows Security process events,
- and any PowerShell or script logging made available by policy.

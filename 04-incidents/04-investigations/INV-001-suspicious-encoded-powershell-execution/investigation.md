# INV-001 — Technical Investigation

## Investigation Objective

The objective of this investigation was to analyze the suspicious encoded PowerShell execution identified during initial triage and determine:

- Which process executed the command
- Which user executed the process
- What command was executed
- What the encoded content contained
- Whether the process generated additional activity
- Whether the available evidence indicated malicious behavior

---

# 1. Process Creation Analysis

Sysmon Event ID 1 was reviewed to identify the process responsible for the detected activity.

## Observed Process

| Field | Value |
|---|---|
| Event ID | 1 |
| Event Type | Process Create |
| UtcTime | 2026-09-05 07:17:34.400 |
| Process ID | 2880 |
| Image | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` |
| User | `DESKTOP-Q9TN2GI\labadmin` |
| Current Directory | `C:\Windows\system32\` |

The process command line contained the PowerShell `-EncodedCommand` parameter.

### Evidence

`evidence/INV-001-Sysmon-process-creation.png`

---

# 2. Command-Line Analysis

The observed PowerShell command used the following execution method:

```text
-EncodedCommand
````

The encoded command was:

```text
VwByAGkAdABlAC0ATwB1AHQAcAB1AHQAIAAiAGQAZQB0AGMAbwBuACAAUABvAHcAZQByAFMAaABlAGwAbAAgAFQAZQBzAHQAIgA=
```

Encoded PowerShell commands require additional analysis because the underlying command content is not immediately visible.

The encoded content was therefore decoded for analysis without executing the decoded command.

---

# 3. Decoded Command Analysis

The encoded PowerShell content was decoded using a decoding-only method.

The decoded command was:

```powershell
Write-Output "detcon PowerShell Test"
```

## Analysis

The decoded command performs a simple output operation.

Based on the decoded content, the command did not demonstrate:

* File creation
* Process execution
* Network communication
* Persistence
* Credential access
* Privilege escalation

The decoded content alone did not indicate malicious behavior.

### Evidence

`evidence/INV-001-PowerShell-decoded-command.png`

---

# 4. Process Context Analysis

Sysmon telemetry showed that the encoded PowerShell process was launched by another PowerShell process.

## Observed Process Relationship

```text
powershell.exe
        ↓
powershell.exe -EncodedCommand
```

The immediate parent process information was recorded from Sysmon Event ID 1.

The available evidence supports identification of the immediate parent process as PowerShell.

Further process ancestry was not required to determine the command content because the decoded command was successfully analyzed.

---

# 5. Process Lifecycle Analysis

Sysmon Event ID 5 was reviewed to identify whether the PowerShell process terminated.

## Process Termination

| Field      | Value                                                       |
| ---------- | ----------------------------------------------------------- |
| Event ID   | 5                                                           |
| Event Type | Process Terminated                                          |
| UtcTime    | 2026-09-05 07:17:34.788                                     |
| Process ID | 2880                                                        |
| Image      | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` |
| User       | `DESKTOP-Q9TN2GI\labadmin`                                  |

The Process GUID matched the PowerShell process identified during the Sysmon Event ID 1 analysis.

This correlated the process creation and process termination events.

## Execution Duration

Process creation:

```text
2026-09-05 07:17:34.400 UTC
```

Process termination:

```text
2026-09-05 07:17:34.788 UTC
```

Approximate execution duration:

```text
388 milliseconds
```

### Evidence

`evidence/INV-001-Sysmon-process-termination.png`

---

# 6. Technical Investigation Summary

The technical investigation confirmed:

1. A PowerShell process executed using the `-EncodedCommand` parameter.
2. The process executed under the `labadmin` user account.
3. Sysmon captured the process creation and command-line telemetry.
4. The encoded command was decoded without executing the decoded content.
5. The decoded command performed a harmless output operation.
6. The PowerShell process terminated approximately 388 milliseconds after creation.

The technical investigation did not identify malicious behavior from the decoded command.

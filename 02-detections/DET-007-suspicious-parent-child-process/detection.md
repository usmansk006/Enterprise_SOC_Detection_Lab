# DET-007: Suspicious PowerShell Parent-Child Process Execution

## Detection

Detect PowerShell spawning another PowerShell process.

Observed process relationship:

```text
powershell.exe
        ↓
powershell.exe
````

---

## Telemetry Source

### Endpoint Telemetry

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Operating System | Windows 10                           |
| Telemetry Tool   | Sysmon                               |
| Log Channel      | Microsoft-Windows-Sysmon/Operational |
| Event ID         | 1                                    |
| Event Type       | Process Create                       |

Sysmon Event ID 1 records process creation activity and provides both parent and child process information.

Relevant fields include:

* Image
* CommandLine
* ParentImage
* ParentCommandLine
* ProcessGuid
* ParentProcessGuid
* User
* IntegrityLevel

---

## Detection Logic

The detection identifies the following process relationship:

```text
ParentImage: powershell.exe

Child Image: powershell.exe
```

The observed relationship is:

```text
powershell.exe
        ↓
powershell.exe
```

Wazuh generated the detection:

| Field       | Value                                          |
| ----------- | ---------------------------------------------- |
| Rule ID     | 92027                                          |
| Description | Powershell process spawned powershell instance |
| Severity    | Level 4                                        |

---

## MITRE ATT&CK Mapping

### T1059.001 — PowerShell

Nested PowerShell execution involves command execution through PowerShell.

MITRE ATT&CK mapping:

| Tactic    | Technique              |
| --------- | ---------------------- |
| Execution | T1059.001 – PowerShell |

---

## Test Procedure

The test was performed in an authorized Windows lab environment.

A PowerShell process was used to create another PowerShell process.

Test command:

```powershell
powershell.exe -NoProfile -Command "Write-Output DET007-PARENT-CHILD-TEST"
```

The test generated a parent-child process relationship.

Expected result:

```text
powershell.exe
        ↓
powershell.exe
```

---

## Detection Evidence

The following evidence was collected:

1. Test execution
2. Sysmon Event ID 1
3. Wazuh alert
4. Process relationship investigation

Evidence files are stored in:

```text
evidence/
```

---

## False Positives

PowerShell spawning another PowerShell process is not inherently malicious.

Legitimate scenarios include:

* Administrative automation
* PowerShell scripts
* Software deployment
* System administration
* Automation frameworks

The detection should therefore be investigated using additional process context.

---

## Detection Limitations

This detection focuses only on the parent-child process relationship.

It does not determine whether the command executed by PowerShell was malicious.

Potential limitations include:

* Legitimate nested PowerShell execution
* Lack of command-line context
* Limited visibility into previous processes
* No correlation with network activity
* No correlation with file activity

---

## Tuning

To reduce false positives, the detection could be enhanced using additional conditions.

Examples include:

* Suspicious PowerShell command-line arguments
* Encoded commands
* Hidden execution
* Unusual execution paths
* Suspicious parent processes
* Network connections following execution

Example behavioral chain:

```text
Suspicious Parent
        ↓
PowerShell
        ↓
PowerShell
        ↓
Network Connection
```

---

## Retest Results

The detection test successfully generated:

* Sysmon Event ID 1 telemetry
* Parent process information
* Child process information
* Wazuh detection

The Wazuh alert identified:

```text
Powershell process spawned powershell instance
```

### Result

**Detection successfully validated in the authorized lab environment.**


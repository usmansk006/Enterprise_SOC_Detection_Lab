# DET-007: Investigation

## Investigation Summary

An alert was generated after Wazuh identified a PowerShell process spawning another PowerShell process.

The investigation focused on determining:

- What process started the child process?
- What command was executed?
- Which user executed the process?
- Was the execution suspicious?
- Is additional investigation required?

---

# Alert Details

| Field | Value |
|---|---|
| Detection ID | DET-007 |
| Wazuh Rule ID | 92027 |
| Alert Description | Powershell process spawned powershell instance |
| Severity | Level 4 |
| Endpoint | WIN10-LAB |
| Telemetry Source | Sysmon |
| Event ID | 1 |

---

# Process Analysis

## Parent Process

The parent process was:

```text
powershell.exe
````

Relevant telemetry field:

```text
ParentImage
```

The parent PowerShell process created another PowerShell process.

---

## Child Process

The child process was:

```text
powershell.exe
```

Relevant telemetry field:

```text
Image
```

The child process executed the following test command:

```text
powershell.exe -NoProfile -Command "Write-Output DET007-PARENT-CHILD-TEST"
```

---

# Process Relationship

The observed execution chain was:

```text
powershell.exe
        ↓
powershell.exe
```

This relationship was identified using Sysmon Event ID 1 process creation telemetry.

---

# User Context

The execution occurred under the following user context:

```text
DESKTOP-Q9TN2GI\labadmin
```

The process integrity level was:

```text
Medium
```

This indicates that the process was running in a standard user context rather than SYSTEM-level execution.

---

# Command-Line Analysis

The child PowerShell process used:

```text
-NoProfile
```

This prevents PowerShell profile scripts from loading.

The test command executed:

```text
Write-Output DET007-PARENT-CHILD-TEST
```

The command was intentionally generated as part of an authorized detection validation test.

No malicious payload was executed.

---

# Security Analysis

Nested PowerShell execution can occur legitimately.

However, attackers may use multiple PowerShell processes to:

* Execute multi-stage commands
* Separate execution stages
* Launch scripts from another process
* Reduce visibility into the original execution chain

For this event, the observed command was a controlled lab test.

---

# Investigation Decision

## Classification

```text
Benign / Authorized Test Activity
```

## Reason

The command contained the controlled test string:

```text
DET007-PARENT-CHILD-TEST
```

The activity was intentionally generated to validate the detection.

No malicious payload, suspicious network activity, or unauthorized process execution was identified.

---

# Investigation Workflow

The investigation followed:

```text
ALERT
  ↓
Validate Telemetry
  ↓
Identify Parent Process
  ↓
Identify Child Process
  ↓
Analyze Command Line
  ↓
Review User Context
  ↓
Determine Legitimacy
  ↓
Close Investigation
```

---

# Recommended Investigation Steps for Real Alerts

If this alert occurs in a production environment, investigate:

1. Parent process path
2. Child process path
3. Parent command line
4. Child command line
5. Executing user
6. Process integrity level
7. Encoded PowerShell commands
8. Network connections
9. File creation activity
10. Previous process activity

---

# Conclusion

The investigation confirmed that a PowerShell process spawned another PowerShell process.

Sysmon successfully captured the parent-child process relationship, and Wazuh generated the corresponding alert.

The activity was determined to be an authorized detection test.

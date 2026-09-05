# DET-005 — Investigation Guide

## Investigation Overview

This document describes the investigation process for DET-005: Suspicious PowerShell Encoded Command Execution.

The purpose of this investigation is to demonstrate how a SOC analyst investigates PowerShell execution using the `-EncodedCommand` parameter and determines whether the activity is legitimate or potentially malicious.

The detection is triggered when Wazuh identifies encoded PowerShell execution and Custom Rule `100105` generates the DET-005 alert.

---

## 1. Initial Alert Triage

When the alert is received, the analyst should first verify the basic alert information.

Review:

- Alert timestamp
- Endpoint name
- Agent ID
- Rule ID
- Rule level
- Process image
- Command line
- User context
- Parent process
- MITRE ATT&CK mapping

Example alert information:

```text
agent.name: WIN10-LAB
rule.id: 100105
rule.level: 10
rule.description: DET-005: Suspicious PowerShell Encoded Command Execution
````

The first objective is to determine:

What happened, where did it happen, and which process performed the activity?

---

## 2. Identify the PowerShell Process

Review the process information recorded by Sysmon.

Important fields include:

* Process image
* Command line
* Parent process
* Process ID
* User account

The analyst should confirm that the process is:

```text
powershell.exe
```

The command line should also be reviewed to determine whether the `-EncodedCommand` parameter was used.

---

## 3. Analyze the Command Line

Encoded PowerShell commands should be investigated carefully.

The analyst should review:

* The encoded command
* The purpose of the command
* Whether the command is expected
* Whether the command was executed by an authorized user
* Whether the activity is related to legitimate administrative tasks

In this lab, the encoded command was used to execute a harmless test.

The decoded command produced:

```text
DET-005 PowerShell Test
```

---

## 4. Review the Parent Process

The parent process should be reviewed to understand how PowerShell was launched.

Investigate:

* Parent process name
* Parent process path
* Parent process command line
* Whether the parent process is expected

PowerShell launched by legitimate administrative tools may be normal.

However, PowerShell launched by unusual or suspicious processes may require further investigation.

---

## 5. Review User Context

Identify the user account associated with the PowerShell process.

Determine:

* Which user executed the command
* Whether the user is authorized
* Whether administrative privileges were used
* Whether the activity matches the user's expected behavior

Unexpected PowerShell activity from an unusual user account may indicate suspicious activity.

---

## 6. Review Related Events

The analyst should search for related events on the same endpoint.

Review:

* Additional PowerShell executions
* Process creation events
* Suspicious child processes
* Network connections
* File creation events
* Other security alerts

This helps determine whether the encoded PowerShell execution was an isolated event or part of a larger sequence of activity.

---

## 7. MITRE ATT&CK Context

The detection is mapped to:

```text
T1059.001 — Command and Scripting Interpreter: PowerShell
```

PowerShell is commonly used for legitimate administration.

However, attackers may also abuse PowerShell for command execution.

The use of encoded commands can make the executed content more difficult to immediately analyze.

---

## 8. Investigation Decision

After reviewing the available evidence, the analyst should classify the activity.

Possible outcomes include:

### Benign

The PowerShell command was authorized and related to legitimate administration or testing.

### Suspicious

The activity cannot be immediately explained and requires additional investigation.

### Malicious

The investigation identifies unauthorized or malicious PowerShell activity.

---

## 9. Incident Response Actions

If the activity is determined to be malicious, possible response actions include:

* Investigate the affected endpoint
* Review related processes and events
* Identify additional affected systems
* Collect relevant evidence
* Escalate the incident
* Contain the affected system if required

The appropriate response depends on the severity and scope of the activity.

---

## Investigation Conclusion

Encoded PowerShell execution should not automatically be considered malicious.

The SOC analyst must investigate the command, process information, parent process, user context, endpoint activity, and related events before making a final determination.

In this lab, the encoded PowerShell execution was intentionally generated using a harmless command to validate the detection.

The investigation workflow demonstrates how encoded PowerShell activity can be triaged and investigated using Sysmon telemetry and Wazuh alerts.


Then your **DET-005 documentation is complete**.

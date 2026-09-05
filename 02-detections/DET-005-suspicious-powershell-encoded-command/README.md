# DET-005 — Suspicious PowerShell Encoded Command Execution

## Overview

DET-005 detects PowerShell execution using the `-EncodedCommand` parameter.

Encoded PowerShell commands may be used to obfuscate command content. Attackers can abuse this technique to make executed commands more difficult to read and analyze.

This detection was developed and tested in an isolated Windows 10 lab environment monitored by Wazuh and Sysmon.

---

## Detection Summary

| Field | Details |
|---|---|
| Detection ID | DET-005 |
| Detection Name | Suspicious PowerShell Encoded Command Execution |
| Data Source | Sysmon Operational Log |
| Event ID | 1 |
| Platform | Windows 10 |
| SIEM | Wazuh |
| Base Rule ID | 92057 |
| Custom Rule ID | 100105 |
| Severity | Level 10 |

---

## Detection Objective

The objective of this detection is to identify PowerShell processes executed with the `-EncodedCommand` parameter and generate a custom Wazuh alert for SOC analyst investigation.

---

## Detection Flow

```text
PowerShell Encoded Command Execution
        ↓
Sysmon Process Create Event ID 1
        ↓
Wazuh Agent Collects Event
        ↓
Wazuh Base Rule 92057
        ↓
Custom Wazuh Rule 100105
        ↓
SOC Alert Generated
````

---

## MITRE ATT&CK Mapping

| Tactic    | Technique                                                 |
| --------- | --------------------------------------------------------- |
| Execution | T1059.001 — Command and Scripting Interpreter: PowerShell |

---

## Lab Test

A harmless PowerShell command was encoded and executed using the `-EncodedCommand` parameter.

The test generated a Sysmon Process Create event and was successfully detected by Wazuh.

The custom Wazuh Rule `100105` generated the following alert:

```text
DET-005: Suspicious PowerShell Encoded Command Execution
```

---

## Detection Result

The detection successfully identified PowerShell execution using an encoded command.

The Wazuh alert contained:

* PowerShell process information
* Encoded command execution details
* Endpoint information
* User context
* Rule information
* MITRE ATT&CK mapping

---

## Evidence

The following evidence was collected during testing:

1. Windows PowerShell Event ID 4104
2. Wazuh encoded PowerShell detection
3. Wazuh Custom Rule 100105
4. Final DET-005 custom detection alert

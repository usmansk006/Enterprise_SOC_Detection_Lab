# DET-005 — Detection Documentation

## Detection Overview

DET-005 detects PowerShell execution using the `-EncodedCommand` parameter.

Encoded PowerShell commands can be used to obfuscate command content and make executed commands more difficult to analyze.

This detection was developed and tested in an isolated Windows 10 lab environment using Sysmon and Wazuh.

---

## Detection Details

| Field | Details |
|---|---|
| Detection ID | DET-005 |
| Detection Name | Suspicious PowerShell Encoded Command Execution |
| Platform | Windows 10 |
| Data Source | Sysmon Operational Log |
| Event ID | 1 — Process Create |
| SIEM | Wazuh |
| Base Rule ID | 92057 |
| Custom Rule ID | 100105 |
| Severity | Level 10 |

---

## Data Source

The detection uses Sysmon Event ID `1`, which records process creation activity.

The event provides useful investigation information, including:

- Process image
- Command line
- Parent process
- User context
- Process identifiers

During testing, Sysmon recorded PowerShell execution using the `-EncodedCommand` parameter.

---

## Detection Logic

Wazuh Base Rule `92057` identifies PowerShell execution involving an encoded Base64 command.

The custom Wazuh Rule `100105` triggers when Base Rule `92057` is matched.

The custom rule generates a dedicated DET-005 alert for SOC investigation.

---

## Custom Detection Rule

```xml
<rule id="100105" level="10">
  <if_sid>92057</if_sid>
  <description>DET-005: Suspicious PowerShell Encoded Command Execution</description>
  <mitre>
    <id>T1059.001</id>
  </mitre>
  <group>det005,windows,powershell,execution,</group>
</rule>
````

---

## Detection Flow

```text
PowerShell Encoded Command Execution
        ↓
Sysmon Event ID 1 Generated
        ↓
Wazuh Agent Collects Event
        ↓
Wazuh Base Rule 92057 Matches
        ↓
Custom Wazuh Rule 100105 Matches
        ↓
DET-005 Alert Generated
```

---

## MITRE ATT&CK Mapping

| Tactic    | Technique                                                 |
| --------- | --------------------------------------------------------- |
| Execution | T1059.001 — Command and Scripting Interpreter: PowerShell |

---

## Detection Validation

A harmless PowerShell command was encoded and executed using the `-EncodedCommand` parameter.

The activity generated a Sysmon Event ID `1`.

Wazuh detected the encoded PowerShell execution using Base Rule `92057`.

Custom Rule `100105` successfully generated the DET-005 alert.

---

## Detection Considerations

Encoded PowerShell execution is not automatically malicious.

Legitimate scripts or administrative tools may use encoded commands.

During investigation, the analyst should review:

* Command line
* PowerShell process
* Parent process
* User account
* Endpoint
* Related events

Additional context is required before determining whether the activity is malicious.

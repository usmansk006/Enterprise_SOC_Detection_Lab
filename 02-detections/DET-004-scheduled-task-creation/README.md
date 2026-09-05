# DET-004 — Windows Scheduled Task Creation

## Overview

DET-004 detects the creation of Windows Scheduled Tasks using Windows Security Event ID `4698`.

Scheduled tasks can be used legitimately for automation and system administration. However, attackers may also abuse scheduled tasks to establish persistence, execute programs, or maintain access to a compromised system.

This detection was developed and tested in an isolated Windows 10 lab environment monitored by Wazuh.

---

## Detection Summary

| Field | Details |
|---|---|
| Detection ID | DET-004 |
| Detection Name | Windows Scheduled Task Creation |
| Data Source | Windows Security Event Log |
| Event ID | 4698 |
| Platform | Windows 10 |
| SIEM | Wazuh |
| Custom Rule ID | 100104 |
| Severity | Level 10 |

---

## Detection Objective

The objective of this detection is to identify Windows scheduled task creation events and generate a custom Wazuh alert for SOC analyst investigation.

Scheduled task creation should be investigated to determine whether the activity was authorized or potentially associated with malicious persistence or execution.

---

## Detection Flow

```text
Scheduled Task Created
        ↓
Windows Security Event ID 4698
        ↓
Wazuh Agent Collects Event
        ↓
Wazuh Base Rule 60228
        ↓
Custom Wazuh Rule 100104
        ↓
SOC Alert Generated
```

---

## Detection Logic

The custom Wazuh rule uses the existing Wazuh rule for Windows Scheduled Task creation events.

```xml
<rule id="100104" level="10">
  <if_sid>60228</if_sid>
  <description>DET-004: Windows scheduled task created</description>
  <group>det004,windows,persistence,scheduled_task,</group>
  <mitre>
    <id>T1053.005</id>
  </mitre>
</rule>
```

The detection is triggered when the parent Wazuh rule identifies a Windows Security Event ID `4698`.

---

## MITRE ATT&CK Mapping

**Technique:** Scheduled Task/Job: Scheduled Task

**Technique ID:** `T1053.005`

Scheduled tasks can be abused to execute programs or establish persistence on Windows systems.

---

## Lab Test

The detection was tested in an isolated Windows 10 lab environment.

A test scheduled task was created using the Windows `schtasks` utility.

Example test activity:

```text
Task Name: DET-004-TestTask
Action: notepad.exe
```

The activity generated Windows Security Event ID `4698`.

Wazuh successfully collected the event and the custom detection rule `100104` generated a Level 10 alert.

---

## Detection Result

The detection successfully generated a Wazuh alert with the following characteristics:

```text
Rule ID: 100104
Rule Level: 10
Event ID: 4698
Detection: DET-004: Windows scheduled task created
MITRE Technique: T1053.005
Agent: WIN10-LAB
```

---

## Evidence

The following evidence was collected during detection development and testing:

1. Windows Security Event ID `4698`
2. Wazuh custom detection rule configuration
3. Wazuh custom detection alert

Evidence files are available in the `evidence` directory.

---

## Repository Files

```text
DET-004-scheduled-task-creation/
│
├── README.md
├── detection.md
├── investigation.md
│
└── evidence/
    ├── DET-004-01-Windows-Scheduled-Task-Event-4698.png
    ├── DET-004-02-Wazuh-Custom-Rule.png
    └── DET-004-03-Wazuh-Custom-Detection-Alert.png
```

---

## Conclusion

DET-004 demonstrates the detection of Windows Scheduled Task creation using Windows Security Event ID `4698` and a custom Wazuh detection rule.

The detection provides visibility into scheduled task creation activity and supports SOC analysts in identifying potentially unauthorized persistence or execution mechanisms.

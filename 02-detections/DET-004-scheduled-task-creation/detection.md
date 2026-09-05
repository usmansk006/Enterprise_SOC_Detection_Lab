# DET-004 — Detection Documentation

## Detection Overview

DET-004 detects the creation of Windows Scheduled Tasks using Windows Security Event ID `4698`.

Scheduled tasks are commonly used for legitimate automation and administrative activities. However, they can also be abused by attackers to execute malicious programs, establish persistence, or maintain access to a compromised system.

This detection was developed and tested in an isolated Windows 10 lab environment monitored by Wazuh.

---

## Detection Objective

The objective of DET-004 is to detect Windows scheduled task creation and generate a high-severity alert for SOC analyst investigation.

The detection focuses on identifying the creation of scheduled tasks and providing visibility into:

- The affected endpoint
- The account responsible for the action
- The scheduled task name
- The event timestamp
- The associated MITRE ATT&CK technique

---

## Data Source

The detection uses the following telemetry source:

| Field | Details |
|---|---|
| Platform | Windows 10 |
| Log Source | Windows Security Event Log |
| Event ID | 4698 |
| Event Description | A scheduled task was created |
| Collection Method | Wazuh Agent |

Windows Security Event ID `4698` is generated when a scheduled task is created.

---

## Detection Telemetry

The primary event used for this detection is:

```text
Event ID: 4698
Log Channel: Security
Provider: Microsoft-Windows-Security-Auditing
```

The event contains useful investigation information, including:

- Subject account
- Subject domain
- Logon ID
- Task name
- Task content
- Client process information

---

## Detection Development

The Wazuh platform already contains a base rule capable of identifying Windows scheduled task creation events.

The base rule identified during testing was:

```text
Rule ID: 60228
```

DET-004 was developed as a custom rule based on this existing Wazuh rule.

---

## Custom Detection Rule

The following custom Wazuh rule was created:

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

---

## Detection Logic

The detection workflow is:

```text
Scheduled Task Created
        ↓
Windows Security Event ID 4698 Generated
        ↓
Wazuh Agent Collects Event
        ↓
Wazuh Base Rule 60228 Matches Event
        ↓
Custom Rule 100104 Evaluates Parent Rule
        ↓
Level 10 Alert Generated
```

The custom rule uses:

```text
<if_sid>60228</if_sid>
```

This means the DET-004 rule is triggered when Wazuh Rule `60228` matches the scheduled task creation event.

---

## Detection Configuration

The custom rule was added to:

```text
/var/ossec/etc/rules/local_rules.xml
```

After adding the rule, the Wazuh Manager was restarted.

```bash
sudo systemctl restart wazuh-manager
```

The service status was then verified.

```bash
sudo systemctl status wazuh-manager
```

The Wazuh Manager successfully loaded the custom detection rule.

---

## Detection Testing

The detection was tested in an isolated Windows 10 lab environment.

A scheduled task was created using the Windows `schtasks` utility.

Example test activity:

```text
Task Name: DET-004-TestTask
Action: notepad.exe
```

The activity generated Windows Security Event ID `4698`.

The Wazuh agent collected the event and the custom rule successfully generated an alert.

---

## Detection Result

The custom detection successfully triggered with:

```text
Rule ID: 100104
Rule Level: 10
Event ID: 4698
Agent: WIN10-LAB
MITRE Technique: T1053.005
```

The alert description was:

```text
DET-004: Windows scheduled task created
```

---

## MITRE ATT&CK Mapping

| Field | Details |
|---|---|
| Technique | Scheduled Task/Job: Scheduled Task |
| Technique ID | T1053.005 |
| Tactics | Execution, Persistence, Privilege Escalation |

Scheduled tasks can be abused by attackers to execute programs automatically or maintain persistence on a Windows system.

---

## Detection Limitations

This detection identifies the creation of scheduled tasks but does not automatically determine whether the activity is malicious.

Legitimate system administrators and software applications may create scheduled tasks.

Therefore, additional investigation is required to determine:

- Who created the task
- Whether the account was authorized
- What program or command the task executes
- Whether the task name is suspicious
- Whether the activity is expected within the environment

---

## Detection Evidence

The following evidence was collected during testing:

1. Windows Security Event ID `4698`
2. Custom Wazuh Rule `100104`
3. Wazuh Level 10 detection alert

Evidence is stored in the `evidence` directory.

---

## Conclusion

DET-004 successfully detects Windows Scheduled Task creation using Windows Security Event ID `4698` and a custom Wazuh detection rule.

The detection demonstrates the complete detection engineering workflow:

```text
Telemetry Collection
        ↓
Event Identification
        ↓
Base Rule Analysis
        ↓
Custom Rule Development
        ↓
Detection Testing
        ↓
Alert Generation
        ↓
SOC Investigation
```

The detection provides useful visibility into scheduled task creation and supports the identification of potentially unauthorized persistence or execution activity.

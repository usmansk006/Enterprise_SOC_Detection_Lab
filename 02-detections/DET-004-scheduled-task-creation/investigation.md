# DET-004 — Investigation Guide

## Windows Scheduled Task Creation Investigation

---

# 1. Investigation Overview

This document describes the SOC investigation process for DET-004: Windows Scheduled Task Creation.

The detection is triggered when a Windows Scheduled Task is created and Windows Security Event ID `4698` is generated.

The event is collected by the Wazuh agent and matched by Custom Wazuh Rule `100104`.

Scheduled tasks can be legitimate administrative or system activities. However, attackers may abuse scheduled tasks to execute programs, establish persistence, or maintain access to a compromised system.

The purpose of this investigation is to determine whether the scheduled task creation activity is authorized or potentially malicious.

---

# 2. Alert Overview

When the alert is received, the SOC analyst should first review the basic alert information.

Key information to review includes:

- Alert timestamp
- Endpoint name
- Agent ID
- Rule ID
- Rule severity
- Windows Event ID
- Account responsible for the activity
- Scheduled task name
- Task content or action

Example alert information:

```text
Agent: WIN10-LAB
Rule ID: 100104
Rule Level: 10
Event ID: 4698
Detection: DET-004: Windows scheduled task created
MITRE Technique: T1053.005
````

The first objective is to answer:

```text
What happened?
Where did it happen?
Who performed the action?
What task was created?
```

---

# 3. Initial Alert Triage

The analyst should confirm that the alert represents a scheduled task creation event.

Review the following field:

```text
data.win.system.eventID: 4698
```

Event ID `4698` indicates that a scheduled task was created.

The analyst should also confirm that the custom detection rule generated the alert.

```text
rule.id: 100104
```

The alert severity should also be reviewed.

```text
rule.level: 10
```

A Level 10 alert requires investigation, but the severity alone does not confirm malicious activity.

---

# 4. Identify the Affected Endpoint

The analyst should identify the system where the scheduled task was created.

Review:

```text
agent.name
agent.id
agent.ip
data.win.system.computer
```

Example:

```text
Agent Name: WIN10-LAB
Agent ID: 001
```

Questions to investigate:

* Is this a workstation or server?
* Is the system expected to create scheduled tasks?
* Is the endpoint associated with a sensitive user or administrator?
* Are other suspicious alerts occurring on the same system?

---

# 5. Identify the Account Responsible

The analyst should identify the account that created the scheduled task.

Review fields such as:

```text
data.win.eventdata.subjectUserName
data.win.eventdata.subjectDomainName
data.win.eventdata.subjectLogonId
```

Example:

```text
User: labadmin
Domain: DESKTOP-Q9TN2GI
```

The analyst should determine:

* Is the account legitimate?
* Is the account authorized to create scheduled tasks?
* Is the account an administrator?
* Was the account expected to perform this activity?

A legitimate account can still perform malicious or unauthorized actions.

---

# 6. Investigate the Scheduled Task

The most important part of the investigation is understanding what task was created.

Review the task-related information available in the Event ID `4698` event.

The analyst should identify:

* Task name
* Task action
* Program or command configured to execute
* Task trigger
* User account associated with the task

Example lab activity:

```text
Task Name: DET-004-TestTask
Action: notepad.exe
```

The analyst should determine whether the task name and action are expected.

Questions to ask:

* Does the task name appear legitimate?
* What executable or command will run?
* Is the executable located in a trusted directory?
* Does the task execute PowerShell or another scripting engine?
* Does the task execute from a temporary directory?
* Does the task execute from a user profile directory?
* Does the task contain suspicious arguments?

---

# 7. Analyze Task Content

The task configuration should be reviewed carefully.

Potentially suspicious task actions may include:

```text
powershell.exe
cmd.exe
wscript.exe
cscript.exe
mshta.exe
rundll32.exe
```

These executables are not automatically malicious.

However, additional investigation is required when they execute:

* Encoded commands
* Scripts from temporary directories
* Files from user profile directories
* Unknown executables
* Suspicious remote resources

The analyst should focus on the complete command or executable configured in the scheduled task.

---

# 8. Check for Persistence

Scheduled tasks are commonly abused as a persistence mechanism.

The analyst should determine:

```text
Will the task execute automatically?
Will the task execute after reboot?
Will the task execute at user logon?
Will the task execute repeatedly?
```

Tasks configured to run automatically may require additional investigation.

The analyst should also determine whether the task was recently created or modified.

---

# 9. Investigate Related Activity

The analyst should search Wazuh for additional activity related to:

* The same endpoint
* The same user account
* The same time period
* The scheduled task name
* The executable configured in the task

Example investigation areas include:

```text
Process execution
PowerShell activity
User account changes
Scheduled task modifications
Suspicious logons
```

The purpose is to determine whether the scheduled task creation is an isolated event or part of a larger sequence of suspicious activity.

---

# 10. MITRE ATT&CK Analysis

DET-004 is mapped to:

```text
T1053.005
Scheduled Task/Job: Scheduled Task
```

Scheduled tasks can be used by attackers for:

```text
Execution
Persistence
Privilege Escalation
```

The MITRE mapping provides context for the potential attacker technique but does not confirm that every scheduled task is malicious.

---

# 11. Determine Whether the Activity Is Authorized

Before classifying the event as malicious, the analyst should determine whether the activity is legitimate.

The following questions should be answered:

* Was the task created by an authorized administrator?
* Is the task associated with approved software?
* Is the task required for system administration?
* Is the executable legitimate?
* Is the timing of the activity expected?

Possible legitimate examples include:

* Software updates
* System maintenance
* Backup tasks
* Administrative automation

---

# 12. Investigation Decision

After reviewing the available evidence, the analyst should classify the activity.

## Benign

The activity may be classified as benign when:

* The account is authorized
* The scheduled task is expected
* The executable is legitimate
* The activity is associated with approved software or administration

---

## Suspicious

The activity may be classified as suspicious when:

* The task was created unexpectedly
* The account is unusual
* The task name appears suspicious
* The task executes an unusual command
* Related suspicious activity is identified

---

## Potentially Malicious

The activity may be classified as potentially malicious when:

* The task executes suspicious scripts or commands
* The task establishes persistence
* The account is unauthorized
* Additional malicious activity is observed
* The task is associated with known malicious behavior

---

# 13. Response Actions

If the scheduled task is determined to be suspicious or malicious, possible response actions include:

```text
Verify the affected endpoint
Review the task configuration
Identify the responsible account
Preserve relevant evidence
Investigate related activity
Disable or remove the malicious task
Investigate the executed program
Check for additional persistence mechanisms
```

Response actions should follow the organization's incident response procedures.

---

# 14. Lab Investigation Result

During the DET-004 lab test, a scheduled task was intentionally created in an isolated Windows 10 environment.

The activity generated:

```text
Windows Security Event ID: 4698
```

The Wazuh agent successfully collected the event.

The event matched the custom Wazuh detection:

```text
Rule ID: 100104
Rule Level: 10
Detection: DET-004: Windows scheduled task created
MITRE Technique: T1053.005
```

The test activity was authorized and performed for detection validation.

Therefore, the lab event was classified as:

```text
Benign — Authorized Detection Test
```

---

# 15. Investigation Workflow

The SOC investigation process for DET-004 can be summarized as:

```text
Alert Received
        ↓
Validate Event ID 4698
        ↓
Identify Affected Endpoint
        ↓
Identify Responsible Account
        ↓
Review Scheduled Task Name
        ↓
Analyze Task Action
        ↓
Search for Related Activity
        ↓
Determine Authorization
        ↓
Classify Activity
        ↓
Respond if Required
```

---

# 16. Conclusion

DET-004 demonstrates the SOC investigation process for Windows Scheduled Task creation.

The investigation focuses on identifying:

* Where the activity occurred
* Who created the scheduled task
* What task was created
* What program or command the task executes
* Whether the activity is authorized
* Whether additional suspicious activity is present

Scheduled task creation alone does not indicate malicious activity.

The event must be investigated in context to determine whether it represents legitimate administration, normal system activity, suspicious behavior, or potential persistence.

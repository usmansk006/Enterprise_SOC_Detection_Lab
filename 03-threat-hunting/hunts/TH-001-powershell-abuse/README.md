# TH-001 — PowerShell Abuse

## 1. Hunt Overview

**Hunt ID:** TH-001
**Hunt Name:** PowerShell Abuse
**Category:** Command and Scripting Interpreter
**Primary Platform:** Windows
**Primary Telemetry:** PowerShell Operational Logs, Sysmon, Windows Security Events, Wazuh
**MITRE ATT&CK:** T1059.001 — PowerShell
**Hunt Type:** Endpoint Threat Hunt

This hunt investigates potentially suspicious use of PowerShell within the Windows environment.

PowerShell is a legitimate Windows administration and automation framework, but it can also be abused by adversaries for execution, discovery, payload retrieval, persistence, credential access, and defense evasion.

The objective of this hunt is therefore not to treat PowerShell execution itself as malicious. Instead, the hunt identifies **PowerShell behaviors and execution contexts that warrant additional investigation**.

---

## 2. Hunt Objective

The objective is to proactively identify suspicious PowerShell activity that may not be adequately represented by existing alert-based detection.

The hunt examines:

* PowerShell process execution
* Command-line arguments
* Encoded commands
* Suspicious execution context
* Parent-child process relationships
* User context
* PowerShell operational events
* Related Sysmon process events
* Associated Wazuh telemetry

The hunt also evaluates whether existing detection coverage successfully identifies the observed behavior.

---

## 3. Hunt Hypothesis

> An adversary may abuse PowerShell for command execution or other post-compromise activity in a way that is observable through Windows endpoint telemetry but is not necessarily identified by existing detection rules.

The hypothesis is investigated through multiple telemetry sources rather than relying on a single event.

---

## 4. MITRE ATT&CK Mapping

### Primary Technique

**T1059.001 — Command and Scripting Interpreter: PowerShell**

PowerShell is frequently used for legitimate administration as well as adversary execution.

The presence of PowerShell alone is therefore insufficient to classify an event as malicious.

The investigation focuses on contextual indicators surrounding PowerShell execution.

### Relevant Behavioral Context

Depending on the observed activity, additional ATT&CK mappings may be applicable, including techniques associated with:

* Execution
* Discovery
* Defense Evasion
* Credential Access
* Persistence
* Command and Control

Additional mappings should only be assigned when the investigated behavior provides sufficient evidence for the technique.

---

## 5. Data Sources

The hunt uses endpoint telemetry available within the laboratory.

### Windows PowerShell Operational Logs

Primary source for PowerShell-specific activity.

Relevant information can include:

* PowerShell execution
* Script activity
* Command details
* Host information
* User context
* Execution timestamps

### Sysmon

Sysmon provides endpoint telemetry that can support process-level investigation.

Relevant fields include:

* Process image
* Parent image
* Command line
* Process ID
* Parent process ID
* User
* Timestamp

Sysmon is treated as an **endpoint telemetry source**, not as an EDR platform.

### Windows Security Logs

Windows Security telemetry provides supporting identity and authentication context.

Potentially relevant information includes:

* User activity
* Logon events
* Process-related security events where available
* Authentication context

### Wazuh

Wazuh provides centralized collection, analysis, alerting, and search capabilities for the endpoint telemetry.

Wazuh is used to correlate PowerShell-related events with surrounding activity.

---

## 6. Hunt Methodology

The hunt follows a structured investigation process.

```text
PowerShell Activity
        ↓
Identify Execution
        ↓
Review Command Line
        ↓
Review User Context
        ↓
Review Parent Process
        ↓
Review Child Processes
        ↓
Correlate Related Events
        ↓
Assess Behavior
        ↓
Review Detection Coverage
        ↓
Identify Detection Gaps
```

The analyst should avoid classifying an event based on a single field.

For example:

```text
powershell.exe
```

is not inherently malicious.

A more meaningful investigation considers the complete execution context.

---

## 7. Initial Hunt Questions

The hunt addresses questions such as:

1. Which systems executed PowerShell?
2. Which users initiated the activity?
3. What PowerShell command or arguments were used?
4. Was the command encoded?
5. What process launched PowerShell?
6. What processes did PowerShell launch?
7. Did the execution occur in an unusual user or system context?
8. Were there related authentication events?
9. Were there related network connections?
10. Did existing detection logic identify the activity?
11. If detection occurred, was the alert sufficiently actionable?
12. If detection did not occur, what telemetry or detection gap existed?

---

## 8. Suspicious PowerShell Indicators

The following indicators can increase the priority of an investigation.

### Encoded Commands

PowerShell execution using encoded command parameters should receive additional scrutiny.

Example indicator:

```text
-EncodedCommand
```

Encoded PowerShell does not automatically prove malicious activity. The analyst should investigate the decoded content and execution context.

### Suspicious Parent Processes

PowerShell launched by an unexpected process may warrant investigation.

Examples of contextual concerns include:

```text
Office application
Script host
Unexpected service
Unknown executable
Unexpected management process
```

The legitimacy of the parent process must be assessed against the environment.

### Suspicious Command-Line Arguments

Examples of parameters that may warrant additional investigation include:

```text
-EncodedCommand
-NoProfile
-ExecutionPolicy Bypass
-WindowStyle Hidden
```

These parameters are not independently proof of malicious activity. They become more significant when combined with other suspicious characteristics.

### Unusual User Context

PowerShell execution from:

* Unexpected accounts
* Administrative accounts outside expected activity
* Service accounts
* Newly created accounts

may warrant additional investigation.

### Suspicious Child Processes

PowerShell spawning unusual child processes can provide important behavioral context.

The analyst should examine both the parent-child relationship and the command line.

---

## 9. Hunting Workflow

### Step 1 — Identify PowerShell Activity

Search the available endpoint telemetry for PowerShell execution.

Primary indicators include:

```text
powershell.exe
pwsh.exe
```

The search should cover the relevant telemetry sources rather than relying exclusively on Wazuh alerts.

---

### Step 2 — Review Command-Line Arguments

For each potentially interesting event, inspect the complete command line.

Important questions include:

* Was a script executed?
* Was a command encoded?
* Was an unusual execution policy specified?
* Was the PowerShell window hidden?
* Were remote resources accessed?
* Was another executable launched?

---

### Step 3 — Investigate the Parent Process

Determine what initiated PowerShell.

The relationship should be represented as:

```text
Parent Process
      ↓
PowerShell
      ↓
Child Process / Activity
```

Unexpected parent-child relationships can provide valuable behavioral context.

---

### Step 4 — Investigate the User

Identify the account associated with the execution.

Compare the observed account with the expected role and normal administrative behavior.

---

### Step 5 — Correlate Events

Search for related activity around the execution timestamp.

Potentially relevant events include:

* Authentication events
* Process creation
* Process termination
* File activity
* Scheduled task activity
* Network activity
* Additional PowerShell events
* Wazuh alerts

Correlation helps distinguish isolated administrative activity from a broader behavioral sequence.

---

### Step 6 — Assess Detection Coverage

Determine whether the activity:

1. Generated an existing Wazuh alert.
2. Was visible in telemetry but did not generate an alert.
3. Was only partially detected.
4. Generated an alert that required tuning.

This step connects threat hunting directly to detection engineering.

---

## 10. Evidence Collection

Evidence should be collected only for relevant findings.

Recommended evidence categories include:

```text
PowerShell event
Sysmon process event
Command line
Parent-child relationship
User context
Related authentication events
Related network activity
Wazuh alert
```

Suggested naming convention:

```text
TH-001-powershell-abuse-powershell-event.png
TH-001-powershell-abuse-sysmon-process.png
TH-001-powershell-abuse-command-line.png
TH-001-powershell-abuse-wazuh-alert.png
```

Actual filenames should reflect the evidence that was genuinely collected.

No fabricated screenshots or event results should be added.

---

## 11. Investigation Criteria

A potentially suspicious PowerShell event should be evaluated using multiple dimensions.

| Investigation Area | Questions                                     |
| ------------------ | --------------------------------------------- |
| User               | Who executed PowerShell?                      |
| Host               | Which endpoint executed it?                   |
| Time               | When did the activity occur?                  |
| Process            | What executable was launched?                 |
| Parent             | What launched PowerShell?                     |
| Command Line       | What arguments were supplied?                 |
| Encoding           | Was encoded execution used?                   |
| Children           | What did PowerShell launch?                   |
| Authentication     | Was there related authentication activity?    |
| Network            | Did the process communicate externally?       |
| Detection          | Did existing rules identify it?               |
| Context            | Is the behavior expected in this environment? |

The final assessment must be based on the combined evidence.

---

## 12. Detection Coverage Assessment

The hunt explicitly evaluates the relationship between observed PowerShell behavior and existing detections.

Possible outcomes:

### Detected

The behavior generated an existing detection.

The analyst evaluates whether:

* The alert contains sufficient context.
* The severity is appropriate.
* The rule is too broad.
* The rule is too narrow.
* Additional correlation would improve fidelity.

### Telemetry Present — Detection Absent

The endpoint generated sufficient telemetry, but no existing detection identified the behavior.

This represents a potential detection-engineering opportunity.

### Detection Requires Tuning

The activity generated an alert, but the detection may produce excessive noise or insufficient context.

The finding can be passed to the detection-engineering lifecycle for tuning.

### Insufficient Telemetry

The required evidence was not available.

This represents a visibility or telemetry gap rather than necessarily a detection-rule problem.

---

## 13. False-Positive Considerations

PowerShell is commonly used by:

* System administrators
* IT automation
* Software deployment systems
* Configuration-management tools
* Monitoring systems
* Security products
* Windows management processes

Therefore, PowerShell execution should not automatically be treated as malicious.

The analyst should consider:

* Expected administrative activity
* Known automation
* Account role
* Host role
* Execution frequency
* Command-line content
* Parent process
* Child processes
* Time of execution
* Related activity

Detection logic should prioritize suspicious combinations of characteristics rather than simply matching `powershell.exe`.

---

## 14. Detection Gap Analysis

The hunt produces actionable output when it identifies a difference between:

```text
Observable Behavior
        ↓
Available Telemetry
        ↓
Current Detection
```

A gap may occur at any of these stages.

### Telemetry Gap

Required activity is not being collected.

### Query Gap

The telemetry exists, but the current hunting logic does not identify the behavior.

### Detection Gap

The behavior is observable and huntable but lacks an appropriate automated detection.

### Context Gap

An alert exists but lacks sufficient information for efficient triage.

### Tuning Gap

The detection identifies too many legitimate PowerShell events.

These distinctions help route findings to the correct engineering activity.

---

## 15. Detection Engineering Handoff

When the hunt identifies a validated detection gap, the result should be transferred to:

```text
05-detection-engineering/
```

The handoff should contain:

* Hunt ID
* Observed behavior
* Relevant telemetry
* ATT&CK technique
* Detection requirement
* Required fields
* Suggested detection logic
* Expected behavior
* False-positive considerations
* Validation requirements

The resulting detection should then enter the detection lifecycle:

```text
Hunt Finding
     ↓
Detection Requirement
     ↓
Rule Development
     ↓
Test Case
     ↓
Validation
     ↓
Tuning
     ↓
Regression Test
     ↓
Retest
```

---

## 16. Hunt Completion Criteria

TH-001 is considered operationally complete when the hunt has:

* A defined hypothesis
* ATT&CK mapping
* Identified telemetry sources
* Repeatable hunting methodology
* Documented queries
* Evidence-handling procedure
* Investigation criteria
* Detection-coverage assessment
* Detection-gap analysis
* Detection-engineering handoff process

Specific findings, screenshots, metrics, and test outcomes should only be documented when they have been actually observed and validated in the laboratory.

---

## 17. Operational Value

This hunt demonstrates a proactive approach to PowerShell monitoring.

Rather than depending exclusively on predefined alerts, the analyst can independently search endpoint telemetry for suspicious PowerShell behavior, investigate the surrounding execution context, assess existing detection coverage, and identify opportunities for detection improvement.

The resulting workflow connects:

```text
ATT&CK
  ↓
Hunt Hypothesis
  ↓
Telemetry
  ↓
Hunt Query
  ↓
Investigation
  ↓
Evidence
  ↓
Detection Coverage
  ↓
Detection Gap
  ↓
Detection Engineering
  ↓
Retesting
```

This makes TH-001 a reusable threat-hunting capability within the broader Enterprise SOC Detection Lab.

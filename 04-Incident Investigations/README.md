# Incident Investigations

## Overview

This section contains structured SOC investigations performed against security alerts generated within the Enterprise SOC Detection Lab.

The investigations demonstrate the complete analyst workflow from initial alert intake through technical analysis, evidence correlation, scope determination, findings, and response recommendations.

The objective is to demonstrate practical SOC investigation capabilities using real telemetry generated within the controlled laboratory environment.

---

## Investigation Workflow

```text
ALERT
  ↓
ALERT INTAKE
  ↓
TRIAGE
  ↓
INVESTIGATION
  ↓
SCOPE ANALYSIS
  ↓
TIMELINE
  ↓
FINDINGS
  ↓
RESPONSE RECOMMENDATIONS
````

---

## Investigation Cases

| ID      | Investigation                           | Primary Focus                                |
| ------- | --------------------------------------- | -------------------------------------------- |
| INV-001 | Suspicious Encoded PowerShell Execution | PowerShell execution and command analysis    |
| INV-002 | Multiple Failed Logons                  | Windows authentication failure analysis      |
| INV-003 | Suspicious Windows Account Creation     | Account creation and process correlation     |
| INV-004 | Suspicious Process Execution            | Parent-child process analysis                |
| INV-005 | Scheduled Task Persistence              | Persistence and scheduled task activity      |
| INV-006 | Suspicious Network Connection           | Endpoint network activity analysis           |
| INV-007 | Malware Alert and Endpoint Triage       | Malware detection and endpoint investigation |
| INV-008 | Suspicious Administrative Activity      | Privileged and administrative activity       |

---

## Investigation Structure

Each investigation follows a standardized SOC case structure:

```text
INV-00X/
├── README.md
├── 01-alert-intake.md
├── 02-triage.md
├── 03-investigation.md
├── 04-scope-analysis.md
├── 05-timeline.md
├── 06-findings.md
├── 07-response-recommendations.md
└── evidence/
```

### Documentation Purpose

| File                             | Purpose                                                    |
| -------------------------------- | ---------------------------------------------------------- |
| `README.md`                      | Investigation overview and case summary                    |
| `01-alert-intake.md`             | Documents the original security alert                      |
| `02-triage.md`                   | Performs initial alert validation and prioritization       |
| `03-investigation.md`            | Documents detailed technical analysis                      |
| `04-scope-analysis.md`           | Determines affected users, hosts, processes, and activity  |
| `05-timeline.md`                 | Reconstructs the sequence of relevant events               |
| `06-findings.md`                 | Documents evidence-based findings and final verdict        |
| `07-response-recommendations.md` | Documents recommended response and remediation actions     |
| `evidence/`                      | Contains supporting screenshots and investigation evidence |

---

## Investigation Methodology

Investigations are performed using an evidence-driven approach.

The analyst evaluates:

* Wazuh security alerts
* Windows Security Event Logs
* Sysmon telemetry
* PowerShell activity
* Process execution
* Authentication activity
* User and endpoint context
* Related events
* MITRE ATT&CK techniques
* Temporal relationships between events

Individual alerts are not automatically treated as malicious. Activity is evaluated within its operational and laboratory context before assigning a final verdict.

---

## Investigation Principles

### Evidence-Based Analysis

Investigation conclusions are based on observable telemetry and supporting evidence.

### Event Correlation

Related events are correlated to establish a more complete understanding of the activity.

### Scope Determination

The investigation attempts to determine:

* What happened?
* When did it happen?
* Which endpoint was involved?
* Which account was involved?
* Which process generated the activity?
* Was the activity local or remote?
* Were additional systems or accounts affected?

### Defensible Findings

The final verdict is based on available evidence.

Where evidence is insufficient to establish malicious intent, the investigation documents the limitation rather than making an unsupported assumption.

---

## Evidence

Each investigation maintains an `evidence/` directory containing relevant screenshots and supporting artifacts.

Evidence is named using the investigation identifier:

```text
INV-001-*.png
INV-002-*.png
INV-003-*.png
```

This provides consistent traceability between investigation documentation and supporting evidence.

---

## Environment

All investigations are performed within an isolated and authorized security laboratory environment.

Primary telemetry sources include:

* Wazuh
* Windows 10
* Sysmon
* Windows Security Event Logs
* PowerShell logging
* Process execution telemetry

---

## Relationship to Detection Engineering

The investigations complement the detection engineering section of the project.

**Detection Engineering asks:**

> Can the security monitoring environment detect the behavior?

**Investigation asks:**

> What actually happened when the alert was generated?

This separation demonstrates both detection development and SOC analyst investigation capabilities.

---

## Investigation Status

An investigation is considered complete when:

* The triggering alert has been identified.
* Relevant telemetry has been collected.
* The activity has been analyzed.
* Related events have been correlated.
* Investigation scope has been established.
* Findings have been documented.
* A final verdict has been reached.
* Response recommendations have been provided.
* Supporting evidence has been preserved.

s.

# SOC Telemetry & Data Flow

## 1. Overview

This document describes the end-to-end flow of security telemetry through the **Enterprise SOC Detection, Threat Hunting & Incident Response Lab**.

The data-flow architecture connects endpoint activity to centralized telemetry collection, detection processing, alert generation, investigation, threat hunting, and detection improvement.

The core telemetry pipeline is:

```text
Security Activity
      ↓
Windows Endpoint
      ↓
Windows Security Logs / Sysmon
      ↓
Wazuh Agent
      ↓
Wazuh Manager
      ↓
Event Processing
      ↓
Detection Rules
      ↓
Security Alert
      ↓
Wazuh Dashboard
      ↓
SOC Analyst
      ↓
Investigation / Threat Hunting
      ↓
Incident Response
      ↓
Detection Engineering
      ↓
Tuning & Regression Testing
```

---

# 2. Data-Flow Objectives

The telemetry architecture is designed to ensure that security-relevant activity can be:

* Generated in a controlled environment.
* Recorded at the endpoint.
* Collected by the security agent.
* Forwarded to centralized monitoring infrastructure.
* Parsed and processed.
* Evaluated against detection logic.
* Converted into actionable alerts.
* Investigated by an analyst.
* Correlated with supporting telemetry.
* Used for threat hunting.
* Incorporated into incident response.
* Used to improve future detection coverage.

---

# 3. Primary Data Sources

The laboratory uses endpoint telemetry as the primary source of security observations.

## 3.1 Windows Security Event Logs

Windows Security Event Logs provide native operating-system security telemetry.

Examples of security-relevant events include:

| Event Type                       | Security Context                  |
| -------------------------------- | --------------------------------- |
| Failed logon                     | Authentication monitoring         |
| Successful logon                 | Authentication context            |
| User account creation            | Identity and account management   |
| Security policy activity         | Security configuration monitoring |
| Other configured security events | Host security monitoring          |

These events provide identity and operating-system context for detection and investigation.

---

## 3.2 Sysmon

Sysmon supplements Windows Security Event Logs with detailed endpoint telemetry.

Relevant telemetry includes:

* Process creation.
* Process termination.
* Parent-child process relationships.
* Command-line information.
* Network-related process activity when configured.
* Additional endpoint activity based on the deployed configuration.

Sysmon provides additional behavioral context that can be correlated with native Windows security events.

---

# 4. Endpoint Telemetry Generation

Security telemetry originates from activity occurring on the monitored endpoint.

Examples include:

* Authentication attempts.
* User account operations.
* Process execution.
* PowerShell execution.
* Scheduled-task activity.
* Security-policy discovery.
* File-related activity.
* Other controlled security-testing activity.

The endpoint generates operating-system and Sysmon events corresponding to observable activity.

The data-flow begins at:

```text
Controlled Activity
        ↓
Operating-System Activity
        ↓
Telemetry Generation
```

---

# 5. Wazuh Agent Collection

The Wazuh Agent operates on the monitored endpoint and acts as the telemetry collection and forwarding component.

Its responsibilities include:

1. Monitoring configured event sources.
2. Collecting relevant endpoint events.
3. Processing endpoint-side collection configuration.
4. Forwarding telemetry to the Wazuh Manager.
5. Maintaining communication with the centralized monitoring infrastructure.

The collection flow is:

```text
Windows Security Logs ─────┐
                           │
                           ▼
                      Wazuh Agent
                           │
Sysmon Events ─────────────┘
                           │
                           ▼
                    Wazuh Manager
```

The agent therefore provides the transport layer between endpoint telemetry and centralized security monitoring.

---

# 6. Telemetry Transmission

Collected events are forwarded from the monitored endpoint to the Wazuh Manager.

The transmission process can be represented as:

```text
Endpoint
   │
   │ Security Telemetry
   ▼
Wazuh Agent
   │
   │ Forwarded Events
   ▼
Wazuh Manager
```

The centralized manager receives telemetry from the monitored environment and processes the events for detection and analysis.

---

# 7. Wazuh Manager Processing

The Wazuh Manager provides the centralized event-processing layer.

Incoming telemetry passes through processing stages including:

```text
Incoming Event
      ↓
Event Parsing
      ↓
Field Extraction
      ↓
Rule Evaluation
      ↓
Correlation
      ↓
Severity Assignment
      ↓
Alert Generation
```

Processing converts raw endpoint observations into structured security events and alerts.

---

# 8. Event Parsing and Normalization

Raw endpoint events contain information about the observed activity.

Relevant fields can include:

* Timestamp.
* Host information.
* User information.
* Process name.
* Process identifier.
* Parent process.
* Command line.
* Event identifier.
* Event source.
* Security-related metadata.

Structured fields allow detection logic to operate on specific event characteristics instead of relying solely on free-form text.

---

# 9. Detection Processing

After event processing, telemetry is evaluated against configured detection logic.

The detection layer can identify patterns such as:

* Repeated authentication failures.
* Suspicious process execution.
* Suspicious PowerShell activity.
* Encoded PowerShell commands.
* Account creation.
* Persistence-related activity.
* Suspicious parent-child relationships.
* Defense-evasion behavior.
* Suspicious network activity.

The detection process is:

```text
Normalized Event
      ↓
Detection Conditions
      ↓
Rule Match
      ↓
Alert
```

Detection content is documented in:

```text
02-detections/
```

while detection engineering implementation and testing are maintained under:

```text
05-detection-engineering/
```

---

# 10. Alert Generation

When telemetry satisfies the conditions of a detection rule, Wazuh generates a security alert.

An alert provides an analyst with structured information that can be used during triage.

Typical investigation fields include:

* Alert timestamp.
* Rule identifier.
* Alert severity.
* Agent information.
* Host information.
* Event identifier.
* User context.
* Process context.
* Command-line information.
* Source information.
* MITRE ATT&CK metadata when mapped.

The alert represents the transition from raw telemetry to an analyst-facing security signal.

---

# 11. Wazuh Dashboard

Generated alerts and searchable event data are exposed through the Wazuh Dashboard.

The dashboard supports:

* Alert review.
* Event searching.
* Filtering.
* Field inspection.
* Timeline analysis.
* Detection validation.
* Investigation.
* Evidence collection.

The analyst workflow begins when a security alert or hunting hypothesis requires investigation.

```text
Wazuh Alert
     ↓
Dashboard
     ↓
SOC Analyst
```

---

# 12. Alert Triage

Alert triage determines whether an alert requires additional investigation.

The initial triage process evaluates:

1. What happened?
2. Which host generated the event?
3. Which user was involved?
4. When did the activity occur?
5. Which process or command was involved?
6. Is the activity expected?
7. Are related events present?
8. Does the behavior correspond to a known ATT&CK technique?
9. Is additional investigation required?

The triage process is:

```text
Alert
 ↓
Validate Event
 ↓
Establish Context
 ↓
Review Supporting Telemetry
 ↓
Determine Scope
 ↓
Investigate / Close
```

---

# 13. Event Correlation

Individual events are not always sufficient to establish the meaning of security activity.

The investigation workflow therefore correlates multiple telemetry sources.

For example:

```text
Windows Security Event
        +
Sysmon Process Event
        +
PowerShell Telemetry
        +
Wazuh Alert
        ↓
Correlated Activity
        ↓
Investigation Timeline
```

Correlation allows analysts to establish relationships between authentication, process, user, and endpoint activity.

---

# 14. Investigation Data Flow

When an alert requires investigation, the analyst follows the available telemetry across multiple event sources.

```text
Alert
  ↓
Primary Event
  ↓
Related Events
  ↓
Process Context
  ↓
User Context
  ↓
Host Context
  ↓
Timeline
  ↓
Behavior Analysis
  ↓
Finding
```

Investigation artifacts are maintained under:

```text
04-Incident-Investigations/
```

---

# 15. Threat Hunting Data Flow

Threat hunting uses the same underlying telemetry but begins from a hypothesis rather than an alert.

The hunting pipeline is:

```text
Threat Hypothesis
      ↓
ATT&CK Technique
      ↓
Required Telemetry
      ↓
Hunting Query
      ↓
Telemetry Search
      ↓
Event Correlation
      ↓
Finding
      ↓
Detection Gap
```

Hunting activities are maintained under:

```text
03-threat-hunting/
```

This enables proactive identification of activity that may not have generated a high-confidence alert.

---

# 16. Incident Response Data Flow

When investigation determines that activity requires response, relevant findings are transferred into the incident-response workflow.

```text
Detection
    ↓
Triage
    ↓
Investigation
    ↓
Scope Assessment
    ↓
Response
    ↓
Evidence Preservation
    ↓
Recovery
    ↓
Post-Incident Review
```

Incident response playbooks and procedures are maintained under:

```text
06-incident-response/
```

---

# 17. Forensic Data Flow

Investigations requiring deeper endpoint analysis can transition into forensic analysis.

```text
Security Alert
      ↓
Investigation
      ↓
Evidence Identification
      ↓
Endpoint Artifact Collection
      ↓
Forensic Analysis
      ↓
Timeline Reconstruction
      ↓
Finding
```

Relevant forensic artifacts may include:

* Windows Event Logs.
* PowerShell artifacts.
* Registry artifacts.
* Prefetch artifacts.
* Persistence artifacts.
* Process timelines.

Forensic material is maintained under:

```text
07-forensics/
```

---

# 18. Network Data Flow

Network telemetry is incorporated as an additional analytical layer.

The network data-flow is:

```text
Network Activity
      ↓
Network Telemetry
      ↓
Network Monitoring / Capture
      ↓
Analysis
      ↓
Detection / Hunting
      ↓
Correlation
      ↓
Investigation
```

Network-security artifacts are maintained under:

```text
08-network-security/
```

Where applicable, network observations can be correlated with endpoint activity to improve investigation context.

---

# 19. Threat Intelligence Data Flow

Indicators discovered during investigation can be extracted and enriched through the threat-intelligence workflow.

```text
Investigation
      ↓
Indicator Identification
      ↓
IOC Extraction
      ↓
Threat Intelligence Enrichment
      ↓
Context
      ↓
Investigation Decision
```

Supported indicator categories include:

* Hashes.
* IP addresses.
* Domains.
* URLs.

Threat intelligence artifacts are maintained under:

```text
09-threat-intelligence/
```

---

# 20. Security Automation Data Flow

Automation can process repetitive SOC tasks using structured alert and telemetry data.

```text
Security Data
      ↓
Automation Script
      ↓
Parsing / Extraction
      ↓
Analysis
      ↓
Output
      ↓
Analyst Review
```

Automation capabilities include:

* Alert analysis.
* IOC extraction.
* Timeline generation.
* Log analysis.
* Detection validation.

Automation artifacts are maintained under:

```text
10-scripts/
```

---

# 21. Detection Engineering Feedback Loop

The data-flow architecture does not end when an alert is investigated.

Investigation and hunting results are fed back into detection engineering.

```text
Detection
    ↓
Investigation
    ↓
Finding
    ↓
Detection Gap
    ↓
Rule Improvement
    ↓
Testing
    ↓
Regression Testing
    ↓
Retesting
    ↓
Improved Detection
```

This feedback loop allows the laboratory to continuously improve detection quality.

---

# 22. Detection Validation Flow

Detection validation verifies that security activity produces the expected telemetry and detection result.

The validation lifecycle is:

```text
Controlled Test Activity
        ↓
Expected Telemetry
        ↓
Telemetry Collection
        ↓
Detection Rule
        ↓
Expected Alert
        ↓
Analyst Verification
        ↓
Evidence Collection
        ↓
Result Documentation
```

Validation artifacts are connected to the corresponding detection and test-case documentation.

---

# 23. Regression Testing

Detection changes are evaluated against previously validated behaviors.

The regression workflow is:

```text
Existing Detection
       ↓
Detection Change
       ↓
Regression Test
       ↓
Expected Behavior
       ↓
Observed Result
       ↓
Pass / Failure Analysis
       ↓
Release / Further Tuning
```

Regression-testing methodology and test cases are maintained under:

```text
05-detection-engineering/
```

---

# 24. Continuous Improvement

The complete data-flow lifecycle forms a continuous improvement loop:

```text
             ┌───────────────────────┐
             │                       │
             ▼                       │
        Security Activity            │
             ↓                       │
          Telemetry                 │
             ↓                       │
         Detection                 │
             ↓                       │
          Triage                   │
             ↓                       │
       Investigation              │
             ↓                       │
       Threat Hunting             │
             ↓                       │
      Incident Response           │
             ↓                       │
          Forensics               │
             ↓                       │
       Gap Identification         │
             ↓                       │
       Detection Engineering      │
             ↓                       │
          Tuning                  │
             ↓                       │
      Regression Testing          │
             ↓                       │
          Retesting ──────────────┘
```

This lifecycle ensures that security monitoring capabilities evolve based on observed behavior, investigation findings, and identified detection gaps.

---

# 25. Data Protection and Evidence Handling

Telemetry and investigation evidence can contain sensitive information.

Public repository artifacts are therefore reviewed before publication.

Information requiring protection includes:

* Passwords.
* Authentication tokens.
* API keys.
* Personal information.
* Unnecessary internal infrastructure details.
* Sensitive host information.
* Other credentials or secrets.

Evidence should preserve the information required to demonstrate the security finding while removing unnecessary sensitive information.

---

# 26. Architecture Summary

The laboratory implements a layered telemetry and security-analysis architecture:

```text
┌───────────────────────────────────────────┐
│              Security Activity            │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│             Endpoint Telemetry             │
│       Windows Security Logs + Sysmon      │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│               Wazuh Agent                 │
│        Collection + Event Forwarding      │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│              Wazuh Manager                │
│      Processing + Detection + Alerts      │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│             Wazuh Dashboard               │
│          Triage + Investigation            │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│       Hunting / Investigation / IR         │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│ Forensics / Network / Threat Intelligence │
└──────────────────────┬────────────────────┘
                       ↓
┌───────────────────────────────────────────┐
│         Detection Engineering             │
│       Tuning + Regression Testing         │
└───────────────────────────────────────────┘
```

The resulting architecture provides an integrated foundation for SOC monitoring, detection engineering, threat hunting, incident investigation, incident response, forensic analysis, network security, threat intelligence, automation, and continuous detection improvement.

# Windows Endpoint Infrastructure

## 1. Overview

The Windows endpoint provides the primary endpoint telemetry source for the SOC lab.

It is configured as a monitored workstation through the Wazuh Agent and provides security telemetry from Windows Security Event Logs, Sysmon, and PowerShell logging.

The endpoint is used to validate the complete security monitoring lifecycle:

```text
Endpoint Activity
      ↓
Telemetry Generation
      ↓
Wazuh Agent Collection
      ↓
Wazuh Manager Processing
      ↓
Detection
      ↓
Alert
      ↓
Investigation
      ↓
Response / Improvement
```

The Windows system operates as an isolated laboratory endpoint for authorized security testing and detection validation.

---

## 2. Endpoint Role

The Windows endpoint provides the following security telemetry:

* Windows Security Events
* Sysmon events
* PowerShell operational events
* Process execution information
* Authentication activity
* Account activity
* System activity
* File and process-related telemetry
* Other configured Windows security events

The endpoint is therefore the primary source for testing Windows-focused SOC detections.

---

## 3. Monitoring Architecture

The Windows endpoint integrates with the Wazuh infrastructure as follows:

```text
┌──────────────────────────────┐
│      Windows Endpoint        │
│                              │
│ Windows Security Logs        │
│ Sysmon                        │
│ PowerShell                    │
└──────────────┬───────────────┘
               │
               │ Wazuh Agent
               ▼
┌──────────────────────────────┐
│        Wazuh Manager         │
│                              │
│ Collection                   │
│ Parsing                      │
│ Detection                    │
│ Alert Generation             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Wazuh Dashboard        │
│                              │
│ Monitoring                   │
│ Investigation                │
│ Hunting                      │
└──────────────────────────────┘
```

This provides centralized monitoring while maintaining the endpoint as the source of the original telemetry.

---

## 4. Wazuh Agent

The Wazuh Agent is installed on the Windows endpoint and is responsible for collecting configured telemetry and forwarding it to the Wazuh Manager.

The agent provides the communication layer between the Windows operating system and the centralized security monitoring infrastructure.

The agent configuration determines which telemetry sources are collected and monitored.

---

## 5. Windows Security Event Logs

Windows Security Event Logs provide security-relevant operating-system activity.

Important event categories used by the project include:

### Authentication

Authentication events can provide visibility into:

* Successful logons
* Failed logons
* Account-related activity
* Authentication anomalies

### Account Management

Account-management events can identify activity such as:

* User creation
* User modification
* Group membership changes
* Other identity-related operations

These events are particularly useful for identity-focused detection engineering and investigation.

---

## 6. Sysmon Telemetry

Sysmon is deployed as an endpoint telemetry source to provide additional visibility into system activity.

Relevant Sysmon telemetry can include:

* Process creation
* Parent-child process relationships
* Command-line information
* File-related activity
* Network connection information where configured

A key advantage of Sysmon telemetry is the additional process context it can provide beyond standard Windows event logging.

### Important Classification

Sysmon is treated within this project as an **endpoint telemetry and logging source**.

It is not classified as an EDR platform.

---

## 7. PowerShell Telemetry

PowerShell is monitored because it is a powerful administrative and scripting capability that can also be abused by attackers.

PowerShell telemetry can provide visibility into:

* Script execution
* Command execution
* Script block activity
* Encoded commands
* Suspicious PowerShell behavior

PowerShell-related detections are documented in:

```text
02-detections/
```

and:

```text
05-detection-engineering/
```

---

## 8. Endpoint Telemetry Sources

The Windows endpoint can be viewed as multiple telemetry layers:

```text
┌─────────────────────────────┐
│ Windows Security Events     │
│ Identity / Authentication   │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│ Sysmon                      │
│ Process / System Telemetry  │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│ PowerShell Logging          │
│ Script / Command Telemetry  │
└──────────────┬──────────────┘
               │
               ▼
         Wazuh Agent
```

Combining multiple telemetry sources improves investigative context and reduces dependence on a single event source.

---

## 9. Process Visibility

Process telemetry is important for identifying suspicious execution chains.

The project uses process-related information to examine:

```text
Parent Process
      ↓
Child Process
      ↓
Command Line
      ↓
User Context
      ↓
Timestamp
      ↓
Related Activity
```

This enables analysts to investigate not only what process executed, but also how it was launched and under which user context.

---

## 10. Authentication Monitoring

Authentication activity provides important security context.

The monitoring architecture supports investigation of:

* Repeated authentication failures
* Unknown-user authentication attempts
* Suspicious account activity
* Related authentication patterns

Authentication detections can then be correlated with:

* Process activity
* Account-management events
* PowerShell activity
* Other endpoint telemetry

This correlation is used in the incident investigation workflow.

---

## 11. Account Activity Monitoring

Windows account-management telemetry supports detection of potentially suspicious identity changes.

Examples include:

```text
User Creation
     ↓
Account Modification
     ↓
Privilege / Group Changes
     ↓
Subsequent Authentication
     ↓
Process Activity
```

This type of correlation can help establish whether account activity represents an isolated administrative action or part of a larger sequence.

---

## 12. Endpoint Detection Workflow

Windows endpoint activity follows the project's detection lifecycle:

```text
Activity Generated
       ↓
Windows Telemetry
       ↓
Wazuh Agent
       ↓
Wazuh Manager
       ↓
Detection Rule
       ↓
Alert
       ↓
SOC Triage
       ↓
Investigation
       ↓
Response
```

Detection scenarios are documented independently so that each detection can be reviewed, tested, investigated, and improved.

---

## 13. Controlled Security Testing

The Windows endpoint is used for authorized security testing inside the isolated laboratory environment.

Testing activities are designed to generate controlled telemetry for validating:

* Detection rules
* Event collection
* Alert generation
* Investigation workflows
* ATT&CK mappings
* Detection tuning
* Regression testing

Testing is performed only against systems owned or explicitly authorized for testing.

---

## 14. Endpoint Investigation

When a Wazuh alert originates from the Windows endpoint, analysts should correlate the alert with underlying endpoint telemetry.

A standard workflow is:

```text
Wazuh Alert
     ↓
Identify Endpoint
     ↓
Review Event Timestamp
     ↓
Check Windows Event Logs
     ↓
Review Sysmon Events
     ↓
Review PowerShell Events
     ↓
Correlate Process Activity
     ↓
Build Timeline
     ↓
Determine Finding
```

This approach provides stronger investigative confidence than relying on a single alert.

---

## 15. Evidence Collection

Endpoint evidence may be collected from:

```text
Windows Event Viewer
Wazuh Dashboard
Sysmon Events
PowerShell Operational Logs
Process Information
```

Relevant evidence should be preserved in the appropriate investigation or detection directory.

Recommended naming conventions include:

```text
DET-XXX-<source>-<description>.png
INV-XXX-<source>-<description>.png
```

Screenshots should clearly demonstrate the relevant event while avoiding unnecessary disclosure of sensitive infrastructure information.

---

## 16. Endpoint Security Considerations

The laboratory endpoint should be treated as a controlled security environment.

Important considerations include:

* Use isolated virtual-machine networking where appropriate
* Avoid using real credentials for attack simulation
* Do not connect malicious test artifacts to production systems
* Keep test accounts and data separate from personal data
* Avoid exposing management interfaces publicly
* Restrict administrative access
* Preserve relevant evidence before modifying the environment
* Revert or rebuild the test environment when required

---

## 17. Relationship to SOC Operations

The Windows endpoint supports multiple SOC functions:

| SOC Function          | Endpoint Contribution                    |
| --------------------- | ---------------------------------------- |
| Monitoring            | Generates security telemetry             |
| Detection             | Provides events evaluated by Wazuh rules |
| Triage                | Supplies host and user context           |
| Investigation         | Provides event and process evidence      |
| Threat Hunting        | Provides searchable endpoint telemetry   |
| Incident Response     | Supports scope and activity analysis     |
| Forensics             | Provides event-level evidence            |
| Detection Engineering | Enables controlled rule testing          |

---

## 18. Repository Integration

Windows infrastructure documentation supports the following project areas:

```text
01-lab/
├── infrastructure/
│   └── windows/
│
02-detections/
│
03-threat-hunting/
│
04-Incident-Investigations/
│
05-detection-engineering/
│
06-incident-response/
│
07-forensics/
```

The endpoint therefore acts as a common telemetry source across the defensive security workflow.

---

## 19. Operational Workflow

The Windows endpoint is integrated into the project's broader SOC lifecycle:

```text
COLLECT
   ↓
DETECT
   ↓
TRIAGE
   ↓
INVESTIGATE
   ↓
HUNT
   ↓
RESPOND
   ↓
IMPROVE
   ↓
RETEST
```

Each stage uses endpoint telemetry differently:

* **Collect:** gather Windows security and system telemetry
* **Detect:** identify suspicious behavior
* **Triage:** establish initial context
* **Investigate:** correlate events and reconstruct activity
* **Hunt:** search for related or previously undetected behavior
* **Respond:** support containment and remediation decisions
* **Improve:** identify telemetry or detection gaps
* **Retest:** verify that improvements work as intended

---

## 20. Summary

The Windows endpoint is the primary endpoint telemetry source for the SOC lab.

Its integration with Wazuh, Windows Security Event Logs, Sysmon, and PowerShell logging provides the visibility required to build and validate realistic SOC detection and investigation workflows.

The endpoint is not treated simply as a machine generating alerts. It is the underlying evidence source that supports the complete workflow:

```text
Endpoint Activity
      ↓
Telemetry
      ↓
Detection
      ↓
Investigation
      ↓
Threat Hunting
      ↓
Incident Response
      ↓
Detection Improvement
      ↓
Regression Testing
```

This architecture establishes the Windows endpoint as a foundational component of the project's defensive security monitoring environment.

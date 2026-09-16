# Wazuh Manager

## 1. Overview

The Wazuh Manager is the central security monitoring and analysis component of the lab. It receives telemetry from monitored endpoints, processes and evaluates security events, applies detection logic, generates alerts, and provides the data required for SOC investigation and threat hunting.

Within this project, the Wazuh Manager functions as the central detection and analysis layer connecting endpoint telemetry with the detection engineering, investigation, threat hunting, and incident response workflows.

---

## 2. Responsibilities

The Wazuh Manager performs the following core functions:

* Receives security telemetry from Wazuh agents
* Processes and normalizes incoming events
* Extracts relevant event fields
* Evaluates events against configured detection rules
* Generates security alerts
* Assigns alert severity
* Associates detections with MITRE ATT&CK techniques where applicable
* Provides structured event data for investigation
* Supports detection tuning and validation
* Maintains centralized security monitoring across monitored endpoints

The manager therefore acts as the primary processing layer between endpoint telemetry and SOC analyst activity.

---

## 3. Architecture Role

The manager is positioned between the monitored endpoints and the analyst-facing dashboard.

```text
┌──────────────────────────────┐
│        Windows Endpoint      │
│                              │
│  Windows Security Events      │
│  Sysmon Telemetry             │
│  PowerShell Events            │
└──────────────┬───────────────┘
               │
               │ Agent Telemetry
               ▼
┌──────────────────────────────┐
│        Wazuh Manager         │
│                              │
│  Event Processing             │
│  Field Extraction             │
│  Rule Evaluation              │
│  Detection Logic              │
│  Alert Generation             │
│  ATT&CK Metadata              │
└──────────────┬───────────────┘
               │
               │ Alerts / Events
               ▼
┌──────────────────────────────┐
│       Wazuh Dashboard        │
│                              │
│  Alert Review                 │
│  Investigation                │
│  Hunting                      │
│  Visualization               │
└──────────────────────────────┘
```

This architecture separates telemetry collection, centralized analysis, and analyst interaction.

---

## 4. Event Processing Pipeline

Security events are processed through a defined sequence:

```text
Endpoint Telemetry
       ↓
Wazuh Agent
       ↓
Wazuh Manager
       ↓
Event Parsing
       ↓
Field Extraction
       ↓
Rule Evaluation
       ↓
Detection Matching
       ↓
Alert Generation
       ↓
Dashboard / Investigation
```

Each stage contributes to converting raw endpoint activity into structured security information that can be investigated by an analyst.

---

## 5. Telemetry Sources

The lab integrates endpoint telemetry from Windows systems, including:

### Windows Security Event Logs

Used for identity and security-related activity such as:

* Authentication failures
* Account creation
* Security policy events
* Other Windows security events relevant to detection engineering

### Sysmon

Sysmon provides detailed endpoint process and system telemetry that can support:

* Process creation analysis
* Parent-child process relationships
* Command-line investigation
* File and process activity
* Network-related telemetry where configured

Sysmon is treated as an **endpoint telemetry source**, not as an EDR platform.

### PowerShell Operational Logging

PowerShell logging provides additional visibility into PowerShell activity and can support detection and investigation of suspicious command execution.

---

## 6. Detection Rule Processing

The manager evaluates incoming events against configured detection logic.

The project uses both:

* Built-in Wazuh detection capabilities
* Custom detection rules developed as part of the project

Custom detection engineering is documented under:

```text
05-detection-engineering/
```

Individual detection scenarios are documented under:

```text
02-detections/
```

This separation allows detection development and operational detection scenarios to remain independently documented.

---

## 7. Alert Generation

When an event satisfies detection criteria, the Wazuh Manager generates an alert containing structured information that can be used for SOC analysis.

Relevant alert information can include:

* Rule ID
* Alert severity
* Timestamp
* Agent name
* Event source
* Event ID
* User information
* Process information
* Command-line information
* Parent process information
* Host information
* MITRE ATT&CK metadata
* Original event details

Analysts use these fields to establish what happened, where it happened, when it happened, and which activity requires further investigation.

---

## 8. Severity Handling

Alert severity provides an initial prioritization signal for SOC analysts.

Severity should not be interpreted in isolation.

An analyst should consider:

1. Alert severity
2. Event context
3. Host involved
4. User involved
5. Process behavior
6. Command-line activity
7. Related events
8. Frequency and timing
9. MITRE ATT&CK mapping
10. Evidence collected during investigation

A lower-severity event can become important when correlated with other suspicious activity.

Likewise, a high-severity alert still requires contextual validation before determining its actual security significance.

---

## 9. MITRE ATT&CK Integration

Detection rules can include MITRE ATT&CK metadata to associate observed behavior with adversary techniques.

For example:

```text
Observed Behavior
      ↓
Detection Rule
      ↓
MITRE ATT&CK Technique
      ↓
Investigation
      ↓
Threat Hunting
```

The project uses ATT&CK mappings to provide behavioral context rather than treating technique IDs as standalone evidence.

This supports consistent analysis across:

* Detection engineering
* Incident investigation
* Threat hunting
* Coverage assessment

---

## 10. SOC Analyst Workflow

The Wazuh Manager supports the following operational workflow:

```text
Alert Generated
      ↓
Alert Triage
      ↓
Validate Detection
      ↓
Review Event Context
      ↓
Correlate Related Activity
      ↓
Investigate Host / User / Process
      ↓
Determine Scope
      ↓
Document Findings
      ↓
Respond
      ↓
Tune Detection
      ↓
Retest
```

This workflow connects the SIEM platform with the broader SOC operating model implemented throughout the repository.

---

## 11. Investigation Support

The manager provides the centralized event data required by investigations documented under:

```text
04-Incident-Investigations/
```

Investigations can use Wazuh data to establish:

* Initial alert time
* Affected endpoint
* Account involved
* Process involved
* Command-line activity
* Related events
* Detection rule triggered
* ATT&CK technique
* Timeline of activity

Additional endpoint and forensic evidence can then be correlated with the Wazuh alert.

---

## 12. Threat Hunting Integration

Wazuh events are also used as a source for proactive threat hunting.

The hunting workflow is:

```text
Hypothesis
    ↓
Relevant Telemetry
    ↓
Search / Query
    ↓
Pattern Identification
    ↓
Event Correlation
    ↓
Suspicious Activity
    ↓
Validation
    ↓
Detection Improvement
```

Threat hunting documentation is maintained under:

```text
03-threat-hunting/
```

This allows hunting activity to identify behaviors that may require new or improved detections.

---

## 13. Detection Engineering Integration

The Wazuh Manager is part of the project's detection engineering lifecycle:

```text
Requirement
    ↓
Detection Design
    ↓
Rule Development
    ↓
Controlled Test
    ↓
Alert Validation
    ↓
Investigation
    ↓
Tuning
    ↓
Regression Test
    ↓
Deployment
```

Supporting documentation is maintained under:

```text
05-detection-engineering/
```

This approach prevents detection rules from being treated as isolated configuration changes and instead evaluates them as part of a repeatable engineering lifecycle.

---

## 14. Configuration Management

Wazuh configuration and custom detection logic are maintained separately from investigation evidence.

The project structure provides dedicated locations for:

```text
01-lab/infrastructure/wazuh/
```

and:

```text
05-detection-engineering/wazuh/
```

The infrastructure directory documents the platform and deployment architecture, while the detection engineering directory contains detection-specific configuration and engineering artifacts.

---

## 15. Evidence and Validation

Wazuh alerts should be validated against the underlying endpoint telemetry whenever possible.

For example:

```text
Wazuh Alert
    ↓
Windows Event
    ↓
Sysmon / PowerShell Telemetry
    ↓
Process / User / Host Context
    ↓
Investigation Finding
```

This reduces dependence on a single alert and allows analysts to determine whether the detection accurately represents the observed activity.

Evidence captured during investigations is stored according to the repository's evidence-management structure.

---

## 16. Security Considerations

The Wazuh Manager is treated as a security-critical component of the lab.

Operational considerations include:

* Restricting administrative access
* Protecting management credentials
* Avoiding credentials in Git repositories
* Avoiding unnecessary exposure of private IP addresses
* Separating test activity from production systems
* Maintaining controlled attack simulation
* Reviewing configuration changes
* Validating custom rules before relying on them
* Preserving relevant investigation evidence

The repository intentionally avoids publishing sensitive credentials, authentication material, or unnecessary infrastructure secrets.

---

## 17. Operational Integration

The Wazuh Manager connects multiple areas of the project:

| Project Area                  | Wazuh Manager Role                           |
| ----------------------------- | -------------------------------------------- |
| `01-lab/`                     | Central monitoring infrastructure            |
| `02-detections/`              | Operational detection scenarios              |
| `03-threat-hunting/`          | Telemetry source for hunting                 |
| `04-Incident-Investigations/` | Alert and event evidence                     |
| `05-detection-engineering/`   | Detection implementation                     |
| `06-incident-response/`       | Incident identification and response support |
| `07-forensics/`               | Event correlation with forensic evidence     |
| `11-metrics/`                 | Detection and coverage analysis              |
| `13-reports/`                 | Technical and incident reporting             |
| `14-screenshots/`             | Visual evidence supporting analysis          |

---

## 18. Documentation References

Additional Wazuh documentation within this project:

```text
01-lab/infrastructure/wazuh/
├── README.md
├── manager.md
└── dashboard.md
```

The documentation separates platform architecture, manager functionality, and analyst-facing dashboard operations.

---

## 19. Summary

The Wazuh Manager provides the centralized security monitoring and detection layer of the lab.

Its role extends beyond simply collecting logs. It processes endpoint telemetry, evaluates detection logic, generates structured alerts, supports ATT&CK-based analysis, enables investigations, and provides telemetry for threat hunting and detection engineering.

The manager therefore forms a core component of the project's SOC workflow:

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

This architecture provides the foundation for the subsequent Windows endpoint, Linux infrastructure, and network telemetry components of the lab.

# Wazuh Security Monitoring Infrastructure

## 1. Overview

Wazuh provides the centralized security monitoring, telemetry processing, detection, and analyst investigation layer of the laboratory.

Within the SOC architecture, Wazuh connects endpoint telemetry with security detection and investigation workflows.

The Wazuh architecture consists of:

```text id="k7xq3m"
Monitored Endpoint
       │
       ▼
 Wazuh Agent
       │
       ▼
 Wazuh Manager
       │
       ▼
Detection Processing
       │
       ▼
 Security Alerts
       │
       ▼
Wazuh Dashboard
       │
       ▼
SOC Analyst
```

The platform provides the centralized foundation for the project's endpoint-focused SOC monitoring capabilities.

---

# 2. Wazuh Responsibilities

The Wazuh environment provides capabilities for:

* Endpoint telemetry collection.
* Centralized event processing.
* Security event analysis.
* Detection rule evaluation.
* Alert generation.
* Alert severity classification.
* MITRE ATT&CK metadata.
* Security monitoring.
* Alert triage.
* Event investigation.
* Detection validation.
* Detection tuning.

Wazuh acts as the central monitoring layer rather than being treated as the only source of security evidence.

---

# 3. Wazuh Components

The laboratory uses the following logical Wazuh components:

| Component           | Responsibility                               |
| ------------------- | -------------------------------------------- |
| Wazuh Agent         | Endpoint telemetry collection and forwarding |
| Wazuh Manager       | Centralized event processing and detection   |
| Wazuh Dashboard     | Analyst monitoring and investigation         |
| Wazuh Rules         | Security detection logic                     |
| Wazuh Configuration | Collection and processing configuration      |

The individual components are documented in:

```text
manager.md
dashboard.md
```

---

# 4. Endpoint Integration

The monitored Windows endpoint runs the Wazuh Agent.

The agent collects configured endpoint telemetry and forwards it to the centralized Wazuh Manager.

The primary telemetry sources include:

* Windows Security Event Logs.
* Sysmon events.
* PowerShell-related telemetry.
* Process activity.
* User and account activity.
* Other configured Windows event sources.

The endpoint integration is:

```text id="q2w8az"
Windows Endpoint
      │
      ├── Security Event Logs
      │
      └── Sysmon
             │
             ▼
        Wazuh Agent
             │
             ▼
        Wazuh Manager
```

---

# 5. Event Processing

The Wazuh Manager processes incoming endpoint events before they are presented to analysts.

The processing workflow is:

```text id="zq3j7h"
Incoming Event
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
```

This allows raw endpoint telemetry to be transformed into structured security alerts.

---

# 6. Detection Integration

Wazuh detection logic is integrated with the project's broader detection-engineering lifecycle.

```text id="7v6h3k"
Telemetry
    ↓
Wazuh Processing
    ↓
Detection Rule
    ↓
Alert
    ↓
Triage
    ↓
Investigation
    ↓
Detection Improvement
```

Detection content is maintained under:

```text id="o4u4i7"
02-detections/
```

Detection-engineering implementation is maintained under:

```text id="b6g5n2"
05-detection-engineering/
```

---

# 7. Alert Severity

Wazuh alerts include severity information that assists with analyst prioritization.

Severity is considered together with:

* Detection confidence.
* Event context.
* User context.
* Host context.
* Process context.
* Supporting telemetry.
* Investigation findings.

Alert severity alone is not treated as proof of malicious activity.

---

# 8. MITRE ATT&CK Integration

Relevant detections are mapped to MITRE ATT&CK techniques and sub-techniques where appropriate.

The mapping provides a common behavioral framework for:

* Detection engineering.
* Threat hunting.
* Investigation.
* Coverage analysis.
* Detection-gap identification.

The ATT&CK relationship can be represented as:

```text id="2l9j0x"
Observed Behavior
       ↓
Telemetry
       ↓
Detection
       ↓
ATT&CK Technique
       ↓
Hunting / Investigation
```

---

# 9. SOC Analyst Workflow

The Wazuh environment supports the analyst workflow from alert generation through investigation.

```text id="zq2c7j"
Alert
 ↓
Triage
 ↓
Validate
 ↓
Collect Context
 ↓
Correlate Events
 ↓
Investigate
 ↓
Determine Scope
 ↓
Respond
 ↓
Document
```

The Wazuh Dashboard provides the primary interface for these activities.

---

# 10. Investigation Support

Wazuh provides structured event information that can be used to reconstruct security activity.

Relevant investigation context can include:

* Event timestamp.
* Rule identifier.
* Alert level.
* Agent information.
* Event identifier.
* User information.
* Process information.
* Command-line information.
* Parent-process information.
* MITRE ATT&CK metadata.
* Supporting event fields.

Additional endpoint and forensic evidence is correlated when required.

---

# 11. Threat Hunting Integration

Wazuh telemetry is also used for proactive threat hunting.

Hunting queries can search for behavioral patterns involving:

* PowerShell.
* Authentication activity.
* Process execution.
* Account activity.
* Persistence.
* Defense evasion.
* Lateral movement.
* Network-related behavior.

Threat hunting artifacts are maintained under:

```text id="6z4b8v"
03-threat-hunting/
```

---

# 12. Detection Engineering Integration

The Wazuh platform provides the operational environment in which detection logic can be developed and validated.

The detection-engineering lifecycle is:

```text id="6f3d1r"
Requirement
    ↓
Detection Hypothesis
    ↓
Telemetry Identification
    ↓
Rule Development
    ↓
Controlled Testing
    ↓
Alert Validation
    ↓
Tuning
    ↓
Regression Testing
    ↓
Deployment
    ↓
Monitoring
```

Detection engineering documentation is maintained under:

```text id="3f7j4a"
05-detection-engineering/
```

---

# 13. Evidence Collection

Wazuh alerts and event records provide supporting evidence for detection and investigation documentation.

Evidence can include:

* Alert details.
* Event details.
* Detection-rule configuration.
* Supporting endpoint events.
* Related process activity.
* Timeline information.
* Investigation findings.

Public repository evidence is reviewed before publication to remove unnecessary sensitive information.

---

# 14. Security Considerations

The Wazuh environment is operated within an authorized laboratory.

Security considerations include:

* Restricted laboratory access.
* Controlled endpoint communication.
* Protection of administrative credentials.
* Sanitization of screenshots.
* Removal of secrets from repository artifacts.
* Controlled attack simulation.
* Separation of public documentation from sensitive configuration.

No credentials, authentication tokens, or API secrets are intentionally stored in the public repository.

---

# 15. Operational Integration

Wazuh integrates with the broader project architecture:

```text id="5u5w3n"
Wazuh
 │
 ├── 02-detections
 │
 ├── 03-threat-hunting
 │
 ├── 04-Incident-Investigations
 │
 ├── 05-detection-engineering
 │
 ├── 06-incident-response
 │
 ├── 07-forensics
 │
 ├── 09-threat-intelligence
 │
 ├── 10-scripts
 │
 └── 11-metrics
```

This integration ensures that Wazuh is used as part of an end-to-end SOC workflow rather than as an isolated SIEM demonstration.

---

# 16. Documentation Structure

The Wazuh infrastructure documentation is divided into:

```text id="u9x5jp"
wazuh/
├── README.md
├── manager.md
└── dashboard.md
```

### `README.md`

Documents the overall Wazuh architecture and its role in the SOC.

### `manager.md`

Documents the Wazuh Manager, event-processing architecture, detection rules, and operational responsibilities.

### `dashboard.md`

Documents the analyst-facing dashboard, alert investigation, event search, and monitoring workflow.

---

# 17. Summary

Wazuh provides the centralized security-monitoring foundation of the laboratory.

It connects endpoint telemetry to:

```text id="q9w2r4"
Collection
   ↓
Processing
   ↓
Detection
   ↓
Alerting
   ↓
Triage
   ↓
Investigation
   ↓
Threat Hunting
   ↓
Incident Response
   ↓
Detection Engineering
   ↓
Continuous Improvement
```

This architecture enables the laboratory to demonstrate practical SOC operations, detection engineering, behavioral investigation, and continuous security-monitoring improvement.

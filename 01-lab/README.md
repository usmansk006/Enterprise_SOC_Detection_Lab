# SOC Detection, Threat Hunting & Incident Response Lab

## 1. Overview

The `01-lab` directory documents the laboratory environment supporting the **Enterprise SOC Detection, Threat Hunting & Incident Response Lab**.

The environment provides an isolated platform for security telemetry collection, detection engineering, alert investigation, threat hunting, incident response, forensic analysis, network security monitoring, threat intelligence enrichment, and security automation.

The laboratory is designed around an end-to-end Security Operations Center workflow:

```text
TELEMETRY
    ↓
DETECTION
    ↓
ALERT TRIAGE
    ↓
INVESTIGATION
    ↓
THREAT HUNTING
    ↓
INCIDENT RESPONSE
    ↓
FORENSICS
    ↓
THREAT INTELLIGENCE
    ↓
DETECTION GAP ANALYSIS
    ↓
TUNING
    ↓
REGRESSION TESTING
    ↓
RETESTING
    ↓
CONTINUOUS IMPROVEMENT
```

The lab is intentionally structured to demonstrate how security telemetry is transformed into actionable detections and investigation outcomes.

---

# 2. Laboratory Objectives

The laboratory provides the infrastructure required to:

* Centralize security telemetry.
* Monitor Windows endpoint activity.
* Collect Windows Security Event Logs.
* Collect Sysmon endpoint telemetry.
* Develop and validate security detections.
* Investigate security alerts.
* Perform behavioral threat hunting.
* Map activity to MITRE ATT&CK.
* Develop incident response workflows.
* Perform endpoint forensic analysis.
* Analyze network security telemetry.
* Enrich investigations with threat intelligence.
* Automate repetitive security operations tasks.
* Measure detection coverage and effectiveness.
* Identify detection gaps.
* Tune detection logic.
* Perform regression testing.
* Maintain reproducible investigation evidence.

The laboratory therefore functions as the technical foundation for the remainder of the repository.

---

# 3. Laboratory Architecture

The core environment consists of:

| Component                | Role                                               |
| ------------------------ | -------------------------------------------------- |
| Ubuntu Server            | Security monitoring infrastructure                 |
| Wazuh Manager            | Centralized telemetry processing and detection     |
| Wazuh Dashboard          | SOC analyst monitoring and investigation interface |
| Windows 10 Endpoint      | Primary monitored endpoint                         |
| Wazuh Agent              | Endpoint telemetry collection and forwarding       |
| Windows Security Logs    | Native Windows security telemetry                  |
| Sysmon                   | Detailed endpoint and process telemetry            |
| Kali Linux               | Authorized security activity simulation            |
| Network Analysis Tooling | Network telemetry analysis and investigation       |

The high-level architecture is:

```text
                   ┌─────────────────────────┐
                   │   Authorized Activity   │
                   │                         │
                   │   Controlled Testing    │
                   └────────────┬────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │    Windows Endpoint     │
                   │                         │
                   │ Windows Security Logs   │
                   │ Sysmon Telemetry        │
                   │ Process Activity        │
                   │ PowerShell Activity     │
                   └────────────┬────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │      Wazuh Agent        │
                   │                         │
                   │ Telemetry Collection    │
                   │ Event Forwarding        │
                   └────────────┬────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │     Wazuh Manager       │
                   │                         │
                   │ Event Processing        │
                   │ Detection Rules         │
                   │ Alert Generation        │
                   └────────────┬────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │    Wazuh Dashboard      │
                   │                         │
                   │ Alert Triage            │
                   │ Investigation            │
                   │ Event Analysis           │
                   └────────────┬────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
        Threat Hunting    Investigations    Incident Response
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                   ┌─────────────────────────┐
                   │ Detection Engineering  │
                   │                         │
                   │ Tuning                  │
                   │ Gap Analysis            │
                   │ Regression Testing      │
                   └─────────────────────────┘
```

The detailed architecture is maintained under:

```text
01-lab/architecture/
```

---

# 4. Telemetry Architecture

The laboratory uses multiple telemetry sources to provide behavioral visibility across the monitored environment.

## Windows Security Event Logs

Windows Security Event Logs provide native operating-system security telemetry.

The environment supports analysis of security-relevant activity including:

* Authentication events.
* Failed authentication.
* Account management.
* User creation.
* Security policy activity.
* Other configured security events.

These events provide foundational identity and operating-system security context.

---

## Sysmon Telemetry

Sysmon provides detailed endpoint telemetry that supplements native Windows event logging.

Relevant telemetry includes:

* Process creation.
* Process termination.
* Parent-child process relationships.
* Command-line information.
* Network-related process activity when configured.
* Additional endpoint activity based on the active Sysmon configuration.

Sysmon is used as an **endpoint telemetry source** and is not treated as a full EDR platform.

---

## Wazuh Telemetry Processing

The Wazuh Agent collects configured endpoint telemetry and forwards it to the Wazuh Manager.

The Wazuh Manager processes incoming events and applies detection logic to identify security-relevant behavior.

The resulting alerts are made available through the Wazuh Dashboard for analyst investigation.

---

# 5. Detection Workflow

The laboratory implements a complete detection workflow:

```text
Security Activity
       ↓
Endpoint Telemetry
       ↓
Wazuh Collection
       ↓
Event Processing
       ↓
Detection Rule
       ↓
Alert Generation
       ↓
Alert Triage
       ↓
Investigation
       ↓
Threat Hunting
       ↓
Response
       ↓
Detection Improvement
       ↓
Regression Testing
       ↓
Retesting
```

Detection content is maintained under:

```text
02-detections/
```

Detection engineering methodology, rules, Sigma content, test cases, and regression testing are maintained under:

```text
05-detection-engineering/
```

---

# 6. Threat Hunting

The laboratory supports proactive threat hunting in addition to alert-driven investigation.

Threat hunting activities use behavioral hypotheses to search available telemetry for:

* Suspicious PowerShell activity.
* Credential-related behavior.
* Persistence mechanisms.
* Lateral movement indicators.
* Suspicious processes.
* Network activity.
* Other ATT&CK-aligned behaviors.

Threat hunting documentation is maintained under:

```text
03-threat-hunting/
```

The hunting process follows:

```text
Hunting Hypothesis
        ↓
ATT&CK Technique
        ↓
Required Telemetry
        ↓
Hunting Query
        ↓
Event Analysis
        ↓
Correlation
        ↓
Finding
        ↓
Detection Gap Analysis
```

---

# 7. Incident Investigation

Detected security activity is investigated using a structured SOC investigation methodology.

The investigation process includes:

1. Alert intake.
2. Initial triage.
3. Alert validation.
4. Timeline construction.
5. User and host context analysis.
6. Process analysis.
7. Command-line analysis.
8. Supporting-event correlation.
9. MITRE ATT&CK mapping.
10. Scope assessment.
11. Evidence collection.
12. Response determination.
13. Documentation.
14. Detection improvement.

Investigation cases are maintained under:

```text
04-Incident-Investigations/
```

Each investigation is designed to demonstrate analyst reasoning rather than simply displaying an alert screenshot.

---

# 8. Incident Response

The incident response layer connects detection and investigation activities to structured response procedures.

The response workflow includes:

```text
Detection
   ↓
Triage
   ↓
Investigation
   ↓
Scoping
   ↓
Containment
   ↓
Eradication
   ↓
Recovery
   ↓
Post-Incident Review
   ↓
Detection Improvement
```

Response playbooks, procedures, and templates are maintained under:

```text
06-incident-response/
```

---

# 9. Digital Forensics

The laboratory includes a forensic analysis layer for investigations requiring deeper endpoint examination.

Forensic analysis can incorporate:

* Windows Event Logs.
* PowerShell artifacts.
* Registry artifacts.
* Prefetch artifacts.
* Persistence artifacts.
* Process timelines.
* Other relevant endpoint evidence.

Forensic material is maintained under:

```text
07-forensics/
```

The forensic capability complements SIEM-based investigation by providing additional evidence when alert telemetry alone is insufficient.

---

# 10. Network Security

The project extends beyond endpoint monitoring by incorporating network-security analysis.

The network security layer covers:

* Wireshark packet analysis.
* Suricata network detection.
* Zeek network telemetry.
* DNS analysis.
* HTTP analysis.
* Network threat hunting.

Network security artifacts are maintained under:

```text
08-network-security/
```

The architecture is designed to correlate endpoint and network observations where the corresponding telemetry is available.

---

# 11. Threat Intelligence

Threat intelligence is incorporated as an enrichment layer for investigation and detection workflows.

The project organizes indicators including:

```text
09-threat-intelligence/
├── iocs/
│   ├── hashes/
│   ├── ips/
│   ├── domains/
│   └── urls/
├── enrichment/
└── intel-reports/
```

Threat intelligence can provide additional context for indicators discovered during investigations, including:

* File hashes.
* IP addresses.
* Domains.
* URLs.

Intelligence enrichment is treated as supporting context and is correlated with internal telemetry and investigative findings.

---

# 12. Security Automation

The laboratory includes a security automation layer for repetitive analyst and detection-engineering tasks.

Automation areas include:

* Wazuh alert analysis.
* IOC extraction.
* Timeline generation.
* Log analysis.
* Detection validation.

Automation artifacts are maintained under:

```text
10-scripts/
```

The objective is to reduce repetitive analyst workload while maintaining human review and investigative context.

---

# 13. Metrics and Detection Improvement

Detection quality is evaluated through a dedicated metrics layer.

The metrics framework covers:

* ATT&CK coverage.
* Detection coverage.
* Detection success.
* False-positive analysis.
* Detection gaps.
* Before/after tuning.
* Investigation metrics.

Metrics are maintained under:

```text
11-metrics/
```

The continuous-improvement cycle is:

```text
Detect
  ↓
Validate
  ↓
Measure
  ↓
Identify Gap
  ↓
Tune
  ↓
Regression Test
  ↓
Retest
  ↓
Measure Again
```

This provides a measurable detection-engineering lifecycle rather than treating individual rules as isolated artifacts.

---

# 14. Laboratory Security Boundary

The environment is designed for controlled and authorized security testing.

Security-testing activities are restricted to systems within the designated laboratory environment.

The following principles apply:

* Attack simulation is performed only for defensive validation.
* Third-party or unauthorized systems are outside the testing scope.
* Credentials and secrets are excluded from public documentation.
* Screenshots are reviewed before publication.
* Sensitive infrastructure information is minimized where unnecessary.
* Security evidence is sanitized before being committed to the public repository.

---

# 15. Documentation Structure

The `01-lab` directory is organized into four primary areas:

```text
01-lab/
├── README.md
├── architecture/
├── infrastructure/
├── deployment/
└── configuration/
```

### `architecture/`

Documents the logical architecture, component relationships, telemetry flow, and data paths.

```text
architecture/
├── enterprise-soc-architecture.png
├── enterprise-soc-architecture.drawio
└── data-flow.md
```

### `infrastructure/`

Documents the systems and security components deployed within the laboratory.

```text
infrastructure/
├── wazuh/
├── windows/
├── linux/
└── network/
```

### `deployment/`

Documents the deployment process used to build and establish the laboratory environment.

### `configuration/`

Documents security-relevant configuration applied to the monitoring infrastructure and endpoints.

---

# 16. Repository Integration

The laboratory acts as the foundation for the complete security portfolio.

| Component                     | Purpose                                    |
| ----------------------------- | ------------------------------------------ |
| `01-lab/`                     | Laboratory architecture and infrastructure |
| `02-detections/`              | Security detection content                 |
| `03-threat-hunting/`          | Proactive threat hunting                   |
| `04-Incident-Investigations/` | Security investigations                    |
| `05-detection-engineering/`   | Detection development and validation       |
| `06-incident-response/`       | Response playbooks and procedures          |
| `07-forensics/`               | Digital forensic analysis                  |
| `08-network-security/`        | Network monitoring and analysis            |
| `09-threat-intelligence/`     | Threat intelligence and IOC enrichment     |
| `10-scripts/`                 | Security automation                        |
| `11-metrics/`                 | Detection and investigation measurement    |
| `12-assets/`                  | Shared project assets                      |
| `13-reports/`                 | Technical and executive reporting          |
| `14-screenshots/`             | Visual evidence                            |
| `docs/`                       | Cross-project technical documentation      |

---

# 17. Reproducibility and Evidence

The laboratory follows a reproducible documentation model.

Where applicable, security activities are supported by:

* Configuration evidence.
* Endpoint telemetry.
* Wazuh events.
* Detection alerts.
* Detection rules.
* Investigation timelines.
* Threat-hunting queries.
* Forensic evidence.
* Network-analysis evidence.
* Validation results.
* Regression-testing results.

Evidence intended for public release is reviewed to remove:

* Passwords.
* API keys.
* Authentication tokens.
* Personal information.
* Unnecessary internal addresses.
* Sensitive infrastructure details.

---

# 18. Design Principles

The laboratory follows the following security engineering principles:

### Observable

Security-relevant behavior should generate usable telemetry.

### Detectable

Relevant behaviors should have corresponding detection logic where sufficient telemetry exists.

### Investigable

Alerts should provide sufficient context to support analyst investigation.

### Huntable

Telemetry should support proactive searches beyond individual alerts.

### Reproducible

Detection and investigation procedures should be repeatable.

### Testable

Detection logic should be validated against controlled activity.

### Measurable

Detection effectiveness and gaps should be measurable.

### Continuously Improved

Investigation findings should feed back into detection engineering and validation.

---

# 19. Related Documentation

The broader project documentation is maintained under:

```text
docs/
```

Key documents include:

* `01-project-overview.md`
* `02-architecture.md`
* `03-telemetry.md`
* `04-detection-engineering.md`
* `05-threat-hunting.md`
* `06-incident-response.md`
* `07-digital-forensics.md`
* `08-network-security.md`
* `09-threat-intelligence.md`
* `10-security-automation.md`
* `11-lessons-learned.md`

These documents provide cross-project technical context while `01-lab/` contains the underlying laboratory implementation and architecture.

---

# 20. Laboratory Status

The laboratory provides the technical foundation for the project's detection engineering, threat hunting, incident investigation, incident response, forensic analysis, network security, threat intelligence, automation, and measurement workflows.

The architecture is modular and supports the addition of new telemetry sources, security technologies, detection content, investigation techniques, and automation capabilities without changing the fundamental SOC workflow.

The laboratory therefore functions as an integrated security engineering environment rather than a collection of isolated security exercises.

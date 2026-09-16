# Enterprise SOC Architecture

## 1. Overview

The **Enterprise SOC Detection, Threat Hunting & Incident Response Lab** is designed as an isolated security operations environment for developing, validating, and investigating security detections across endpoint, identity, process, and network telemetry.

The architecture separates monitored endpoints, security monitoring infrastructure, telemetry collection, detection processing, analyst investigation, and controlled attack simulation.

The environment supports the complete defensive security workflow:

```text
Controlled Activity
        ↓
Monitored Endpoint
        ↓
Telemetry Generation
        ↓
Telemetry Collection
        ↓
Wazuh Manager
        ↓
Detection Processing
        ↓
Security Alert
        ↓
SOC Triage
        ↓
Investigation
        ↓
Threat Hunting
        ↓
Incident Response
        ↓
Forensics / Intelligence
        ↓
Detection Improvement
        ↓
Regression Testing
```

The architecture is intentionally modular so additional telemetry sources, detection technologies, network monitoring capabilities, automation, and forensic tooling can be integrated without redesigning the core monitoring workflow.

---

## 2. Architecture Objectives

The architecture was implemented to provide the following capabilities:

* Centralized security telemetry collection.
* Windows endpoint monitoring.
* Windows Security Event Log analysis.
* Sysmon-based endpoint telemetry.
* Centralized security alert processing.
* Detection engineering and rule development.
* Alert triage and investigation.
* Threat hunting based on behavioral hypotheses.
* MITRE ATT&CK technique mapping.
* Incident response workflow development.
* Digital forensic analysis.
* Network security monitoring.
* Threat intelligence enrichment.
* Security automation.
* Detection performance measurement.
* Detection tuning and regression testing.

The architecture prioritizes **observable security behavior and reproducible analysis** rather than relying exclusively on individual security products.

---

## 3. High-Level Architecture

```text
                         ┌──────────────────────────┐
                         │    Controlled Activity    │
                         │                          │
                         │  Authorized Test Actions │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │     Windows Endpoint     │
                         │                          │
                         │  Windows Security Logs   │
                         │  PowerShell Telemetry    │
                         │  Sysmon Telemetry        │
                         │  Process Activity        │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │       Wazuh Agent        │
                         │                          │
                         │ Telemetry Collection     │
                         │ Log Forwarding           │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │     Wazuh Manager        │
                         │                          │
                         │ Log Processing           │
                         │ Rule Evaluation          │
                         │ Alert Generation         │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │     Wazuh Dashboard      │
                         │                          │
                         │ Alert Triage             │
                         │ Investigation            │
                         │ Search & Correlation     │
                         └────────────┬─────────────┘
                                      │
                         ┌────────────┴────────────┐
                         ▼                         ▼
              ┌─────────────────────┐   ┌─────────────────────┐
              │ Threat Hunting      │   │ Incident Response   │
              │                     │   │                     │
              │ Hypothesis          │   │ Triage              │
              │ Queries             │   │ Containment         │
              │ Correlation         │   │ Eradication         │
              └──────────┬──────────┘   │ Recovery             │
                         │              └──────────┬──────────┘
                         │                         │
                         └────────────┬────────────┘
                                      ▼
                         ┌──────────────────────────┐
                         │ Detection Engineering    │
                         │                          │
                         │ Rule Development         │
                         │ Tuning                   │
                         │ Gap Analysis             │
                         │ Regression Testing       │
                         └──────────────────────────┘
```

The architecture diagram is maintained separately in:

* `enterprise-soc-architecture.drawio` — editable architecture source.
* `enterprise-soc-architecture.png` — rendered architecture overview.

---

## 4. Core Architecture Components

### 4.1 Windows Endpoint

The Windows endpoint represents the primary monitored workstation within the laboratory.

It generates security-relevant operating system telemetry including:

* Authentication activity.
* Account management activity.
* Process creation.
* Process termination.
* PowerShell activity.
* Parent-child process relationships.
* Command-line information.
* Security policy-related activity.
* Endpoint security events.

The endpoint is intentionally used as the primary telemetry source because Windows environments generate a broad range of data relevant to SOC detection engineering.

---

### 4.2 Wazuh Agent

The Wazuh Agent operates on the monitored endpoint and provides telemetry collection and forwarding capabilities.

Its responsibilities include:

* Collecting configured Windows event telemetry.
* Collecting Sysmon events.
* Forwarding relevant events to the Wazuh Manager.
* Applying endpoint-side collection configuration.
* Maintaining communication with the centralized monitoring infrastructure.

The agent provides the telemetry transport layer between the monitored endpoint and the centralized security monitoring platform.

---

### 4.3 Wazuh Manager

The Wazuh Manager provides the centralized security monitoring and detection-processing layer.

Its responsibilities include:

* Receiving endpoint telemetry.
* Parsing security events.
* Applying detection rules.
* Generating alerts.
* Assigning alert severity.
* Supporting MITRE ATT&CK mappings.
* Providing centralized event processing for investigation.

Custom detection logic is maintained within the repository's detection-engineering documentation and corresponding Wazuh configuration artifacts.

---

### 4.4 Wazuh Dashboard

The Wazuh Dashboard provides the analyst-facing investigation interface.

It is used for:

* Alert triage.
* Event searching.
* Event filtering.
* Alert investigation.
* Timeline analysis.
* Field-level inspection.
* Detection validation.
* Evidence collection.

The dashboard represents the primary analyst interface for the Wazuh-based SOC workflow.

---

### 4.5 Sysmon

Sysmon provides detailed Windows endpoint telemetry that supplements native Windows Security Event Logs.

Relevant telemetry can include:

* Process creation.
* Process termination.
* Parent-child relationships.
* Command-line information.
* Network-related process activity when configured.
* File and other endpoint events when configured.

Sysmon is treated as an **endpoint telemetry source**, not as a full EDR platform.

Its primary purpose within this architecture is to improve behavioral visibility and support detection correlation.

---

### 4.6 Kali Linux

Kali Linux is used as an authorized attack-simulation platform within the isolated laboratory environment.

Its role is to generate controlled activity that can be used to validate defensive capabilities.

The workflow is:

```text
Authorized Simulation
        ↓
Observable Endpoint Activity
        ↓
Telemetry Generation
        ↓
Telemetry Collection
        ↓
Detection
        ↓
Investigation
        ↓
Detection Validation
```

Kali activity is restricted to systems within the authorized laboratory boundary.

---

## 5. Telemetry Architecture

The laboratory uses multiple telemetry layers rather than depending on a single event source.

### Windows Security Telemetry

Provides native Windows security events associated with activities such as:

* Authentication.
* Account creation.
* Account management.
* Security policy events.
* Other configured security auditing events.

### Sysmon Telemetry

Provides additional endpoint visibility into:

* Process execution.
* Process relationships.
* Command-line activity.
* Process termination.
* Other configured Sysmon events.

### Wazuh Telemetry Processing

Wazuh centralizes the collection and processing of these events and applies detection logic before exposing security alerts to the analyst.

This creates a layered telemetry model:

```text
Windows Security Logs
          │
          ├──────────────┐
          │              │
          ▼              ▼
      Wazuh Agent     Sysmon
          │              │
          └──────┬───────┘
                 ▼
          Wazuh Manager
                 │
                 ▼
           Detection Rules
                 │
                 ▼
              Alerts
```

---

## 6. Detection Architecture

Detection logic is implemented as a separate layer from the underlying telemetry.

This separation allows detection rules to be developed, tested, tuned, documented, and regression-tested independently of the endpoint data-generation process.

The detection workflow is:

```text
Raw Telemetry
      ↓
Event Parsing
      ↓
Detection Logic
      ↓
Rule Matching
      ↓
Alert Generation
      ↓
Severity Classification
      ↓
MITRE ATT&CK Mapping
      ↓
Analyst Investigation
```

The primary detection engineering implementation is documented under:

`05-detection-engineering/`

Detection examples are maintained under:

`02-detections/`

---

## 7. Investigation Architecture

Security alerts are not treated as isolated events.

The investigation workflow correlates:

* Alert metadata.
* Event timestamps.
* User context.
* Process information.
* Command-line information.
* Parent-child relationships.
* Supporting Windows events.
* Supporting Sysmon events.
* Related alerts.
* Threat hunting results.

The investigation model is:

```text
Alert
 ↓
Initial Triage
 ↓
Context Collection
 ↓
Event Correlation
 ↓
Timeline Construction
 ↓
Behavior Analysis
 ↓
MITRE ATT&CK Mapping
 ↓
Scope Assessment
 ↓
Response Decision
 ↓
Evidence Documentation
```

Investigation artifacts are maintained under:

`04-Incident-Investigations/`

---

## 8. Threat Hunting Architecture

Threat hunting operates independently from reactive alert investigation.

The hunting workflow begins with a behavioral hypothesis and searches available telemetry for evidence supporting or disproving that hypothesis.

```text
Threat Hypothesis
       ↓
Relevant ATT&CK Technique
       ↓
Required Telemetry
       ↓
Hunting Query
       ↓
Event Collection
       ↓
Correlation
       ↓
Finding
       ↓
Detection Gap Analysis
       ↓
Detection Improvement
```

Threat hunting documentation is maintained under:

`03-threat-hunting/`

---

## 9. Incident Response Integration

Detection and investigation outputs feed into the incident response layer.

The response architecture supports:

* Alert prioritization.
* Incident scoping.
* Evidence preservation.
* Containment planning.
* Eradication activities.
* Recovery activities.
* Post-incident review.
* Detection improvement.

Incident response documentation is maintained under:

`06-incident-response/`

The response process is connected directly to detection engineering so lessons learned from incidents can be converted into improved detection coverage.

---

## 10. Forensic Integration

The forensic layer provides deeper analysis when security events require additional investigation.

Potential evidence sources include:

* Windows Event Logs.
* PowerShell artifacts.
* Registry artifacts.
* Prefetch artifacts.
* Persistence-related artifacts.
* Process timelines.
* Other endpoint evidence.

Forensic artifacts and procedures are maintained under:

`07-forensics/`

The forensic workflow supports the broader investigation lifecycle:

```text
Detection
   ↓
Investigation
   ↓
Evidence Identification
   ↓
Forensic Analysis
   ↓
Timeline Reconstruction
   ↓
Finding
   ↓
Incident Response
```

---

## 11. Network Security Integration

The architecture is designed to incorporate network telemetry alongside endpoint telemetry.

The network security layer includes:

* Wireshark analysis.
* Suricata monitoring.
* Zeek telemetry.
* DNS analysis.
* HTTP analysis.
* Network threat hunting.

Network-security artifacts are maintained under:

`08-network-security/`

The architectural objective is to correlate endpoint and network observations where telemetry is available.

```text
Endpoint Telemetry ──────┐
                         ├──→ Correlation → Investigation
Network Telemetry ───────┘
```

---

## 12. Threat Intelligence Integration

Threat intelligence provides contextual enrichment for indicators discovered during investigations.

Relevant indicators may include:

* File hashes.
* IP addresses.
* Domains.
* URLs.

The threat-intelligence layer is maintained under:

`09-threat-intelligence/`

The enrichment workflow is:

```text
Investigation
      ↓
Indicator Extraction
      ↓
Threat Intelligence Enrichment
      ↓
Contextual Analysis
      ↓
Investigation Decision
```

Threat intelligence is treated as supporting evidence and context rather than as a substitute for direct telemetry analysis.

---

## 13. Security Automation

Automation capabilities are maintained under:

`10-scripts/`

The automation layer supports repetitive SOC activities such as:

* Wazuh alert analysis.
* IOC extraction.
* Timeline generation.
* Log analysis.
* Detection validation.

Automation is designed to reduce repetitive analyst workload while preserving analyst review and investigation context.

---

## 14. Metrics and Continuous Improvement

The architecture includes a measurement layer under:

`11-metrics/`

Metrics are used to evaluate:

* ATT&CK coverage.
* Detection coverage.
* Detection success.
* False-positive behavior.
* Detection gaps.
* Before/after tuning.
* Investigation performance.

The improvement lifecycle is:

```text
Detection
    ↓
Validation
    ↓
Measurement
    ↓
Gap Identification
    ↓
Tuning
    ↓
Regression Testing
    ↓
Retesting
    ↓
Measurement
```

This prevents detection engineering from becoming a one-time rule-writing exercise.

---

## 15. Security Boundary

The laboratory operates as an isolated and authorized security-testing environment.

The following principles apply:

* Security testing is restricted to authorized laboratory systems.
* Attack simulation is performed for defensive validation.
* Credentials and secrets are not stored in public documentation.
* Sensitive infrastructure information is minimized in screenshots.
* Evidence intended for public repositories is reviewed for unnecessary sensitive information.
* Production or third-party systems are outside the testing scope.

---

## 16. Repository Integration

The architecture is directly connected to the rest of the project:

| Repository Area               | Architectural Role                         |
| ----------------------------- | ------------------------------------------ |
| `01-lab/`                     | Laboratory infrastructure and architecture |
| `02-detections/`              | Detection implementations                  |
| `03-threat-hunting/`          | Proactive security investigations          |
| `04-Incident-Investigations/` | Alert-driven investigations                |
| `05-detection-engineering/`   | Detection lifecycle and engineering        |
| `06-incident-response/`       | Response procedures and playbooks          |
| `07-forensics/`               | Digital forensic analysis                  |
| `08-network-security/`        | Network telemetry and analysis             |
| `09-threat-intelligence/`     | Indicator enrichment                       |
| `10-scripts/`                 | Security automation                        |
| `11-metrics/`                 | Detection and investigation measurement    |
| `12-assets/`                  | Shared architecture and security assets    |
| `13-reports/`                 | Executive and technical reporting          |
| `14-screenshots/`             | Supporting visual evidence                 |
| `docs/`                       | Cross-project technical documentation      |

---

## 17. Architecture Design Principles

The laboratory architecture follows several security engineering principles:

### Observable

Security behavior must generate telemetry that can be collected and analyzed.

### Detectable

Relevant behavior should have corresponding detection logic where sufficient telemetry exists.

### Investigable

Alerts should provide enough context to support analyst investigation.

### Huntable

Telemetry should support proactive searches beyond individual alerts.

### Reproducible

Detection and investigation workflows should be repeatable using documented procedures.

### Testable

Detection logic should be validated against controlled security activity.

### Measurable

Detection effectiveness and gaps should be evaluated using documented metrics.

### Continuously Improved

Investigation findings and detection gaps should feed back into detection engineering.

---

## 18. Related Architecture Documentation

Additional architecture documentation is maintained alongside this document:

* `enterprise-soc-architecture.drawio` — editable architecture diagram.
* `enterprise-soc-architecture.png` — architecture visualization.
* `data-flow.md` — detailed telemetry and data-flow documentation.

The architecture documentation provides the foundation for the infrastructure, detection engineering, threat hunting, investigation, response, forensic, network security, and automation components of the repository.

---

## 19. Architecture Status

The SOC laboratory architecture provides the foundational design for an integrated security monitoring, detection engineering, threat hunting, investigation, incident response, forensic analysis, network security, threat intelligence, and automation environment.

The architecture is modular and can be extended with additional telemetry sources, security technologies, detection content, automation capabilities, and analytical workflows while preserving the existing security operations lifecycle.

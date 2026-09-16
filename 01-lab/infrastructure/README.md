# Laboratory Infrastructure

## 1. Overview

The `infrastructure` directory documents the systems and security components that form the operational foundation of the **Enterprise SOC Detection, Threat Hunting & Incident Response Lab**.

The infrastructure is organized into four logical areas:

```text
infrastructure/
├── wazuh/
├── windows/
├── linux/
└── network/
```

Each area represents a distinct layer of the security monitoring environment.

The infrastructure supports the following security operations lifecycle:

```text
Endpoint Activity
      ↓
Telemetry Generation
      ↓
Telemetry Collection
      ↓
Centralized Monitoring
      ↓
Detection
      ↓
Alert Triage
      ↓
Investigation
      ↓
Threat Hunting
      ↓
Incident Response
      ↓
Forensics
      ↓
Detection Improvement
```

---

# 2. Infrastructure Objectives

The infrastructure was designed to provide:

* Centralized security monitoring.
* Endpoint telemetry collection.
* Windows security-event visibility.
* Detailed process telemetry.
* Security detection processing.
* Alert investigation capabilities.
* Controlled attack simulation.
* Threat-hunting capabilities.
* Incident-response support.
* Forensic evidence sources.
* Network-security analysis capabilities.
* A foundation for security automation.
* Reproducible security testing.

---

# 3. Infrastructure Components

| Infrastructure Layer | Primary Function                                                 |
| -------------------- | ---------------------------------------------------------------- |
| Wazuh                | Centralized security monitoring and detection                    |
| Windows              | Primary monitored endpoint                                       |
| Linux                | Supporting security infrastructure and future endpoint telemetry |
| Network              | Network monitoring and analysis layer                            |

The components are integrated through the laboratory's telemetry architecture.

---

# 4. Wazuh Infrastructure

The Wazuh infrastructure provides the centralized security monitoring and detection layer.

It consists of:

```text
Wazuh Manager
      ↓
Wazuh Detection Processing
      ↓
Wazuh Alerts
      ↓
Wazuh Dashboard
      ↓
SOC Analyst
```

The Wazuh infrastructure is responsible for:

* Receiving endpoint telemetry.
* Processing security events.
* Applying detection rules.
* Generating security alerts.
* Supporting event investigation.
* Providing analyst-facing security visibility.

Detailed Wazuh infrastructure documentation is maintained under:

```text
infrastructure/wazuh/
```

---

# 5. Windows Infrastructure

Windows provides the primary monitored endpoint environment.

The endpoint generates security telemetry used throughout the detection and investigation lifecycle.

Primary telemetry sources include:

* Windows Security Event Logs.
* PowerShell-related telemetry.
* Sysmon events.
* Process execution telemetry.
* Process relationship information.
* User and account activity.
* Other configured Windows security events.

The Windows infrastructure provides the primary source of endpoint security observations used by the project.

Detailed Windows documentation is maintained under:

```text
infrastructure/windows/
```

---

# 6. Linux Infrastructure

Linux infrastructure provides supporting functionality for the laboratory environment.

The Linux layer is also designed to support future expansion of the monitoring environment with Linux endpoint telemetry and security monitoring capabilities.

Potential Linux security telemetry includes:

* Authentication events.
* Process activity.
* System activity.
* Service activity.
* File-system activity.
* Security-relevant operating-system events.

Linux infrastructure documentation is maintained under:

```text
infrastructure/linux/
```

Only implemented and validated Linux capabilities are documented as operational components.

---

# 7. Network Infrastructure

The network layer provides the foundation for network-security monitoring and analysis.

Network security capabilities are integrated with the broader SOC architecture to provide additional context during investigations.

The network-security layer supports analysis through:

* Packet capture.
* Protocol analysis.
* Network intrusion detection.
* Network metadata.
* DNS analysis.
* HTTP analysis.
* Network threat hunting.

Detailed network infrastructure documentation is maintained under:

```text
infrastructure/network/
```

---

# 8. Infrastructure-to-Telemetry Relationship

The infrastructure components form a layered telemetry architecture:

```text
┌─────────────────────────────────────┐
│          Windows Endpoint           │
│                                     │
│ Windows Security Logs               │
│ Sysmon                              │
│ Process / User Activity             │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│            Wazuh Agent              │
│                                     │
│ Collection + Forwarding             │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│           Wazuh Manager             │
│                                     │
│ Processing + Detection              │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          Wazuh Dashboard            │
│                                     │
│ Triage + Investigation              │
└──────────────────┬──────────────────┘
                   │
                   ▼
        SOC Investigation Workflow
```

Network telemetry and additional infrastructure components provide complementary security context where implemented.

---

# 9. Infrastructure Security Boundary

The laboratory infrastructure operates within an isolated and authorized security-testing environment.

The environment is designed so that security-testing activity can be performed without intentionally targeting third-party systems.

Security boundaries include:

* Controlled laboratory endpoints.
* Authorized attack-simulation systems.
* Segmented virtual-machine infrastructure.
* Controlled telemetry sources.
* Sanitized public evidence.

Security credentials and secrets are not stored within public repository documentation.

---

# 10. Infrastructure Documentation Model

Each infrastructure component is documented according to its operational role.

The documentation model is:

```text
Component
    ↓
Purpose
    ↓
Architecture
    ↓
Deployment
    ↓
Configuration
    ↓
Telemetry
    ↓
Security Monitoring
    ↓
Validation
    ↓
Operational Considerations
```

This ensures infrastructure documentation remains useful to both security engineers and SOC analysts.

---

# 11. Integration With Detection Engineering

Infrastructure telemetry provides the raw data required by the detection-engineering lifecycle.

```text
Infrastructure
      ↓
Telemetry
      ↓
Detection Development
      ↓
Detection Testing
      ↓
Validation
      ↓
Deployment
      ↓
Monitoring
      ↓
Tuning
      ↓
Regression Testing
```

Detection content is maintained under:

```text
02-detections/
05-detection-engineering/
```

---

# 12. Integration With Threat Hunting

The infrastructure provides the telemetry required for proactive threat hunting.

Hunting activities can use:

* Authentication telemetry.
* Process telemetry.
* PowerShell telemetry.
* User-account activity.
* Endpoint events.
* Network telemetry.

The hunting workflow is:

```text
Infrastructure Telemetry
        ↓
Hunting Hypothesis
        ↓
Query
        ↓
Event Analysis
        ↓
Correlation
        ↓
Finding
```

Hunting content is maintained under:

```text
03-threat-hunting/
```

---

# 13. Integration With Incident Investigations

Infrastructure telemetry provides the evidence used during alert investigations.

The investigation process correlates information from:

* Monitored endpoints.
* Windows Security Logs.
* Sysmon.
* Wazuh alerts.
* Process activity.
* User activity.
* Network telemetry where available.

Investigation documentation is maintained under:

```text
04-Incident-Investigations/
```

---

# 14. Integration With Incident Response

Infrastructure provides the technical context required to support response activities.

Relevant information can include:

* Affected host.
* User context.
* Process context.
* Security events.
* Timeline information.
* Network observations.
* Supporting forensic evidence.

Response procedures are maintained under:

```text
06-incident-response/
```

---

# 15. Infrastructure and Forensics

The monitored infrastructure provides endpoint artifacts that can support forensic analysis.

Potential evidence sources include:

* Windows Event Logs.
* PowerShell artifacts.
* Registry artifacts.
* Prefetch.
* Persistence-related artifacts.
* Process timelines.
* Other endpoint artifacts.

Forensic analysis is maintained under:

```text
07-forensics/
```

---

# 16. Infrastructure and Network Security

The network infrastructure provides an additional telemetry layer for security monitoring.

Where endpoint and network telemetry overlap, the data can be correlated to improve investigation context.

```text
Endpoint Activity
       +
Network Activity
       ↓
Correlation
       ↓
Security Investigation
```

Network-security artifacts are maintained under:

```text
08-network-security/
```

---

# 17. Infrastructure and Security Automation

Infrastructure telemetry provides structured input for security automation.

Automation can process:

* Wazuh alerts.
* Endpoint events.
* IOC information.
* Log data.
* Investigation timelines.
* Detection-validation results.

Automation artifacts are maintained under:

```text
10-scripts/
```

---

# 18. Operational Documentation

Infrastructure documentation is separated from deployment and configuration documentation.

| Directory         | Purpose                                               |
| ----------------- | ----------------------------------------------------- |
| `infrastructure/` | What systems and components exist                     |
| `deployment/`     | How the environment was deployed                      |
| `configuration/`  | How security and telemetry components were configured |
| `architecture/`   | How components interact and how data flows            |

This separation makes the repository easier to maintain and allows individual components to evolve without mixing architectural, deployment, and configuration information.

---

# 19. Evidence and Validation

Infrastructure capabilities are validated through observable telemetry and operational behavior.

Validation can include:

* Endpoint connectivity.
* Telemetry generation.
* Agent communication.
* Event ingestion.
* Detection processing.
* Alert generation.
* Dashboard visibility.
* Investigation capability.
* Controlled security testing.

Supporting evidence is maintained within the relevant detection, investigation, hunting, and screenshot directories.

---

# 20. Infrastructure Summary

The laboratory infrastructure provides the technical foundation for the complete SOC security lifecycle.

```text
             INFRASTRUCTURE
                   │
                   ▼
               TELEMETRY
                   │
                   ▼
              DETECTION
                   │
                   ▼
                TRIAGE
                   │
                   ▼
             INVESTIGATION
                   │
          ┌────────┴────────┐
          ▼                 ▼
      HUNTING           RESPONSE
          │                 │
          └────────┬────────┘
                   ▼
              FORENSICS
                   │
                   ▼
        THREAT INTELLIGENCE
                   │
                   ▼
        DETECTION ENGINEERING
                   │
                   ▼
          TUNING & TESTING
                   │
                   ▼
         CONTINUOUS IMPROVEMENT
```

The infrastructure layer therefore serves as the operational foundation connecting endpoint telemetry, centralized monitoring, detection engineering, threat hunting, investigations, incident response, forensics, network security, threat intelligence, automation, and security metrics.

# Linux Infrastructure

## 1. Overview

Linux infrastructure provides the server-side foundation for the SOC lab and hosts the centralized Wazuh monitoring components.

The Linux environment is responsible for supporting the security monitoring infrastructure, processing endpoint telemetry, hosting security services, and providing a controlled platform for operational and detection-engineering activities.

The primary Linux security-monitoring role in this project is the Wazuh Manager infrastructure.

---

## 2. Linux Infrastructure Role

The Linux environment supports the following security functions:

* Centralized Wazuh management
* Security event processing
* Detection rule evaluation
* Alert generation
* Endpoint-agent management
* Security monitoring infrastructure
* Detection-engineering activities
* Administrative and operational logging

The architecture separates the monitored Windows endpoint from the centralized security-monitoring infrastructure.

---

## 3. Infrastructure Architecture

The Linux monitoring infrastructure connects the endpoint telemetry layer to the analyst interface:

```text id="b7x2fd"
┌──────────────────────────────┐
│      Windows Endpoint        │
│                              │
│ Security Events              │
│ Sysmon                        │
│ PowerShell                    │
└──────────────┬───────────────┘
               │
               │ Wazuh Agent
               ▼
┌──────────────────────────────┐
│       Linux Server VM        │
│                              │
│      Wazuh Manager          │
│                              │
│ Event Processing             │
│ Detection Rules              │
│ Alert Generation             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Wazuh Dashboard        │
│                              │
│ SOC Monitoring               │
│ Investigation                │
│ Threat Hunting               │
└──────────────────────────────┘
```

This architecture provides centralized visibility into endpoint security activity.

---

## 4. Linux Server Responsibilities

The Linux server provides the infrastructure required for centralized security monitoring.

Its responsibilities include:

### Wazuh Management

The server hosts the Wazuh Manager responsible for processing telemetry received from monitored endpoints.

### Detection Processing

Security events are evaluated against configured Wazuh detection logic.

### Alert Generation

Events that satisfy detection criteria are converted into structured alerts for analyst review.

### Infrastructure Administration

The Linux environment also provides the administrative interface required to manage the monitoring infrastructure and validate its operational state.

---

## 5. Wazuh Manager Integration

The Linux server hosts the Wazuh Manager component described in:

```text id="l4s3w1"
01-lab/infrastructure/wazuh/manager.md
```

The manager receives telemetry from Wazuh agents and processes it through the detection pipeline:

```text id="4r4f0n"
Wazuh Agent
     ↓
Linux Wazuh Manager
     ↓
Event Parsing
     ↓
Rule Evaluation
     ↓
Alert Generation
     ↓
Dashboard
```

This makes the Linux server a central component of the lab's monitoring architecture.

---

## 6. Linux as a Security Monitoring Platform

The Linux environment provides several characteristics useful for a security laboratory:

* Stable server environment
* Centralized service hosting
* Command-line administration
* Log-based operational visibility
* Flexible security tooling
* Automation support
* Integration with security-monitoring platforms

The platform is therefore suitable for hosting the centralized defensive infrastructure required by this project.

---

## 7. Service Monitoring

Security-monitoring infrastructure requires continuous validation of service health.

Operational checks should verify:

* Wazuh Manager availability
* Agent connectivity
* Event ingestion
* Alert generation
* Dashboard accessibility
* Relevant service status
* System resource availability

A basic operational validation workflow is:

```text id="a8eyvi"
Service Status
      ↓
Agent Connectivity
      ↓
Telemetry Ingestion
      ↓
Event Processing
      ↓
Alert Generation
      ↓
Dashboard Visibility
```

This ensures that a missing alert is not incorrectly interpreted as proof that suspicious activity did not occur.

---

## 8. Linux Logging

Linux system and service logs provide operational visibility into the monitoring infrastructure.

These logs can help investigate:

* Service startup failures
* Configuration errors
* Connectivity problems
* Authentication issues
* Event-processing problems
* Resource-related issues

Operational logs should be reviewed when the expected telemetry or alerts are not appearing in the dashboard.

---

## 9. Troubleshooting Workflow

When endpoint telemetry is not visible, troubleshooting should proceed from the endpoint toward the dashboard.

```text id="1dz4pa"
Windows Activity
      ↓
Wazuh Agent
      ↓
Agent Connectivity
      ↓
Wazuh Manager
      ↓
Event Processing
      ↓
Detection Rule
      ↓
Alert Storage
      ↓
Dashboard
```

This approach isolates the failure point instead of immediately modifying detection rules.

Potential failure categories include:

### Collection Failure

The endpoint did not generate or collect the expected telemetry.

### Connectivity Failure

The agent cannot communicate with the Wazuh infrastructure.

### Processing Failure

The manager receives telemetry but does not process it as expected.

### Detection Failure

The event is processed but does not satisfy the configured detection logic.

### Visualization Failure

The alert exists but is not being displayed as expected in the analyst interface.

---

## 10. Detection Engineering Support

The Linux environment provides the platform for managing and validating Wazuh detection logic.

Detection-engineering artifacts are maintained under:

```text id="7p0sjd"
05-detection-engineering/wazuh/
```

The workflow is:

```text id="i8n0f4"
Detection Requirement
       ↓
Rule Development
       ↓
Controlled Test
       ↓
Wazuh Manager Processing
       ↓
Alert Validation
       ↓
Tuning
       ↓
Regression Test
```

This connects infrastructure operations with detection engineering.

---

## 11. Controlled Testing

The Linux infrastructure participates in authorized laboratory testing.

Testing may involve generating controlled endpoint activity and validating whether the Wazuh Manager processes the resulting telemetry correctly.

All offensive testing within the project is limited to systems owned or explicitly authorized for testing.

The objective is to validate defensive visibility rather than conduct unauthorized activity.

---

## 12. Security Hardening Considerations

The Linux monitoring server should be treated as security-sensitive infrastructure.

Recommended controls include:

* Restrict administrative access
* Use strong authentication
* Keep software packages updated
* Minimize unnecessary services
* Restrict management interfaces
* Protect configuration files
* Protect authentication material
* Avoid storing secrets in Git
* Monitor service health
* Maintain controlled network exposure
* Separate laboratory infrastructure from production systems

Public documentation should not expose credentials, private keys, tokens, or unnecessary infrastructure details.

---

## 13. Administrative Access

Administrative access to the Linux server should be limited to authorized users.

Administrative operations should be performed through controlled access mechanisms and should avoid unnecessary exposure of privileged credentials.

Security-sensitive configuration should remain local to the laboratory environment when it is not required for demonstrating the project.

---

## 14. Network Considerations

The Linux monitoring server communicates with monitored endpoints and the analyst interface.

A simplified network model is:

```text id="x0n1ha"
Windows Endpoint
       │
       │ Security Telemetry
       ▼
Linux Wazuh Server
       │
       │ Alert / Event Data
       ▼
Analyst Dashboard
```

Network configuration should ensure that monitoring traffic is permitted while unnecessary exposure is minimized.

Private laboratory addresses should not be included in public documentation unless they are necessary to explain a technical configuration.

---

## 15. Evidence and Documentation

Linux infrastructure evidence can include:

* Service-status output
* Wazuh Manager configuration
* Agent connectivity
* Event-processing validation
* Detection-rule configuration
* Operational troubleshooting evidence

Evidence should be stored according to its purpose.

Infrastructure evidence belongs primarily under:

```text id="l17z6q"
01-lab/
```

Detection evidence belongs under:

```text id="a8k9qv"
02-detections/
```

Investigation evidence belongs under:

```text id="h8khfw"
04-Incident-Investigations/
```

This separation maintains a clear distinction between infrastructure documentation and security-analysis evidence.

---

## 16. Relationship to Other Infrastructure

The Linux server does not operate independently.

It integrates with:

| Component        | Relationship                                              |
| ---------------- | --------------------------------------------------------- |
| Windows Endpoint | Provides endpoint telemetry                               |
| Wazuh Agent      | Forwards endpoint events                                  |
| Wazuh Manager    | Processes telemetry and generates alerts                  |
| Wazuh Dashboard  | Provides analyst visibility                               |
| Kali Linux       | Authorized source of controlled security-testing activity |
| Network Layer    | Provides laboratory connectivity                          |

The infrastructure therefore forms a complete security-monitoring environment rather than a collection of independent virtual machines.

---

## 17. SOC Workflow Integration

Linux infrastructure supports the complete defensive workflow:

```text id="e4av5x"
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

The Linux server is particularly important during:

* Telemetry collection
* Detection processing
* Alert generation
* Detection validation
* Operational troubleshooting
* Detection engineering

---

## 18. Operational Validation

Before relying on the monitoring infrastructure for a security exercise, the following conditions should be validated:

```text id="5x0mcv"
[ ] Linux server operational
[ ] Wazuh Manager operational
[ ] Endpoint agent connected
[ ] Expected telemetry being received
[ ] Detection rules loaded
[ ] Test events processed
[ ] Alerts visible to analyst
```

This validation establishes a known-good monitoring baseline before security testing begins.

---

## 19. Repository Integration

Linux infrastructure documentation supports:

```text id="x9ft6d"
01-lab/
├── infrastructure/
│   ├── wazuh/
│   └── linux/
│
05-detection-engineering/
│
06-incident-response/
│
07-forensics/
│
10-scripts/
```

Automation and administrative scripts can be maintained under:

```text id="gy4y5k"
10-scripts/bash/
```

Python-based security automation is maintained under:

```text id="7x6w9e"
10-scripts/python/
```

---

## 20. Operational Principles

The Linux infrastructure is managed according to the following principles:

### Reliability

Security monitoring must remain operational before detection results can be trusted.

### Least Privilege

Administrative access and exposed services should be minimized.

### Observability

Service health and event flow should be observable.

### Separation

Infrastructure configuration, detection logic, evidence, and reports should remain logically separated.

### Validation

Changes should be tested before being treated as operationally reliable.

### Reproducibility

Configuration and procedures should be documented sufficiently to reproduce the monitoring environment.

---

## 21. Summary

The Linux infrastructure provides the server-side foundation of the SOC lab.

It hosts the centralized Wazuh monitoring environment and supports:

* Endpoint telemetry processing
* Detection evaluation
* Alert generation
* Security monitoring
* Detection engineering
* Operational troubleshooting
* Controlled security testing

Its role within the architecture can be summarized as:

```text id="w6j6y4"
Windows Telemetry
       ↓
Wazuh Agent
       ↓
Linux Wazuh Infrastructure
       ↓
Detection Processing
       ↓
Security Alert
       ↓
SOC Analysis
```

The Linux environment therefore provides the centralized infrastructure required to operate the project's detection, investigation, hunting, and response workflows.

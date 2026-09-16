# SOC Lab Deployment

## 1. Overview

The deployment layer defines how the security-monitoring environment is provisioned, configured, validated, and maintained.

The objective is to provide a repeatable deployment model for the SOC lab rather than treating each virtual machine or security component as an isolated installation.

The deployment workflow covers:

* Virtual infrastructure
* Operating-system preparation
* Wazuh deployment
* Endpoint-agent deployment
* Telemetry configuration
* Network configuration
* Detection configuration
* Validation
* Operational readiness

---

## 2. Deployment Architecture

The laboratory deployment consists of multiple logical components:

```text
┌────────────────────────────────────────────┐
│              Laboratory Host               │
│                                            │
│  ┌──────────────────────────────────────┐  │
│  │         Linux Server VM              │  │
│  │                                      │  │
│  │ Wazuh Manager / Monitoring Services  │  │
│  └──────────────────┬───────────────────┘  │
│                     │                      │
│                     │ Telemetry            │
│                     ▼                      │
│  ┌──────────────────────────────────────┐  │
│  │          Windows 10 VM              │  │
│  │                                      │  │
│  │ Wazuh Agent / Sysmon / Windows Logs │  │
│  └──────────────────────────────────────┘  │
│                                            │
│  ┌──────────────────────────────────────┐  │
│  │           Kali Linux VM             │  │
│  │                                      │  │
│  │ Authorized Security Testing         │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

The exact virtualization platform and private network addressing are intentionally not exposed in public documentation.

---

## 3. Deployment Principles

The deployment follows several core principles.

### Isolation

Security testing is performed inside an authorized laboratory environment.

### Reproducibility

Important configuration and deployment decisions are documented so the environment can be recreated.

### Separation of Responsibilities

Infrastructure, detection logic, evidence, and investigation documentation remain separated.

### Validation

Each deployment stage is validated before moving to the next stage.

### Least Privilege

Administrative access and exposed services are minimized.

### Security by Design

Credentials, secrets, tokens, and unnecessary infrastructure information are excluded from public repository content.

---

## 4. Deployment Lifecycle

The overall deployment lifecycle is:

```text
Plan
 ↓
Provision
 ↓
Configure
 ↓
Integrate
 ↓
Validate
 ↓
Test
 ↓
Document
 ↓
Operate
 ↓
Improve
```

This lifecycle ensures that deployment is treated as an operational process rather than a one-time installation task.

---

## 5. Phase 1 — Environment Planning

Before deployment, the required components and their responsibilities are defined.

| Component           | Primary Role                            |
| ------------------- | --------------------------------------- |
| Linux Server        | Central Wazuh monitoring infrastructure |
| Windows Endpoint    | Endpoint telemetry source               |
| Kali Linux          | Authorized security testing             |
| Analyst Workstation | Dashboard and analysis interface        |

The architecture is documented under:

```text
01-lab/architecture/
```

---

## 6. Phase 2 — Virtual Machine Provisioning

Each required system is provisioned as a dedicated laboratory virtual machine.

The provisioning process establishes:

* Operating system
* CPU and memory allocation
* Virtual storage
* Network interface
* Hostname
* Administrative access
* Required software prerequisites

Resources should be sized according to the workload of the individual component.

The monitoring server should receive sufficient resources for event processing and dashboard operation.

---

## 7. Phase 3 — Linux Server Deployment

The Linux server is prepared to host the centralized monitoring infrastructure.

The deployment process includes:

```text
Operating System
      ↓
System Configuration
      ↓
Network Configuration
      ↓
Required Dependencies
      ↓
Wazuh Components
      ↓
Service Validation
```

After deployment, the server becomes the central processing point for endpoint security telemetry.

Detailed Linux infrastructure information is maintained under:

```text
01-lab/infrastructure/linux/
```

---

## 8. Phase 4 — Wazuh Deployment

Wazuh is deployed as the centralized security-monitoring platform.

The deployment establishes the required components for:

* Agent communication
* Event processing
* Detection
* Alert generation
* Analyst visibility

The Wazuh infrastructure is documented under:

```text
01-lab/infrastructure/wazuh/
```

The deployment should be validated before endpoint telemetry is introduced.

---

## 9. Phase 5 — Windows Endpoint Deployment

The Windows endpoint is prepared as the primary monitored workstation.

The endpoint deployment includes:

```text
Windows Operating System
       ↓
System Preparation
       ↓
Wazuh Agent
       ↓
Windows Security Logging
       ↓
Sysmon
       ↓
PowerShell Logging
       ↓
Telemetry Validation
```

The endpoint infrastructure is documented under:

```text
01-lab/infrastructure/windows/
```

---

## 10. Phase 6 — Wazuh Agent Integration

The Wazuh Agent establishes communication between the Windows endpoint and the Wazuh Manager.

The integration lifecycle is:

```text
Agent Installation
       ↓
Manager Registration
       ↓
Agent Configuration
       ↓
Connectivity Validation
       ↓
Telemetry Validation
```

The agent should be considered operational only after the manager receives expected endpoint telemetry.

---

## 11. Phase 7 — Endpoint Telemetry Configuration

The endpoint is configured to provide security-relevant telemetry.

Primary sources include:

### Windows Security Logs

Used for authentication and account-management visibility.

### Sysmon

Used for detailed endpoint process and system telemetry.

### PowerShell Logging

Used to provide additional visibility into PowerShell execution and script activity.

The telemetry architecture is documented under:

```text
docs/03-telemetry.md
```

---

## 12. Phase 8 — Network Integration

The laboratory network is configured to support communication between:

```text
Windows Endpoint
       ↓
Wazuh Manager
       ↓
Wazuh Dashboard
```

Authorized testing systems are also connected to the laboratory environment where required.

Network deployment should verify:

* Endpoint connectivity
* Manager connectivity
* Dashboard accessibility
* Required service communication
* Appropriate isolation

Network architecture is documented under:

```text
01-lab/infrastructure/network/
```

---

## 13. Phase 9 — Detection Configuration

Once telemetry is operational, detection logic can be introduced.

The detection workflow is:

```text
Telemetry Available
       ↓
Detection Requirement
       ↓
Rule Configuration
       ↓
Controlled Activity
       ↓
Alert Generation
       ↓
Validation
```

Detection implementations are maintained under:

```text
05-detection-engineering/
```

Operational detection scenarios are maintained under:

```text
02-detections/
```

---

## 14. Phase 10 — Detection Validation

Every detection should be validated against expected telemetry.

Validation should answer:

* Was the expected event generated?
* Was the event collected?
* Was it processed by Wazuh?
* Did the intended rule trigger?
* Was the alert severity appropriate?
* Was the relevant context available?
* Was the ATT&CK mapping appropriate?
* Can the alert be investigated?

The validation workflow is:

```text
Test Activity
      ↓
Telemetry
      ↓
Wazuh Processing
      ↓
Detection
      ↓
Alert
      ↓
Analyst Review
```

---

## 15. Phase 11 — Operational Validation

Before conducting investigation exercises, the complete monitoring pipeline should be validated.

```text
[ ] Linux server operational
[ ] Wazuh Manager operational
[ ] Wazuh Dashboard operational
[ ] Windows endpoint operational
[ ] Wazuh Agent connected
[ ] Windows telemetry available
[ ] Sysmon telemetry available
[ ] PowerShell telemetry available
[ ] Detection rules loaded
[ ] Test alerts generated
[ ] Alerts visible to analyst
```

This creates a known-good baseline for subsequent SOC activities.

---

## 16. Troubleshooting Model

Deployment problems should be investigated layer by layer.

```text
Infrastructure
     ↓
Operating System
     ↓
Network
     ↓
Security Service
     ↓
Wazuh Agent
     ↓
Telemetry
     ↓
Detection
     ↓
Dashboard
```

For example, if an alert does not appear:

```text
No Alert
   ↓
Check Dashboard
   ↓
Check Alert Processing
   ↓
Check Detection Rule
   ↓
Check Event Ingestion
   ↓
Check Agent
   ↓
Check Endpoint Telemetry
   ↓
Check Test Activity
```

This avoids making unnecessary configuration changes before identifying the actual failure point.

---

## 17. Configuration Management

Deployment-related configuration is separated according to purpose.

```text
01-lab/configuration/
```

contains laboratory configuration documentation.

Wazuh-specific infrastructure information is maintained under:

```text
01-lab/infrastructure/wazuh/
```

Detection-specific Wazuh configuration belongs under:

```text
05-detection-engineering/wazuh/
```

This separation improves maintainability and prevents infrastructure configuration from becoming mixed with detection-development artifacts.

---

## 18. Security Controls

Deployment should maintain the following security controls:

* Restricted administrative access
* Protected credentials
* No secrets committed to Git
* Controlled network exposure
* Isolated security testing
* Minimal unnecessary services
* Controlled management interfaces
* Regular configuration review
* Appropriate software updates
* Evidence protection

The laboratory should remain separate from production and personal systems.

---

## 19. Deployment Documentation

Deployment documentation should allow another analyst to understand:

1. What components are required
2. What role each component performs
3. How the components communicate
4. What telemetry is collected
5. Where detection logic is configured
6. How the environment is validated
7. How common failures are diagnosed

The objective is reproducibility without publishing sensitive infrastructure information.

---

## 20. Evidence

Deployment evidence can include:

* Architecture diagrams
* Service-status evidence
* Agent connectivity
* Dashboard availability
* Telemetry ingestion
* Detection validation
* Configuration validation

Recommended evidence locations include:

```text
14-screenshots/
├── architecture/
├── telemetry/
└── detections/
```

Evidence should be sanitized before publication.

---

## 21. Deployment and SOC Operations

The deployment layer establishes the foundation for all subsequent SOC activities.

```text
DEPLOY
  ↓
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

Without reliable deployment and telemetry, downstream detection and investigation results cannot be trusted.

---

## 22. Maintenance

The environment should be periodically reviewed for:

* Service availability
* Agent connectivity
* Configuration changes
* Detection changes
* Telemetry coverage
* Storage requirements
* Resource utilization
* Security exposure
* Deprecated configurations

Changes should be documented and validated before being considered operational.

---

## 23. Deployment Completion Criteria

The deployment is considered operational when:

```text
Infrastructure
      ↓
Services
      ↓
Network
      ↓
Agent
      ↓
Telemetry
      ↓
Detection
      ↓
Dashboard
```

are functioning as an integrated monitoring pipeline.

The final validation should demonstrate that controlled endpoint activity can produce telemetry, reach the monitoring infrastructure, satisfy applicable detection logic, and become available to the analyst for investigation.

---

## 24. Repository Integration

Deployment connects the following repository areas:

```text
01-lab/
├── architecture/
├── infrastructure/
├── deployment/
└── configuration/

02-detections/

03-threat-hunting/

04-Incident-Investigations/

05-detection-engineering/

06-incident-response/

07-forensics/

08-network-security/
```

This establishes deployment as the infrastructure foundation for the remainder of the project.

---

## 25. Summary

The deployment layer provides a repeatable operational model for building and validating the SOC laboratory.

It integrates:

* Linux monitoring infrastructure
* Wazuh
* Windows endpoint telemetry
* Sysmon
* PowerShell logging
* Laboratory networking
* Authorized security testing
* Detection engineering
* Analyst investigation

The deployment lifecycle is:

```text
PLAN
 ↓
PROVISION
 ↓
CONFIGURE
 ↓
INTEGRATE
 ↓
VALIDATE
 ↓
TEST
 ↓
OPERATE
 ↓
IMPROVE
```

A successful deployment establishes the trusted foundation required for detection engineering, threat hunting, incident investigation, digital forensics, and incident response.

# Enterprise-Style SOC Detection, Threat Hunting & Incident Response Lab

## Project Overview

This project is a hands-on Security Operations Center (SOC) laboratory
designed to demonstrate security monitoring, detection engineering,
threat hunting, incident investigation, and incident response.

The laboratory uses Wazuh as the primary SIEM and security monitoring
platform. Windows 10 is used as the monitored endpoint, while Sysmon
will provide enhanced Windows telemetry. Kali Linux will be used only
for authorized security testing within the isolated laboratory
environment.

The project follows the SOC lifecycle:

> Collect → Detect → Triage → Investigate → Hunt → Respond → Document

---

## Objectives

The project aims to demonstrate practical ability in:

- SIEM deployment and monitoring
- Windows endpoint security monitoring
- Security event analysis
- Detection engineering
- Threat hunting
- Alert triage
- Incident investigation
- MITRE ATT&CK mapping
- Incident response
- Detection tuning
- Security documentation

---

## Technologies

| Technology | Purpose |
|---|---|
| Wazuh | SIEM and security monitoring |
| Ubuntu Server | Wazuh server |
| Windows 10 | Monitored endpoint |
| Wazuh Agent | Endpoint telemetry collection |
| Sysmon | Enhanced Windows telemetry |
| Kali Linux | Authorized security testing |
| VMware Workstation | Virtualization |
| MITRE ATT&CK | Threat behavior mapping |
| GitHub | Project documentation |

---

## Current Lab

### Wazuh Server

- Operating System: Ubuntu Server
- Role: SIEM server
- Wazuh Manager: Installed
- Wazuh Indexer: Installed
- Wazuh Dashboard: Installed

### Windows Endpoint

- Operating System: Windows 10
- Role: Monitored endpoint
- Wazuh Agent: Installed
- Sysmon: Planned

### Kali Linux

- Role: Authorized security testing
- Purpose: Generate controlled security activity for detection
  validation

---

## Planned Detection Scenarios

| ID | Detection | Status |
|---|---|---|
| DET-001 | Multiple failed Windows logins | Planned |
| DET-002 | Suspicious PowerShell activity | Planned |
| DET-003 | Suspicious process execution | Planned |
| DET-004 | Network reconnaissance | Planned |
| DET-005 | Persistence activity | Planned |

A detection will only be marked as completed after it has been
successfully tested, detected, investigated, and documented.

---

## SOC Workflow

```text
Security Activity
       ↓
Endpoint Telemetry
       ↓
Wazuh Collection
       ↓
Detection
       ↓
Alert
       ↓
Triage
       ↓
Investigation
       ↓
MITRE ATT&CK Mapping
       ↓
Response
       ↓
Documentation

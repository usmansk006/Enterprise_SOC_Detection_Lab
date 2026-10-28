# SOC Detection Lab
### Windows Security Monitoring & Detection Engineering with Wazuh

A hands-on blue-team project focused on Windows security telemetry, host-based threat detection, and detection documentation using Wazuh in a VMware virtualized lab.

## Project Overview

The SOC Detection Lab documents a Windows-focused security monitoring environment built around two virtual machines:

- **Ubuntu Server VM** — provides the environment for the Wazuh server-side deployment.
- **Windows 10 VM** — serves as the monitored endpoint and source of Windows security telemetry.
- **VMware** — provides the virtualization layer for the lab.

The project concentrates on understanding Windows event data, documenting detection logic, and connecting existing detection use cases with their technical implementation and available evidence.

The repository is organized to make the lab architecture, telemetry flow, detection content, and evidence traceable for technical review.

> **Scope note:** This README describes the project and its documented components. It does not claim that every Wazuh service is currently running or that every detection has been revalidated in the present environment.

## Project Objectives

- Document a virtualized Windows security monitoring environment.
- Understand the flow of endpoint telemetry through a Wazuh-based monitoring pipeline.
- Maintain Windows-focused detection use cases and their supporting technical documentation.
- Explain the security relevance of observed activity and the conditions used by detection rules.
- Associate existing event records, alerts, and other artifacts with the relevant detection where evidence is available.
- Distinguish implemented detection logic from historically observed and validated behavior.

## Lab Architecture

```text
                 VMware Virtual Environment

  ┌─────────────────────────┐
  │      Windows 10 VM      │
  │                         │
  │  Windows Security Logs  │
  │  Endpoint Activity      │
  │           │             │
  │           ▼             │
  │      Wazuh Agent        │
  └───────────┬─────────────┘
              │
              │ Configured telemetry
              ▼
  ┌─────────────────────────┐
  │    Ubuntu Server VM     │
  │                         │
  │     Wazuh Manager       │
  │           │             │
  │           ▼             │
  │  Detection Rule         │
  │  Evaluation             │
  │           │             │
  │           ▼             │
  │  Alert Review           │
  │  Dashboard, if available│
  └─────────────────────────┘
```

*This is a logical architecture diagram. It does not establish the current installation state of the Manager, Indexer, Dashboard, or any other service.*

### Technology Stack

| Technology | Role |
|---|---|
| VMware | Virtual machine hosting |
| Ubuntu Server | Linux environment for the Wazuh server-side deployment |
| Windows 10 | Monitored endpoint |
| Wazuh Agent | Configured endpoint telemetry collection and forwarding |
| Wazuh Manager | Event processing and detection-rule evaluation |
| Wazuh Dashboard | Alert review interface when deployed and available |
| Windows Event Logs | Primary source of Windows security telemetry |

The actual installation state and configuration of each component should be established from the repository's technical records.

## Detection Coverage

The existing project scope includes Windows-focused detection categories such as:

| Detection category | Security monitoring objective |
|---|---|
| Authentication failures | Identify repeated or suspicious failed logon activity |
| Suspicious PowerShell activity | Identify PowerShell behavior relevant to investigation |
| Security-policy discovery | Identify relevant discovery activity where covered by existing rules |
| Windows account creation | Monitor account-management activity |
| Scheduled-task creation | Monitor task creation associated with potential persistence |
| Encoded PowerShell | Identify encoded command execution where the relevant telemetry and rule conditions are present |
| Windows Defender detections | Review recorded antivirus or malware-detection events |
| Suspicious parent-child processes | Identify process relationships that warrant investigation |
| CertUtil file decoding | Monitor relevant CertUtil activity for potentially suspicious file operations |

These are detection categories, not a claim that every scenario is currently enabled or validated. Exact rule identifiers, event requirements, and implementation details should be taken from the existing detection files.

## Detection Engineering Approach

The project uses an evidence-oriented approach to detection documentation:

1. **Define the objective** — describe the behavior the detection is intended to identify.
2. **Identify telemetry** — determine the relevant Windows event source and fields where known.
3. **Review the implementation** — refer to the existing Wazuh rule or configuration.
4. **Explain detection logic** — document the conditions and expected behavior.
5. **Review available evidence** — link existing events, alerts, or historical records.
6. **Record limitations** — identify dependencies and potential false positives where established.
7. **State validation status accurately** — distinguish implementation from demonstrated detection behavior.

A rule file alone does not prove that a rule was successfully triggered. Historical evidence does not prove current operational status.

## Repository Structure

The repository includes the following main areas:

| Path | Purpose |
|---|---|
| `01-lab/` | Lab overview, architecture, environment, and telemetry flow |
| `02-detections/` | Existing detection implementations and their documentation |
| `docs/` | Documentation hub, evidence standards, and detection engineering methodology |
| `evidence/` | Location for existing supporting artifacts and an index of available evidence |
| `README.md` | Project overview and navigation |

If the actual detection directory has a different name, update the path above to match the repository. Only treat files and artifacts that actually exist in the repository as implemented deliverables.

### Start Here

- [Lab Overview](01-lab/README.md)
- [Lab Architecture](01-lab/architecture.md)
- [Lab Environment](01-lab/environment.md)
- [Telemetry Flow](01-lab/telemetry-flow.md)
- [Documentation Hub](docs/README.md)
- [Evidence and Validation Standards](docs/evidence-and-validation.md)
- [Detection Engineering Methodology](docs/detection-engineering.md)
- [Existing Detection Files](02-detections/)

## Evidence and Validation

Evidence is important to understanding what the project has demonstrated.

Depending on what is already available, supporting artifacts may include:

- Wazuh rule or configuration files
- Windows event records
- Corresponding alert records
- Historical screenshots
- Existing validation notes

Evidence should be linked to the detection or configuration it supports. Missing evidence should be identified honestly rather than replaced with invented screenshots, test results, or performance figures.

The `evidence/` directory is part of the repository organization; its presence does not mean evidence has already been collected or stored there.

## Scope and Limitations

This project focuses on Windows security monitoring and Wazuh-based detection in a VMware lab.

The documented scope does not imply the implementation of:

- Multiple SIEM platforms or cross-SIEM correlation
- Automated incident response or remediation
- Enterprise high availability
- Threat-intelligence integrations
- Production-scale continuous monitoring
- Quantified detection accuracy or performance benchmarks

These capabilities should only be claimed if separately implemented and supported by technical evidence.

## Security Considerations

- Keep credentials, API keys, tokens, and private keys out of the repository.
- Redact sensitive values from screenshots and event exports.
- Treat security alerts as investigation leads rather than automatic proof of malicious activity.
- Preserve the distinction between historical evidence and current observations.
- Document technical limitations clearly.

## Project Status

The repository documents a VMware-based Windows security monitoring project with Wazuh-focused detection content.

The implementation status of individual detections and the current availability of the lab services must be determined from the relevant configuration and evidence. This project overview does not assert that all components are currently operational or that every detection has passed end-to-end validation.

The project's emphasis is practical understanding of Windows telemetry, SIEM workflows, detection logic, and evidence-based blue-team documentation.

---

**Project focus:** Blue Team / SOC Detection Engineering  
**Virtualization:** VMware  
**Endpoint:** Windows 10 VM  
**Server environment:** Ubuntu Server VM  
**Monitoring platform:** Wazuh

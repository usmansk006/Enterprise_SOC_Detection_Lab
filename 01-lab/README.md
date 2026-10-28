# SOC Detection Lab — Lab Environment

**Windows Security Monitoring and Threat Detection with Wazuh**

## 1. Overview

The SOC Detection Lab is a hands-on blue-team project focused on monitoring Windows security activity, collecting endpoint telemetry, and documenting security detections using Wazuh.

The lab environment is built with VMware and uses two virtual machines: Ubuntu Server and Windows 10. The Windows virtual machine serves as the monitored endpoint, while the Ubuntu Server virtual machine provides the environment for the Wazuh server-side components.

The project focuses on practical detection engineering: understanding security telemetry, documenting detection logic, examining available alerts, and maintaining traceable evidence for Windows security monitoring use cases.

This repository documents the lab architecture, environment, existing detection content, and supporting evidence. It does not assume that the environment is currently running or that historical detections have been revalidated.

## 2. Project Objectives

The lab is designed to support the following blue-team objectives:

- Understand how endpoint security events move through a SIEM monitoring pipeline.
- Monitor relevant Windows security activity using Wazuh.
- Develop and document Windows-focused detection use cases.
- Understand the relationship between event sources, detection rules, and generated alerts.
- Maintain documentation that connects each detection to its purpose, relevant telemetry, and available evidence.
- Build practical experience with security monitoring and detection engineering in a virtualized environment.

## 3. Lab Architecture

The lab uses VMware to run the Windows endpoint and Ubuntu Server in separate virtual machines.

```text
                 VMware Virtual Environment
                 ┌─────────────────────────┐
                 │                         │
                 │   Windows 10 VM         │
                 │                         │
                 │   Windows Security      │
                 │   Events and Telemetry  │
                 │            │            │
                 │       Wazuh Agent       │
                 │            │            │
                 │            ▼            │
                 │   Ubuntu Server VM      │
                 │                         │
                 │       Wazuh Manager     │
                 │            │            │
                 │            ▼            │
                 │   Alert Review Layer    │
                 │   (Dashboard, if        │
                 │    deployed and usable) │
                 │                         │
                 └─────────────────────────┘
```

*The diagram represents the intended logical workflow. It is not a verified network diagram or proof that every component is currently operational.*

### Environment components

| Component | Purpose |
|---|---|
| VMware | Hosts and isolates the lab virtual machines |
| Ubuntu Server VM | Provides the Linux environment for the Wazuh server-side deployment |
| Windows 10 VM | Generates endpoint security telemetry |
| Wazuh Agent | Collects and forwards configured Windows telemetry |
| Wazuh Manager | Processes events and evaluates applicable detection rules |
| Wazuh Dashboard | Provides an interface for reviewing alerts when the required services are available |

The Indexer, Dashboard, and other Wazuh services must be documented according to their actual installation and availability. Their presence in the architecture does not, by itself, establish that they were successfully deployed.

## 4. Telemetry and Detection Workflow

The intended monitoring workflow consists of the following stages:

1. **Event generation:** Windows 10 generates security events as users and processes perform system activities.
2. **Event collection:** The Wazuh Agent collects telemetry enabled by the endpoint's logging and agent configuration.
3. **Event processing:** The Wazuh Manager receives and processes the available events.
4. **Rule evaluation:** Applicable detection rules evaluate event fields and conditions.
5. **Alert review:** Resulting alerts can be reviewed through the available Wazuh interface.
6. **Documentation:** Detection logic, relevant event details, and existing evidence are recorded in the repository.

Actual detection coverage depends on Windows audit settings, event collection configuration, rule implementation, and the telemetry available for analysis.

## 5. Detection Coverage

The project is focused on Windows security detections documented in the repository's existing detection directory.

The intended coverage areas include the following categories where supported by the existing rules and evidence:

- Authentication failures and suspicious login activity
- Suspicious PowerShell activity and security-policy discovery
- Windows account creation
- Scheduled-task creation
- Encoded PowerShell execution
- Windows Defender malware-detection events
- Suspicious parent-child process relationships
- CertUtil activity associated with file decoding

These categories describe the project's known detection scope, not a claim that every scenario is currently enabled, has been successfully tested, or is producing alerts in a live environment. Each detection's implementation and validation status should be established from its own documentation and evidence.

## 6. Documentation and Evidence

The lab documentation is intended to provide a traceable view of the environment and its detection content.

Supporting records may include:

- Architecture and environment documentation
- Detection rule files and associated explanations
- Relevant Windows event records
- Historical alert screenshots or exports
- Existing validation notes
- Known limitations and configuration dependencies

Evidence should be associated with the specific detection or configuration it supports. Historical evidence must not be presented as proof of current operational status.

Missing evidence should be identified explicitly rather than replaced with fabricated screenshots, event records, metrics, or test outcomes.

## 7. Scope and Limitations

This project is centered on Windows endpoint monitoring and Wazuh-based detection in a VMware lab.

The documented scope does not automatically include:

- Multiple SIEM platforms or cross-SIEM correlation
- Automated incident response or remediation
- Enterprise-scale high availability
- Threat-intelligence integrations
- Production-grade service monitoring
- Quantified detection accuracy or performance benchmarks

These capabilities should be added to the project description only if they are actually implemented and supported by evidence.

The current availability of the lab components is not asserted by this documentation. Historical configuration and evidence should be interpreted according to the time they were recorded.

## 8. Project Structure

The repository's existing structure is the source of truth for its files and directories.

The following documentation files describe the lab environment:

- `README.md` — Lab overview, architecture, objectives, and scope
- `architecture.md` — Logical component architecture
- `environment.md` — Virtual machines and component responsibilities
- `telemetry-flow.md` — Event collection and detection workflow

Detection documentation and evidence remain in their existing repository locations. Update any relative links in this document if the actual directory names differ.

## 9. Security and Evidence Handling

- Do not commit credentials, access tokens, private keys, or other secrets.
- Redact sensitive information from screenshots and event exports where appropriate.
- Preserve the distinction between configuration, observed activity, and validated detection outcomes.
- Document dependencies and limitations that affect detection behavior.
- Keep historical evidence clearly identified as historical.

## 10. Project Status

The repository documents a Windows-focused security monitoring and detection project built around a VMware lab with Ubuntu Server and Windows 10 virtual machines.

The project's existing detection content and supporting records should be evaluated individually. This README does not claim that the lab is currently operational, that all Wazuh services are available, or that every detection has been revalidated.

The project is intended to demonstrate practical understanding of Windows telemetry, SIEM workflows, detection logic, and evidence-based blue-team documentation.

---

**Project:** SOC Detection Lab  
**Focus:** Windows Security Monitoring and Threat Detection  
**Virtualization:** VMware  
**Endpoint:** Windows 10 VM  
**Server environment:** Ubuntu Server VM  
**SIEM platform:** Wazuh

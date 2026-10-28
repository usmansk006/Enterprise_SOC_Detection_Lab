# SOC Detection Lab — Documentation Hub

**Project:** SOC Detection Lab  
**Focus:** Windows Security Monitoring and Threat Detection  
**Virtualization:** VMware   
**Virtual Machines:** Ubuntu Server and Windows 10  
**Monitoring Platform:** Wazuh

## 1. Overview

This directory serves as the central documentation hub for the SOC Detection Lab.

The project focuses on Windows endpoint monitoring, security-event analysis, and Wazuh-based detection engineering in a VMware-hosted lab environment.

The documentation connects the lab architecture and telemetry workflow with the existing detection implementations and their supporting evidence.

The project is intended to demonstrate practical blue-team skills through documented detection logic, Windows telemetry analysis, and evidence-based security monitoring.

## 2. Documentation Structure

| Documentation area | Purpose |
|---|---|
| `01-lab/` | Lab architecture, environment, and telemetry workflow |
| `02-detections/` | Existing detection rules, use cases, and related technical documentation |
| `evidence/` | Existing screenshots, event records, and other supporting artifacts, if present |
| `docs/` | Central documentation index and project-wide guidance |

These paths describe the intended documentation organization. If the repository uses different directory names, update the references to match the actual structure.

## 3. Lab Documentation

Start with the lab documentation to understand the monitoring environment.

- [Lab Overview](../01-lab/README.md)
- [Architecture](../01-lab/architecture.md)
- [Environment Documentation](../01-lab/environment.md)
- [Telemetry Flow](../01-lab/telemetry-flow.md)

These documents describe the VMware environment, Ubuntu Server and Windows 10 virtual machines, and the intended flow of telemetry through Wazuh.

## 4. Detection Documentation

The detection directory contains the project's existing Windows-focused detection work.

Use the individual detection documents and rule files to understand:

- The behavior or security condition being detected
- The relevant Windows telemetry
- The detection logic and its dependencies
- The significance of a matching event
- The available evidence and validation status
- Known limitations and false-positive considerations, where documented

[Open the detection documentation directory](../02-detections/)

Detection status should be based on the actual rule implementation and supporting records, not inferred from the presence of a Markdown document.

## 5. Evidence and Traceability

Evidence supports the technical claims made throughout the project.

Where available, associate each evidence artifact with its relevant detection or configuration. Distinguish clearly between:

- **Configuration evidence:** Shows how a component or rule is configured.
- **Telemetry evidence:** Shows the event data that was collected or recorded.
- **Alert evidence:** Shows a corresponding alert or detection outcome.
- **Validation evidence:** Supports a specific test or verification claim.
- **Historical evidence:** Records a previous state of the environment.

A single artifact may support one or more of these categories, but its significance should be stated accurately.

Do not claim that a detection was successfully validated unless the available records support that conclusion. Historical evidence does not establish current operational status.

## 6. Technical Documentation Standards

All project documentation should follow these principles:

1. Use precise terminology for Windows events, Wazuh components, and detection rules.
2. Explain the relationship between telemetry, detection logic, and security significance.
3. Link technical claims to the relevant configuration or evidence where possible.
4. Distinguish implemented capabilities from planned or unverified capabilities.
5. Record dependencies, limitations, and relevant false-positive scenarios.
6. Avoid fabricated metrics, screenshots, event records, and test results.
7. Never commit credentials, tokens, private keys, or other secrets.

## 7. Project Scope

The documented project is focused on Windows security monitoring and Wazuh-based detections in a virtualized lab.

The presence of this documentation does not imply that the project includes other SIEM platforms, automated response, production-scale monitoring, or capabilities that have not been independently implemented and evidenced.

The implementation status of individual detections, the availability of Wazuh services, and the results of historical validation should be determined from the corresponding technical records.

The project emphasizes transparent documentation, traceable evidence, and practical Windows detection engineering.

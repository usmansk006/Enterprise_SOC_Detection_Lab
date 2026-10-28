# SOC Detection Lab — Evidence Repository

This directory contains supporting evidence for the SOC Detection Lab, a virtualized Windows security-monitoring environment built around Wazuh.

The evidence documents the lab environment, Windows agent service state, Wazuh server component status, and agent connectivity where demonstrated by the available artifacts.

Evidence is intended to support transparent technical documentation. The presence of a screenshot does not, by itself, establish successful end-to-end monitoring or detection validation.

## 1. Evidence Objectives

This directory supports the following documentation goals:

- Record the virtualized lab environment.
- Document the observed state of the Windows Wazuh Agent service.
- Record Wazuh server-side component status.
- Preserve evidence related to agent connectivity.
- Establish a foundation for future detection-validation records.
- Distinguish observed facts from assumptions and unverified functionality.

## 2. Evidence Inventory

| Evidence file | Purpose | Interpretation and limitations |
|---|---|---|
| `vmware-lab-architecture.png` | Documents the VMware lab layout. | Supports descriptions of virtual machines and their visible arrangement. Does not prove network connectivity or successful monitoring. |
| `wazuh-agent-service.png` | Documents the Windows Wazuh Agent service. | Records the service state visible at capture time. A running service alone does not prove communication with the manager. |
| `wazuh-agent-connected.png` | Intended to document Windows agent connectivity with Wazuh. | Use as connectivity evidence only if the screenshot visibly demonstrates a connected or active agent state through an appropriate Wazuh status view or equivalent evidence. |
| `wazuh-core-services-status.png` | Documents Wazuh component service status on Ubuntu Server. | Records the states visible in the captured output. Does not independently prove that the complete monitoring pipeline is operational. |

These descriptions identify the intended purpose of each artifact. Claims must be adjusted if the actual screenshot contents do not support them.

## 3. Lab Environment Context

The lab uses VMware to host virtual machines for security monitoring and investigation.

| Component | Role |
|---|---|
| Ubuntu Server VM | Intended Wazuh server-side environment |
| Windows 10 VM | Endpoint used for Windows security monitoring |
| Wazuh Agent | Endpoint component intended to forward supported telemetry |
| Wazuh Manager | Server-side component responsible for processing events and evaluating applicable detection rules |

The actual installation and operational state of each component must be established from available evidence. The presence of a component in the architecture does not establish that it is currently running or communicating successfully.

## 4. Evidence Interpretation

### 4.1 VMware lab environment

`vmware-lab-architecture.png` documents the visible virtual-machine arrangement. Use it as environmental context rather than proof of successful event collection.

### 4.2 Windows Wazuh Agent service

`wazuh-agent-service.png` records the Windows service state shown in the screenshot. A running service is a useful operational indicator, but it is not equivalent to confirmed manager connectivity.

### 4.3 Agent connectivity

`wazuh-agent-connected.png` is intended to support agent-connectivity documentation. Before describing the agent as connected, verify that the screenshot shows an explicit connected or active status from an appropriate source.

If it shows only the Windows service running, describe it as service-status evidence instead.

### 4.4 Wazuh server components

`wazuh-core-services-status.png` documents the service states visible in the Ubuntu Server output. Missing, stopped, failed, and running components should be recorded accurately.

Service status is time-specific. A historical screenshot should not be presented as proof of current availability.

## 5. Detection Evidence and Validation

The screenshots in this directory primarily document infrastructure and component status. They do not independently establish that an existing detection rule successfully generated an alert.

For each detection-validation exercise, record:

1. **Detection objective:** The behavior or event being examined.
2. **Test conditions:** The environment and procedure used.
3. **Expected behavior:** The event or alert expected from the existing detection.
4. **Observed behavior:** What actually occurred.
5. **Supporting artifact:** The relevant event record, alert, screenshot, or log.
6. **Conclusion:** The result supported by the collected evidence.

Use these validation labels consistently:

- **Implemented:** The relevant detection configuration or rule exists.
- **Observed:** The relevant event or alert was actually seen.
- **Validated:** Evidence confirms expected detection behavior under documented test conditions.
- **Partially validated:** Some expected behavior was confirmed, but validation remains incomplete.
- **Not validated:** Testing or supporting evidence has not confirmed the expected behavior.

Do not mark a detection as validated solely because its rule file exists.

## 6. Evidence Handling Standards

- Preserve original screenshots where possible.
- Use descriptive filenames that accurately represent their contents.
- Record the capture date and environment details when known.
- Redact credentials, tokens, and sensitive personal information before publication.
- Avoid altering screenshots in ways that change their technical meaning.
- Keep expected results separate from observed results.
- Do not present historical screenshots as proof of current operational status.
- Update this inventory when evidence is added, replaced, or reclassified.

## 7. Current Scope and Limitations

This directory provides supporting evidence for the documented lab environment and its observable component states.

The available screenshots must be evaluated individually before making claims about agent connectivity, event ingestion, alert generation, or detection effectiveness.

Where evidence is missing or inconclusive, the relevant capability should be described as unverified rather than assumed to be functional.

## 8. Evidence Maintenance

When adding a new artifact:

1. Confirm that it originates from the actual lab.
2. Choose a filename that reflects the contents.
3. Check for sensitive information.
4. Update the evidence inventory.
5. Document what the artifact proves and what it does not prove.
6. Commit the artifact and documentation together when practical.

The objective is a reproducible, technically accurate evidence repository that supports the SOC Detection Lab without overstating its implementation or validation status.

## 9. Detection-to-Evidence Mapping

This section maps the existing detection directories to the evidence needed to assess their implementation and validation status.

The detection directory names identify the intended detection scenarios. They do not independently establish successful alert generation or validation.

| Detection ID | Detection scenario | Evidence to collect or reference | Validation status |
|---|---|---|---|
| DET-001 | Multiple failed logins | Relevant Windows authentication events and a matching alert, if available | Not yet confirmed |
| DET-002 | PowerShell security-policy discovery | Relevant PowerShell event records and a matching alert, if available | Not yet confirmed |
| DET-003 | Windows user account creation | Windows account-management event and a matching alert, if available | Not yet confirmed |
| DET-004 | Scheduled task creation | Relevant task-creation event and a matching alert, if available | Not yet confirmed |
| DET-005 | Suspicious PowerShell encoded command | Relevant PowerShell event record and a matching alert, if available | Not yet confirmed |
| DET-006 | Windows Defender malware detection | Actual Defender detection event and a matching alert, if available | Not yet confirmed |
| DET-007 | Suspicious parent-child process | Process telemetry showing the relevant parent-child relationship and a matching alert, if available | Not yet confirmed |
| DET-008 | CertUtil LOLBin file decoding | Relevant process or command-line telemetry and a matching alert, if available | Not yet confirmed |

### Evidence classification

Use the following distinctions when updating this mapping:

- **Configuration evidence:** The detection rule or relevant configuration exists in the repository.
- **Event evidence:** The underlying Windows or endpoint event was observed.
- **Alert evidence:** The monitoring platform generated a corresponding alert.
- **Validation evidence:** A documented test and its observed outcome support the detection's expected behavior.

A detection may have configuration evidence without event, alert, or validation evidence.

### Current status

The infrastructure screenshots in this directory document the lab environment and selected component states. They should not be treated as proof that any of the eight detection scenarios generated an alert.

Update each detection's status only when its actual configuration, event records, alert output, or test results have been reviewed.

Do not claim successful detection or validation when supporting evidence is unavailable.

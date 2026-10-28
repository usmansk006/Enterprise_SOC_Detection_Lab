# Windows Detection Engineering — Wazuh

This directory contains eight Windows-focused detection scenarios for the SOC Detection Lab. The scenarios cover authentication activity, PowerShell execution, account management, scheduled tasks, endpoint protection, process relationships, and the use of CertUtil as a living-off-the-land binary (LOLBin).

The project uses a virtualized lab environment with a Windows 10 endpoint and an Ubuntu Server environment intended to host Wazuh server-side components.

This README serves as the index for the existing detection scenarios. Each detection's implementation and validation status must be assessed using its actual configuration and supporting evidence.

## 1. Project Objectives

The detection collection is intended to demonstrate the following detection-engineering practices:

- Identify security-relevant Windows activity.
- Define detection objectives and expected event characteristics.
- Use available endpoint telemetry to identify potentially suspicious behavior.
- Document detection logic and its technical rationale.
- Map detections to relevant event sources and investigative context.
- Evaluate alert quality and potential false positives.
- Maintain evidence that distinguishes implementation from successful validation.

## 2. Detection Catalog

| ID | Detection scenario | Security objective |
|---|---|---|
| DET-001 | Multiple failed logins | Identify repeated authentication failures that may indicate password guessing or other suspicious login activity. |
| DET-002 | PowerShell security-policy discovery | Identify PowerShell activity associated with security-policy or configuration discovery. |
| DET-003 | Windows user account creation | Identify account-creation activity that may require investigation for unauthorized account changes. |
| DET-004 | Scheduled task creation | Identify scheduled-task creation that may warrant investigation for persistence or unauthorized automation. |
| DET-005 | Suspicious PowerShell encoded command | Identify encoded PowerShell command execution requiring further analysis. |
| DET-006 | Windows Defender malware detection | Identify Windows Defender malware-detection events and their associated security context. |
| DET-007 | Suspicious parent-child process | Identify potentially suspicious relationships between parent and child processes. |
| DET-008 | CertUtil LOLBin file decoding | Identify CertUtil activity associated with file decoding that may warrant investigation. |

These descriptions summarize the intended scenarios based on the detection directory names. Exact detection conditions, event identifiers, rule logic, and data requirements must be verified against each detection's files.

## 3. Repository Structure

```text
02-detections/
├── README.md
├── DET-001-multiple-failed-logins/
├── DET-002-powershell-security-policy-discovery/
├── DET-003-windows-user-account-creation/
├── DET-004-scheduled-task-creation/
├── DET-005-suspicious-powershell-encoded-command/
├── DET-006-windows-defender-malware-detection/
├── DET-007-suspicious-parent-child-process/
└── DET-008 — Detection of CertUtil LOLBin File Decoding/
```

Each directory represents an existing detection scenario. Its contents should be reviewed before documenting the implementation details or claiming that a detection has been tested.

## 4. Detection Engineering Workflow

Each detection should be documented and assessed using a consistent workflow.

### 4.1 Detection objective

Define the suspicious or security-relevant behavior the detection is intended to identify, along with its defensive value.

### 4.2 Telemetry requirements

Identify the required event source and telemetry fields. Depending on the scenario, these may include authentication records, process-creation events, PowerShell logs, account-management events, scheduled-task events, or endpoint-protection records.

Actual availability depends on the Windows audit configuration, enabled logging, agent configuration, and installed components.

### 4.3 Detection logic

Document the actual rule or configuration used by the detection. Include its relevant conditions, dependencies, severity, and limitations only when those details can be verified from the files.

### 4.4 Validation

Where testing is performed, record the test conditions, expected behavior, observed results, and supporting evidence. A rule's existence alone does not demonstrate that it generates the intended alert.

### 4.5 Investigation and tuning

Where sufficient alert data exists, document the investigation context, possible benign explanations, false-positive considerations, and any evidence-based tuning decisions.

## 5. Evidence and Validation

Supporting lab and component screenshots are maintained in `03-evidence/`. These artifacts document environmental context and component states; they do not independently validate the eight detection scenarios.

Detection-specific evidence should be linked to the corresponding scenario and should include, where available:

- The relevant detection configuration.
- The underlying Windows or endpoint event.
- The corresponding Wazuh alert.
- The test procedure and observed outcome.
- An investigation note explaining the result.

Use the following status definitions consistently:

| Status | Meaning |
|---|---|
| Implemented | The relevant detection configuration exists and has been reviewed. |
| Observed | The relevant event or alert has actually been seen. |
| Validated | Documented test results and supporting evidence confirm the expected detection behavior under the tested conditions. |
| Partially validated | Some expected behavior has been confirmed, but validation is incomplete. |
| Not validated | Available evidence does not yet establish successful detection behavior. |

Do not assign a stronger status than the evidence supports. Where a status has not been assessed, describe it as **not yet confirmed**.

## 6. Operational Dependencies and Limitations

Detection behavior depends on the availability and configuration of the relevant telemetry, endpoint agent, Wazuh server-side components, and detection rules.

The Wazuh dashboard is currently reported as inaccessible. Therefore, current dashboard-based alert review cannot be assumed to be available. Existing detection files can still be documented, but successful event ingestion and alert generation require separate evidence.

The project documentation must distinguish historical observations from current system state.

## 7. Security and Safe Testing

Detection testing should be performed only in the authorized lab environment.

- Use controlled test conditions and document the actions performed.
- Avoid using real malware or destructive payloads.
- Protect credentials and sensitive system information in published evidence.
- Preserve relevant logs and record the test outcome accurately.
- Do not claim that a test succeeded when the expected event or alert was not observed.

## 8. Detection Documentation Standard

Each detection's documentation should cover, where applicable:

1. Detection ID and title.
2. Objective and threat context.
3. Required telemetry and prerequisites.
4. Actual rule or configuration.
5. Expected behavior and relevant event fields.
6. Testing procedure and observed results.
7. Supporting evidence links.
8. False-positive considerations and limitations.
9. Current validation status.

Only include implementation details supported by the actual detection files or collected evidence.

## 9. Current Project Scope

This directory documents the eight existing detection scenarios listed above. It does not claim that all scenarios are currently operational, that every required telemetry source is available, or that every detection has been validated.

The next stage of documentation is to review each detection directory, verify its actual implementation, and associate it with genuine event or alert evidence where available.

The objective is a technically accurate, reproducible detection portfolio that demonstrates the reasoning behind each detection and clearly identifies any remaining validation gaps.

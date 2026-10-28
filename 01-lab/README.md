# SOC Detection Lab — Laboratory Environment and Architecture

## 1. Project Overview

The SOC Detection Lab is a practical blue-team project focused on Windows security monitoring and threat detection using Wazuh.

The laboratory provides the technical foundation for the completed detection implementations maintained in this repository. It documents the relationship between endpoint security telemetry, event processing, detection rules, and generated security alerts.

The project demonstrates core SOC monitoring concepts through documented detection use cases, their technical implementation, and the available supporting evidence.

## 2. Project Objectives and Deliverables

The project brings together the following deliverables:

- A documented laboratory architecture for the existing detection environment.
- Documentation of the relevant Windows security telemetry sources.
- A structured collection of completed detection implementations.
- Technical explanations of the suspicious behaviors targeted by each detection.
- Documentation of the relationship between collected events and detection logic.
- References to available screenshots, alert records, and configuration artifacts.
- A consolidated detection inventory and relevant MITRE ATT&CK mappings.

The documentation reflects the implementation and evidence available in the repository. Individual claims are supported by the corresponding detection files and artifacts where available.

## 3. Laboratory Architecture

The laboratory uses a Wazuh-based monitoring workflow to process configured endpoint telemetry and identify security-relevant activity.

```text
┌─────────────────────────────────┐
│       Windows Endpoint          │
│                                 │
│  Windows Security Telemetry     │
│  Configured Endpoint Events     │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│          Wazuh Agent            │
│                                 │
│  Configured Event Collection    │
│  Telemetry Forwarding           │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│         Wazuh Manager           │
│                                 │
│  Event Processing               │
│  Detection Rule Evaluation      │
│  Security Alert Generation      │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│        Wazuh Dashboard          │
│                                 │
│  Alert Review                   │
│  Security Event Analysis        │
└─────────────────────────────────┘
```

The diagram represents the documented logical monitoring workflow. Component-specific details should match the actual deployment and the records retained from the completed lab.

## 4. Monitoring Components

| Component | Function |
|---|---|
| Windows endpoint | Produces the operating-system and security activity covered by the detection use cases. |
| Wazuh Agent | Collects and forwards configured endpoint telemetry. |
| Wazuh Manager | Processes received events and evaluates applicable detection rules. |
| Wazuh Dashboard | Provides access to available alerts and security-event information. |
| Detection rules | Identify the security-relevant behaviors covered by the completed implementations. |

The table describes the roles of the components in the documented architecture. Specific versions and deployment settings are recorded only where supported by existing configuration or evidence.

## 5. Telemetry Processing and Detection Workflow

The detection workflow is organized around the following sequence:

1. **Event generation:** Security-relevant activity occurs on the monitored endpoint.
2. **Telemetry collection:** Configured event sources record relevant activity.
3. **Event forwarding:** The Wazuh Agent forwards configured telemetry to the monitoring infrastructure.
4. **Event processing:** The Wazuh Manager processes the received events.
5. **Rule evaluation:** Applicable detection rules evaluate events against their configured conditions.
6. **Alert generation:** Matching activity produces alerts when the rule conditions are satisfied.
7. **Analyst review:** Available alerts provide a starting point for examining the detected behavior.

The actual event source, rule logic, and alert fields are documented at the individual detection level.

## 6. Implemented Detection Coverage

The repository contains completed detection work covering selected Windows security behaviors.

The known areas of coverage include:

- Failed authentication attempts.
- Suspicious PowerShell activity.
- Windows account creation.
- Scheduled-task creation.
- Encoded PowerShell execution.
- Microsoft Defender malware detections.
- Suspicious parent-child process relationships.
- CertUtil-based decoding activity.

These categories should be reconciled with the current detection inventory. Each detection should link to its actual rule, explanation, and available supporting evidence.

## 7. Detection Documentation and Traceability

Each detection should provide a consistent record of its purpose and implementation.

| Documentation element | Expected content |
|---|---|
| Detection objective | Security behavior the detection is intended to identify. |
| Data source | Windows event source or other telemetry used by the rule. |
| Detection logic | Existing Wazuh rule or relevant implementation reference. |
| Alert interpretation | Meaning of the relevant alert fields and conditions. |
| ATT&CK mapping | Applicable technique and a justification for the mapping. |
| False-positive considerations | Plausible legitimate activity that may trigger the rule. |
| Evidence references | Links to existing screenshots, alert records, or configuration artifacts. |
| Validation record | Previously documented test procedure and actual result, where available. |

This structure supports traceability between the implementation, its intended behavior, and the evidence retained in the repository.

## 8. Evidence and Validation Records

Evidence is an important part of the project because it allows reviewers to distinguish documented functionality from unverified claims.

The evidence record should reference artifacts such as:

- Existing Wazuh alert screenshots.
- Relevant detection-rule configuration.
- Available Windows event records.
- Recorded examples of matching alerts.
- Existing validation notes or test records.
- Supporting configuration details.

Each artifact should identify the detection it supports and explain what it demonstrates.

A screenshot of a rule proves that the rule configuration is documented; it does not, by itself, prove that the rule generated an alert. Similarly, an alert screenshot demonstrates a recorded alert, while a successful validation claim requires evidence connecting the relevant activity to the expected detection outcome.

Historical evidence from the completed lab can be retained even if the environment is no longer available for additional testing.

## 9. Technical Accuracy and Limitations

The documentation distinguishes between implemented detection logic, recorded observations, and capabilities that have not been independently verified.

- Existing detection rules are documented from their actual implementation.
- Historical alerts and screenshots are identified as retained evidence.
- Configuration details are included when supported by available records.
- Validation results are reported only when documented evidence supports them.
- Current operational status is not inferred from historical screenshots.
- Detection coverage is limited to the behaviors represented by the existing rules.

These boundaries preserve the technical credibility of the project and make its results easier for reviewers to assess.

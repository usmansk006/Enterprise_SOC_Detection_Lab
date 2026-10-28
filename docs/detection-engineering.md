# Detection Engineering Methodology

## 1. Purpose

This document describes the methodology used to organize, explain, and maintain the existing Windows-focused detection content in the SOC Detection Lab.

The project uses Wazuh as its primary detection platform and focuses on Windows endpoint telemetry collected in a VMware-based lab environment.

This document explains the detection engineering approach. It does not claim that additional detection rules have been created, that new tests have been performed, or that the lab is currently operational.

## 2. Detection Engineering Lifecycle

A detection use case can be documented through the following lifecycle:

1. **Define the security objective:** Identify the behavior or event pattern the detection is intended to identify.
2. **Identify relevant telemetry:** Determine which Windows event sources and fields are required.
3. **Review the implementation:** Examine the existing Wazuh rule and its dependencies.
4. **Describe expected behavior:** Document the conditions under which the rule should match.
5. **Review available evidence:** Associate existing events, alerts, screenshots, and validation records with the detection.
6. **Record limitations:** Document dependencies, coverage gaps, and potential false positives where known.
7. **Report validation status:** State what the available evidence actually establishes.

This lifecycle is a documentation and review framework. It should not be interpreted as evidence that every stage has been completed for every detection.

## 3. Existing Detection Scope

The project's known Windows-focused detection categories include:

- Authentication failures
- Suspicious PowerShell activity and security-policy discovery
- Windows account creation
- Scheduled-task creation
- Encoded PowerShell execution
- Windows Defender malware-detection events
- Suspicious parent-child process relationships
- CertUtil activity associated with file decoding

The exact coverage of each category depends on the existing rule implementation and its supporting records.

## 4. Detection Documentation Structure

Each detection should document the following information where it is available:

| Field | Purpose |
|---|---|
| Detection name | Identifies the behavior being monitored |
| Security objective | Explains why the behavior matters |
| Telemetry source | Identifies the relevant event source |
| Detection logic | Describes the existing rule conditions |
| Required fields | Identifies relevant event fields and dependencies |
| Expected outcome | Explains the intended detection result |
| Supporting evidence | Links existing artifacts that support the documented behavior |
| Limitations | Describes known dependencies and false-positive considerations |
| Validation status | Records the status supported by available evidence |

Use actual rule identifiers, event identifiers, field names, and thresholds from the implementation. Do not invent missing technical details.

## 5. Telemetry and Detection Logic

A detection is only as useful as the telemetry and conditions on which it depends.

When reviewing an existing rule, consider:

- Whether the required Windows event source is available
- Whether the relevant event fields are present
- Whether the rule conditions reflect the intended behavior
- Whether related rules or configuration dependencies exist
- Whether legitimate administrative activity could produce similar events
- Whether available evidence supports the expected result

These considerations describe a review framework; they do not establish that every item has been tested.

## 6. False Positives and Context

Security-relevant activity is not automatically malicious.

Examples such as PowerShell execution, account creation, scheduled-task creation, and CertUtil usage may occur during legitimate administration or software operations.

Detection documentation should explain the suspicious conditions relevant to the actual rule rather than treating every occurrence of a tool or event as confirmed malicious activity.

False-positive claims should be supported by observed results or documented analysis.

## 7. Evidence-Based Validation

Validation status must reflect the available technical records.

- **Implemented:** The detection logic is present and identifiable.
- **Historically observed:** Existing records show a relevant event or alert from an earlier observation.
- **Validated:** Available test evidence supports the stated detection behavior under documented conditions.
- **Partially validated:** Evidence supports only a subset of the expected behavior.
- **Unverified:** Available evidence is insufficient to establish the behavior.
- **Not currently assessed:** Current operational behavior has not been assessed.

These labels should be applied to individual detections according to their evidence. They must not be applied to the entire project as a single blanket status.

## 8. Maintenance and Change Control

When documenting changes to existing detection content:

1. Preserve the original detection objective unless there is a justified design change.
2. Review dependent rules and configuration before describing behavior.
3. Keep supporting documentation consistent with the implementation.
4. Retain the distinction between historical evidence and current observations.
5. Record known limitations rather than hiding unresolved issues.
6. Avoid reporting improvements or test results that have not been established.

This section describes recommended maintenance practices; it does not claim that unrecorded changes or reviews have taken place.

## 9. Scope Boundaries

This methodology applies to the existing Wazuh-based Windows detection content in the repository.

It does not imply that the project includes multiple SIEM platforms, automated incident response, production-scale monitoring, quantified detection performance, or capabilities that are not independently implemented and documented.

# Evidence and Validation

This directory stores supporting evidence for the SOC Detection Lab, including screenshots, alert records, detection-validation results, and relevant investigation artifacts.

Evidence should demonstrate what was configured, what activity was observed, and whether the corresponding detection behaved as expected.

## 1. Evidence Objectives

The evidence repository is intended to demonstrate:

- Lab environment and monitoring configuration.
- Windows security events and relevant telemetry.
- Wazuh alerts associated with existing detection rules.
- Detection-validation procedures and observed outcomes.
- Investigation context and technical analysis.
- Limitations, troubleshooting findings, and validation status.

## 2. Evidence Categories

Organize evidence into the following categories as genuine artifacts become available.

| Category | Evidence to collect |
|---|---|
| Lab environment | VMware lab configuration and relevant VM details |
| Agent and connectivity | Wazuh agent status and connection evidence, when available |
| Authentication | Relevant Windows authentication events and associated alerts |
| PowerShell | Relevant PowerShell event records and corresponding alerts |
| Account activity | Evidence of account-related events and matching alerts |
| Scheduled tasks | Relevant task-creation events and corresponding alerts |
| Defender detections | Actual Defender event records and matching alerts, if observed |
| Other detections | Evidence mapped to the existing detection rules in this repository |

Only collect categories relevant to the detections and components actually present in the lab.

## 3. Recommended File-Naming Convention

Use descriptive filenames that identify the detection or activity and the evidence type.

Examples:

- `lab-environment-overview.png`
- `wazuh-agent-status.png`
- `authentication-failure-event.png`
- `powershell-detection-alert.png`
- `scheduled-task-event.png`
- `detection-validation-notes.md`

These are naming examples, not claims that the files already exist.

## 4. Evidence Requirements

For each detection-validation exercise, record the following where applicable:

1. **Objective:** What behavior or event is being examined?
2. **Environment:** Which endpoint and relevant components were involved?
3. **Procedure:** What action or test was performed?
4. **Expected result:** What event or alert was expected?
5. **Observed result:** What actually happened?
6. **Evidence:** Which screenshot, event record, or log supports the observation?
7. **Conclusion:** Was the detection validated, partially validated, not triggered, or not tested?

Redact passwords, access tokens, personal information, and other sensitive data before publishing evidence.

## 5. Validation Status Definitions

Use these labels consistently in the project documentation.

- **Implemented:** The relevant configuration or detection rule exists in the repository.
- **Observed:** The relevant event or alert was actually seen.
- **Validated:** Evidence confirms that the detection behaved as expected under the documented test conditions.
- **Partially validated:** Some expected behavior was confirmed, but validation remains incomplete.
- **Not validated:** The required evidence is not yet available or testing has not confirmed the result.

Do not mark a detection as validated solely because its rule file exists.

## 6. Current Evidence Status

The evidence directory is being prepared for documented, verifiable artifacts. Until actual evidence files are added, no screenshots, alert records, or validation results should be assumed to exist.

The operational status of the Wazuh components must be confirmed before collecting evidence that depends on them.

## 7. Publishing Checklist

Before committing an evidence artifact:

- [ ] Confirm that it came from the actual lab.
- [ ] Ensure that its filename describes the contents accurately.
- [ ] Remove sensitive information.
- [ ] Record the related detection or validation activity.
- [ ] Distinguish expected results from observed results.
- [ ] Update the relevant project documentation when appropriate.

Evidence should be reproducible, technically relevant, and consistent with the implementation documented in this repository.

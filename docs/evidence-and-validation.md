# Evidence and Validation Standards

## 1. Purpose

This document defines how implementation records, Windows telemetry, Wazuh alerts, and historical validation evidence are organized and interpreted in the SOC Detection Lab.

The objective is to make detection documentation traceable, technically accurate, and suitable for professional portfolio review.

These standards apply to the project's existing Windows-focused detection use cases. They do not imply that additional testing has been performed or that the lab is currently operational.

## 2. Evidence Categories

Evidence should be classified according to what it demonstrates.

| Evidence category | What it can establish | What it does not establish by itself |
|---|---|---|
| Configuration evidence | The contents of a relevant configuration or rule file | That the configuration was loaded or operated successfully |
| Telemetry evidence | The contents of a recorded Windows event or other event record | That a detection rule matched the event |
| Alert evidence | The details of a recorded alert | That the alert is necessarily malicious or that the detection has no false positives |
| Validation evidence | The result of a documented verification procedure | Behavior beyond the conditions and environment actually tested |
| Historical evidence | A recorded state or observation from an earlier time | The current state of the environment |
| Documentation evidence | The documented design, reasoning, and intended behavior | That the described implementation exists unless supported by technical artifacts |

An artifact may support multiple categories. Its interpretation should remain limited to the claims it can substantiate.

## 3. Detection Traceability

Each existing detection should be traceable through the following information wherever the relevant details are available:

1. **Detection objective:** The suspicious behavior or security condition of interest.
2. **Telemetry source:** The Windows event source or other input used by the rule.
3. **Detection implementation:** The relevant Wazuh rule, configuration, or other existing implementation artifact.
4. **Expected behavior:** The conditions under which the detection is intended to match.
5. **Supporting evidence:** Existing event records, alert records, screenshots, or validation notes.
6. **Limitations:** Known dependencies, coverage gaps, and relevant false-positive considerations.
7. **Validation status:** The status supported by the available records.

Do not invent missing rule identifiers, event identifiers, thresholds, test outcomes, or evidence references.

## 4. Validation Status Definitions

Use explicit status terminology when describing individual detections.

| Status | Meaning |
|---|---|
| Implemented | The relevant detection implementation is present in the repository or otherwise established by available technical records |
| Historically observed | Existing records document an event, alert, or behavior from an earlier observation |
| Validated | Available test records substantiate the stated detection behavior under documented conditions |
| Partially validated | Evidence supports only part of the expected behavior or a limited set of conditions |
| Unverified | Available evidence is insufficient to establish the stated behavior |
| Not currently assessed | Current operational behavior has not been assessed |

These statuses are not interchangeable. For example, a rule file may support an **Implemented** status without supporting **Validated** status.

Historical evidence may substantiate a past result without establishing that the same result can be reproduced in the current environment.

## 5. Evidence Collection Principles

When existing evidence is available, retain enough context to understand what it represents.

Relevant context may include:

- The associated detection or configuration
- The source of the event or alert
- The event timestamp, where recorded
- Relevant event fields
- The corresponding rule or alert identifier, where available
- The conditions under which the evidence was captured
- Known limitations affecting interpretation

Preserve the original meaning of historical records. Do not alter screenshots, event details, or test results in a way that changes what they demonstrate.

If evidence is incomplete, document the limitation rather than reconstructing missing information.

## 6. Screenshot and Artifact Handling

Screenshots and exported records should support a specific technical claim.

For each existing artifact, document the following where known:

| Field | Description |
|---|---|
| Artifact name | The actual filename in the repository |
| Associated detection | The detection or component the artifact supports |
| Evidence type | Configuration, telemetry, alert, validation, or historical |
| Observation context | What the artifact records |
| Date or time | The recorded observation time, when available |
| Limitations | Any relevant missing context or uncertainty |

Do not assign invented timestamps, test identifiers, or validation results to existing artifacts.

Redact credentials, access tokens, private keys, and unrelated sensitive information before committing evidence.

## 7. Interpreting Detection Results

A security event, a detection rule, and an alert represent different stages of the monitoring process.

- A Windows event records activity reported by the operating system or an associated event source.
- A detection rule defines conditions used to identify relevant event patterns.
- An alert records a detection outcome produced by the monitoring system.
- An investigation interprets the available evidence in context.

A matching alert should not automatically be described as confirmed malicious activity. Likewise, the absence of an alert does not independently prove that an activity was benign or that the detection pipeline was functioning correctly.

Interpret results in light of the available telemetry, configuration, rule conditions, and supporting records.

## 8. Evidence Integrity and Security

The repository should not contain:

- Passwords or authentication secrets
- API keys or access tokens
- Private keys or private certificates
- Unredacted credentials embedded in screenshots or configuration files
- Unnecessary personal or sensitive information

Keep evidence files associated with the relevant detection and preserve a clear distinction between original records and explanatory documentation.

## 9. Limitations and Reporting

Documentation should clearly distinguish established implementation details from historical observations and unverified behavior.

Do not claim:

- Successful validation without supporting records
- Current service availability based only on historical screenshots
- Detection accuracy or false-positive rates without measured results
- Complete telemetry coverage without supporting configuration and evidence
- Performance improvements without recorded measurements

When a claim cannot be established, state the limitation explicitly.

## 10. Review Checklist

Use this checklist when reviewing an existing detection document.

- [ ] The detection objective is clearly explained.
- [ ] The existing implementation is referenced accurately.
- [ ] The relevant telemetry source is identified where known.
- [ ] Expected detection behavior is described.
- [ ] Supporting evidence is linked where available.
- [ ] Validation status reflects the actual evidence.
- [ ] Known limitations are documented.
- [ ] No unsupported metrics or test results are claimed.
- [ ] Sensitive information has been removed or redacted.

This checklist is a documentation standard, not a statement that every detection has already passed review.

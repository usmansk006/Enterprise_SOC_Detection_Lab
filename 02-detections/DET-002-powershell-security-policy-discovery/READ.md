# DET-002 — PowerShell Security Policy Discovery Using Secedit

## Overview

DET-002 is a custom Wazuh detection designed to identify PowerShell activity involving the Windows `secedit` utility.

The detection was developed and tested in an isolated SOC laboratory environment using Windows PowerShell Script Block Logging and Wazuh.

`secedit` is a legitimate Windows utility used to configure and analyze security policies. However, security policy discovery may also be performed during system reconnaissance.

This detection demonstrates how PowerShell telemetry can be collected, analyzed, and converted into a custom detection for SOC investigation.

---

## Detection Summary

| Field              | Details                                            |
| ------------------ | -------------------------------------------------- |
| Detection ID       | DET-002                                            |
| Detection Name     | PowerShell Security Policy Discovery Using Secedit |
| Detection Type     | Custom Wazuh Detection                             |
| Platform           | Windows                                            |
| Telemetry Source   | PowerShell Script Block Logging                    |
| Windows Event ID   | 4104                                               |
| Log Channel        | Microsoft-Windows-PowerShell/Operational           |
| Detection Platform | Wazuh                                              |
| Detection Category | Security Policy Discovery                          |
| Test Environment   | Isolated SOC Lab                                   |

---

## Detection Objective

The objective of this detection is to identify PowerShell activity involving the Windows `secedit` utility.

Security policy discovery can provide information about:

* Local security policy settings
* Password policies
* Account policies
* Security configuration
* System security settings

While `secedit` is a legitimate administrative utility, its execution should be evaluated within the context of the user, process, command, and surrounding activity.

---

## Threat Scenario

An attacker or administrator may use built-in Windows utilities to discover security configuration information.

PowerShell Script Block Logging provides visibility into PowerShell commands executed on the endpoint.

The detection focuses on identifying PowerShell script content involving:

```text
secedit
```

The activity may represent legitimate administration or security discovery.

Additional investigation is required to determine the intent.

---

## Detection Flow

```text
PowerShell Activity
        ↓
PowerShell Script Block Logging
        ↓
Windows Event ID 4104
        ↓
Wazuh Agent
        ↓
Wazuh Manager
        ↓
Custom Wazuh Rule
        ↓
Security Alert
        ↓
SOC Investigation
```

---

## Telemetry Source

### Primary Telemetry

**PowerShell Script Block Logging**

| Field       | Value                                    |
| ----------- | ---------------------------------------- |
| Log Channel | Microsoft-Windows-PowerShell/Operational |
| Event ID    | 4104                                     |
| Event Type  | PowerShell Script Block Logging          |
| Platform    | Windows                                  |

Windows Event ID `4104` records PowerShell script block activity when Script Block Logging is enabled.

This telemetry provides visibility into PowerShell commands and script content.

---

## Detection Logic

The detection identifies PowerShell telemetry containing activity associated with:

```text
secedit
```

The detection workflow is:

1. PowerShell activity occurs on the Windows endpoint.
2. PowerShell Script Block Logging records the activity.
3. Windows generates Event ID `4104`.
4. The Wazuh Agent collects the event.
5. Wazuh processes the PowerShell telemetry.
6. The custom detection logic identifies `secedit` activity.
7. A security alert is generated for investigation.

---

## Custom Detection

DET-002 uses a custom Wazuh rule.

The rule analyzes PowerShell Script Block Logging telemetry and identifies PowerShell activity involving the Windows `secedit` utility.

The custom detection was created to demonstrate:

* Detection engineering
* PowerShell telemetry analysis
* Custom Wazuh rule development
* Detection testing
* Troubleshooting
* Detection tuning
* Retesting

---

## Test Procedure

The detection was tested in the authorized laboratory environment.

### Step 1 — Generate PowerShell Activity

PowerShell activity involving `secedit` was executed on the monitored Windows endpoint.

### Step 2 — Validate Windows Telemetry

Confirm that Windows generated:

```text
Event ID: 4104
Log Channel: Microsoft-Windows-PowerShell/Operational
```

### Step 3 — Validate Wazuh Collection

Confirm that the Wazuh Agent collected the PowerShell telemetry.

### Step 4 — Validate Detection

Confirm that the custom Wazuh rule processed the telemetry and generated an alert.

### Step 5 — Investigate the Alert

Review the following:

* PowerShell script content
* Command execution context
* User account
* Endpoint
* Timestamp
* Related process activity

---

## Evidence

The detection should be supported by evidence collected during testing.

Recommended evidence includes:

### 1. Test Execution

Shows the PowerShell activity executed in the lab.

```text
evidence/DET-002-01-test-execution.png
```

---

### 2. PowerShell Telemetry

Shows Windows PowerShell Script Block Logging.

```text
evidence/DET-002-02-powershell-event-4104.png
```

---

### 3. Wazuh Detection Alert

Shows the custom Wazuh detection alert.

```text
evidence/DET-002-03-wazuh-alert.png
```

---

### 4. Custom Detection Rule

Shows the custom Wazuh rule used for the detection.

```text
evidence/DET-002-04-custom-rule.png
```

---

## Investigation Considerations

When investigating this activity, an analyst should determine:

* Which user executed the PowerShell command?
* Which endpoint generated the event?
* What PowerShell content was executed?
* Was `secedit` used for legitimate administration?
* Was the activity expected?
* Were additional discovery commands executed?
* Did suspicious activity occur before or after the event?

The presence of `secedit` alone does not confirm malicious activity.

---

## Threat Hunting Opportunities

This detection can be expanded into a broader hunt for security discovery activity.

Potential hunt questions include:

> Are additional PowerShell commands being used for system or security discovery?

> Is the same user executing multiple discovery commands?

> Is PowerShell being used with other built-in Windows utilities?

> Does the activity occur on multiple endpoints?

> Is the activity followed by credential access, persistence, or other suspicious behavior?

---

## False Positives

Legitimate causes may include:

* System administration
* Security auditing
* Compliance checks
* Security policy analysis
* Troubleshooting
* Configuration validation

Analysts should determine whether the activity is expected in the environment.

---

## Detection Limitations

This detection has several limitations:

* `secedit` is a legitimate Windows utility.
* The detection does not independently determine malicious intent.
* PowerShell Script Block Logging must be enabled.
* Event ID `4104` must be collected by the Wazuh Agent.
* The detection may not identify `secedit` activity executed outside the monitored PowerShell telemetry.
* Additional endpoint and process telemetry may be required for complete investigation.

---

## Tuning Considerations

Potential tuning improvements include:

* Reviewing the specific `secedit` command arguments.
* Identifying expected administrative users.
* Identifying expected administrative endpoints.
* Correlating PowerShell activity with process creation telemetry.
* Excluding known legitimate automation.
* Monitoring repeated security discovery activity.

Tuning should reduce unnecessary alerts without removing visibility into potentially suspicious behavior.

---

## Retest Results

The detection lifecycle was validated after troubleshooting and tuning.

```text
PowerShell Activity
        ↓
Event ID 4104 Generated
        ↓
Wazuh Agent Collection
        ↓
Custom Detection Processing
        ↓
Alert Generated
        ↓
Investigation
```

**Retest Result: Successful**

---

## Detection Lifecycle

```text
ACTIVITY
        ↓
TELEMETRY
PowerShell Event ID 4104
        ↓
DETECT
Custom Wazuh Rule
        ↓
INVESTIGATE
Review Script Content and Context
        ↓
HUNT
Search for Related Discovery Activity
        ↓
RESPOND
Determine Whether Activity Is Authorized
        ↓
IMPROVE
Tune Detection Logic
        ↓
RETEST
Validate Detection
```

---

## Detection Status

| Validation Stage     | Result     |
| -------------------- | ---------- |
| Test Execution       | Successful |
| PowerShell Telemetry | Successful |
| Wazuh Collection     | Successful |
| Custom Detection     | Successful |
| Alert Investigation  | Successful |
| Retest               | Successful |

**Final Status: DET-002 Successfully Validated**

---

## Conclusion

DET-002 demonstrates the development of a custom Wazuh detection using PowerShell Script Block Logging.

The detection identifies PowerShell activity involving the Windows `secedit` utility and provides visibility for SOC investigation.

The project demonstrates the complete detection engineering lifecycle:

```text
Activity
→ Telemetry
→ Detection
→ Investigation
→ Troubleshooting
→ Tuning
→ Retesting
→ Validation
```

The detection does not classify `secedit` activity as malicious by default. The activity must be evaluated using surrounding context and related telemetry.

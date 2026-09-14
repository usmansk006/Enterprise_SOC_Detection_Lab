# INV-001 — Initial Triage

## Triage Objective

The purpose of the initial triage was to assess the Wazuh alert, determine why the activity was suspicious, and identify the information required for further investigation.

At this stage, the activity was not classified as malicious or benign.

---

## Alert Summary

Wazuh generated an alert for PowerShell execution using the `-EncodedCommand` parameter on the monitored Windows endpoint.

The alert was associated with:

| Field | Value |
|---|---|
| Rule ID | 100105 |
| Rule Level | 10 |
| Endpoint | WIN10-LAB |
| MITRE ATT&CK | T1059.001 |
| Technique | PowerShell |
| Tactic | Execution |

---

## Why the Activity Required Investigation

The use of the `-EncodedCommand` parameter can obscure the underlying PowerShell command.

Encoded PowerShell execution is commonly investigated because attackers may use command encoding to reduce command visibility and obscure malicious activity.

However, encoded PowerShell execution alone does not confirm malicious behavior.

Further analysis was required to determine the actual command content and execution context.

---

## Initial Observations

The following information was available during triage:

- A PowerShell-related Wazuh alert was generated.
- The detection was mapped to MITRE ATT&CK technique `T1059.001`.
- The alert identified encoded PowerShell execution.
- The monitored endpoint was `WIN10-LAB`.

The initial alert did not independently establish whether the underlying command was malicious.

---

## Initial Severity Assessment

### Initial Assessment: Medium

The activity required investigation because encoded PowerShell execution can be associated with malicious execution and command obfuscation.

The severity was treated as an initial assessment and was subject to change based on:

- Command-line analysis
- Decoded command content
- Process context
- Parent process analysis
- Related endpoint activity
- Investigation scoping

---

## Investigation Questions

The following questions were defined during triage:

1. What exact PowerShell command was executed?
2. What user executed the process?
3. What process launched PowerShell?
4. What was the decoded command content?
5. Did the PowerShell process create additional activity?
6. Did the process terminate normally?
7. Were additional encoded PowerShell executions observed?
8. Does the available evidence indicate malicious or authorized activity?

---

## Triage Decision

The alert was escalated for endpoint telemetry analysis.

The next investigation stage was to review Sysmon process creation telemetry to identify the PowerShell process and obtain the complete command-line context.

---

## Triage Status

**Status:** Escalated for Investigation

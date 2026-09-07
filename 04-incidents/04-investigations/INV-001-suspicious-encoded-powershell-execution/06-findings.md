# INV-001 — Findings

## Investigation Findings

This document records the confirmed findings and final assessment for INV-001.

---

# 1. Confirmed Facts

The investigation confirmed the following:

1. Wazuh generated an alert using detection rule `100105`.
2. The alert was mapped to MITRE ATT&CK technique `T1059.001 — PowerShell`.
3. Sysmon Event ID 1 recorded the creation of a PowerShell process.
4. The PowerShell process used the `-EncodedCommand` parameter.
5. The process executed under the user account `DESKTOP-Q9TN2GI\labadmin`.
6. The encoded command was decoded without executing the decoded content.
7. The decoded command was:

```powershell
Write-Output "detcon PowerShell Test"
````

8. Sysmon Event ID 5 recorded termination of the same PowerShell process.
9. The process creation and termination events were correlated using the same Process GUID.
10. The PowerShell process executed for approximately 388 milliseconds.
11. Scope analysis identified no additional related encoded PowerShell executions within the selected investigation timeframe and available Wazuh telemetry.

---

# 2. Technical Assessment

The Wazuh detection correctly identified PowerShell execution using the `-EncodedCommand` parameter.

The use of encoded PowerShell required investigation because command encoding can obscure the underlying command content.

After decoding and reviewing the command, the observed activity was determined to perform a simple output operation.

The available evidence did not identify malicious behavior associated with the decoded command.

---

# 3. Observations

The following observations were made during the investigation:

* The encoded PowerShell process was launched by another PowerShell process.
* The process executed for a very short duration.
* No additional related encoded PowerShell executions were identified during scope analysis.
* The activity occurred under the laboratory user account `labadmin`.

These observations provide context but should not independently be interpreted as proof of malicious or benign behavior.

---

# 4. Investigation Limitations

The investigation was limited to:

* Available Wazuh telemetry
* Available Sysmon telemetry
* The monitored Windows laboratory endpoint
* The selected investigation timeframe

The investigation cannot establish the absence of activity that was not collected by the available telemetry.

---

# 5. Final Verdict

## Verdict: Benign True Positive

The detection correctly triggered on PowerShell execution using the `-EncodedCommand` parameter.

The decoded command was:

```powershell
Write-Output "detcon PowerShell Test"
```

The command performed a harmless output operation and was associated with authorized laboratory testing.

Based on the available evidence, no malicious behavior was identified.

---

# 6. Confidence Assessment

**Confidence: High**

The final assessment is supported by:

* Wazuh alert telemetry
* Sysmon process creation telemetry
* Full command-line visibility
* Safe decoding of the encoded command
* Process termination correlation
* Scope analysis

---

# 7. Key Lesson

Encoded PowerShell execution should not automatically be classified as malicious.

An analyst must investigate the execution context, process telemetry, command content, related activity, and available evidence before assigning a final verdict.

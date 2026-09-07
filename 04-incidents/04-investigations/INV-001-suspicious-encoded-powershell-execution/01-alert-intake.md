# INV-001 — Alert Intake

## Alert Overview

This investigation was initiated after Wazuh generated an alert for suspicious PowerShell execution using an encoded command on the monitored Windows endpoint.

The alert was reviewed to determine whether the activity represented authorized testing, benign behavior, or potentially malicious execution.

---

## Alert Details

| Field | Value |
|---|---|
| Investigation ID | INV-001 |
| Alert Source | Wazuh |
| Rule ID | 100105 |
| Rule Level | 10 |
| Endpoint | WIN10-LAB |
| MITRE ATT&CK ID | T1059.001 |
| MITRE Tactic | Execution |
| MITRE Technique | PowerShell |

---

## Alert Timestamp

The Wazuh alert was observed on:

```text
Sep 5, 2026 @ 12:47:35
````

The endpoint telemetry uses UTC timestamps. Timestamp normalization and event correlation are documented later in the investigation timeline.

---

## Alert Trigger

The detection identified PowerShell execution using the following behavior:

```text
-EncodedCommand
```

Encoded PowerShell commands can obscure the underlying command content and are therefore relevant for investigation.

The presence of an encoded command alone does not confirm malicious activity.

---

## Initial Investigation Question

The primary question at alert intake was:

> What command was executed through PowerShell, and does the surrounding process activity indicate malicious behavior?

---

## Initial Evidence

The following evidence was collected during alert intake:

* Wazuh detection alert
* Detection rule metadata
* MITRE ATT&CK mapping


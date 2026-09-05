# DET-003 — Windows User Account Creation

## Overview

DET-003 detects the creation of a Windows user account using Windows Security Event ID `4720`.

Unauthorized account creation can indicate persistence, unauthorized administrative activity, or an attempt to maintain access to a compromised system.

This detection was developed and tested in an isolated Windows 10 lab monitored by Wazuh.

---

## Detection Summary

| Field          | Details                       |
| -------------- | ----------------------------- |
| Detection ID   | DET-003                       |
| Detection Name | Windows User Account Creation |
| Platform       | Windows 10                    |
| SIEM           | Wazuh                         |
| Data Source    | Windows Security Event Log    |
| Event ID       | 4720                          |
| Custom Rule ID | 100103                        |
| Severity       | Level 10                      |

---

## Detection Objective

The objective of this detection is to identify Windows user account creation events and generate an alert for SOC analyst investigation.

---

## Detection Flow

Windows User Account Created
↓
Windows Security Event ID 4720 Generated
↓
Wazuh Agent Collects Event
↓
Wazuh Custom Rule 100103 Matches Event
↓
SOC Alert Generated

---

## Lab Test

The detection was tested by creating a Windows user account in the isolated lab environment.

The activity generated:

* Windows Security Event ID `4720`
* A Wazuh alert
* Custom Rule ID `100103`

Additional Sysmon telemetry was collected to provide process execution context.

---

## Detection Result

The custom Wazuh rule successfully detected the Windows user account creation event.

The alert was classified as:

**True Positive — Authorized Lab Activity**

---

## MITRE ATT&CK

* **T1098 — Account Manipulation**

---

## Evidence

Supporting screenshots and evidence are available in the `evidence/` directory.

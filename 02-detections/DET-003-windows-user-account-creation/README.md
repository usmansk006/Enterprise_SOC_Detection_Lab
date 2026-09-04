# DET-003 — Windows User Account Creation Detection

## Overview

DET-003 detects the creation of a Windows user account using Windows Security Event ID 4720.

Unauthorized account creation can indicate persistence, unauthorized administrative activity, or an attacker establishing additional access to a compromised system.

This detection was developed and tested in an isolated Windows 10 lab environment monitored by Wazuh.

---

## Detection Summary

| Field | Details |
|---|---|
| Detection ID | DET-003 |
| Detection Name | Windows User Account Creation |
| Data Source | Windows Security Event Log |
| Event ID | 4720 |
| Platform | Windows 10 |
| SIEM | Wazuh |
| Custom Rule ID | 100103 |
| Severity | Level 10 |

---

## Detection Objective

The objective of this detection is to identify Windows user account creation events and generate a custom Wazuh alert for SOC analyst investigation.

---

## Detection Flow

```text
Windows User Account Created
        ↓
Windows Security Event ID 4720
        ↓
Wazuh Agent Collects Event
        ↓
Custom Wazuh Rule 100103
        ↓
SOC Alert Generated

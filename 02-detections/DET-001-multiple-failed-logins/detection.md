# DET-001 — Multiple Failed Windows Logins

## Overview

This detection identifies failed Windows authentication attempts
generated on the monitored Windows endpoint.

The detection uses Windows Security Event ID 4625, which is generated
when an account fails to log on.

Wazuh collects the Windows Security event from the endpoint, analyzes
the event using its detection rules, and generates a security alert
for investigation.

---

## Detection Objective

The objective of this detection is to identify suspicious or repeated
authentication failures that could indicate:

- Password guessing
- Brute-force activity
- Invalid credentials
- Unauthorized access attempts
- Misconfigured applications or services

---

## Lab Environment

| Component | Configuration |
|---|---|
| SIEM | Wazuh |
| Wazuh Server | Ubuntu Server |
| Endpoint | Windows 10 |
| Agent | Wazuh Agent |
| Event Source | Windows Security Log |
| Event ID | 4625 |
| Detection Type | Failed authentication |

---

## Detection Flow

```text
Windows Authentication Failure
            ↓
Windows Security Event 4625
            ↓
Wazuh Agent
            ↓
Wazuh Manager
            ↓
Wazuh Detection Rule
            ↓
Security Alert
            ↓
SOC Analyst Investigation

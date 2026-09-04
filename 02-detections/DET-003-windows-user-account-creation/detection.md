# DET-003 — Detection Engineering Documentation

## Detection Name

Windows User Account Creation

## Detection ID

DET-003

---

## Objective

Detect the creation of Windows user accounts and generate a custom Wazuh alert for SOC investigation.

Unauthorized account creation may indicate:

- Unauthorized administrative activity
- Persistence attempts
- Privilege abuse
- Creation of an attacker-controlled account

This detection does not determine whether the activity is malicious. It identifies the event so that an analyst can investigate it.

---

## Data Source

| Field | Value |
|---|---|
| Operating System | Windows 10 |
| Log Source | Windows Security Event Log |
| Event ID | 4720 |
| Event Provider | Microsoft-Windows-Security-Auditing |
| SIEM | Wazuh |
| Endpoint | WIN10-LAB |

---

## Telemetry

Windows Security Event ID 4720 is generated when a user account is created.

Important investigation fields include:

- `data.win.eventdata.subjectUserName`
- `data.win.eventdata.subjectDomainName`
- `data.win.eventdata.targetUserName`
- `data.win.eventdata.targetDomainName`
- `data.win.eventdata.targetSid`
- `data.win.system.eventID`
- `data.win.system.systemTime`

### Subject Account

The subject account identifies the user responsible for creating the new account.

Example:

```text
subjectUserName: labadmin

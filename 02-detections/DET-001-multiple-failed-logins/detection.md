# DET-001 — Detection Engineering

## Detection Name

Multiple Failed Windows Logins

## Detection Objective

Detect failed Windows authentication attempts that may indicate
password guessing, brute-force activity, invalid credentials, or
unauthorized access attempts.

## Data Source

Windows Security Event Log

## Windows Event ID

4625

Event ID 4625 indicates that an account failed to log on.

## Wazuh Detection

| Field | Value |
|---|---|
| Wazuh Rule ID | 60122 |
| Rule Level | 5 |
| Rule Description | Logon Failure - Unknown user or bad password |
| Rule Groups | windows, windows_security, authentication_failed |
| Agent ID | 001 |
| Agent Name | WIN10-LAB |
| Log Channel | Security |
| Windows Event ID | 4625 |

## Important Event Fields

The following fields were reviewed during investigation:

| Field | Observed Value |
|---|---|
| Target Username | labadmin |
| Event Channel | Security |
| Event ID | 4625 |
| Workstation | DESKTOP-Q9TN2GI |
| Authentication Package | Negotiate |
| Logon Process | User32 |
| Logon Type | 2 |
| Source Address | 127.0.0.1 |

## Detection Logic

The detection is based on Windows Security Event ID 4625.

A single failed authentication does not automatically indicate a
malicious attack.

Repeated authentication failures, especially when associated with
the same source address, multiple usernames, or suspicious timing,
should be investigated for possible brute-force or password-spraying
activity.

## Validation

The detection was successfully validated through the following
workflow:

1. A failed authentication event was generated on the Windows
   endpoint.
2. Windows generated Security Event ID 4625.
3. The Wazuh Agent collected the event.
4. Wazuh received the Windows security telemetry.
5. Wazuh Rule 60122 classified the event as a logon failure.
6. The event was investigated using the Wazuh event details.

## False Positive Considerations

Possible legitimate causes include:

- User entering an incorrect password
- Expired credentials
- Incorrect service credentials
- Applications using outdated credentials
- Scheduled tasks using invalid credentials
- Local authentication failures

Repeated or unusual authentication failures require additional
investigation.

## Detection Status

**Completed**

The detection was successfully generated, collected, detected,
and investigated in the laboratory environment.

# Detection Details — DET-001

## 1. Detection Objective

Detect failed Windows authentication attempts that may indicate invalid credentials, unauthorized access attempts, password guessing, or other suspicious authentication activity.

The detection identifies Windows Security Event ID `4625` and generates a Wazuh alert for SOC investigation.

---

## 2. Threat Behavior

Windows generates Event ID `4625` when an account fails to log on.

Authentication failures can occur for legitimate reasons. However, repeated failures may indicate suspicious activity.

Potential behaviors include:

* Incorrect password attempts
* Invalid usernames
* Password guessing
* Brute-force attempts
* Misconfigured applications
* Outdated service credentials

A single authentication failure does not independently confirm malicious activity.

---

## 3. Telemetry Source

### Primary Telemetry

**Windows Security Event Log**

| Field      | Value            |
| ---------- | ---------------- |
| Log Source | Windows Security |
| Event ID   | 4625             |
| Event Name | Failed Logon     |
| Platform   | Windows          |

Windows Event ID `4625` indicates that an account failed to log on.

---

## 4. Relevant Telemetry Fields

The following fields are important during detection and investigation:

```text
Target Username
Workstation Name
Authentication Package
Logon Process
Logon Type
Source Address
Event ID
Event Channel
```

### Observed Fields

| Field                  | Observed Value  |
| ---------------------- | --------------- |
| Target Username        | labadmin        |
| Event Channel          | Security        |
| Event ID               | 4625            |
| Workstation            | DESKTOP-Q9TN2GI |
| Authentication Package | Negotiate       |
| Logon Process          | User32          |
| Logon Type             | 2               |
| Source Address         | 127.0.0.1       |

---

## 5. Detection Platform

**Wazuh**

The Windows endpoint forwards Security Event telemetry through the Wazuh Agent.

The detection used a built-in Wazuh rule.

| Field            | Value                                        |
| ---------------- | -------------------------------------------- |
| Wazuh Rule ID    | 60122                                        |
| Rule Description | Logon Failure - Unknown user or bad password |
| Rule Level       | 5                                            |
| Detection Type   | Built-in Wazuh Rule                          |
| Agent ID         | 001                                          |
| Agent Name       | WIN10-LAB                                    |

---

## 6. Detection Logic

The detection identifies Windows Security Event ID `4625`.

Detection flow:

```text
Windows Authentication Failure
        ↓
Windows Security Event ID 4625
        ↓
Wazuh Agent Collects Event
        ↓
Wazuh Manager Processes Telemetry
        ↓
Wazuh Rule 60122
        ↓
Logon Failure Alert
```

The alert identifies a failed authentication event.

Additional correlation is required to determine whether repeated failures represent brute-force or password-guessing activity.

---

## 7. Detection Rule

The detection used the following Wazuh rule:

```text
Rule ID: 60122

Event Source:
Windows Security Log

Windows Event ID:
4625

Alert Description:
Logon Failure - Unknown user or bad password
```

This project validates a built-in Wazuh detection.

---

## 8. MITRE ATT&CK Relevance

Failed authentication activity may become relevant to password-guessing or brute-force behavior when multiple related authentication failures are observed.

However, the evidence collected for this detection documents a failed authentication event and does not independently prove a brute-force attack.

Therefore, a specific ATT&CK technique is not assigned based solely on the available evidence.

---

## 9. Test Procedure

The detection was tested in the authorized laboratory environment.

### Step 1 — Generate a Failed Authentication Attempt

A failed authentication attempt was generated on the Windows endpoint.

### Step 2 — Validate Windows Telemetry

Confirm that Windows generated:

```text
Event ID: 4625
Log Channel: Security
```

### Step 3 — Validate Wazuh Collection

Confirm that the Wazuh Agent collected the Windows Security event.

### Step 4 — Validate Detection

Confirm that Wazuh generated an alert using:

```text
Rule ID: 60122

Description:
Logon Failure - Unknown user or bad password
```

---

## 10. Evidence

The detection was validated using the following evidence.

### Windows Security Event

```text
evidence/DET-001-Windows-Event-4625.png
```

Shows Windows Security Event ID `4625`.

### Wazuh Event Details

```text
evidence/DET-001-Wazuh-event-details.png
```

Shows the event collected and processed by Wazuh.

### Wazuh Detection Rule

```text
evidence/DET-001-Wazuh-detection-rule.png
```

Shows Wazuh Rule `60122`.

---

## 11. Detection Validation

The following detection chain was successfully validated:

```text
Failed Authentication Attempt
        ↓
Windows Security Event ID 4625
        ↓
Wazuh Agent
        ↓
Wazuh Manager
        ↓
Rule 60122 Matched
        ↓
Alert Generated
```

---

## 12. False Positives

Potential legitimate causes include:

* Incorrect passwords
* Expired credentials
* Incorrect application credentials
* Service authentication failures
* Scheduled tasks using outdated credentials
* Local authentication activity

Authentication failures should be investigated within their operational context.

---

## 13. Detection Limitations

This detection has several limitations:

* A single Event ID `4625` does not prove malicious activity.
* The detection does not independently identify brute-force attacks.
* Additional correlation is required to identify repeated failures.
* Legitimate users can generate authentication failures.
* Source addresses require contextual analysis.
* Local activity may generate failed authentication events.

The observed source address in this lab was:

```text
127.0.0.1
```

This indicates local loopback activity.

---

## 14. Tuning Recommendations

Potential detection improvements include:

* Correlating multiple Event ID `4625` events.
* Monitoring repeated failures within a defined time window.
* Identifying multiple targeted usernames.
* Tracking repeated failures from the same source.
* Correlating failed Event ID `4625` events with successful Event ID `4624` events.
* Reviewing unusual logon types.

Tuning should be based on known legitimate authentication behavior.

---

## 15. Retest Results

The detection pipeline was successfully validated.

```text
Failed Authentication
        ↓
Windows Event ID 4625
        ↓
Wazuh Agent
        ↓
Wazuh Telemetry Processing
        ↓
Rule 60122 Matched
        ↓
Alert Generated
```

**Retest Result: Successful**

---

## 16. Detection Status

| Validation Stage     | Result     |
| -------------------- | ---------- |
| Test Execution       | Successful |
| Windows Telemetry    | Successful |
| Wazuh Collection     | Successful |
| Rule 60122 Detection | Successful |
| Alert Generation     | Successful |
| Retest               | Successful |

**Final Status: DET-001 Successfully Validated**

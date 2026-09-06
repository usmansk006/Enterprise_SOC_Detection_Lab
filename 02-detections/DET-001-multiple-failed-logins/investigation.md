# Investigation — DET-001

## 1. Investigation Objective

Investigate a Wazuh alert generated for a failed Windows authentication attempt.

The objective is to determine:

* Which account failed to authenticate
* Where the authentication occurred
* What source initiated the attempt
* What type of logon was attempted
* Whether the activity appears legitimate or suspicious
* Whether additional authentication events require investigation

---

## 2. Alert Summary

| Field             | Value                                        |
| ----------------- | -------------------------------------------- |
| Detection ID      | DET-001                                      |
| Detection Name    | Failed Windows Authentication                |
| Wazuh Rule ID     | 60122                                        |
| Alert Description | Logon Failure - Unknown user or bad password |
| Rule Level        | 5                                            |
| Endpoint          | WIN10-LAB                                    |
| Telemetry Source  | Windows Security Log                         |
| Windows Event ID  | 4625                                         |

The alert indicates that a Windows authentication attempt failed.

---

## 3. Initial Triage

### What happened?

A Windows authentication attempt failed.

Windows generated:

```text
Event ID: 4625
```

This event indicates that an account failed to log on.

### Where did it happen?

The event occurred on the monitored Windows endpoint:

```text
WIN10-LAB
```

### Which account was targeted?

The observed target username was:

```text
labadmin
```

### What was the source address?

The observed source address was:

```text
127.0.0.1
```

This is the local loopback address.

Therefore, the event does not by itself demonstrate an authentication attempt originating from an external network host.

---

## 4. Alert Details

| Field                  | Observed Value                |
| ---------------------- | ----------------------------- |
| Detection              | Failed Windows Authentication |
| Wazuh Rule ID          | 60122                         |
| Rule Level             | 5                             |
| Windows Event ID       | 4625                          |
| Agent ID               | 001                           |
| Agent Name             | WIN10-LAB                     |
| Log Channel            | Security                      |
| Target Username        | labadmin                      |
| Workstation            | DESKTOP-Q9TN2GI               |
| Authentication Package | Negotiate                     |
| Logon Process          | User32                        |
| Logon Type             | 2                             |
| Source Address         | 127.0.0.1                     |

---

## 5. Initial Assessment

A failed authentication event was successfully detected.

However, a single Windows Event ID `4625` does not automatically indicate:

* Brute-force activity
* Password spraying
* Credential compromise
* Unauthorized access

Additional context is required.

The event should be investigated together with related authentication activity.

---

## 6. Evidence Reviewed

The investigation used the following evidence.

### Windows Event Viewer

Windows Event Viewer confirmed the presence of:

```text
Windows Security Event ID 4625
```

Evidence:

```text
evidence/DET-001-Windows-Event-4625.png
```

---

### Wazuh Event Details

The Wazuh event confirmed that the Windows Security telemetry was collected and processed.

Evidence:

```text
evidence/DET-001-Wazuh-event-details.png
```

---

### Wazuh Detection Rule

Wazuh Rule `60122` classified the event as:

```text
Logon Failure - Unknown user or bad password
```

Evidence:

```text
evidence/DET-001-Wazuh-detection-rule.png
```

---

## 7. Authentication Analysis

The failed authentication involved the account:

```text
labadmin
```

The analyst should determine:

* Whether the account exists
* Whether the user was expected to authenticate
* Whether the account experienced additional failures
* Whether successful authentication occurred after the failures
* Whether other accounts were targeted

A single failure provides limited information.

Repeated failures would increase the significance of the event.

---

## 8. Source Address Analysis

The observed source address was:

```text
127.0.0.1
```

This represents the local loopback interface.

The event should therefore be interpreted as local activity rather than automatically being considered an external authentication attempt.

Additional investigation should identify:

* The process involved
* Other local authentication activity
* Related Windows events
* Whether the activity was expected

---

## 9. Logon Type Analysis

The observed logon type was:

```text
Logon Type: 2
```

This information should be considered when determining how the authentication attempt occurred.

Authentication context should be reviewed alongside:

* Target account
* Source address
* Logon process
* Authentication package
* Related authentication events

---

## 10. Investigation Questions

The following questions should be answered during further investigation:

### Account Activity

* Was `labadmin` expected to authenticate?
* Did the account experience additional failed logons?
* Did successful authentication occur afterward?

### Source Activity

* Were other source addresses involved?
* Were multiple authentication failures generated?
* Was the activity local or remote?

### Timing

* Did failures occur repeatedly?
* Did failures occur within a short time period?
* Was the activity outside normal usage patterns?

### Related Events

Investigate:

```text
Event ID 4625 — Failed Logon

Event ID 4624 — Successful Logon
```

Correlation between failed and successful authentication events can provide additional context.

---

## 11. Threat Hunting Opportunities

This detection can be expanded into authentication-focused threat hunting.

### Hunt Question 1

> Are there additional Event ID 4625 events on the endpoint?

### Hunt Question 2

> Are multiple usernames experiencing failed authentication attempts?

### Hunt Question 3

> Is the same source generating repeated authentication failures?

### Hunt Question 4

> Does a successful Event ID 4624 occur after repeated failures?

### Hunt Question 5

> Are authentication failures occurring during unusual time periods?

---

## 12. False Positive Analysis

Potential legitimate causes include:

* User entering an incorrect password
* Expired credentials
* Incorrect application credentials
* Misconfigured services
* Scheduled tasks using outdated credentials
* Local authentication failures

The event must be evaluated within the operational context.

---

## 13. Investigation Decision

Based on the available evidence, the activity was classified as:

```text
Suspicious Authentication Failure
```

### Confidence

```text
Low
```

### Reason

The event confirms a failed authentication attempt.

However:

* Only a single failed authentication event was documented.
* No repeated authentication failures were demonstrated.
* No evidence of password guessing was confirmed.
* The observed source address was `127.0.0.1`.
* The available evidence does not establish unauthorized access.

Additional correlated authentication events would be required to increase confidence.

---

## 14. Recommended Response

Because the available evidence does not confirm malicious activity, aggressive containment is not justified.

Recommended actions include:

* Search for additional Event ID 4625 events.
* Review authentication frequency.
* Identify targeted usernames.
* Review source addresses.
* Search for Event ID 4624 following failed authentication.
* Review related processes and network activity.
* Determine whether the authentication activity is expected.

---

## 15. Investigation Outcome

The investigation confirmed the following detection chain:

```text
Failed Authentication Attempt
        ↓
Windows Security Event ID 4625
        ↓
Wazuh Agent Collection
        ↓
Wazuh Rule 60122
        ↓
Alert Generated
        ↓
Authentication Context Reviewed
        ↓
Suspicious Activity Requires Additional Correlation
```

---

## 16. Lessons Learned

This investigation demonstrates that authentication alerts require correlation and context.

A failed authentication event alone does not prove an attack.

Effective authentication investigation requires analysis of:

* Target account
* Source address
* Logon type
* Authentication package
* Frequency of failures
* Multiple targeted accounts
* Successful logons following failures
* Related system activity

Detection identifies potentially suspicious activity.

Investigation determines whether the activity represents legitimate behavior, misconfiguration, or malicious activity.

---

## Final Status

| Investigation Stage          | Result                            |
| ---------------------------- | --------------------------------- |
| Alert Reviewed               | Completed                         |
| Windows Event Reviewed       | Completed                         |
| Account Reviewed             | Completed                         |
| Source Address Reviewed      | Completed                         |
| Logon Context Reviewed       | Completed                         |
| Related Event Considerations | Completed                         |
| Final Classification         | Suspicious Authentication Failure |
| Confidence                   | Low                               |

**DET-001 Investigation: Completed**

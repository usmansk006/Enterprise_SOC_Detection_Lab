# DET-001 — Investigation

## 1. Alert Summary

A Windows authentication failure was detected on the monitored
Windows endpoint.

The event was generated as Windows Security Event ID 4625 and was
collected by the Wazuh Agent.

Wazuh classified the event using Rule ID 60122:

> Logon Failure - Unknown user or bad password

---

## 2. Alert Details

| Field | Value |
|---|---|
| Detection | Multiple Failed Windows Logins |
| Wazuh Rule ID | 60122 |
| Rule Level | 5 |
| Windows Event ID | 4625 |
| Agent ID | 001 |
| Agent Name | WIN10-LAB |
| Log Channel | Security |
| Target Username | labadmin |
| Workstation | DESKTOP-Q9TN2GI |
| Authentication Package | Negotiate |
| Logon Process | User32 |
| Logon Type | 2 |
| Source Address | 127.0.0.1 |

---

## 3. Initial Triage

### What happened?

A Windows authentication attempt failed.

Windows generated Security Event ID 4625, which indicates that an
account failed to log on.

### Where did it happen?

The event originated from the monitored Windows endpoint:

`WIN10-LAB`

### What account was targeted?

The observed target username was:

`labadmin`

### What was the source address?

The event reported:

`127.0.0.1`

This is the local loopback address. Therefore, this particular event
does not by itself demonstrate that the failed authentication came
from an external network host.

---

## 4. Evidence Reviewed

The investigation was performed using three primary evidence sources.

### Windows Event Viewer

Windows Event Viewer confirmed the presence of Security Event ID 4625.

Evidence:

`evidence/DET-001-Windows-Event-4625.png`

### Wazuh Event Details

The Wazuh event document confirmed that the Windows security telemetry
was successfully collected by the Wazuh Agent.

Evidence:

`evidence/DET-001-Wazuh-event-details.png`

### Wazuh Detection Rule

Wazuh Rule 60122 classified the event as:

`Logon Failure - Unknown user or bad password`

Evidence:

`evidence/DET-001-Wazuh-detection-rule.png`

---

## 5. Investigation Analysis

The observed event confirms a failed authentication attempt.

However, a single Event ID 4625 should not automatically be classified
as a brute-force attack.

Additional evidence is required before determining whether the activity
is malicious.

The following factors should be examined:

- Number of authentication failures
- Frequency of failures
- Source IP address
- Target usernames
- Authentication type
- Successful logons following failures
- Related Windows security events
- Process activity
- Network activity
- Activity occurring before and after the alert

---

## 6. False Positive Assessment

Potential legitimate explanations include:

- Incorrect password entered by a user
- Expired credentials
- Incorrect credentials stored by an application
- Service authentication failure
- Scheduled task using outdated credentials
- Local authentication failure

Because the observed source address is `127.0.0.1`, local activity
should be considered during further investigation.

---

## 7. Analyst Assessment

### Classification

**Suspicious authentication failure — requires additional investigation**

### Confidence

**Low**

### Reason

The event confirms an authentication failure, but the available
evidence does not establish a confirmed brute-force attack or
unauthorized access attempt.

Additional correlated events would be required to increase confidence.

---

## 8. Recommended Next Steps

If additional authentication failures are observed, the following
investigation should be performed:

1. Identify the total number of Event ID 4625 events.
2. Determine whether the failures occur repeatedly within a short
   time period.
3. Identify the source IP address for each event.
4. Check whether multiple usernames are being targeted.
5. Search for successful Event ID 4624 logons following the failures.
6. Review the associated logon types.
7. Investigate related process and network activity.
8. Determine whether the activity is expected or unauthorized.

---

## 9. MITRE ATT&CK Relevance

The activity may be relevant to the MITRE ATT&CK credential access
and brute-force categories if repeated authentication failures are
identified.

A specific ATT&CK technique should only be assigned after the observed
behavior provides sufficient evidence.

---

## 10. Final Conclusion

The SOC laboratory successfully detected and collected a Windows
authentication failure.

The event was confirmed in Windows Event Viewer and subsequently
identified in Wazuh using Rule 60122.

The current evidence is insufficient to classify the activity as a
confirmed brute-force attack.

The detection is therefore classified as a suspicious authentication
failure requiring additional investigation.

This investigation demonstrates the SOC workflow:

**Detect → Triage → Investigate → Assess → Document**

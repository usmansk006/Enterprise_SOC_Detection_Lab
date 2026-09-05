# DET-003 — Investigation Guide

## Investigation Overview

This document describes the investigation process for DET-003: Windows User Account Creation.

The purpose of this investigation is to determine who created the account, which account was created, how the account was created, and whether the activity was authorized.

Unauthorized account creation may indicate persistence, unauthorized administrative activity, or an attacker attempting to maintain access to a compromised system.

---

## 1. Initial Alert Triage

The investigation begins by reviewing the Wazuh alert.

The analyst should verify:

* Alert timestamp
* Endpoint name
* Agent ID
* Rule ID
* Rule severity
* Windows Event ID
* Account responsible for the action
* Newly created account

The alert generated during testing contained:

* Agent: `WIN10-LAB`
* Rule ID: `100103`
* Rule Level: `10`
* Event ID: `4720`

The alert confirmed that a Windows user account creation event occurred.

The initial investigation question is:

**What happened, on which system, and who performed the action?**

---

## 2. Identify the Affected Endpoint

The Wazuh alert identified the affected endpoint.

During the lab test:

* Endpoint: `WIN10-LAB`
* Operating System: Windows 10
* Agent ID: `001`

The endpoint information helps the analyst identify where the activity occurred.

In a production environment, the analyst should determine the role and importance of the affected system.

For example:

* User workstation
* Administrator workstation
* Server
* Domain controller
* Critical infrastructure system

---

## 3. Identify the Account That Created the User

Windows Security Event ID `4720` contains information about the account responsible for creating the new user.

Relevant fields include:

* `data.win.eventdata.subjectUserName`
* `data.win.eventdata.subjectDomainName`
* `data.win.eventdata.subjectUserSid`
* `data.win.eventdata.subjectLogonId`

During the lab test, the account responsible for the action was:

* Account Name: `labadmin`
* Domain: `DESKTOP-Q9TN2GI`

The investigation should determine whether the account performing the action was authorized to create user accounts.

Important questions include:

* Is the account an administrator?
* Is the account expected to create users?
* Was the activity performed during normal working hours?
* Is the account compromised?
* Are there other suspicious activities associated with the account?

---

## 4. Identify the Newly Created Account

Event ID `4720` also contains information about the newly created account.

Relevant fields include:

* `data.win.eventdata.targetUserName`
* `data.win.eventdata.targetDomainName`
* `data.win.eventdata.targetSid`
* `data.win.eventdata.samAccountName`

During the lab test, the newly created account was:

`DEt003-TestUser`

The analyst should determine whether the new account is legitimate.

Questions to investigate include:

* Is the account expected?
* Was the account requested or approved?
* Does the account name follow organizational naming conventions?
* Does the account have elevated privileges?
* Was the account created by an authorized administrator?

---

## 5. Review Account Attributes

Event ID `4720` provides additional information about the newly created account.

The analyst should review:

* User Account Control settings
* Account status
* Password settings
* Account expiration
* Primary group
* Account domain

During the investigation, these fields should be reviewed for suspicious configurations.

Examples of suspicious account configurations include:

* Password not required
* Account configured to never expire
* Unexpected administrative privileges
* Disabled logging or auditing
* Accounts created outside normal procedures

Account attributes should always be evaluated using organizational context.

---

## 6. Investigate Process Execution Context

Windows Security Event ID `4720` confirms that the account was created.

However, it does not provide complete information about the process used to create the account.

Additional Sysmon telemetry was reviewed to identify the process execution.

Sysmon Event ID `1` recorded process creation activity.

Relevant fields included:

* Process image
* Parent process
* Command line
* Parent command line
* Executing user
* Process ID
* Process GUID
* File hash

During the lab test, the account creation was associated with:

* Parent Process: `net.exe`
* Child Process: `net1.exe`
* Executing User: `labadmin`

The command executed was:

`net user DEt003-TestUser2 Password123! /add`

This telemetry provided process-level context for the account creation event.

---

## 7. Correlate Security and Sysmon Events

The investigation correlated multiple data sources.

### Windows Security Event

Windows Security Event ID `4720` confirmed that a user account was created.

### Sysmon Process Creation Event

Sysmon Event ID `1` provided information about the process responsible for the activity.

The correlation between these events showed the following sequence:

Process Execution
↓
`net.exe` executed
↓
User creation command executed
↓
`net1.exe` process activity recorded
↓
Windows Security Event ID `4720` generated
↓
Wazuh alert generated

This correlation provides stronger evidence than relying on a single event source.

---

## 8. Determine Whether the Activity Is Suspicious

Account creation should not automatically be classified as malicious.

The analyst must evaluate the activity using available evidence and environmental context.

During this lab test:

* The account creation was intentionally performed.
* The activity occurred in an isolated lab environment.
* The account was created by the lab administrator.
* The process command was known and expected.

Based on this information, the event was classified as:

**True Positive — Authorized Lab Activity**

---

## 9. Investigation Decision

The final investigation decision was:

**Classification: True Positive**

The detection correctly identified a real user account creation event.

**Disposition: Authorized Activity**

The activity was authorized because it was intentionally performed as part of the DET-003 detection test.

No incident response action was required.

---

## 10. Potential Response Actions

If the same activity occurred in a production environment and was determined to be unauthorized, potential response actions could include:

1. Disable the newly created account.
2. Preserve relevant logs and evidence.
3. Identify the account responsible for the creation.
4. Review the responsible account for signs of compromise.
5. Review account group memberships and privileges.
6. Search for additional accounts created during the same period.
7. Investigate related process execution activity.
8. Escalate the incident according to the organization's incident response procedures.

Response actions should depend on the organization's environment and incident response process.

---

## 11. Threat Hunting Opportunities

Following the investigation, a threat hunt can be performed to identify related activity.

Potential hunting questions include:

* Were other user accounts created recently?
* Were multiple accounts created by the same user?
* Did the same process create additional accounts?
* Were newly created accounts added to privileged groups?
* Did account creation occur outside normal working hours?
* Did other endpoints show similar activity?

Useful hunting telemetry includes:

* Windows Security Event ID `4720`
* Windows Security Event ID `4728`
* Windows Security Event ID `4732`
* Windows Security Event ID `4756`
* Sysmon Event ID `1`

This expands the investigation from a single alert into a broader search for related activity.

---

## 12. Investigation Conclusion

The investigation confirmed that a Windows user account was created on the monitored endpoint.

Windows Security Event ID `4720` provided evidence of the account creation.

The Wazuh custom rule `100103` successfully generated a Level 10 alert.

Sysmon Event ID `1` provided additional process execution context and identified the command used to create the account.

The investigation successfully correlated:

* Windows Security telemetry
* Wazuh detection data
* Sysmon process telemetry

The final classification was:

**True Positive — Authorized Lab Activity**

The event demonstrates the importance of correlating multiple telemetry sources during SOC investigations.

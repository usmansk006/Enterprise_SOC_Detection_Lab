# TH-001 — PowerShell Abuse: Hunting Methodology

## 1. Purpose

This document defines the repeatable methodology used to investigate potentially suspicious PowerShell activity within the Windows endpoint environment.

The methodology is designed to support proactive threat hunting rather than relying exclusively on existing Wazuh alerts.

The hunt follows:

```text
Hypothesis
    ↓
Telemetry Discovery
    ↓
PowerShell Identification
    ↓
Context Analysis
    ↓
Event Correlation
    ↓
Behavior Assessment
    ↓
Detection Coverage Review
    ↓
Detection Gap Analysis
```

---

## 2. Hunt Scope

### Primary Platform

Windows endpoint telemetry.

### Primary Data Sources

* Windows PowerShell Operational logs
* Sysmon
* Windows Security Event Logs
* Wazuh collected events and alerts

### Primary Behavior

Suspicious PowerShell execution.

### Primary ATT&CK Technique

**T1059.001 — Command and Scripting Interpreter: PowerShell**

The hunt may identify additional techniques when the observed behavior provides sufficient evidence for additional ATT&CK mappings.

---

## 3. Hunt Preparation

Before executing the hunt, confirm that the required telemetry sources are available.

The analyst should verify:

```text
Windows endpoint
      ↓
Wazuh Agent
      ↓
Wazuh Manager
      ↓
Relevant telemetry
```

The analyst should also identify the time range being investigated.

A consistent time window should be used when correlating events so that activity from different telemetry sources can be compared accurately.

---

## 4. Phase 1 — Identify PowerShell Activity

Search the available telemetry for PowerShell execution.

Primary process indicators include:

```text
powershell.exe
pwsh.exe
```

The search should consider both process-name and command-line telemetry.

Where available, process creation telemetry should be preferred for establishing execution context.

The analyst records:

* Timestamp
* Host
* User
* Process name
* Process ID
* Parent process
* Command line

---

## 5. Phase 2 — Examine Command-Line Activity

The command line is one of the most important sources of context.

Review for:

* Encoded commands
* Obfuscated arguments
* Download-related parameters
* Script execution
* Unusual execution policies
* Hidden execution
* Remote resource access
* Unexpected child-process creation

Examples of parameters requiring additional investigation include:

```text
-EncodedCommand
-NoProfile
-ExecutionPolicy Bypass
-WindowStyle Hidden
```

These indicators are not independently malicious.

They increase investigative priority when combined with other suspicious behavior.

---

## 6. Phase 3 — Examine the Parent Process

Determine which process launched PowerShell.

Represent the relationship as:

```text
Parent Process
      ↓
powershell.exe
```

Investigate whether the parent process is expected.

Examples of contexts requiring additional investigation may include:

* Office applications
* Script hosts
* Unknown executables
* Unexpected services
* Unusual administrative utilities

The analyst should validate the context rather than automatically classifying the parent process as malicious.

---

## 7. Phase 4 — Examine Child Processes

Identify processes launched by PowerShell.

Represent the relationship as:

```text
powershell.exe
      ↓
Child Process
```

Unexpected child processes may provide additional evidence about the purpose of the PowerShell execution.

Relevant information includes:

* Child process name
* Command line
* Execution time
* User
* Parent process
* Subsequent activity

---

## 8. Phase 5 — Examine User Context

Determine which account executed PowerShell.

The analyst should assess whether the account is expected to perform the observed activity.

Consider:

* Account type
* Administrative privileges
* Host ownership
* Expected administrative duties
* Time of execution
* Related authentication activity

An administrative account executing PowerShell is not inherently suspicious.

The significance depends on the complete execution context.

---

## 9. Phase 6 — Correlate PowerShell Telemetry

Correlate PowerShell-specific events with endpoint telemetry.

The correlation process should consider:

```text
PowerShell Event
      +
Sysmon Process Event
      +
Windows Security Event
      +
Wazuh Alert
      +
Related Network Activity
```

Not every source will contain information for every event.

The purpose of correlation is to establish a coherent activity timeline.

---

## 10. Phase 7 — Build the Activity Timeline

For potentially suspicious activity, construct a chronological sequence.

Example:

```text
T0 — User authentication
T1 — Parent process starts
T2 — PowerShell starts
T3 — Command executes
T4 — Child process starts
T5 — Network/file activity occurs
T6 — Related Wazuh alert generated
```

The actual sequence must be based on observed telemetry.

Do not create events merely to complete the timeline.

---

## 11. Phase 8 — Investigate Encoded PowerShell

If encoded PowerShell is identified, record:

* Presence of encoded execution
* Associated command-line parameters
* User
* Host
* Timestamp
* Parent process
* Child processes
* Related telemetry

If the encoded content can be safely decoded within the isolated laboratory, the decoded content may be analyzed as additional evidence.

Decoded content should be treated as evidence and not automatically interpreted as malicious without contextual validation.

---

## 12. Phase 9 — Investigate Related Network Activity

Where network telemetry is available, investigate whether PowerShell activity corresponds with network communication.

Potentially relevant observations include:

* Outbound connections
* DNS requests
* Connections to unusual destinations
* Download activity
* Remote service communication

Network activity should be correlated by:

* Host
* Process
* Timestamp
* Destination
* User context

A network connection alone does not establish malicious PowerShell activity.

---

## 13. Phase 10 — Review Wazuh Detection Coverage

After identifying potentially suspicious PowerShell activity, determine whether Wazuh generated a corresponding detection.

The analyst should compare:

```text
Observed Behavior
        ↓
Available Telemetry
        ↓
Wazuh Detection
```

Possible outcomes:

### Detection Generated

The activity was identified by an existing rule.

Evaluate:

* Alert accuracy
* Severity
* Available context
* ATT&CK mapping
* Triage usefulness
* Potential false positives

### Telemetry Present but No Detection

The behavior is visible in telemetry but did not trigger a relevant detection.

This may indicate a detection gap.

### Detection Generated but Insufficient

The alert exists but lacks information required for efficient investigation.

This may indicate a context or enrichment gap.

### Telemetry Missing

The required evidence is unavailable.

This indicates a visibility or telemetry-collection gap.

---

## 14. Phase 11 — Assess the Behavior

The analyst should classify the investigation based on available evidence.

Possible assessment categories:

```text
Benign
Suspicious
Malicious
Inconclusive
```

The assessment must be supported by evidence.

The presence of PowerShell alone is insufficient for a malicious classification.

---

## 15. Phase 12 — False-Positive Analysis

The analyst should consider legitimate PowerShell activity such as:

* System administration
* Software deployment
* Configuration management
* Monitoring
* Automation
* Security tooling
* Maintenance scripts

Potentially suspicious activity should be compared against known legitimate administrative patterns where available.

Detection logic should avoid creating broad rules that alert on all PowerShell execution.

---

## 16. Phase 13 — Detection Gap Analysis

The hunt determines whether the observed behavior is adequately covered.

The analyst evaluates four areas:

### Telemetry Coverage

Can the required activity be observed?

### Hunt Coverage

Can the activity be discovered through proactive searches?

### Detection Coverage

Does an automated detection identify the activity?

### Investigation Context

Does the resulting alert contain sufficient information for triage?

This creates the following model:

```text
Telemetry
   ↓
Hunting
   ↓
Detection
   ↓
Investigation
```

A weakness at any stage should be documented separately.

---

## 17. Phase 14 — Detection Engineering Handoff

When a validated detection gap is identified, document the requirement for the detection-engineering workflow.

The handoff should include:

```text
Hunt ID
Observed behavior
Telemetry source
Relevant fields
ATT&CK technique
Detection requirement
Expected legitimate behavior
Potential false positives
Validation requirements
```

The resulting work moves into:

```text
05-detection-engineering/
```

---

## 18. Evidence Requirements

Evidence should be collected only when relevant to the finding.

Potential evidence includes:

```text
PowerShell event
Sysmon process event
Command line
Parent-child process relationship
User context
Authentication event
Network activity
Wazuh alert
```

Recommended naming format:

```text
TH-001-powershell-abuse-<evidence-type>.<extension>
```

Examples:

```text
TH-001-powershell-abuse-sysmon-process.png
TH-001-powershell-abuse-wazuh-alert.png
TH-001-powershell-abuse-command-line.png
```

Only evidence that actually exists should be committed to the repository.

---

## 19. Repeatability

The hunt should be executable repeatedly against the same telemetry sources.

A repeatable hunt requires:

* Defined hypothesis
* Defined telemetry
* Documented search logic
* Defined investigation fields
* Consistent assessment criteria
* Evidence conventions
* Detection-coverage assessment

This allows the hunt to be reused after detection changes.

---

## 20. Retesting

After detection engineering changes are implemented, the hunt should be repeated.

The retest evaluates:

```text
Original Hunt
     ↓
Detection Improvement
     ↓
Regression Testing
     ↓
Repeat Hunt
     ↓
Coverage Comparison
```

The objective is to determine whether the identified detection gap has been addressed without introducing unacceptable detection noise.

Actual retest results must be documented only after the retest has been performed.

---

## 21. Methodology Completion Criteria

The methodology is complete when the analyst can:

* Identify PowerShell activity
* Examine command-line context
* Analyze parent-child relationships
* Review user context
* Correlate endpoint telemetry
* Construct an activity timeline
* Investigate encoded execution
* Correlate network activity where available
* Assess Wazuh detection coverage
* Identify telemetry and detection gaps
* Document evidence
* Initiate detection-engineering improvements
* Repeat the hunt after changes

This methodology provides a consistent operational process for investigating PowerShell abuse throughout the SOC Detection Lab.

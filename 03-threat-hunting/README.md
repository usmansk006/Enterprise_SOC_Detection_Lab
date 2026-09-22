# Threat Hunting

## 1. Overview

The `03-threat-hunting/` section implements the proactive threat hunting capability of the Enterprise SOC Detection Lab.

Threat hunting extends the SOC beyond alert-driven monitoring by systematically searching available telemetry for suspicious activity that may be:

* Undetected by existing detection rules
* Below alert thresholds
* Misclassified or insufficiently correlated
* Associated with legitimate tools used in suspicious ways
* Indicative of attacker behavior that has not yet produced a high-confidence alert

The hunting process is hypothesis-driven and follows an operational lifecycle:

```text
Threat Intelligence / ATT&CK
            ↓
      Hunt Hypothesis
            ↓
       Data Sources
            ↓
       Hunt Queries
            ↓
     Evidence Collection
            ↓
    Analyst Investigation
            ↓
     Findings / Assessment
            ↓
 Detection Gap Identification
            ↓
 Detection Engineering
            ↓
       Retesting
```

The objective is to demonstrate practical threat-hunting capability across endpoint, identity, process, PowerShell, and network telemetry.

---

## 2. Objectives

This section demonstrates the ability to:

* Develop threat-hunting hypotheses
* Identify appropriate telemetry sources
* Translate attacker behaviors into observable indicators
* Construct repeatable hunting queries
* Search Wazuh and endpoint telemetry
* Analyze Windows and Sysmon events
* Investigate suspicious process and command-line activity
* Hunt for credential abuse and persistence
* Investigate potential lateral-movement activity
* Analyze suspicious network behavior
* Map hunting activity to MITRE ATT&CK
* Document evidence and findings
* Identify visibility and detection gaps
* Convert validated hunting findings into detection-engineering requirements
* Retest the environment after detection improvements

---

## 3. Threat-Hunting Philosophy

Threat hunting in this laboratory is not based on randomly searching logs.

Each hunt follows a defined hypothesis.

A hunt begins with a question such as:

> Could an attacker abuse PowerShell in a way that is not currently detected by the existing detection rules?

The analyst then determines:

1. What behavior would be observable?
2. Which telemetry sources could contain that evidence?
3. Which fields are relevant?
4. What query or search logic can identify the behavior?
5. What would constitute suspicious activity?
6. What legitimate activity could create the same telemetry?
7. What additional evidence is required for validation?
8. Does the existing detection capability identify the behavior?
9. If not, what detection gap exists?

This approach makes hunting repeatable and operationally useful.

---

## 4. Hunt Lifecycle

Every documented hunt follows a consistent lifecycle.

### Phase 1 — Hypothesis

Define the attacker behavior being investigated.

Example:

```text
An adversary may abuse PowerShell for execution while attempting
to avoid existing detection logic.
```

### Phase 2 — ATT&CK Mapping

Identify the relevant MITRE ATT&CK technique or sub-technique.

Examples include:

* PowerShell
* Command and Scripting Interpreter
* Credential Access
* Scheduled Task/Job
* Account Manipulation
* Remote Services
* Process Discovery

The exact technique mapping is documented within each individual hunt.

### Phase 3 — Data-Source Identification

Determine which telemetry sources can support the hunt.

Potential sources include:

* Wazuh alerts
* Windows Security Event Logs
* Sysmon
* PowerShell operational logs
* Process creation telemetry
* Authentication events
* Network telemetry
* DNS activity
* File and persistence telemetry

### Phase 4 — Query Development

Develop a repeatable query or search procedure that can identify the behavior.

Queries are stored separately under:

```text
queries/
├── wazuh/
├── windows/
├── sysmon/
└── network/
```

This separation allows hunting logic to be reused and refined independently from the narrative hunt documentation.

### Phase 5 — Evidence Collection

Relevant events and supporting artifacts are preserved under:

```text
evidence/
```

Evidence should contain enough context to support the analyst's conclusion without unnecessarily storing sensitive information.

### Phase 6 — Investigation

Potential findings are investigated using surrounding telemetry.

The analyst considers:

* Timestamp
* Host
* User
* Process
* Parent process
* Command line
* Authentication context
* Network connections
* Related events
* Event sequence
* Expected baseline behavior

### Phase 7 — Assessment

The analyst determines whether the observed activity is:

* Benign
* Suspicious
* Malicious
* Inconclusive

The assessment must be supported by documented evidence.

### Phase 8 — Detection Gap Analysis

The hunt determines whether existing detection coverage successfully identifies the behavior.

Possible outcomes include:

```text
Hunt Finding
     ↓
Existing Detection Works
     │
     └── Validate / Tune / Retest

OR

Hunt Finding
     ↓
Detection Gap
     │
     └── Detection Engineering
             ↓
          New Rule
             ↓
          Testing
             ↓
          Regression Testing
```

---

## 5. Hunt Categories

The laboratory contains hunts covering several major attacker behaviors.

### TH-001 — PowerShell Abuse

Investigates suspicious PowerShell execution and command-line behavior.

Primary telemetry:

* PowerShell operational logs
* Sysmon process creation
* Windows process telemetry
* Wazuh events

Relevant ATT&CK coverage may include:

* T1059.001 — PowerShell

---

### TH-002 — Credential Abuse

Investigates suspicious authentication and credential-related behavior.

Potential telemetry includes:

* Windows Security events
* Authentication failures
* Account activity
* Process activity
* Related endpoint telemetry

The hunt evaluates both individual events and behavioral patterns.

---

### TH-003 — Persistence

Investigates common persistence mechanisms visible through endpoint telemetry.

Potential areas include:

* Scheduled tasks
* Startup mechanisms
* Registry-based persistence
* Services
* Account-related persistence

The hunt correlates persistence-related activity with process and user context.

---

### TH-004 — Lateral Movement

Investigates activity potentially associated with movement between systems.

Potential telemetry includes:

* Authentication events
* Remote-service activity
* Process creation
* Network connections
* Account usage

The objective is to identify behavior that warrants additional investigation rather than treating every remote connection as malicious.

---

### TH-005 — Suspicious Processes

Investigates abnormal process execution and process relationships.

Key investigation fields include:

* Image name
* Parent process
* Command line
* User
* Process ID
* Creation timestamp
* Child processes

Sysmon process-creation telemetry is particularly useful for this hunt.

---

### TH-006 — Network Activity

Investigates suspicious network behavior using available network and endpoint telemetry.

Potential hunting areas include:

* Unusual outbound connections
* Suspicious destinations
* DNS activity
* Unexpected communication patterns
* Endpoint-to-network relationships

Where network telemetry is available, findings are correlated with endpoint activity.

---

## 6. Hunt Documentation Standard

Every hunt directory follows a consistent structure.

Example:

```text
TH-001-powershell-abuse/
├── README.md
├── hypothesis.md
├── methodology.md
├── queries.md
├── findings.md
├── mitre-mapping.md
└── evidence/
```

The exact supporting files may vary depending on the hunt.

Each hunt should clearly document:

```text
Hunt ID
Hunt Name
Objective
Hypothesis
ATT&CK Mapping
Data Sources
Hunt Methodology
Queries
Expected Observations
Investigation Process
Evidence
Findings
Detection Coverage
Detection Gaps
Recommendations
Retest Requirements
```

---

## 7. Query Organization

Reusable hunting logic is maintained separately from individual hunt narratives.

```text
queries/
├── wazuh/
│   └── *.md
├── windows/
│   └── *.md
├── sysmon/
│   └── *.md
└── network/
    └── *.md
```

This structure supports:

* Query reuse
* Query refinement
* Consistent hunting procedures
* Cross-hunt analysis
* Detection-engineering handoff

Queries should include sufficient context to explain:

* Data source
* Fields searched
* Search conditions
* Expected results
* Interpretation
* Limitations

---

## 8. Evidence Management

Hunting evidence is stored separately from the hunt narrative.

```text
03-threat-hunting/evidence/
```

Evidence may include:

* Relevant event records
* Screenshots
* Exported log samples
* Query output
* Timeline excerpts
* Supporting investigation artifacts

Evidence filenames should use a predictable convention.

Example:

```text
TH-001-powershell-abuse-wazuh-results.png
TH-001-powershell-abuse-sysmon-events.png
TH-002-credential-abuse-auth-events.png
```

Evidence should never contain:

* Passwords
* Authentication secrets
* API keys
* Private tokens
* Unnecessary personal information
* Sensitive production data

---

## 9. Detection Engineering Integration

Threat hunting is directly connected to the detection-engineering lifecycle.

A hunt can produce one of three important outcomes:

### Existing Detection Confirmed

The behavior is already detected adequately.

The analyst validates the existing rule and identifies whether tuning or additional coverage is required.

### Existing Detection Requires Improvement

The behavior generates telemetry but the current detection has limitations.

The result is passed to detection engineering for refinement.

### Detection Gap Identified

The behavior is observable but is not adequately detected.

The finding becomes a detection-engineering requirement.

```text
Threat Hunt
    ↓
Behavior Observed
    ↓
Detection Coverage Review
    ↓
┌───────────────────────────────┐
│ Existing detection sufficient │
│ Existing detection needs tune │
│ Detection gap identified      │
└───────────────────────────────┘
                ↓
       Detection Engineering
                ↓
             Testing
                ↓
        Regression Testing
                ↓
             Retest
```

This creates a continuous feedback loop between hunting and detection engineering.

---

## 10. MITRE ATT&CK Integration

Hunts are mapped to the relevant MITRE ATT&CK techniques and sub-techniques where applicable.

The mapping provides a common language for describing adversary behavior and allows the laboratory to connect:

```text
ATT&CK Technique
       ↓
Adversary Behavior
       ↓
Observable Telemetry
       ↓
Hunt Hypothesis
       ↓
Detection
       ↓
Investigation
       ↓
Response
```

ATT&CK mappings should be based on the actual behavior investigated rather than being added only for documentation purposes.

---

## 11. Hunting Quality Standards

A completed hunt should be:

* Hypothesis-driven
* Repeatable
* Evidence-based
* ATT&CK-mapped where applicable
* Supported by identifiable telemetry
* Clear about legitimate alternatives
* Explicit about limitations
* Connected to detection coverage
* Capable of producing actionable findings

A hunt should not be considered complete merely because a query returns events.

The analyst must determine what those events mean in context.

---

## 12. Operational Workflow

The complete hunting workflow is:

```text
Threat Intelligence
        ↓
ATT&CK Technique
        ↓
Hunt Hypothesis
        ↓
Telemetry Identification
        ↓
Query Development
        ↓
Hunt Execution
        ↓
Evidence Collection
        ↓
Contextual Investigation
        ↓
Finding Assessment
        ↓
Detection Coverage Review
        ↓
Detection Gap Analysis
        ↓
Detection Engineering
        ↓
Testing
        ↓
Regression Testing
        ↓
Retest
        ↓
Continuous Improvement
```

This ensures threat hunting is integrated into the broader SOC operating model rather than functioning as an isolated activity.

---

## 13. Relationship to the Rest of the SOC Lab

The threat-hunting capability integrates with the other project components.

```text
01-lab
  │
  └── Telemetry Infrastructure
          ↓
02-detections
  │
  └── Existing Detection Coverage
          ↓
03-threat-hunting
  │
  ├── Proactive Discovery
  ├── Detection Validation
  └── Detection Gap Identification
          ↓
04-Incident-Investigations
  │
  └── Deeper Analysis
          ↓
05-detection-engineering
  │
  └── Detection Improvement
          ↓
06-incident-response
  │
  └── Response Procedures
```

The sections therefore form a connected operational system rather than independent demonstrations.

---

## 14. Expected Professional Outcome

This section demonstrates practical threat-hunting capability across endpoint, identity, process, PowerShell, and network telemetry.

It demonstrates the ability to:

* Think in terms of attacker behavior rather than isolated indicators
* Develop and test hunting hypotheses
* Work with multiple telemetry sources
* Perform contextual analysis
* Identify suspicious behavior
* Recognize detection limitations
* Translate hunting findings into detection requirements
* Support continuous detection improvement

The final objective is not simply to produce hunting queries.

The objective is to demonstrate a repeatable process for discovering potentially malicious behavior, validating the evidence, measuring detection coverage, and improving the SOC's ability to detect future activity.

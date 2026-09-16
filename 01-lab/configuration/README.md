# SOC Lab Configuration

## 1. Overview

The configuration layer documents the security-monitoring settings that control how the laboratory infrastructure collects telemetry, processes events, generates detections, and supports analyst workflows.

Configuration is separated from deployment documentation so that infrastructure provisioning and operational settings can be maintained independently.

This layer provides a structured reference for:

* Endpoint telemetry configuration
* Wazuh configuration
* Logging configuration
* Detection-related settings
* Network configuration
* Security controls
* Configuration validation
* Change management

---

## 2. Configuration Architecture

The configuration model can be represented as:

```text id="0u6r1b"
Infrastructure
      ↓
System Configuration
      ↓
Telemetry Configuration
      ↓
Wazuh Configuration
      ↓
Detection Configuration
      ↓
Validation
      ↓
SOC Operations
```

Each configuration layer contributes to the final security-monitoring capability.

---

## 3. Configuration Principles

The laboratory configuration follows these principles:

### Separation of Concerns

Infrastructure, telemetry, detection logic, and investigation evidence are maintained separately.

### Least Privilege

Services and accounts should receive only the permissions required for their intended purpose.

### Reproducibility

Important configuration decisions should be documented so that the environment can be recreated.

### Validation

Configuration changes should be tested before being treated as operational.

### Security

Credentials, tokens, private keys, and other secrets must never be committed to the public repository.

### Traceability

Significant configuration changes should be documented through version control and associated documentation.

---

## 4. Configuration Layers

The laboratory configuration is divided into the following layers:

```text id="c8e4vn"
┌──────────────────────────────┐
│ Infrastructure Configuration │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Endpoint Configuration       │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Telemetry Configuration      │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Wazuh Configuration          │
└──────────────┬───────────────┘
               ↓
┌──────────────────────────────┐
│ Detection Configuration      │
└──────────────────────────────┘
```

---

## 5. Endpoint Configuration

The Windows endpoint is configured to generate security telemetry required by the monitoring architecture.

Key configuration areas include:

* Windows Security Event Logging
* Sysmon
* PowerShell logging
* Wazuh Agent
* Relevant endpoint security settings

The endpoint configuration supports the telemetry requirements documented under:

```text id="7j3r2m"
docs/03-telemetry.md
```

---

## 6. Wazuh Agent Configuration

The Wazuh Agent is configured to communicate with the centralized Wazuh Manager and collect the required endpoint telemetry.

The configuration determines:

* Manager communication
* Agent identity
* Log sources
* Event collection
* Monitoring behavior
* Agent operational settings

Agent configuration should be reviewed whenever:

* A new telemetry source is added
* A detection requires additional event data
* Collection stops unexpectedly
* Endpoint architecture changes

---

## 7. Windows Security Logging Configuration

Windows Security Event Logs provide identity and operating-system security telemetry.

Configuration requirements should ensure that relevant security events are generated and available to the Wazuh Agent.

The project uses Windows security telemetry for scenarios involving:

* Authentication
* Account management
* Security-related activity

The required event categories should be validated through controlled testing rather than assumed to be available.

---

## 8. Sysmon Configuration

Sysmon configuration determines which endpoint activities are logged.

The configuration should provide sufficient visibility for:

* Process creation
* Parent-child process relationships
* Command-line activity
* File activity where configured
* Network activity where configured

Sysmon configuration should balance visibility and operational noise.

Overly broad collection can create unnecessary telemetry volume, while overly restrictive configuration can create detection blind spots.

---

## 9. PowerShell Logging Configuration

PowerShell logging is configured to provide visibility into script and command execution.

Relevant telemetry may include:

* PowerShell operational events
* Script execution
* Script block activity
* Command information
* Encoded-command activity

PowerShell telemetry supports detections and investigations involving suspicious PowerShell execution.

---

## 10. Wazuh Manager Configuration

The Wazuh Manager configuration controls centralized event processing and monitoring behavior.

Important configuration areas include:

* Agent communication
* Log collection
* Event processing
* Detection rules
* Alert generation
* Integration settings
* Monitoring behavior

Manager-specific documentation is maintained under:

```text id="p4w5my"
01-lab/infrastructure/wazuh/manager.md
```

---

## 11. Custom Detection Configuration

Custom Wazuh rules are maintained separately from general infrastructure configuration.

The repository location is:

```text id="f2v0v4"
05-detection-engineering/wazuh/rules/
```

This separation ensures that detection logic can be reviewed, tested, tuned, and version-controlled independently.

A detection rule should have:

```text id="1s9q3m"
Requirement
   ↓
Logic
   ↓
Test
   ↓
Validation
   ↓
Tuning
   ↓
Regression Test
```

---

## 12. Detection Configuration Standards

Detection configurations should clearly define:

* Detection objective
* Data source
* Relevant event fields
* Matching logic
* Severity
* ATT&CK mapping where applicable
* Expected behavior
* Validation method
* Known limitations

This creates consistency across detection scenarios.

---

## 13. Configuration Validation

Configuration should be validated at multiple levels.

### Syntax Validation

Confirm that configuration files are structurally valid.

### Service Validation

Confirm that affected services start and operate correctly.

### Telemetry Validation

Confirm that expected events are being generated and collected.

### Detection Validation

Confirm that expected test activity produces the intended alert.

### Regression Validation

Confirm that changes do not break existing detections.

The complete process is:

```text id="v8h0b2"
Configuration Change
       ↓
Syntax Check
       ↓
Service Validation
       ↓
Telemetry Validation
       ↓
Detection Test
       ↓
Regression Test
       ↓
Approved Configuration
```

---

## 14. Configuration Change Management

Configuration changes should follow a controlled process:

```text id="b2h9r4"
Identify Requirement
       ↓
Document Change
       ↓
Modify Configuration
       ↓
Validate
       ↓
Test
       ↓
Review
       ↓
Commit
       ↓
Monitor
```

Changes that affect detection behavior should also be reflected in the relevant detection-engineering documentation.

---

## 15. Troubleshooting Configuration Problems

When a configuration change causes unexpected behavior, troubleshooting should begin by identifying the affected layer.

```text id="a2p7vd"
Configuration
      ↓
Service
      ↓
Telemetry
      ↓
Processing
      ↓
Detection
      ↓
Dashboard
```

For example, if a detection stops triggering after a configuration change:

```text id="q0zq8v"
Check Rule
   ↓
Check Rule Loading
   ↓
Check Incoming Event
   ↓
Check Required Fields
   ↓
Check Event Parsing
   ↓
Check Alert Generation
```

This avoids changing multiple components simultaneously and makes troubleshooting more deterministic.

---

## 16. Configuration and Detection Engineering

Configuration is directly connected to detection engineering.

A detection can only be reliable when the telemetry required by its logic is consistently available.

The relationship is:

```text id="v6w7uk"
Detection Requirement
       ↓
Telemetry Requirement
       ↓
Endpoint Configuration
       ↓
Wazuh Collection
       ↓
Detection Rule
       ↓
Validation
```

This is why telemetry configuration must be considered part of detection engineering rather than a completely separate concern.

---

## 17. Configuration and Threat Hunting

Threat-hunting requirements can expose telemetry gaps.

For example:

```text id="8x5hkd"
Hunting Hypothesis
       ↓
Required Telemetry
       ↓
Telemetry Available?
       ↓
YES ──────────→ Hunt
       │
       NO
       ↓
Configuration Improvement
       ↓
Retest
```

This creates a feedback loop between hunting and telemetry engineering.

---

## 18. Configuration and Incident Investigation

Incident investigations may identify missing fields or telemetry.

Examples include:

* Missing command-line data
* Missing process context
* Missing authentication information
* Insufficient event detail
* Missing network context

These findings can result in configuration improvements.

```text id="svd4j5"
Investigation
      ↓
Evidence Gap
      ↓
Telemetry Requirement
      ↓
Configuration Change
      ↓
Validation
      ↓
Improved Investigation Capability
```

---

## 19. Configuration Security

Configuration files can contain sensitive information.

Before committing configuration to GitHub, verify that it does not contain:

* Passwords
* API keys
* Authentication tokens
* Private keys
* Session identifiers
* Personal information
* Production credentials
* Sensitive infrastructure addresses

Use placeholders or sanitized examples where necessary.

---

## 20. Public Repository Standards

The public repository should contain enough configuration information to demonstrate technical understanding without exposing the actual security environment.

Recommended approach:

```text id="7y8m4h"
PUBLIC REPOSITORY
      │
      ├── Sanitized Configuration
      ├── Documentation
      ├── Detection Logic
      ├── Test Cases
      └── Evidence
       
PRIVATE LAB
      │
      ├── Credentials
      ├── Secrets
      ├── Private Keys
      ├── Sensitive Configuration
      └── Infrastructure-Specific Data
```

This distinction is particularly important when screenshots or configuration files are published publicly.

---

## 21. Configuration Evidence

Useful evidence may include:

* Configuration excerpts
* Successful service validation
* Agent connectivity
* Telemetry ingestion
* Detection-rule loading
* Detection test results
* Regression-test results

Configuration screenshots should demonstrate the relevant technical point without exposing unnecessary sensitive information.

---

## 22. Repository Structure

Configuration-related artifacts are distributed according to their purpose:

```text id="w2yqk0"
01-lab/
├── configuration/
├── infrastructure/
└── deployment/

05-detection-engineering/
├── wazuh/
│   ├── rules/
│   ├── decoders/
│   └── configurations/
└── detection-lifecycle/
```

This prevents configuration from becoming a single unstructured collection of files.

---

## 23. Configuration Lifecycle

The project uses the following configuration lifecycle:

```text id="b1xq5n"
DEFINE
  ↓
CONFIGURE
  ↓
VALIDATE
  ↓
TEST
  ↓
DOCUMENT
  ↓
VERSION CONTROL
  ↓
MONITOR
  ↓
IMPROVE
```

Each configuration change should have a measurable operational purpose.

---

## 24. Operational Readiness

The monitoring environment should be considered configuration-ready when:

```text id="3l6r1d"
[ ] Endpoint logging configured
[ ] Sysmon configured
[ ] PowerShell telemetry configured
[ ] Wazuh Agent configured
[ ] Wazuh Manager configured
[ ] Detection rules loaded
[ ] Required telemetry available
[ ] Test events processed
[ ] Alerts generated as expected
[ ] Regression validation completed
[ ] Sensitive information excluded
```

---

## 25. Summary

The configuration layer provides the operational settings that connect infrastructure, telemetry, Wazuh processing, and detection engineering.

Its central principle is:

```text id="z5s4u9"
CONFIGURE
    ↓
COLLECT
    ↓
DETECT
    ↓
VALIDATE
    ↓
INVESTIGATE
    ↓
HUNT
    ↓
RESPOND
    ↓
IMPROVE
    ↓
RETEST
```

Configuration is therefore treated as an active part of the SOC engineering lifecycle rather than static infrastructure documentation.

A controlled, validated, and documented configuration provides the foundation required for reliable detection engineering and repeatable security investigations.

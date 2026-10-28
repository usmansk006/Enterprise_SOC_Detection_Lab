# SOC Detection Lab — Architecture

## 1. Purpose

This document describes the logical architecture of the SOC Detection Lab and the relationship between endpoint telemetry, Wazuh processing, detection rules, and security alerts.

The architecture provides technical context for the existing Windows security detections documented in this repository.

## 2. Architecture Overview

The lab follows a SIEM-based endpoint monitoring workflow. Windows security activity is collected through configured telemetry sources, processed by Wazuh, and evaluated against applicable detection rules.

```text
┌────────────────────────────────────┐
│         Windows Endpoint           │
│                                    │
│  Windows Security Event Logs       │
│  Additional Configured Telemetry   │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│            Wazuh Agent             │
│                                    │
│  Configured Log Collection         │
│  Event Forwarding                  │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│           Wazuh Manager            │
│                                    │
│  Event Processing                  │
│  Rule Evaluation                   │
│  Alert Generation                  │
└──────────────────┬─────────────────┘
                   │
                   ▼
┌────────────────────────────────────┐
│          Wazuh Dashboard           │
│                                    │
│  Alert Review                      │
│  Event Inspection                  │
└────────────────────────────────────┘
```

**Architecture note:** The diagram represents the logical monitoring workflow. The components and telemetry sources included in the final implementation should match the available configuration records and evidence.

## 3. Component Responsibilities

### Windows Endpoint

The monitored endpoint generates operating-system and security events relevant to the existing detection use cases.

Depending on the configured event sources, these may include authentication activity, account management, process execution, PowerShell activity, and other security-relevant behavior.

### Wazuh Agent

The agent collects configured endpoint telemetry and forwards it to the Wazuh monitoring infrastructure.

Collection depends on the enabled log sources and agent configuration. Not every Windows event or activity is necessarily collected.

### Wazuh Manager

The manager processes incoming events and evaluates applicable rules.

When an event satisfies the conditions of a configured rule, Wazuh can generate an alert containing relevant event details and rule metadata.

### Wazuh Dashboard

The dashboard provides an interface for reviewing available security alerts and events. The information displayed depends on the deployed components, configuration, and retained data.

## 4. Telemetry and Alert Flow

The monitoring workflow can be summarized as follows:

1. Windows records security-relevant activity.
2. Configured collection mechanisms obtain the relevant event data.
3. The Wazuh Agent forwards collected telemetry.
4. The Wazuh Manager processes the incoming events.
5. Applicable rules evaluate events against their configured conditions.
6. Matching events may produce alerts.
7. The available alert information supports review of the detected behavior.

The exact event IDs, rule identifiers, and alert fields vary by detection and should be documented in each detection's implementation notes.

## 5. Detection Layer

The detection layer consists of the existing Wazuh rules and their associated documentation.

Each detection should identify:

- The behavior it is intended to identify.
- The relevant telemetry source.
- The rule logic or configuration reference.
- The expected alert characteristics, where established.
- Applicable MITRE ATT&CK mapping.
- Known false-positive considerations.
- Available evidence and validation records.

The detection implementation remains the source of truth for the rule's actual conditions and behavior.

## 6. Architecture Boundaries

This project documents a focused detection lab rather than a complete enterprise SOC deployment.

The architecture does not imply the presence of additional SIEM platforms, automated response systems, network detection sensors, or threat intelligence integrations unless those capabilities are explicitly documented and supported by evidence.

Historical architecture documentation and screenshots should not be interpreted as proof that all components are currently operational.

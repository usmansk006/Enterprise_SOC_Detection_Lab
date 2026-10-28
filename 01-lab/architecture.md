# SOC Detection Lab — Architecture

**Architecture Type:** Virtualized Windows Security Monitoring Lab  
**Virtualization Platform:** VMware  
**Monitoring Platform:** Wazuh

## 1. Architecture Overview

The SOC Detection Lab uses a virtualized environment to study Windows security telemetry and host-based threat detection.

The environment consists of two virtual machines:

- **Ubuntu Server VM:** Provides the Linux environment for the Wazuh server-side deployment.
- **Windows 10 VM:** Serves as the monitored endpoint and source of Windows security events.

The intended architecture connects Windows event collection to centralized processing and detection through Wazuh. The resulting alerts can be reviewed through the Wazuh Dashboard when the necessary services are deployed and available.

## 2. Logical Architecture Diagram

```text
┌──────────────────────────────────────────────────────────────┐
│                     VMware Environment                       │
│                                                              │
│  ┌─────────────────────────┐                                 │
│  │    Windows 10 VM        │                                 │
│  │                         │                                 │
│  │  Windows Security Logs  │                                 │
│  │  Process Activity       │                                 │
│  │  Authentication Events  │                                 │
│  │            │            │                                 │
│  │            ▼            │                                 │
│  │      Wazuh Agent        │                                 │
│  └────────────┬────────────┘                                 │
│               │                                              │
│               │ Collected telemetry                          │
│               ▼                                              │
│  ┌─────────────────────────┐                                 │
│  │   Ubuntu Server VM      │                                 │
│  │                         │                                 │
│  │     Wazuh Manager       │                                 │
│  │            │            │                                 │
│  │            ▼            │                                 │
│  │   Event Processing and  │                                 │
│  │   Detection Evaluation  │                                 │
│  │                         │                                 │
│  │   Indexer / Dashboard   │                                 │
│  │   only if deployed      │                                 │
│  └─────────────────────────┘                                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

*The diagram illustrates the intended logical workflow. It does not establish the exact VM network configuration, the placement of every Wazuh service, or the current operational status of the components.*

## 3. Architecture Components

### 3.1 VMware Virtualization Layer

VMware provides the virtualization environment in which the Ubuntu Server and Windows 10 virtual machines operate.

The virtualized design allows the server and endpoint roles to be maintained separately for lab-based security monitoring.

The precise VMware product, virtual network mode, assigned resources, and IP addresses should be documented only where confirmed by the existing environment records.

### 3.2 Windows 10 Endpoint

The Windows 10 VM is the primary endpoint telemetry source.

Relevant activity can include:

- Authentication attempts
- Account-management operations
- PowerShell execution
- Scheduled-task creation
- Windows Defender events
- Process execution and parent-child relationships
- Other activity covered by the existing detection rules

The events available for analysis depend on Windows auditing, event-channel configuration, and the collection settings in use.

### 3.3 Wazuh Agent

The Wazuh Agent provides the collection and forwarding path between the Windows endpoint and the Wazuh server-side environment.

Its detection coverage depends on the event sources configured for collection and the telemetry successfully delivered to the server.

### 3.4 Ubuntu Server VM

The Ubuntu Server VM provides the Linux environment used for the Wazuh server-side deployment.

The Wazuh Manager is responsible for processing received events and evaluating applicable detection rules.

The installation and availability of the Indexer and Dashboard must be established separately. Their appearance in a logical architecture diagram is not proof that either service is installed or operational.

### 3.5 Wazuh Detection and Alert Review

The detection workflow uses event data and applicable Wazuh rules to identify activity matching defined conditions.

Where the required services are available, alerts can be reviewed through the Wazuh Dashboard.

A detection should be considered validated only to the extent supported by its existing rule configuration, relevant event data, and recorded test or investigation evidence.

## 4. Telemetry Flow

The intended processing sequence is:

1. Windows 10 generates security-relevant activity.
2. Windows logging and auditing produce the corresponding event records.
3. The Wazuh Agent collects configured telemetry.
4. The agent forwards available data to the Wazuh server-side environment.
5. The Wazuh Manager processes events and evaluates applicable rules.
6. Matching events may produce alerts.
7. Available alerts and supporting records are reviewed and documented.

The sequence describes the logical workflow; actual behavior depends on the configuration and availability of each component.

## 5. Detection Engineering Layer

The architecture supports the project's existing Windows-focused detection use cases.

Documented categories include authentication failures, suspicious PowerShell activity, account creation, scheduled-task creation, Defender malware-detection events, suspicious process relationships, and CertUtil activity where supported by the existing detection files.

Each use case should be documented independently, including:

- Detection objective
- Relevant telemetry source
- Rule logic or detection conditions
- Expected security significance
- Available supporting evidence
- Known limitations and validation status

The presence of a detection document alone does not prove that a rule is currently enabled or that it has been successfully triggered.

## 6. Architecture Boundaries

This architecture describes a focused Windows endpoint monitoring lab using Wazuh.

It does not claim the implementation of:

- Multiple SIEM platforms or cross-SIEM correlation
- Automated containment or incident response
- Enterprise high availability
- Additional endpoint platforms
- Production-scale monitoring infrastructure
- Detection performance metrics without recorded measurements

These capabilities are outside the documented scope unless separate implementation evidence establishes otherwise.

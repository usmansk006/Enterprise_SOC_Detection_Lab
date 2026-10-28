# SOC Detection Lab — Environment Documentation

**Project:** SOC Detection Lab  
**Virtualization Platform:** VMware  
**Server Operating System:** Ubuntu Server  
**Monitored Endpoint:** Windows 10  
**Security Monitoring Platform:** Wazuh

## 1. Environment Overview

The SOC Detection Lab is a virtualized environment designed for Windows security monitoring and host-based threat detection.

VMware provides the virtualization layer for two virtual machines: Ubuntu Server and Windows 10. The Windows VM serves as the monitored endpoint, while the Ubuntu Server VM provides the environment for the Wazuh server-side deployment.

The lab supports the project's existing Windows detection use cases and their associated documentation and evidence.

This document describes the intended environment and component responsibilities. It does not claim that all services are currently operational.

## 2. Virtual Machine Inventory

| Virtual machine | Operating system | Primary responsibility |
|---|---|---|
| Ubuntu Server VM | Ubuntu Server | Hosts the Wazuh server-side components that are installed and configured |
| Windows Endpoint VM | Windows 10 | Generates Windows security events and endpoint telemetry |

Specific VM names, allocated memory, processor counts, disk sizes, IP addresses, and network settings should be added only when verified against the actual configuration or existing records.

## 3. Ubuntu Server Environment

### Purpose

The Ubuntu Server VM provides the Linux environment for the Wazuh server-side deployment.

### Intended responsibilities

- Receive endpoint telemetry through the configured Wazuh communication path.
- Process events through the Wazuh Manager when available.
- Evaluate events against applicable detection rules.
- Support alert review through the related services when those services are deployed and available.

### Component status

The installation state of each Wazuh service must be distinguished from its intended role.

| Component | Documented role | Status |
|---|---|---|
| Wazuh Manager | Event processing and detection-rule evaluation | Not asserted as currently operational |
| Wazuh Indexer | Stores and indexes monitoring data | Installation and availability require separate verification |
| Wazuh Dashboard | Provides the interface for reviewing alerts | Installation and availability require separate verification |

The presence of these components in the table does not establish that they are all installed or running.

## 4. Windows 10 Environment

### Purpose

The Windows 10 VM acts as the monitored endpoint and primary source of Windows security telemetry.

### Relevant telemetry

The existing detection content may use events associated with:

- Authentication failures
- User and account management
- PowerShell execution
- Scheduled-task creation
- Windows Defender detections
- Process execution and parent-child relationships
- CertUtil activity and related file-decoding behavior

The availability and usefulness of these events depend on Windows auditing, event-channel configuration, and the collection settings used by the Wazuh Agent.

### Wazuh Agent

The Wazuh Agent provides the configured endpoint collection and forwarding path.

Its effective coverage depends on the agent configuration, enabled event sources, connectivity, and the condition of the agent during the relevant observation period.

## 5. Virtualization and Networking

VMware hosts the Ubuntu Server and Windows 10 virtual machines as separate systems.

Their ability to communicate depends on the configured virtual networking and applicable firewall rules.

The following details should be recorded if supported by existing environment records:

| Setting | Recorded value |
|---|---|
| VMware product and version | Not documented here |
| Ubuntu Server VM address | Not documented here |
| Windows 10 VM address | Not documented here |
| VMware network mode | Not documented here |
| Wazuh communication configuration | Refer to existing configuration evidence |
| Resource allocation | Not documented here |

These fields are intentionally left unspecified rather than populated with assumed values.

## 6. Event Collection and Processing

The intended event-processing workflow is:

1. Windows 10 generates security-relevant activity.
2. Windows logging records applicable events.
3. The Wazuh Agent collects configured telemetry.
4. The server-side Wazuh deployment processes the received data.
5. Applicable detection rules evaluate events.
6. Resulting alerts can be reviewed through the available monitoring interface.

This is the intended workflow, not a claim that the complete pipeline has been verified in the current environment.

## 7. Evidence and Configuration Management

Relevant project artifacts may include:

- Existing Wazuh configuration files
- Detection rules and their documentation
- Windows event records
- Historical alert screenshots or exports
- Existing validation notes
- Configuration records supporting the documented architecture

Each artifact should be associated with the component or detection it supports.

Sensitive values, including credentials, private keys, tokens, and other secrets, must not be committed to the repository.

Historical evidence should be identified as historical. It should not be represented as proof of current service health or current detection behavior.

## 8. Environment Limitations

The environment is intended for lab-based security monitoring and detection engineering.

The documentation does not claim:

- Continuous or production-grade monitoring
- High availability or disaster recovery
- Automated incident response
- Multiple SIEM integrations
- Verified detection performance metrics
- Current availability of every Wazuh service

Any additional capability should be documented only when the implementation and supporting evidence are available.


The Windows VM supplies endpoint telemetry, while the Ubuntu Server VM provides the environment for the applicable Wazuh server-side components. The existing detection documentation and evidence describe the project's implemented detection work.

Current service availability and detection validation must be established from the relevant configuration and records, not inferred from the architecture alone.

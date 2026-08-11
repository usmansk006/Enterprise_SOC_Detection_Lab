# SOC Lab Architecture

## Overview

The Enterprise SOC Detection Lab is an isolated virtualized security environment designed to demonstrate security monitoring, detection engineering, threat hunting, incident investigation, and incident response.

Wazuh is deployed as the primary security monitoring and SIEM platform.

## Architecture

```text
                    ┌──────────────────────┐
                    │      Kali Linux      │
                    │ Authorized Security  │
                    │       Testing        │
                    └──────────┬───────────┘
                               │
                               │ Controlled
                               │ Security Activity
                               ▼
                    ┌──────────────────────┐
                    │    Windows 10 VM     │
                    │   Monitored Endpoint  │
                    │                      │
                    │    Wazuh Agent       │
                    │    Sysmon*           │
                    └──────────┬───────────┘
                               │
                               │ Endpoint
                               │ Telemetry
                               ▼
              ┌────────────────────────────────┐
              │      Ubuntu Wazuh Server       │
              │                                │
              │  ┌──────────────────────────┐  │
              │  │     Wazuh Manager        │  │
              │  └──────────────────────────┘  │
              │                                │
              │  ┌──────────────────────────┐  │
              │  │     Wazuh Indexer        │  │
              │  └──────────────────────────┘  │
              │                                │
              │  ┌──────────────────────────┐  │
              │  │    Wazuh Dashboard       │  │
              │  └──────────────────────────┘  │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │       SOC Analyst    │
                    │                      │
                    │ Triage → Investigate │
                    │ Hunt → Respond       │
                    └──────────────────────┘

* Sysmon is included once installed and validated.

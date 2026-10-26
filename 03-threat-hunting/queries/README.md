# Threat Hunting Query Library

## Purpose

This directory contains reusable queries and search procedures that support investigations across the Enterprise SOC Detection Lab.

Queries are organized by telemetry source so they can be maintained, validated, and reused across multiple threat hunts.

## Query Categories

| Directory | Purpose |
|---|---|
| `wazuh/` | Searches and filters for events available in Wazuh |
| `windows/` | Windows Event Log investigation queries |
| `sysmon/` | Sysmon event investigation queries |
| `network/` | Network telemetry investigation queries, where available |

## Query Development Standards

Each query should document:

- **Query ID:** A unique identifier.
- **Purpose:** The behavior or question being investigated.
- **Data source:** The log or telemetry source required.
- **Prerequisites:** Required logging configuration and permissions.
- **Query:** The executable search or command.
- **Time range:** The period being investigated.
- **Expected output:** The fields or events the query is intended to return.
- **Limitations:** Known visibility gaps and query constraints.
- **Validation status:** Whether the query has been tested against actual lab telemetry.

## Operational Guidance

1. Confirm that the required telemetry is enabled and available.
2. Select a time range appropriate to the investigation.
3. Execute the query against the correct data source.
4. Validate the returned events before interpreting them.
5. Record the execution time, relevant results, and any errors.
6. Retain evidence needed to reproduce the investigation.

Queries must be adapted to the fields and syntax supported by the installed versions of the relevant tools. A query documented in this repository must not be described as validated until it has been executed and its behavior checked.

## Relationship to Individual Hunts

Hunt-specific documentation belongs under `hunts/TH-XXX-hunt-name/`. Shared queries belong in this library when they are reusable across investigations.

For example, a PowerShell process-creation query may support TH-001 and later hunts involving suspicious process execution.

## Validation and Maintenance

Queries should be reviewed when log sources, collection configurations, field mappings, or SIEM versions change. Failed queries and missing telemetry should be documented rather than silently treated as having returned no suspicious activity.

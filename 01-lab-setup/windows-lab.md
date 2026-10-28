# Lab setup overview

This section provides the guidance required to build a safe, minimal Windows lab for evaluating HTA detection content. The emphasis is on local validation using Sysmon, Windows Security logs, and controlled process generation.

## Goals

- validate telemetry coverage for `mshta.exe`, parent-child process lineage, and command-line fields,
- confirm Sysmon event availability and field quality,
- validate detection logic with synthetic or authorized test fixtures,
- and document operational assumptions before claiming detection effectiveness.

## Core lab components

- one Windows endpoint for telemetry collection,
- Sysmon installed and configured for process-creation and network events,
- Windows Security logs enabled for process creation and auditing where supported,
- a local environment for testing Python scripts and rule validation,
- and documented safety boundaries for authorized lab execution only.

## Minimum validation checklist

- Windows VM or isolated host with no production exposure,
- Sysmon installed with a supported schema version,
- process creation audit policy reviewing command-line details,
- access to event logs that capture process lineage, script behavior, and file creation,
- safe examples and synthetic fixtures used for validation,
- explicit documentation of untested live scenarios.

## Safety note

Only run authorized test artifacts in a lab environment. Never execute untrusted HTML applications, downloaded payloads, or unknown scripts on a regular workstation or production machine.

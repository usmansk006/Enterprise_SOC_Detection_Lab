# Final project report

## Executive summary

The repository has been transformed from a Wazuh-centric SOC lab into a local-first, SIEM-independent HTA detection engineering lab. The project documents how to build, validate, and investigate suspicious `mshta.exe` execution in a controlled environment.

## Scope

- environment setup and Sysmon guidance,
- detection engineering catalog,
- Sigma and query examples,
- local Python analysis tooling,
- validation matrix,
- threat-hunting and investigation guidance,
- and detection-quality reporting.

## Status

The repository contains a coherent architecture and meaningful content across all planned directories. Live Windows validation remains unexecuted in this environment and should be treated as an explicit next step in an authorized lab.

## Remaining work

- run authorized Windows telemetry validation,
- tune detection thresholds to real event data,
- expand regression coverage with additional fixtures,
- and refine documentation based on observed telemetry quality.

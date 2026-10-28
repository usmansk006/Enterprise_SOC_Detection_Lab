# Root README

## HTA Sentinel — Windows HTA Threat Detection & Engineering Lab

This repository is being transformed from a Wazuh-oriented SOC lab into a professional, SIEM-independent HTA detection engineering project focused on `mshta.exe` execution and related Windows process behavior.

## Project objective

Build a practical red/blue detection engineering lab that demonstrates how to:

- identify suspicious HTA execution chains,
- use Sysmon and Windows event telemetry,
- author Sigma-style detection logic,
- analyze command line, process lineage, and network activity,
- perform local Python-based validation and correlation,
- and document detection quality honestly.

## Current status

| Area | Status |
| --- | --- |
| Repository inspection | Verified |
| Legacy Wazuh material preservation | Preserved |
| HTA detection architecture | Implemented |
| Root documentation | Implemented |
| Lab setup guidance | Implemented |
| Detection catalog | Implemented |
| Local Python toolkit | Implemented |
| Validation framework | Implemented |
| Threat hunting and investigation docs | Implemented |
| Full live Windows validation | Not run |

## Repository structure

```text
01-lab-setup/            Local Windows lab setup and Sysmon guidance
02-detections/           HTA-focused detection catalog and rule documentation
03-detection-rules/      Sigma and query references
04-validation/           test matrix and synthetic fixtures
05-threat-hunting/       hunting and investigation playbooks
06-local-analysis-toolkit/ Python tools and unit tests
07-evidence/             evidence standards and sample artifacts
08-detection-quality/    gaps, coverage, false positives, and limitations
09-reports/              catalog, MITRE mapping, project report
10-legacy-detections/    retained older content
docs/                   documentation and architecture references
```

## Important project boundaries

This project intentionally does not require Wazuh, Splunk, Elastic, Sentinel, or another SIEM to be operational. The detection engineering workflow is local and evidence-driven.

Sigma rules are documentation and rule logic, not an execution engine. A compatible rule-processing environment may still be needed for conversion or operational use.

## Safe lab usage

- Use only in authorized lab or isolated test environments.
- Do not execute unknown HTA files outside a controlled lab.
- Treat all findings as hypotheses until confirmed by telemetry and investigation.

## Key sections

- `01-lab-setup/` for host and Sysmon setup
- `02-detections/` for the HTA detection set
- `03-detection-rules/` for Sigma guidance and examples
- `04-validation/` for synthetic validation matrix
- `06-local-analysis-toolkit/` for local Python tooling
- `09-reports/` for detection catalog and mapping

## Contributing

See `CONTRIBUTING.md`.

## Disclaimer

See `DISCLAIMER.md`.

## License

This project is distributed under the MIT license. See `LICENSE`.

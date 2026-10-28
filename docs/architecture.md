# HTA Sentinel — Architecture

This document describes the repository architecture for the SIEM-independent HTA detection engineering lab.

## Repository purpose

The repository exists to demonstrate how to build a local Windows detection engineering and threat-hunting lab focused on `mshta.exe` execution and related HTA abuse behavior.

The emphasis is on:

- Windows endpoint telemetry
- Sysmon process creation and command-line visibility
- Sigma detection rule authoring
- Python-based log parsing and correlation
- structured validation and honest reporting
- detection quality assessment and documentation

## Repository layout

```text
Enterprise_SOC_Detection_Lab/
├── README.md
├── LICENSE
├── DISCLAIMER.md
├── CONTRIBUTING.md
├── .gitignore
├── 01-lab-setup/
├── 02-detections/
├── 03-detection-rules/
├── 04-validation/
├── 05-threat-hunting/
├── 06-local-analysis-toolkit/
├── 07-evidence/
├── 08-detection-quality/
├── 09-reports/
├── 10-legacy-detections/
├── docs/
└── legacy-wazuh-content/ (retained only where already present)
```

## Design principles

- Local-first: no dependency on proprietary SIEM platforms
- Evidence-driven: identify telemetry requirements before claiming detection feasibility
- Contextual: HTA detections should account for false positives and legitimate admin use
- Maintainable: rules should be readable, testable, and documented
- Honest: validation status must be explicit

## Architecture flow

```text
Windows endpoint
    -> Sysmon + Security logs
    -> JSON/JSONL event fixtures or lab exports
    -> local parser + correlation tooling
    -> Sigma rule logic review
    -> validation matrix
    -> hunting and incident investigation
```

## Relationship to legacy content

This repository already contains a Wazuh-focused lab structure. This migration preserves that historical content under its existing directories and adds a new SIEM-independent architecture intended to serve as a professional detection engineering portfolio artifact.

The new architecture does not assume Wazuh, Splunk, Elastic, or Microsoft Sentinel is required to perform local detection engineering.

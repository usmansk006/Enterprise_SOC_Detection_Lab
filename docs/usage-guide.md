# Usage Guide

This guide explains how to use the repository after setup.

## Repository usage

- Review `02-detections/` for the HTA-related detection catalog.
- Review `03-detection-rules/` for Sigma-style detection logic and rule assumptions.
- Use `06-local-analysis-toolkit/` for parsing, validation, and correlation.
- Use `04-validation/` to review test coverage and expected outcomes.
- Use `05-threat-hunting/` for investigation workflows.

## Typical workflow

```text
1. Prepare Windows endpoint telemetry
2. Review event fixtures or local logs
3. Parse events with the toolkit
4. Validate Sigma YAML structure
5. Correlate HTA-related activity
6. Review false positives and blind spots
7. Document testing outcome honestly
```

## Safe usage notes

- Never run unknown HTA content outside a lab environment.
- Treat all suspicious HTA activity as potentially malicious until validated.
- Keep all evidence and fixtures synthetic unless specifically collected in an authorized lab environment.

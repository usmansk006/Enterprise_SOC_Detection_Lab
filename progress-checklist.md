# Troubleshooting

## Common issues

- YAML parsing fails because the file is not valid YAML.
- Required fields are missing from an event file.
- `mshta.exe` process creation is not visible because Sysmon or Windows process logging is not enabled.
- Network or file creation telemetry is absent because the host policy does not include those events.

## Recommended steps

- confirm event source and log channels,
- review the telemetry assumptions in the detection README,
- validate field names before applying rules,
- and keep a clear record of missing data or collection gaps.

## Scope note

This repository documents a local-first detection engineering process. Full live validation requires actual telemetry and an authorized environment.

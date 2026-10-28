# Troubleshooting

## Common issues

### Python dependency errors

If `yaml` or `pytest` is missing, install the relevant packages explicitly and re-run validation.

### Sigma files do not validate

Review structure, required fields, and unsupported fields. This toolkit performs structural validation, not full Sigma engine validation.

### Missing telemetry fields

Some detections require Sysmon process creation fields and Security log fields that may not be available in every host configuration.

### Correlation returns too many results

Use a small time window and require stable identifiers such as process GUID or session host + PID when available.

## Safe operating posture

Do not assume detections are complete because the rule is syntactically valid. Telemetry quality and field availability are central to real-world effectiveness.

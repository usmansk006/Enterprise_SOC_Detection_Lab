# Limitations

This project is intentionally honest about the limits of detection engineering.

- process creation evidence can lack full execution context
- file execution may be blocked or occur off-host
- network activity may be hidden by proxy or NAT
- some malicious HTA chains use staging and indirect execution
- no production environment was used to validate live detections here

## Evasion considerations

Attackers may encode or stage HTA content to avoid simplistic detection. Multi-stage techniques and execution wrappers may reduce the value of single-event rules.

# Sigma examples

This folder contains example Sigma-style documentation tailored to HTA-focused telemetry assumptions.

## Example rule

```yaml
title: Suspicious mshta.exe execution from scriptable parent
id: 5a2042ce-8603-4d5d-a4b7-712d6b3b5a2d
status: experimental
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\mshta.exe'
    ParentImage|endswith:
      - '\powershell.exe'
      - '\cmd.exe'
  condition: selection
falsepositives:
  - internal admin automation
level: medium
fields:
  - Image
  - ParentImage
  - CommandLine
  - User
  - ProcessGuid
```

## Notes

This is an example abstraction, not a direct guarantee of enterprise deployment compatibility. Real-world rule validation depends on actual Sysmon and Windows event fields.

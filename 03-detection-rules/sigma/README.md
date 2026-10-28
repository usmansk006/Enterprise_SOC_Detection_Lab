# Detection rules overview

This directory stores the rule logic and query references that support the HTA detection catalog. It deliberately separates detection logic from the narrative documentation in `02-detections/`.

## Contents

- Sigma rules and examples
- Windows event queries
- PowerShell investigation snippets
- correlation logic notes and assumptions

## Rule quality standards

- unique rule IDs,
- documented telemetry assumptions,
- clear ATT&CK mapping,
- and a distinction between structural validation and end-to-end rule execution.

## Important note

Sigma rules are logic definitions. They do not execute telemetry collection or conversion by themselves. A compatible pipeline or conversion tool may still be needed in an operational environment.

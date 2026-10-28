# Detection Gaps

This document captures the limitations in the active detection library.

## Notable gaps

- event loss or log retention gaps
- missing command-line data on some systems
- incomplete Sysmon configuration
- absent file creation telemetry
- no full Windows live validation in this environment

## Analytical impact

Without strong context, HTA detections may under-detect or produce noise. Correlation quality is dependent on event completeness and timestamp quality.

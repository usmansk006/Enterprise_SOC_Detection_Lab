# False Positive Analysis

This file documents likely false positives for HTA detections.

## Common false-positive scenarios

- legitimate internal help or admin tools call `mshta.exe`
- approved IT support scripts open local `.hta` files
- browser or software helper mechanisms invoke HTA in signed environments
- security tooling or malware analysis harnesses simulate HTA execution in lab environments

## Mitigations

- require contextual indicators such as suspicious command lines or user-writable file paths
- combine process lineage with network or file creation data
- use higher confidence only when multiple events align

## Risk

Single `mshta.exe` execution alone is not enough to classify meaning malicious activity.

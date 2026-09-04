# DET-002: PowerShell Security Policy Discovery Using Secedit

## Overview

DET-002 is a custom Wazuh detection designed to identify PowerShell activity involving the Windows `secedit` utility.

The detection was developed and tested in an isolated SOC lab using PowerShell Script Block Logging and Wazuh.

This project demonstrates the detection engineering lifecycle:

```text
Activity
↓
Telemetry Collection
↓
Detection
↓
Investigation
↓
Troubleshooting
↓
Tuning
↓
Retesting
↓
Validation

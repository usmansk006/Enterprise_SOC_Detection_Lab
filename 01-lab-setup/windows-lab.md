# Windows Lab Preparation

This document covers the lab host setup for a Windows-based HTA detection engineering environment.

## Baseline configuration

- OS: Windows 10 or 11 workstation or VM
- user role: local administrator for test environment only
- network: isolated or lab-only networking
- controls: disable unnecessary services and external connections

## Security logging recommendations

- Security log process creation auditing
- PowerShell script block logging where feasible
- module and image load logging if configured
- Sysmon process creation and network capture

## Validation steps

1. Confirm event log channel access.
2. Confirm Sysmon service is running.
3. Confirm `Event ID 1`, `Event ID 3`, and relevant process creation events are being logged.
4. Confirm you can query the XML and event data locally.

## Limitations

Windows telemetry availability depends on OS build, policy, and security settings. A host may be configured to drop or obscure certain fields.

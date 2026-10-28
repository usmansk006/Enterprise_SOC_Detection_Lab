# Installation and verification

## Installation

1. Download Sysmon from the Microsoft Sysinternals site.
2. Install using a validated configuration file.
3. Confirm the service is running as `Sysmon64` or equivalent.
4. Review the default event log channel for process creation and network connection data.

## Verification steps
 
Use a controlled test host and confirm:

- `Event ID 1` appears for process creation,
- `CommandLine` is captured without truncation where configured,
- `ParentImage` and `ParentCommandLine` are available,
- and network or file creation events are visible for known test activity.

## Commands and checks

Example validation steps:

```powershell
Get-Service Sysmon
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 20
Get-WinEvent -LogName "Security" -MaxEvents 20 | Where-Object {$_.Id -eq 4688}
```

## Safety and scope

These steps are for authorized lab testing only. Do not run unknown HTA files or untrusted script content. Validate results only in an isolated environment and document any missing telemetry.

## Notes

Sysmon schema may vary by version. Use the version that matches your environment and validate the XML against the supported schema before production use. The included XML is a practical starting point for an isolated lab, not a guarantee of every environment-specific field.

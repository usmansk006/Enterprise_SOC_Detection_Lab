# Installation and Verification

## Install Sysmon

Use a supported Sysmon binary and load this XML configuration in a controlled lab environment.

```powershell
Sysmon64.exe -i sysmon-configuration.xml -accepteula
```

## Verify the service

```powershell
Get-Service Sysmon
```

## Validate event logs

Open Event Viewer and review:

- Application and Services Logs > Microsoft > Windows > Sysmon > Operational
- Windows Logs > Security

Look for:

- Sysmon Event ID 1: process creation
- Sysmon Event ID 3: network connection
- Sysmon Event ID 11: file creation

## Validate command line visibility

```powershell
gwmi win32_process | Select-Object Name, ProcessId, CommandLine
```

## Safe verification

Use benign test commands only. Confirm the telemetry exists before using any suspicious or untrusted HTA content in the lab.

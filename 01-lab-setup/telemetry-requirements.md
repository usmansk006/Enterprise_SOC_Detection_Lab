# Telemetry Requirements

The HTA detection lab depends on several event sources.

## Core sources

- Windows Security logs
- Sysmon process creation events
- Sysmon network connection events
- PowerShell logs where available
- optional file creation and script execution telemetry

## Required fields

For robust HTA analysis, the lab should provide access to:

- timestamp
- host name
- user name
- process name
- image path
- parent process
- command line
- process ID and parent PID
- process GUID where available
- destination IP/port for network activity
- file path for file creation activity

## Collection limitations

- Some event fields are not always available
- Some security policies suppress or restrict command-line data
- Process GUIDs may not be present in all event sources
- time synchronization between systems may be imperfect

## Safe verification

Verify that telemetry exists by checking event logs and Sysmon output before using any detection logic or correlation rule.

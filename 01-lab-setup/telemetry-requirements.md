# Windows lab design

## Recommended environment

A repeatable lab should consist of:

- Windows 10 or Windows 11 VM,
- no production dependencies,
- outbound network restricted or isolated,
- standard user and administrator accounts for process testing,
- Sysmon installed with a test configuration,
- and snapshots or rollback capability for safe resets.

## Required considerations

### Endpoint telemetry sources

- Windows Security log: process creation, logon, and object access,
- Sysmon event stream: process creation, network connection, file creation, image load, and script execution where available,
- PowerShell operational logs where configured,
- and local event-export or CSV conversion for toolkit validation.

### Constraints

Telemetry quality varies by system configuration, Windows version, policy settings, and event log retention. Rules should not be treated as universally reliable without confirming event field names and availability.

## Authorized testing workflow

1. Prepare a disposable VM or isolated lab host.
2. Install Sysmon and verify the service is healthy.
3. Confirm event IDs relevant to process creation are present.
4. Exercise benign or synthetic HTA behavior.
5. Review events for parent/child process and command-line coverage.
6. Validate results with the repository's Python tooling.
7. Record limitations and do not claim broader effectiveness.

## Operational boundary

This lab is for defensive detection engineering and training only. It is not designed for offensive testing, payload delivery, or broad external validation.

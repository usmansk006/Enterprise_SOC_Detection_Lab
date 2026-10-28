# Investigation Playbook

## Objective

Identify whether HTA execution represents a routine event or suspicious behavior requiring escalation.

## Steps

1. Confirm the host, user, and time window.
2. Review the initial `mshta.exe` process.
3. Review parent and child processes.
4. Inspect command line and script arguments.
5. Correlate file creation and network activity.
6. Determine whether the file was remote or local.
7. Assess whether execution occurs in temp or user-writable paths.
8. Document observed evidence and analyst inferences separately.

## Triage and escalation

Escalate when the process chain includes network activity, suspicious scripting, parent process anomalies, or file writes in writable locations.

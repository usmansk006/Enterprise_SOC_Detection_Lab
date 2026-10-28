# Setup Guide

This guide explains how to prepare a local Windows lab for HTA detection engineering.

## Lab prerequisites

- Windows 10 or 11 test system
- Sysmon installed and configured
- Security log auditing enabled where possible
- Local administrator access for validation in an authorized lab
- Python 3.10+ for parsing and validation scripts
- access to a synthetic or isolated environment only

## Security boundaries

This lab must be run only on systems explicitly authorized for testing.

## Recommended configuration summary

- enable Process Creation auditing for Security logs where permitted
- install Sysmon with configuration to capture process creation, command line, network, integrity, and image loads
- use isolated script files and benign test payloads only

## Quick start

1. Review the contents of `01-lab-setup/`.
2. Install Sysmon with the XML configuration provided there.
3. Validate telemetry availability.
4. Use the local analysis toolkit for parsing and rule validation.
5. Run the synthetic validation fixtures as needed.

## Important limitations

Telemetry availability depends on host configuration, security policy, and the event sources present in the environment. Not every Windows host will expose all fields required for high-confidence detection.

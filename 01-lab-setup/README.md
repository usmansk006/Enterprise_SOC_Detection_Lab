# Lab Setup

This section describes the Windows lab preparation work needed for the HTA detection engineering portfolio.

## Purpose

The lab provides a safe, local environment to validate detection content related to `mshta.exe` execution, process lineage, network activity, file creation, and suspicious script execution.

## Required skills and tooling

- Windows administration knowledge
- understanding of Sysmon, process creation, and command line telemetry
- Python for validation and local analysis
- a controlled lab VM or isolated environment

## Setup checklist

- Create a dedicated Windows VM
- Disable unnecessary external connectivity
- Install Sysmon and confirm event collection
- Enable process creation auditing where supported
- Review command line logging
- Prepare benign synthetic fixtures for testing

## Safety principle

Only run authorized test artifacts. Do not execute untrusted HTA or downloaded samples in a regular workstation environment.

# Lab Environment

## Virtualization Platform

The laboratory is hosted using VMware Workstation.

The virtualized environment allows the security infrastructure and monitored endpoints to operate in an isolated testing environment.

## Wazuh Server

| Property | Configuration |
|---|---|
| Operating System | Ubuntu Server |
| Role | Wazuh Server |
| Wazuh Manager | Installed |
| Wazuh Indexer | Installed |
| Wazuh Dashboard | Installed |
| Virtualization | VMware Workstation |

## Windows Endpoint

| Property | Configuration |
|---|---|
| Operating System | Windows 10 |
| Role | Monitored Endpoint |
| Wazuh Agent | Installed |
| Sysmon | To be installed and validated |

## Kali Linux

| Property | Configuration |
|---|---|
| Operating System | Kali Linux |
| Role | Security Testing |
| Purpose | Authorized lab testing |
| Network | Isolated laboratory |

## Host System

The virtual machines are hosted on a Windows workstation using VMware Workstation.

Detailed host hardware information is intentionally minimized because it is not required for the security objectives of the project.

## Security Considerations

The laboratory is intended for authorized security testing.

No production systems or third-party systems are targeted.

Credentials, API keys, private keys, and other secrets are not included in the repository.

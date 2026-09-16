# Network Infrastructure

## 1. Overview

The network infrastructure provides the communication layer connecting the security-monitoring components and monitored endpoints within the laboratory environment.

The network is designed to support:

* Wazuh agent-to-manager communication
* Analyst access to the Wazuh Dashboard
* Controlled security testing
* Network telemetry collection
* Security monitoring
* Investigation and threat-hunting activities

The environment is isolated and intended for authorized laboratory use.

---

## 2. Network Architecture

The core laboratory communication model is:

```text
                         ┌──────────────────────┐
                         │   Analyst Workstation │
                         │                      │
                         │ Browser / Tools      │
                         └──────────┬───────────┘
                                    │
                                    │ Dashboard Access
                                    ▼
                         ┌──────────────────────┐
                         │   Linux Server VM    │
                         │                      │
                         │   Wazuh Manager      │
                         │   Wazuh Dashboard    │
                         └──────────┬───────────┘
                                    │
                                    │ Security Telemetry
                                    ▼
                         ┌──────────────────────┐
                         │   Windows 10 VM      │
                         │                      │
                         │ Wazuh Agent          │
                         │ Sysmon               │
                         │ Windows Logs         │
                         └──────────────────────┘

                         ┌──────────────────────┐
                         │     Kali Linux VM    │
                         │                      │
                         │ Authorized Testing   │
                         └──────────────────────┘
```

The exact laboratory IP addressing is intentionally excluded from public documentation.

---

## 3. Network Segmentation

The laboratory environment should separate security-testing systems from production or personal infrastructure.

A conceptual segmentation model is:

```text
┌─────────────────────────────────────────────┐
│              Laboratory Network             │
│                                             │
│   ┌──────────┐      ┌──────────────┐       │
│   │ Windows  │─────▶│ Wazuh Server │       │
│   │ Endpoint │      │    / SIEM    │       │
│   └──────────┘      └──────────────┘       │
│          ▲                   ▲              │
│          │                   │              │
│          └──── Kali ─────────┘              │
│             Testing                         │
└─────────────────────────────────────────────┘
```

The objective is to keep controlled attack simulation and security testing within the intended laboratory boundary.

---

## 4. Wazuh Communication

The Windows Wazuh Agent communicates with the Wazuh Manager over the laboratory network.

The communication path is:

```text
Windows Endpoint
      ↓
Wazuh Agent
      ↓
Network
      ↓
Wazuh Manager
      ↓
Event Processing
      ↓
Alert Generation
```

Network connectivity is therefore a prerequisite for endpoint telemetry collection.

If connectivity fails, the absence of alerts should not automatically be interpreted as an absence of suspicious activity.

---

## 5. Analyst Access

The analyst interacts with the monitoring infrastructure through the Wazuh Dashboard.

The communication path is:

```text
Analyst Browser
      ↓
Laboratory Network
      ↓
Wazuh Dashboard
      ↓
Wazuh Security Data
```

Dashboard access should remain restricted to the intended laboratory environment.

Management interfaces should not be unnecessarily exposed to the public Internet.

---

## 6. Security Testing Network

Kali Linux is used as an authorized testing system within the laboratory.

Its role is to generate controlled security activity that can be observed by the defensive monitoring infrastructure.

The testing workflow is:

```text
Authorized Test
      ↓
Kali Linux
      ↓
Target Laboratory Endpoint
      ↓
Windows Telemetry
      ↓
Wazuh
      ↓
Detection
      ↓
Investigation
```

Testing should only target systems that are owned or explicitly authorized for testing.

---

## 7. Network Telemetry

Network activity can provide additional context during security investigations.

Depending on the configured telemetry sources, useful network information may include:

* Source endpoint
* Destination endpoint
* Destination port
* Protocol
* Connection timestamp
* DNS activity
* HTTP activity
* Network process association
* Connection frequency

Network telemetry can be correlated with endpoint process and authentication events.

---

## 8. Endpoint-to-Network Correlation

A network connection by itself may not provide sufficient context.

Correlation can establish the relationship between a process and network activity:

```text
Process Creation
      ↓
Process Identifier
      ↓
Network Connection
      ↓
Destination
      ↓
User Context
      ↓
Timestamp Correlation
```

This allows analysts to investigate questions such as:

* Which process generated the connection?
* Which user executed the process?
* When did the connection occur?
* Was the activity associated with other suspicious events?
* Does the behavior correspond to a known detection or ATT&CK technique?

---

## 9. Network Security Monitoring

Network security monitoring is expanded in:

```text
08-network-security/
```

The repository provides dedicated areas for:

```text
08-network-security/
├── wireshark/
├── suricata/
├── zeek/
├── dns-analysis/
├── http-analysis/
└── network-hunting/
```

These components can provide network-level visibility complementary to endpoint telemetry.

---

## 10. Network Detection Workflow

Network-based detection follows the same engineering principles used for endpoint detections:

```text
Network Activity
      ↓
Telemetry Collection
      ↓
Parsing
      ↓
Detection Logic
      ↓
Alert
      ↓
Triage
      ↓
Investigation
      ↓
Response
      ↓
Detection Improvement
```

Network detections should be validated against the underlying traffic or telemetry whenever possible.

---

## 11. DNS Monitoring

DNS activity can provide useful threat-hunting information.

Potential investigative indicators include:

* Unusual domain requests
* Repeated requests
* High-frequency lookups
* Suspicious domain patterns
* Unexpected destinations
* Host-to-domain relationships

DNS information should be correlated with endpoint activity before drawing conclusions about the nature of the activity.

---

## 12. HTTP Monitoring

HTTP traffic can provide additional visibility into:

* Destination hosts
* Request patterns
* URLs
* Methods
* User-agent information
* Response behavior

Where encrypted traffic prevents content inspection, metadata and endpoint telemetry can still provide useful investigative context.

---

## 13. Network Hunting

Threat hunting can combine network and endpoint telemetry.

Example workflow:

```text
Hunting Hypothesis
      ↓
Identify Network Indicators
      ↓
Search DNS / HTTP / Connection Data
      ↓
Identify Related Hosts
      ↓
Correlate Endpoint Activity
      ↓
Review Processes / Users
      ↓
Validate Activity
      ↓
Detection Improvement
```

Network hunting documentation is maintained under:

```text
03-threat-hunting/hunts/
```

and:

```text
08-network-security/network-hunting/
```

---

## 14. Incident Investigation

Network information can be incorporated into incident investigations.

A network-aware investigation may follow:

```text
Initial Alert
      ↓
Identify Host
      ↓
Establish Timeline
      ↓
Review Process Activity
      ↓
Review Network Connections
      ↓
Identify Destinations
      ↓
Correlate DNS / HTTP
      ↓
Determine Scope
      ↓
Document Findings
```

Network evidence should be correlated with endpoint and authentication evidence to establish a complete activity timeline.

---

## 15. Network Security Controls

The laboratory network should follow basic security principles:

### Restricted Exposure

Monitoring and management services should not be unnecessarily exposed externally.

### Controlled Connectivity

Only required communication paths should be permitted.

### Isolation

Security-testing traffic should remain within the authorized laboratory environment.

### Monitoring

Important network activity should be observable through available telemetry.

### Credential Protection

Credentials, tokens, keys, and authentication material should not be transmitted or stored unnecessarily.

---

## 16. Troubleshooting Network Connectivity

When telemetry is not arriving at the Wazuh Manager, network troubleshooting should follow a layered approach.

```text
Physical / Virtual Network
          ↓
IP Connectivity
          ↓
Required Service Port
          ↓
Wazuh Agent
          ↓
Wazuh Manager
          ↓
Event Processing
          ↓
Detection
          ↓
Dashboard
```

This prevents analysts from changing detection rules when the actual problem is network connectivity.

---

## 17. Network Evidence

Network evidence may include:

* Packet captures
* DNS records
* HTTP metadata
* Network connection events
* Firewall events
* Wazuh network-related alerts
* Zeek logs
* Suricata alerts

Evidence should be preserved according to the investigation or detection scenario in which it is used.

Sensitive information should be reviewed before publishing network evidence to GitHub.

---

## 18. Privacy and Information Exposure

Public screenshots and documentation should avoid unnecessarily exposing:

* Private IP addresses
* Public IP addresses
* Personal hostnames
* MAC addresses
* Usernames
* Email addresses
* Authentication tokens
* Credentials
* Internal DNS information
* Unnecessary network topology details

Where network information is required to demonstrate a technical finding, only the minimum necessary information should be retained.

---

## 19. Network Infrastructure and Detection Engineering

Network infrastructure supports the detection-engineering lifecycle:

```text
Network Behavior
      ↓
Telemetry Requirement
      ↓
Detection Design
      ↓
Implementation
      ↓
Controlled Test
      ↓
Alert Validation
      ↓
Tuning
      ↓
Regression Testing
```

Network detection artifacts belong under:

```text
05-detection-engineering/
```

while operational network monitoring content belongs under:

```text
08-network-security/
```

---

## 20. Network Infrastructure and Threat Intelligence

Network indicators can also feed the threat-intelligence workflow.

Examples include:

```text
IP Address
Domain
URL
Hash
      ↓
Enrichment
      ↓
Context
      ↓
Confidence Assessment
      ↓
Detection / Investigation
```

Threat-intelligence artifacts are maintained under:

```text
09-threat-intelligence/
```

The presence of an indicator should be evaluated in context rather than automatically treated as proof of malicious activity.

---

## 21. Network Infrastructure and Incident Response

Network telemetry can support incident-response decisions by helping determine:

* Which systems communicated
* When communication occurred
* Which destinations were contacted
* Whether activity spread to other systems
* Whether additional hosts require investigation

The response workflow remains:

```text
Detection
   ↓
Investigation
   ↓
Scope
   ↓
Containment
   ↓
Eradication
   ↓
Recovery
   ↓
Lessons Learned
```

Detailed response procedures are maintained under:

```text
06-incident-response/
```

---

## 22. Operational Validation

Before conducting a security exercise, verify:

```text
[ ] Laboratory network operational
[ ] Wazuh Manager reachable
[ ] Windows endpoint reachable
[ ] Wazuh Agent connected
[ ] Dashboard accessible
[ ] Required monitoring services operational
[ ] Authorized testing path available
[ ] Network telemetry functioning where configured
```

This creates a known-good baseline for subsequent detection testing.

---

## 23. Repository Integration

Network infrastructure connects multiple repository components:

```text
01-lab/
└── infrastructure/
    └── network/

02-detections/

03-threat-hunting/

04-Incident-Investigations/

05-detection-engineering/

06-incident-response/

08-network-security/

09-threat-intelligence/

11-metrics/
```

This makes network visibility a supporting layer across the broader SOC workflow.

---

## 24. SOC Lifecycle Integration

Network infrastructure contributes to the complete defensive lifecycle:

```text
COLLECT
   ↓
DETECT
   ↓
TRIAGE
   ↓
INVESTIGATE
   ↓
HUNT
   ↓
RESPOND
   ↓
IMPROVE
   ↓
RETEST
```

Network telemetry can strengthen each stage by providing additional context around endpoint and identity activity.

---

## 25. Summary

The network infrastructure provides the communication and network-observability foundation of the SOC lab.

It connects:

* Windows endpoints
* Wazuh monitoring infrastructure
* Analyst interfaces
* Authorized security-testing systems
* Network-security monitoring components

The network layer supports the broader defensive workflow:

```text
Network Activity
      ↓
Telemetry
      ↓
Detection
      ↓
Correlation
      ↓
Investigation
      ↓
Threat Hunting
      ↓
Incident Response
      ↓
Detection Improvement
```

A properly controlled network environment allows the project to demonstrate not only endpoint detection, but also the correlation of endpoint, identity, and network telemetry within an enterprise-style SOC workflow.

# Threat Hunting

## Overview

This section documents a structured, hypothesis-driven threat-hunting capability within the Enterprise SOC Detection Lab. The objective is to investigate potentially suspicious activity using endpoint telemetry, SIEM data, investigative queries, and documented analytical procedures.

Threat hunting complements rule-based detection by investigating behaviors that may not generate an existing alert.

## Objectives

- Develop and test evidence-based threat hypotheses.
- Investigate suspicious endpoint and process activity.
- Correlate Windows, Sysmon, and Wazuh telemetry where available.
- Identify visibility gaps and opportunities to improve detection coverage.
- Document investigative methods, evidence, findings, and recommendations.
- Convert validated hunting insights into improvements to detection and incident-response workflows.

## Hunting Workflow

1. Define the hypothesis and investigation scope.
2. Identify required telemetry and verify data availability.
3. Select appropriate queries and establish a time window.
4. Execute queries against the available lab data.
5. Review results and investigate relevant events.
6. Correlate related activity and assess alternative explanations.
7. Document findings and evidence.
8. Recommend detection, monitoring, or response improvements.
9. Record limitations and identify follow-up investigations.

## Hunt Catalogue

| Hunt ID | Hunt Name | Primary Focus | Status |
|---|---|---|---|
| TH-001 | PowerShell Abuse | Suspicious PowerShell execution and related process activity | In progress |
| TH-002 | Credential Abuse | Potential credential-access activity | Planned |
| TH-003 | Persistence | Potential mechanisms for maintaining access | Planned |
| TH-004 | Lateral Movement | Potential movement between systems | Planned |
| TH-005 | Suspicious Processes | Unusual process execution and relationships | Planned |
| TH-006 | Network Activity | Potentially suspicious network behavior | Planned |

Hunt statuses must be updated according to actual implementation and evidence. A planned hunt is not considered completed until its investigation has been executed and documented.

## Technology and Telemetry

The hunting workflow is designed to use the telemetry actually available in the lab, including:

- **Wazuh:** centralized log collection, searching, and event investigation.
- **Windows Event Logs:** Windows security and PowerShell operational events, where enabled and collected.
- **Sysmon:** process creation and other configured endpoint telemetry.
- **Network telemetry:** available network logs or observations, where configured.

Telemetry availability depends on endpoint configuration, collection settings, and successful ingestion into the relevant platform. The presence of a data source in the architecture does not by itself prove that usable events are available.

## Repository Structure

```text
03-threat-hunting/
├── README.md
├── hunts/
│   └── TH-001-powershell-abuse/
│       ├── README.md
│       ├── hypothesis.md
│       ├── methodology.md
│       ├── queries.md
│       ├── findings.md
│       ├── recommendations.md
│       └── evidence/
│           └── README.md
├── queries/
│   ├── README.md
│   ├── wazuh/
│   ├── windows/
│   ├── sysmon/
│   └── network/
└── evidence/
    └── README.md
```

The hunt-specific directory contains the investigation plan, hypothesis, queries, findings, and recommendations. The shared `queries/` directory is intended for reusable query implementations, while the root `evidence/` directory can hold evidence shared across multiple hunts.

## Evidence and Reporting Standards

- Record the query, source, time range, and relevant filters used during an investigation.
- Preserve relevant timestamps and event identifiers.
- Capture genuine screenshots from the lab environment.
- Distinguish observed facts from hypotheses and interpretations.
- Record negative results and telemetry limitations accurately.
- Do not classify activity as malicious solely because it involves PowerShell or another administrative tool.
- Do not invent findings, test outcomes, screenshots, or metrics.

## Completion Criteria

A hunt may be marked complete when its hypothesis has been evaluated against available evidence, the investigative process and queries are documented, the findings and limitations are recorded, and actionable recommendations have been considered.

## Current Progress

The current investigation is TH-001: PowerShell Abuse. The next activities are to verify endpoint telemetry, execute the hunting queries, review the results, and document evidence-based findings.

This section is maintained as part of the Enterprise SOC Detection Lab and supports continuous improvement of threat visibility, detection engineering, and incident investigation.

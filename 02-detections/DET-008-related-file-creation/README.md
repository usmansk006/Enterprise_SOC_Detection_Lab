# DET-007: Relevant network activity

## Hypothesis

`mshta.exe` network activity can help identify whether an HTA file is reaching external infrastructure. Even an otherwise benign HTA may be suspicious when it opens outbound channels to unusual destinations or communicates with unapproved infrastructure.

## Telemetry

- Sysmon Event ID 3 (`NetworkConnect`)
- `Image`
- `DestinationIp`
- `DestinationPort`
- `Protocol`
- `ProcessGuid`

## Detection logic

Correlate `mshta.exe` process creation with outbound network events. Flag unusual destinations, long-lived connections, or remote file retrieval patterns.

## Investigation steps

- determine the requested remote URL or service,
- review destination IP and domain,
- map to known internal allowlists,
- and correlate with process lineage and file creation.

## Validation status

This detection requires network telemetry validation and is documented as a high-context scenario.

# Limitations and evasion considerations

Detection engineering for `mshta.exe` has several important constraints:

- process execution alone does not reveal intent,
- attackers may use environment variables, encoding, or alternate script wrappers,
- legitimate software may trigger similar patterns,
- and event availability may differ between Windows versions and policies.

## Evasion risk

Attackers may bypass simplistic detection rules by:

- using encoded remote references,
- nesting script strings,
- staging files in user-writable directories,
- or executing through a disguised parent process.

## Recommendation

Use these rules as contextual, analyst-supported detections, not autonomous blocking logic. Pair them with investigation and telemetry validation.

# MITRE ATT&CK mapping

## Relevant techniques

- T1218.005: `Mshta`
- T1059: Command and Scripting Interpreter
- T1071: Application Layer Protocol
- T1105: Ingress Tool Transfer
- T1053: Scheduled Task/Job (when used for persistence or automation)

## Mapping notes

`mshta.exe` is commonly associated with `T1218.005`, especially when used as a script host or execution vector. Additional context, such as network connections and script abuse, may also align with other ATT&CK techniques depending on the observed behavior.

## Operational caveat

ATT&CK mapping should be used as an analyst aid, not as proof of malicious intent on its own.

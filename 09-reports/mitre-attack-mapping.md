# MITRE ATT&CK Mapping

This mapping documents how the HTA detection set aligns with ATT&CK concepts.

| Technique | Description | Use in this lab |
| --- | --- | --- |
| T1218.005 | Mshta | Primary technique for HTA execution detection |
| T1059 | Command and Scripting Interpreter | Inline script and command-line indicators |
| T1105 | Ingress Tool Transfer | Relevant when HTA fetches remote content |
| T1566 | Phishing | could be involved in initial lure delivery |
| T1027 | Obfuscated Files or Information | command-line obfuscation |
| T1055 | Process Injection | related child or parent process anomalies |

## Caveat

ATT&CK mapping is contextual and should not be used as proof of maliciousness without supporting telemetry.

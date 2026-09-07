# INV-001 — Investigation Timeline

## Timeline Objective

This timeline reconstructs the sequence of events identified during the investigation using available Wazuh and Sysmon telemetry.

---

## Event Timeline

| Timestamp | Timezone | Event | Source | Analyst Interpretation |
|---|---|---|---|---|
| 2026-09-05 07:17:34.400 | UTC | PowerShell process created using `-EncodedCommand` | Sysmon Event ID 1 | Encoded PowerShell execution initiated |
| 2026-09-05 07:17:34.788 | UTC | PowerShell process terminated | Sysmon Event ID 5 | Process terminated shortly after execution |
| 2026-09-05 12:47:35 | Dashboard local time | Wazuh alert generated | Wazuh Rule 100105 | Encoded PowerShell activity detected |

---

## Process Lifecycle

The Sysmon telemetry identified the following process lifecycle:

```text
07:17:34.400 UTC
        │
        ▼
PowerShell Process Created
powershell.exe -EncodedCommand
        │
        │ 388 milliseconds
        ▼
07:17:34.788 UTC
PowerShell Process Terminated
````

---

## Timestamp Correlation

The Sysmon process creation event occurred at:

```text
2026-09-05 07:17:34.400 UTC
```

The Wazuh alert was displayed at approximately:

```text
2026-09-05 12:47:35
```

The difference is consistent with a UTC and IST (+05:30) display difference.

The timestamps therefore appear consistent with the same underlying activity.

---

## Timeline Assessment

The available telemetry shows a short-lived PowerShell process executing an encoded command.

The process:

1. Was created using the `-EncodedCommand` parameter.
2. Executed under the `labadmin` user account.
3. Terminated approximately 388 milliseconds after creation.
4. Generated a Wazuh alert mapped to PowerShell execution.

The decoded command content was analyzed separately during the technical investigation.

---

## Timeline Limitations

The timeline is based on the telemetry collected and available within the laboratory environment.

Events not collected by the configured data sources cannot be represented in this timeline.

Then we will create **`06-findings.md`**. This is where we formally separate **confirmed facts, observations, limitations, and the final verdict**.

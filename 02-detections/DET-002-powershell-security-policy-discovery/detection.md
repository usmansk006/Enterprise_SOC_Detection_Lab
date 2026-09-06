# Detection Details — DET-002

## 1. Detection Objective

Detect PowerShell activity involving the Windows `secedit` utility.

The detection was developed to identify PowerShell commands that may be associated with Windows security policy discovery.

The controlled test command was:

```powershell
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

The objective is not to classify all `secedit` activity as malicious.

Instead, the detection provides visibility into potentially relevant security configuration discovery activity for SOC investigation.

---

## 2. Threat Behavior

`secedit` is a legitimate Windows utility used to manage and analyze security configuration.

The controlled activity exported Windows security policy configuration to a temporary file.

Potential information available through security policy discovery may include:

* Security configuration
* Password policy settings
* Account policy settings
* Local security settings

The activity requires contextual investigation because legitimate administrators may use `secedit`.

---

## 3. Telemetry Source

### Primary Telemetry

**PowerShell Script Block Logging**

| Field              | Value                                    |
| ------------------ | ---------------------------------------- |
| Platform           | Windows                                  |
| Log Channel        | Microsoft-Windows-PowerShell/Operational |
| Windows Event ID   | 4104                                     |
| Telemetry Type     | PowerShell Script Block Logging          |
| Detection Platform | Wazuh                                    |

PowerShell Script Block Logging provides visibility into PowerShell script content.

The detection uses Event ID `4104` because the original planned process creation telemetry, Windows Event ID `4688`, was not available in the lab environment.

The detection approach was therefore changed to use available and validated telemetry.

---

## 4. Detection Telemetry

The controlled PowerShell activity generated:

```text
Windows Event ID: 4104

Channel:
Microsoft-Windows-PowerShell/Operational
```

The relevant PowerShell Script Block content contained:

```text
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

This confirmed the following telemetry pipeline:

```text
PowerShell Execution
        ↓
PowerShell Script Block Logging
        ↓
Windows Event ID 4104
        ↓
Wazuh Agent
        ↓
Wazuh Manager
        ↓
Wazuh Indexer
        ↓
Wazuh Dashboard
```

---

## 5. Detection Platform

**Wazuh**

The Wazuh Agent monitors:

```text
Microsoft-Windows-PowerShell/Operational
```

The Event ID `4104` telemetry is forwarded from the Windows endpoint to the Wazuh Manager for processing.

---

## 6. Base Detection

Before the custom rule was developed, the PowerShell event matched an existing Wazuh rule.

| Field           | Value                                                   |
| --------------- | ------------------------------------------------------- |
| Base Rule ID    | 91816                                                   |
| Base Rule Level | 4                                                       |
| Description     | Powershell script querying system environment variables |

The base rule confirmed that the PowerShell telemetry was successfully reaching Wazuh.

However, the base rule was not specific to the DET-002 objective.

A custom detection was therefore created.

---

## 7. Custom Detection Rule

The DET-002 custom rule was created in:

```text
/var/ossec/etc/rules/local_rules.xml
```

The final rule is:

```xml
<rule id="100102" level="8">
  <if_sid>91816</if_sid>
  <field name="win.eventdata.scriptBlockText" type="pcre2">(?i)secedit</field>
  <description>DET-002: PowerShell security policy discovery using secedit</description>
  <group>powershell,discovery,det002,</group>
</rule>
```

---

## 8. Detection Logic

The detection contains two primary conditions.

### Parent Rule

```xml
<if_sid>91816</if_sid>
```

The custom rule builds on Wazuh Rule `91816`.

This ensures that the detection applies to PowerShell-related telemetry already identified by the base rule.

---

### Script Block Matching

```xml
<field name="win.eventdata.scriptBlockText" type="pcre2">(?i)secedit</field>
```

The detection examines the PowerShell Script Block content.

The expression:

```text
(?i)secedit
```

performs a case-insensitive match for the keyword:

```text
secedit
```

---

## 9. Detection Flow

```text
PowerShell Execution
        ↓
secedit /export
        ↓
PowerShell Script Block Logging
        ↓
Windows Event ID 4104
        ↓
Wazuh Agent Collection
        ↓
Wazuh Manager Processing
        ↓
Base Rule 91816
        ↓
Custom Rule 100102
        ↓
DET-002 Alert
```

---

## 10. Alert Details

| Field             | Value                                    |
| ----------------- | ---------------------------------------- |
| Detection ID      | DET-002                                  |
| Custom Rule ID    | 100102                                   |
| Alert Level       | 8                                        |
| Parent Rule       | 91816                                    |
| Event ID          | 4104                                     |
| Log Channel       | Microsoft-Windows-PowerShell/Operational |
| Detection Field   | win.eventdata.scriptBlockText            |
| Detection Pattern | (?i)secedit                              |
| Detection Type    | Custom Wazuh Rule                        |

### Alert Description

```text
DET-002: PowerShell security policy discovery using secedit
```

---

## 11. Detection Test Procedure

The detection was tested in the authorized isolated SOC laboratory.

### Step 1 — Generate Controlled Activity

Execute the controlled PowerShell command:

```powershell
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

### Step 2 — Validate Windows Telemetry

Confirm that Windows generates:

```text
Event ID: 4104

Channel:
Microsoft-Windows-PowerShell/Operational
```

### Step 3 — Validate Wazuh Collection

Confirm that the Wazuh Agent collects the PowerShell event.

### Step 4 — Validate Base Rule Processing

Confirm that Wazuh processes the event using the PowerShell-related base rule.

### Step 5 — Validate Custom Detection

Confirm that the event matches:

```text
Rule ID: 100102

Level: 8
```

### Step 6 — Review the Alert

Confirm that the alert description is:

```text
DET-002: PowerShell security policy discovery using secedit
```

---

## 12. Evidence

The detection was validated using evidence collected during testing.

### Test Execution

Shows the controlled PowerShell activity executed on the Windows endpoint.

```text
evidence/DET-002-01-test-execution.png
```

### PowerShell Telemetry

Shows PowerShell Script Block Logging telemetry containing Event ID `4104`.

```text
evidence/DET-002-02-powershell-event-4104.png
```

### Wazuh Alert

Shows the successful custom Wazuh detection.

```text
evidence/DET-002-03-wazuh-alert.png
```

### Custom Rule

Shows the custom Wazuh detection logic.

```text
evidence/DET-002-04-custom-rule.png
```

---

## 13. MITRE ATT&CK Relevance

The activity involves security configuration discovery.

The custom Wazuh rule itself does not contain a MITRE ATT&CK mapping.

Therefore, no specific ATT&CK technique is claimed by the custom rule.

The base event was associated with Discovery-related information in Wazuh, but this should not be automatically treated as the final ATT&CK classification for DET-002.

Any future ATT&CK mapping should be based on the exact observed behavior and documented detection logic.

---

## 14. False Positives

Legitimate causes may include:

* System administration
* Security configuration audits
* Compliance checks
* Security policy analysis
* Administrative scripts
* Security tools

The presence of `secedit` alone does not indicate malicious activity.

---

## 15. Detection Limitations

The current detection has several limitations.

* `secedit` is a legitimate Windows utility.
* The detection matches the keyword `secedit`.
* The detection does not independently determine malicious intent.
* PowerShell Script Block Logging must be enabled.
* Windows Event ID `4104` must be collected.
* The detection only identifies activity visible in the monitored PowerShell telemetry.
* The current rule does not distinguish all specific `secedit` arguments.
* Activity executed outside PowerShell may not be detected by this rule.

---

## 16. Detection Tuning

Potential improvements include increasing the specificity of the detection.

Examples include matching:

```text
secedit /export
```

instead of detecting every occurrence of:

```text
secedit
```

Additional tuning opportunities include:

* Reviewing expected administrative users
* Identifying approved administrative endpoints
* Allowlisting approved automation
* Matching specific command arguments
* Correlating with Sysmon Event ID 1
* Correlating with Windows Event ID 4688 when available
* Reviewing parent process activity

Tuning should reduce unnecessary alerts without removing useful visibility.

---

## 17. Troubleshooting

The detection development process encountered several issues.

### Issue 1 — Event ID 4688 Was Unavailable

The initial detection design relied on Windows process creation Event ID `4688`.

The required telemetry was not available.

### Resolution

The detection strategy was changed to:

```text
PowerShell Script Block Logging
Event ID 4104
```

---

### Issue 2 — Custom Rule Did Not Initially Trigger

The PowerShell event reached Wazuh and triggered Rule `91816`.

However, the custom Rule `100102` did not initially match.

### Resolution

The actual event structure was reviewed.

The relevant event field was identified as:

```text
data.win.eventdata.scriptBlockText
```

The corresponding Wazuh rule field was:

```text
win.eventdata.scriptBlockText
```

The rule was updated to use the validated normalized field.

---

### Detection Engineering Lesson

```text
Do not assume telemetry field names.

Validate the actual event structure first.
```

---

## 18. Retest Results

After correcting the detection logic, the controlled PowerShell activity was executed again.

The final detection sequence was:

```text
PowerShell Execution
        ↓
Event ID 4104 Generated
        ↓
Wazuh Agent Collection
        ↓
Base Rule 91816
        ↓
Custom Rule 100102
        ↓
DET-002 Alert
        ↓
Level 8 Alert
```

The custom rule successfully triggered.

**Retest Result: Successful**

---

## 19. Detection Status

| Validation Stage                | Result     |
| ------------------------------- | ---------- |
| Controlled Activity             | Successful |
| Event ID 4104 Generation        | Successful |
| PowerShell Telemetry Validation | Successful |
| Wazuh Agent Collection          | Successful |
| Wazuh Event Ingestion           | Successful |
| Base Rule Processing            | Successful |
| Custom Rule Development         | Successful |
| Rule Validation                 | Successful |
| Detection Retest                | Successful |
| Custom Rule Triggered           | Successful |

**Final Status: DET-002 Successfully Validated**

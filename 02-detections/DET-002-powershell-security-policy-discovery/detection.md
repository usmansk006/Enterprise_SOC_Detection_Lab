# Detection Engineering – DET-002

## 1. Detection Objective

The objective of DET-002 was to develop a custom Wazuh detection capable of identifying PowerShell activity involving the Windows `secedit` utility.

The controlled test focused on the following command:

```powershell
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

This command exports Windows security policy configuration to a file.

The detection goal was not to classify all `secedit` activity as malicious. Instead, the goal was to detect and investigate PowerShell activity that may be associated with security configuration discovery.

---

# 2. Initial Detection Approach

The initial detection approach focused on Windows process creation telemetry.

The expected telemetry source was:

```text
Windows Security Event ID 4688
```

Event ID 4688 records process creation activity and can provide useful information for detecting command execution.

However, Event ID 4688 was not available in the lab environment.

Because the required process creation telemetry was unavailable, the detection approach was changed.

This decision was based on the following detection engineering principle:

```text
Detection logic must be based on available and validated telemetry.
```

Instead of continuing to build a detection around missing telemetry, an alternative telemetry source was selected.

---

# 3. Alternative Telemetry Selection

The alternative telemetry source selected was:

```text
PowerShell Script Block Logging
```

PowerShell Script Block Logging records PowerShell code execution.

The relevant Windows event is:

```text
Event ID: 4104

Channel:
Microsoft-Windows-PowerShell/Operational
```

Event ID 4104 provides visibility into PowerShell script block content.

This telemetry source was suitable for the detection because the objective involved identifying specific PowerShell command content.

---

# 4. PowerShell Script Block Logging Validation

Before creating a custom Wazuh rule, the telemetry had to be validated.

The first requirement was confirming that the Windows endpoint was generating PowerShell Event ID 4104 events.

The Wazuh Agent configuration confirmed that the following event channel was being monitored:

```text
Microsoft-Windows-PowerShell/Operational
```

The Wazuh Agent log contained:

```text
Analyzing event log:
'Microsoft-Windows-PowerShell/Operational'
```

This confirmed that the Wazuh Agent was configured to monitor the required PowerShell event channel.

---

# 5. Controlled Activity Generation

A controlled PowerShell command was executed on the Windows 10 lab endpoint.

The command used was:

```powershell
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

The command exports the Windows security policy configuration to a temporary file.

Additional commands were used to inspect and remove the temporary file.

Examples included:

```powershell
Get-Content "$env:TEMP\DET-002-secpol.cfg"
```

and:

```powershell
Remove-Item "$env:TEMP\DET-002-secpol.cfg"
```

These commands generated separate PowerShell Script Block events.

This was an important observation during testing.

PowerShell activity should not always be expected to appear as a single event.

---

# 6. Windows Event ID 4104 Validation

After executing the controlled PowerShell activity, the event was successfully observed in Wazuh.

The relevant event contained:

```text
data.win.system.eventID: 4104
```

The event channel was:

```text
Microsoft-Windows-PowerShell/Operational
```

The PowerShell Script Block content contained:

```text
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

This confirmed the following:

1. PowerShell Script Block Logging was functioning.
2. Windows generated Event ID 4104.
3. The Wazuh Agent collected the event.
4. The event was forwarded to the Wazuh Manager.
5. The event was visible in the Wazuh Dashboard.

At this stage, the telemetry pipeline was confirmed.

---

# 7. Telemetry Pipeline

The complete telemetry flow was:

```text
PowerShell Execution
        ↓
PowerShell Script Block Logging
        ↓
Windows Event ID 4104
        ↓
Microsoft-Windows-PowerShell/Operational
        ↓
Wazuh Agent
        ↓
Wazuh Manager
        ↓
Wazuh Indexer
        ↓
Wazuh Dashboard
```

This validation was necessary before developing the custom detection.

A detection rule should not be blamed before confirming that the underlying telemetry is actually reaching the SIEM.

---

# 8. Initial Wazuh Event

The PowerShell event initially triggered an existing Wazuh rule.

The event was associated with:

```text
Rule ID: 91816
Rule Level: 4
```

The rule description was:

```text
Powershell script querying system environment variables
```

The event also contained MITRE ATT&CK information:

```text
Tactic: Discovery
Technique: T1082
Technique Name: System Information Discovery
```

However, the existing rule was not specific to the DET-002 detection objective.

A custom detection was therefore required.

---

# 9. Custom Detection Development

The Wazuh local rules file was used to create the custom detection.

The configuration file was:

```text
/var/ossec/etc/rules/local_rules.xml
```

The custom detection was assigned:

```text
Rule ID: 100102
Rule Level: 8
```

The rule was designed to identify PowerShell events containing the keyword:

```text
secedit
```

---

# 10. Initial Custom Rule

The custom rule was added to:

```text
/var/ossec/etc/rules/local_rules.xml
```

The initial detection logic focused on:

- PowerShell events
- Event ID 4104
- Script Block content
- The `secedit` keyword

The objective was to create a more specific detection than the existing base rule.

---

# 11. Wazuh Manager Issue

During the detection development process, the Wazuh Manager experienced a startup failure.

The service showed a failed state.

This required troubleshooting before detection development could continue.

The Wazuh Manager configuration and service status were checked.

The Manager was restarted and its operational status was verified.

After troubleshooting, the Wazuh Manager successfully returned to an operational state.

This was an important reminder that detection development depends on the health of the entire detection infrastructure.

A custom rule cannot be tested if the Wazuh Manager is not processing events.

---

# 12. Initial Detection Failure

After creating the initial custom detection, the expected custom alert did not trigger.

Instead, the PowerShell event continued to match the existing Wazuh rule:

```text
Rule ID: 91816
```

This indicated that the telemetry was successfully reaching Wazuh, but the custom rule was not matching as expected.

The issue was therefore narrowed down to detection logic rather than event collection.

This distinction was important:

```text
Telemetry Problem?
        No

Wazuh Agent Problem?
        No

Event Ingestion Problem?
        No

Detection Rule Problem?
        Yes
```

---

# 13. Rule Troubleshooting

The event fields were reviewed directly in the Wazuh Dashboard.

The relevant event field was identified as:

```text
data.win.eventdata.scriptBlockText
```

The corresponding Wazuh rule field was:

```text
win.eventdata.scriptBlockText
```

The event contained:

```text
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

The detection logic was updated to match the actual event structure.

This troubleshooting step demonstrated an important detection engineering principle:

```text
Detection rules must be based on the actual normalized event fields.
```

Assumptions about field names should not be used without validating the event data.

---

# 14. Final Detection Rule

The final custom rule was:

```xml
<rule id="100102" level="8">
  <if_sid>91816</if_sid>
  <field name="win.eventdata.scriptBlockText" type="pcre2">(?i)secedit</field>
  <description>DET-002: PowerShell security policy discovery using secedit</description>
  <group>powershell,discovery,det002,</group>
</rule>
```

The rule contains the following logic.

## Parent Rule

```xml
<if_sid>91816</if_sid>
```

The custom rule builds on Wazuh Rule ID 91816.

This ensures that the custom detection applies to events already identified as PowerShell-related.

---

## Script Block Matching

```xml
<field name="win.eventdata.scriptBlockText" type="pcre2">(?i)secedit</field>
```

The detection examines the PowerShell Script Block content.

The expression:

```text
(?i)secedit
```

performs a case-insensitive match for:

```text
secedit
```

---

## Alert Severity

The detection uses:

```text
Level: 8
```

This provides a higher severity than the original base event.

The increased severity reflects the fact that the event matches a specific detection use case.

However, severity does not automatically indicate malicious activity.

---

# 15. Wazuh Rule Validation

After modifying the detection rule, the Wazuh configuration was validated.

Configuration validation was performed before relying on the rule in production testing.

This step is important because:

- XML syntax errors can prevent rule loading.
- Invalid configurations can affect the Wazuh Manager.
- Incorrect rules can cause unexpected detection behavior.

The configuration was successfully validated before continuing.

---

# 16. Wazuh Manager Restart

After the rule configuration was validated, the Wazuh Manager was restarted.

The service status was checked to confirm that the Manager was operational.

The Wazuh Manager successfully started.

This confirmed that the custom rule did not introduce a configuration issue that prevented the Manager from running.

---

# 17. Detection Retest

The controlled PowerShell activity was executed again:

```powershell
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

The following sequence was expected:

```text
PowerShell Execution
        ↓
Event ID 4104
        ↓
Wazuh Agent Collection
        ↓
Wazuh Event Processing
        ↓
Rule 91816
        ↓
Custom Rule 100102
        ↓
DET-002 Alert
```

The event was then reviewed in the Wazuh Dashboard.

---

# 18. Successful Detection

The final test successfully triggered the custom Wazuh rule.

The final alert contained:

```text
Rule ID: 100102
```

The alert level was:

```text
Level: 8
```

The detection description was:

```text
DET-002: PowerShell security policy discovery using secedit
```

The event also confirmed:

```text
Event ID: 4104

Channel:
Microsoft-Windows-PowerShell/Operational
```

The Script Block content contained:

```text
secedit /export /cfg "$env:TEMP\DET-002-secpol.cfg"
```

This successfully validated the detection.

---

# 19. Final Detection Result

The final detection pipeline was successfully validated:

```text
[Windows 10 Endpoint]

PowerShell Execution
        ↓

secedit /export

        ↓

PowerShell Script Block Logging
        ↓

Event ID 4104
        ↓

Wazuh Agent
        ↓

Wazuh Manager
        ↓

Rule 91816
        ↓

Custom Rule 100102
        ↓

DET-002 Alert
        ↓

Level 8 Alert
```

---

# 20. Challenges Encountered

## Challenge 1: Event ID 4688 Was Not Available

### Problem

The original detection approach depended on Windows Event ID 4688.

The required process creation telemetry was not available.

### Resolution

The detection approach was changed to PowerShell Script Block Logging.

Event ID 4104 provided the required visibility into PowerShell command content.

### Lesson

```text
Do not build detection logic around telemetry that does not exist.
```

---

## Challenge 2: Event ID 4104 Was Not Initially Visible

### Problem

PowerShell telemetry needed to be confirmed in the Wazuh Dashboard.

### Resolution

The Wazuh Agent log was reviewed.

The following configuration was confirmed:

```text
Microsoft-Windows-PowerShell/Operational
```

PowerShell Event ID 4104 was then successfully observed.

### Lesson

```text
Always validate telemetry before developing detection logic.
```

---

## Challenge 3: Wazuh Manager Startup Failure

### Problem

The Wazuh Manager entered a failed state during development.

### Resolution

The service and configuration were checked and the Manager was restored to an operational state.

### Lesson

```text
Detection engineering depends on infrastructure reliability.
```

---

## Challenge 4: Custom Rule Did Not Initially Trigger

### Problem

The PowerShell event triggered Rule 91816 instead of the custom Rule 100102.

### Resolution

The actual event structure was reviewed in Wazuh.

The Script Block field was identified and used in the final rule:

```text
win.eventdata.scriptBlockText
```

### Lesson

```text
Write detections using actual event fields, not assumptions.
```

---

## Challenge 5: Multiple PowerShell Events

### Problem

The controlled activity generated multiple PowerShell Event ID 4104 events.

Examples included:

```text
secedit
Get-Content
Remove-Item
```

Each command could generate a separate Script Block event.

### Resolution

The relevant event containing the `secedit` command was identified and used for detection validation.

### Lesson

```text
Understand how the telemetry source represents activity.
```

One user action may generate multiple events.

---

# 21. Detection Engineering Lessons

This detection demonstrated several important principles.

## Telemetry First

Before creating detection logic, confirm that:

```text
The activity occurred.
        ↓
The endpoint generated telemetry.
        ↓
The agent collected telemetry.
        ↓
The SIEM received telemetry.
```

Only after these steps should detection logic be developed.

---

## Investigate Detection Failures Systematically

When a detection does not trigger:

```text
Activity
   ↓
Did the activity execute?
   ↓
Was telemetry generated?
   ↓
Was telemetry collected?
   ↓
Did the SIEM ingest the event?
   ↓
Did a base rule match?
   ↓
Did the custom rule match?
```

This prevents random troubleshooting.

---

## Use Real Event Data

Detection rules should be based on:

```text
Actual Event Fields
```

and not assumptions.

The Wazuh Dashboard event details were used to identify the correct Script Block field.

---

## Retest After Changes

Detection development is iterative:

```text
Develop
   ↓
Test
   ↓
Fail
   ↓
Investigate
   ↓
Modify
   ↓
Retest
   ↓
Validate
```

The final detection was confirmed only after the controlled activity was executed again.

---

# 22. Limitations

The current detection has limitations.

The rule detects PowerShell Script Block content containing:

```text
secedit
```

This does not automatically indicate malicious behavior.

Legitimate use cases may include:

- System administration
- Security configuration audits
- Compliance checks
- Security tools
- Administrative scripts

Therefore, additional context should be reviewed during investigation.

Potential future improvements include:

- Command-line context
- User context
- Parent process analysis
- Process creation telemetry
- Host-based baselining
- Allowlisting approved administrative activity
- More specific command pattern matching

---

# 23. Future Improvements

The detection can be improved by increasing specificity.

Potential improvements include detecting specific `secedit` command patterns.

For example:

```text
secedit /export
```

Additional telemetry could also improve investigation.

Useful telemetry sources include:

```text
Sysmon Event ID 1
Windows Event ID 4688
PowerShell Event ID 4104
```

Combining multiple telemetry sources would provide stronger detection context.

---

# 24. Final Status

```text
Telemetry Validation: SUCCESS

Windows Event ID 4104: SUCCESS

Wazuh Agent Collection: SUCCESS

Wazuh Event Ingestion: SUCCESS

Custom Rule Development: SUCCESS

Wazuh Rule Validation: SUCCESS

Detection Retest: SUCCESS

Custom Rule Triggered: SUCCESS
```

---

# 25. Conclusion

DET-002 was successfully developed as a custom Wazuh detection for PowerShell activity involving the `secedit` utility.

The project required changing the original detection approach after Event ID 4688 telemetry was unavailable.

PowerShell Script Block Logging and Event ID 4104 were selected as the alternative telemetry source.

The detection development process involved:

```text
Telemetry Selection
        ↓
Telemetry Validation
        ↓
Controlled Activity
        ↓
Wazuh Event Collection
        ↓
Event Analysis
        ↓
Custom Rule Development
        ↓
Troubleshooting
        ↓
Rule Correction
        ↓
Retesting
        ↓
Successful Detection
```

The final custom Wazuh rule successfully generated:

```text
Rule ID: 100102
Level: 8

DET-002: PowerShell security policy discovery using secedit
```

The detection demonstrates a complete practical detection engineering workflow rather than simply creating a rule and assuming it works.

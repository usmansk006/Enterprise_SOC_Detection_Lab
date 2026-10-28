# Windows event queries

Example event review patterns for local analysis and threat hunting:

```powershell
# Process creation review for mshta.exe
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" | Where-Object {$_.Message -match "mshta.exe"}

# Review process creation events with command line
Get-WinEvent -LogName "Security" -FilterXPath "*[System[(EventID=4688)]]" | Select-Object TimeCreated, @{Name='Message';Expression={$_.Message}}
```

Use these queries as starting points only. Confirm field names and event availability in the target environment before operationalizing them.

# PowerShell snippets

Example snippets for telemetry and investigation support:

```powershell
Get-CimInstance Win32_Process | Where-Object {$_.Name -match "mshta"}
Get-WinEvent -LogName "Security" -FilterXPath "*[System[(EventID=4688)]]" | Select-Object TimeCreated, Id, Message
```

These are local investigation utilities and not a replacement for Sysmon or a full SIEM pipeline.

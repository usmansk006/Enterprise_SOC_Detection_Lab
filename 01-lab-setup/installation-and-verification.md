<Sysmon schemaversion="4.90">
  <EventFiltering>
    <ProcessCreate onmatch="include">
      <Image condition="is">C:\Windows\System32\mshta.exe</Image>
      <CommandLine condition="contains">mshta</CommandLine>
      <ParentImage condition="contains">powershell.exe</ParentImage>
      <ParentImage condition="contains">cmd.exe</ParentImage>
      <ParentImage condition="contains">rundll32.exe</ParentImage>
      <ParentImage condition="contains">wmic.exe</ParentImage>
      <ParentImage condition="contains">wscript.exe</ParentImage>
      <ParentImage condition="contains">cscript.exe</ParentImage>
    </ProcessCreate>

    <NetworkConnect onmatch="include">
      <Image condition="is">C:\Windows\System32\mshta.exe</Image>
      <Image condition="is">C:\Windows\System32\cmd.exe</Image>
      <Image condition="is">C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe</Image>
    </NetworkConnect>

    <FileCreate onmatch="include">
      <TargetFilename condition="contains">.hta</TargetFilename>
      <TargetFilename condition="contains">Temp</TargetFilename>
      <TargetFilename condition="contains">AppData</TargetFilename>
    </FileCreate>
  </EventFiltering>
</Sysmon>

# Investigation — DET-008

## 1. Investigation Objective

Investigate a Wazuh alert generated for the use of `certutil.exe` to decode a file.

The objective is to determine:

* What process executed CertUtil
* Which user executed the process
* What command was used
* Which process launched CertUtil
* Whether the activity appears authorized
* Whether additional investigation is required

---

## 2. Alert Summary

| Field              | Value                    |
| ------------------ | ------------------------ |
| Detection ID       | DET-008                  |
| Alert Description  | Certutil decoding a file |
| Wazuh Rule ID      | 92072                    |
| Detection Platform | Wazuh                    |
| Endpoint           | WIN10-LAB                |
| Telemetry Source   | Sysmon                   |
| Event ID           | 1                        |
| ATT&CK Technique   | T1140                    |

The alert indicates that `certutil.exe` was executed with the `-decode` argument.

---

## 3. Initial Triage

The first step is to determine whether the alert represents:

1. Authorized administrative activity
2. Security testing
3. Suspicious LOLBin abuse
4. Potential malicious activity

`certutil.exe` is a legitimate Windows binary. Therefore, the presence of the executable alone is insufficient to classify the event as malicious.

The command line and surrounding process context must be reviewed.

---

## 4. Process Analysis

The Sysmon Process Create event should be reviewed.

Important fields include:

```text
Image
CommandLine
ParentImage
ParentCommandLine
User
ProcessGuid
ParentProcessGuid
Hashes
```

### Process Image

The process image identifies the executable:

```text
C:\Windows\System32\certutil.exe
```

This confirms that the process was the legitimate Windows CertUtil binary.

---

## 5. Command-Line Analysis

The command line is the primary detection indicator.

The test behavior included:

```text
certutil.exe -decode C:\Temp\det008.b64 C:\Temp\det008-decoded.txt
```

Important investigation questions:

* What file was decoded?
* Where was the source file located?
* Where was the output file written?
* Is the output directory unusual?
* Is the command expected for the executing user?

The `-decode` argument triggered the Wazuh detection.

---

## 6. Parent Process Analysis

The parent process should be reviewed to understand how CertUtil was launched.

During the test, the parent process was:

```text
powershell.exe
```

Parent-child relationships provide important context.

Examples of potentially suspicious scenarios include:

```text
Office Application
      ↓
PowerShell
      ↓
CertUtil
```

or:

```text
Script Host
      ↓
CertUtil
```

A parent process should always be evaluated in context.

---

## 7. User Analysis

The executing user should be identified.

Questions to investigate:

* Is the user expected to perform this activity?
* Is the account privileged?
* Was the activity performed interactively?
* Is the execution time normal?
* Has the user performed similar activity previously?

In this lab, the activity was performed by an authorized user during controlled security testing.

---

## 8. File Analysis

The investigator should review both files involved in the operation.

### Source File

```text
C:\Temp\det008.b64
```

Questions:

* When was the file created?
* What created it?
* Is the content expected?
* Does the file originate from a trusted source?

### Output File

```text
C:\Temp\det008-decoded.txt
```

Questions:

* What is the decoded content?
* Is the output executable or script content?
* Was the file subsequently executed?
* Does the file contain suspicious data?

In this lab, the test file contained harmless test data.

---

## 9. Process Tree Investigation

A simplified process tree for the lab activity:

```text
PowerShell
    │
    └── certutil.exe
            │
            └── Decodes test file
```

The process tree helps determine whether CertUtil execution is part of a legitimate workflow or suspicious activity.

---

## 10. Additional Investigation Steps

If the activity appears suspicious, investigate:

### A. Additional CertUtil Activity

Search for:

* Other `certutil.exe` executions
* Repeated `-decode` activity
* Unusual CertUtil arguments
* Executions by the same user

### B. Related Processes

Review:

* Parent processes
* Child processes
* Subsequent execution of decoded files

### C. File Activity

Investigate:

* Source file creation
* Output file creation
* File hashes
* File locations

### D. User Activity

Review:

* Other processes executed by the user
* Login activity
* Privilege changes
* Unusual command execution

---

## 11. Threat Hunting Opportunities

This detection can be expanded into a threat hunt.

Potential hunt questions:

### Hunt Question 1

> Has CertUtil been executed on other endpoints?

### Hunt Question 2

> Are other CertUtil commands being used?

### Hunt Question 3

> Are decoded files subsequently executed?

### Hunt Question 4

> Are unusual parent processes launching CertUtil?

### Hunt Question 5

> Are users executing CertUtil from unusual directories or contexts?

---

## 12. False Positive Analysis

CertUtil is a legitimate Windows utility.

Potential legitimate causes include:

* Administrative activity
* Automation scripts
* Software deployment
* Troubleshooting
* Authorized security testing

Before escalating the alert, the analyst should validate:

```text
User
+
Command Line
+
Parent Process
+
Files
+
Execution Context
```

---

## 13. Investigation Decision

The observed activity was classified as:

```text
Authorized Security Testing
```

Reason:

* The activity occurred in an isolated lab environment.
* A harmless test file was used.
* The CertUtil command was intentionally executed.
* The resulting Wazuh alert was expected.

---

## 14. Response

Because the activity was authorized testing:

```text
No containment required.
No account action required.
No endpoint isolation required.
```

However, in a production environment, suspicious CertUtil decoding should be investigated further.

Potential response actions may include:

* Investigating the source and output files
* Reviewing process ancestry
* Reviewing the executing user
* Searching for related activity
* Determining whether decoded content was executed

---

## 15. Investigation Outcome

The investigation successfully confirmed the complete detection chain:

```text
CertUtil Execution
        ↓
Sysmon Event ID 1
        ↓
Wazuh Alert
        ↓
Process and Command-Line Review
        ↓
Parent Process Analysis
        ↓
File Context Analysis
        ↓
Authorized Lab Activity Confirmed
```

**Final Classification: Authorized Security Testing**

---

## 16. Lessons Learned

This investigation demonstrates that LOLBin detections require context.

The execution of a legitimate Windows binary is not automatically malicious.

Effective investigation requires analysis of:

* Process image
* Command line
* Parent process
* User context
* File activity
* Process ancestry
* Subsequent activity

Detection should identify potentially suspicious behavior, while investigation determines whether the behavior is actually malicious or authorized.

---

## Final Status

| Investigation Stage     | Result                      |
| ----------------------- | --------------------------- |
| Alert Reviewed          | Completed                   |
| Process Analyzed        | Completed                   |
| Command Line Reviewed   | Completed                   |
| Parent Process Reviewed | Completed                   |
| User Context Reviewed   | Completed                   |
| File Context Reviewed   | Completed                   |
| Authorization Confirmed | Completed                   |
| Final Classification    | Authorized Security Testing |

**DET-008 Investigation: Completed**

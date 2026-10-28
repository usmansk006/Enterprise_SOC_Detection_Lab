# Detection gaps

## Telemetry gaps

- missing parent-process lineage,
- absent command-line logging,
- event loss or log retention gaps,
- incomplete file creation or network telemetry,
- inconsistent Sysmon coverage across endpoint versions.

## Logic gaps

- process creation alone does not show purpose,
- remote URLs may be legitimate internal services,
- some malicious behavior may be encoded or split across multiple events,
- and native logs may not capture all script execution details.

## Improvement roadmap

- add more synthetic fixtures and lab telemetry,
- tune rules against real-world benign patterns,
- document confidence and overlap across detection families,
- and align detections with actual field availability.

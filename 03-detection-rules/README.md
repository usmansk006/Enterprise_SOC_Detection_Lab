# DET-010: Correlated multi-event HTA behavior

## Hypothesis

The strongest HTA detections usually arise from a sequence: `mshta.exe` launch, remote or script-like command line, file creation, and often a suspicious child process or network event. A single event is less reliable than correlated behavior.

## Telemetry

- `ProcessCreate`
- `FileCreate`
- `NetworkConnect`
- `ParentImage`
- `CommandLine`
- `ProcessGuid`

## Detection logic

Construct a minimal timeline around HTA execution and correlate the likely `mshta.exe` process with script artifacts, network destinations, and child processes.

## Investigation steps

- establish the event sequence,
- determine whether the HTA was launched from a shell or script,
- inspect related source files,
- and assess whether external destination or child execution matches suspicious behavior.

## Validation status

Correlated model documented and ready for lab-based validation. The repository does not claim this detection is confirmed without evidence.

# Negative tests

Negative tests are designed to evaluate whether a detection avoids over-alerting on common, benign behavior.

## Example benign scenarios

- a legitimate internal administrative `.hta` file,
- `mshta.exe` invoked by an approved enterprise tool,
- user-generated help content in a controlled environment,
- repeated local process execution that lacks suspicious context.

## Use

These cases help protect against false positives and establish a realistic level of confidence before lab execution.

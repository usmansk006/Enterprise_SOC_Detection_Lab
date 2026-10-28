# Negative Tests

This content documents benign or expected non-malicious cases.

## Negative scenarios

- legitimate sign-in or internal IT support script loads an HTA file
- administrative tool launches a local `.hta` file for approved workflow
- `mshta.exe` calls a user-approved internal help application
- false-positive process lineage due to normal parent-child relationships

## Expected result

The detection logic should avoid flagging these without surrounding suspicious context.

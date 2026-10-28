# False-positive analysis

## Common false positives

- internal help applications using HTA,
- approved admin or support tooling,
- custom enterprise wrappers built around `mshta.exe`,
- user-generated local files in `%Temp%` or Downloads,
- or script automation that legitimately launches HTA for local tasks.

## Mitigation strategy

- prioritize suspicious parent-child logic,
- require more than one strong signal,
- correlate with network or file creation events,
- and document the trade-off between detection sensitivity and noise.

## Confidence guidance

- single `mshta.exe` execution: low to medium confidence,
- remote URL or script pattern: medium to high confidence,
- correlated process + network + file creation: highest confidence, but still hypothesis-driven.

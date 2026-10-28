# Validation Framework

This directory stores the formal validation matrix, synthetic fixtures, and artifact expectations.

## Structure

- `test-matrix.csv`: end-to-end validation matrix
- `positive-tests/`: expected suspicious activity cases
- `negative-tests/`: expected benign activity cases
- `regression-tests/`: stability checks
- `event-fixtures/`: synthetic event records used in tests
- `results/`: results and evidence references

## Status expectations

Live Windows validation has not been performed in this environment. Any test marked as `NOT_RUN` must remain clearly labeled as such.

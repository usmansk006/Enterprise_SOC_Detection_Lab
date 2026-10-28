# Validation Methodology

The repository uses a layered validation model.

## Validation layers

1. Schema and syntax checks for YAML and Python code
2. Input validation for parser and correlation scripts
3. Unit tests for normal, malformed, and boundary conditions
4. detection rule review against telemetry assumptions
5. scenario-based synthetic fixtures and negative tests
6. honest live validation status reporting

## Status labels

- `IMPLEMENTED`: available in repository with documentation and code
- `TESTED`: unit tests or fixtures executed successfully in this environment
- `NOT_RUN`: live lab testing not performed
- `PLANNED`: conceptual work not yet implemented

## Evidence expectations

Each detection or test case should tie back to a fixture or documented procedure. Synthetic data must be clearly labeled as synthetic and never presented as operational evidence.

# Local analysis toolkit

This toolkit provides a minimal set of Python utilities for handling event data, validating YAML-like rule structure, and correlating Windows process events.

## Included tools

- `event-parser.py`: parse JSON and JSONL event input safely
- `rule-validator.py`: perform basic structural checks on Sigma-style YAML
- `event-correlator.py`: correlate process events using timestamps and GUIDs when available

## Usage

```bash
python 06-local-analysis-toolkit/event-parser.py --input 04-validation/event-fixtures/sample-mshta-process.json
python 06-local-analysis-toolkit/rule-validator.py --input 02-detections/DET-001-mshta-execution/det-001-mshta-execution.yml
python 06-local-analysis-toolkit/event-correlator.py --input 04-validation/event-fixtures/sample-mshta-process.json
```

## Notes

These scripts are deliberately lightweight and rely on standard library components where possible. Full Sigma compatibility requires a broader validation workflow or a dedicated Sigma parser.

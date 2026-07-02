# api-error-taxonomy

> Lint API error taxonomies for ambiguous codes and missing retry guidance.

## Workflow Overview

Lint API error taxonomies for ambiguous codes and missing retry guidance. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts API error taxonomy. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
api-error-taxonomy examples/sample.txt
api-error-taxonomy examples/sample.txt --json --fail-on medium
python -m api_error_taxonomy --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-error` | high | unknown error code detected |
| `unknown-retry` | medium | retry guidance missing |
| `ambiguous-message` | low | message is ambiguous |

## Validation Notes

```bash
ruff check .
pytest
python -m api_error_taxonomy --help
```

Example risky input:

```text
error UNKNOWN retry unknown http 500 message ambiguous
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.

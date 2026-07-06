# API Error Taxonomy

Lint API error taxonomies for ambiguous codes and missing retry guidance. This repo keeps the work close to the terminal: clear input, predictable output, and no service to babysit.

## Project card

<img src="assets/readme-cover.svg" alt="API Error Taxonomy cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | api contracts |
| Command | `api-error-taxonomy` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `unknown-error` | high | unknown error code detected |
| `unknown-retry` | medium | retry guidance missing |
| `ambiguous-message` | low | message is ambiguous |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/api-error-taxonomy.git
cd api-error-taxonomy
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
api-error-taxonomy examples/sample.txt
api-error-taxonomy examples/sample.txt --json
```

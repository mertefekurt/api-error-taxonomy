<img src="assets/readme-cover.svg" alt="API Error Taxonomy cover" width="100%" />

# API Error Taxonomy

Lint API error taxonomies for ambiguous codes and missing retry guidance.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `api-error-taxonomy` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `unknown-error` | high | unknown error code detected |
| `unknown-retry` | medium | retry guidance missing |
| `ambiguous-message` | low | message is ambiguous |

## Command line

```bash
python -m pip install -e ".[dev]"
api-error-taxonomy examples/sample.txt
api-error-taxonomy examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
error UNKNOWN retry unknown http 500 message ambiguous
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```

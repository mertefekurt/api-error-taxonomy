from __future__ import annotations

from api_error_taxonomy.models import Rule

PROJECT_NAME = 'api-error-taxonomy'
SUMMARY = 'Lint API error taxonomies for ambiguous codes and missing retry guidance.'
SAMPLE_RISK = 'error UNKNOWN retry unknown http 500 message ambiguous'
SAMPLE_CLEAN = 'error RATE_LIMIT retry after http 429 message clear'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-error',
        severity='high',
        pattern='error\\s+UNKNOWN',
        message='unknown error code detected',
        recommendation='replace with specific error code',
    ),
    Rule(
        code='unknown-retry',
        severity='medium',
        pattern='retry\\s+unknown',
        message='retry guidance missing',
        recommendation='document retry behavior',
    ),
    Rule(
        code='ambiguous-message',
        severity='low',
        pattern='ambiguous',
        message='message is ambiguous',
        recommendation='make message actionable',
    ),
)

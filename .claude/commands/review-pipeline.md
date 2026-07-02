---
description: Review pipeline changes on the current branch for data engineering pitfalls
---
## Changed files
!`git diff --name-only main...HEAD`

## Diff
!`git diff main...HEAD`

Review the changes above as a senior data engineer. Check specifically for:
1. **Idempotency** — will re-running produce duplicates? Any blind INSERTs?
2. **Backfill safety** — any `datetime.now()` instead of execution date? Hardcoded dates?
3. **Incremental correctness** — late-arriving data handled? Lookback window present?
4. **Schema safety** — breaking changes to columns other models depend on? Run `dbt ls -s <model>+` mentally.
5. **Data quality** — new models missing tests or YAML? Audit logging present?
6. **Security** — credentials, PII in logs, SQL injection via f-strings?
7. **Performance** — full table scans, missing partition filters, SELECT *?

Give findings per file, ordered by severity. Be specific with line references.

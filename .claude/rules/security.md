# Security Rules

- NEVER read, print, or log values from `.env`, secret managers, or credential files
- NEVER hardcode connection strings, API keys, tokens — use env var names only
- PII columns (email, phone, name, address) must be tagged in dbt YAML
  (`meta: {pii: true}`) and never appear in logs or sample outputs
- When showing query results in conversation, mask PII columns
- Any new external destination for data (API, bucket, email) requires explicit
  confirmation from the user before implementation
- SQL passed to warehouses must use parametrized queries — never f-string interpolation
  of user-provided values

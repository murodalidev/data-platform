# Data Quality Rules

When creating or modifying any pipeline or dbt model:

1. **Every new dbt model** ships with a YAML file containing:
   - description, grain (in meta), column descriptions
   - tests: `unique` + `not_null` on the primary key at minimum
2. **Every ingestion pipeline** must record row counts (extracted, loaded, rejected)
   to the `_meta.pipeline_runs` audit table via `src/utils/audit.py`
3. **Freshness**: sources declared in dbt `sources.yml` must have `freshness` config
   (warn_after / error_after) appropriate to their SLA
4. **Rejected rows**: schema-invalid rows go to `_meta.rejected_rows` with reason —
   never silently dropped
5. **Volume anomaly guard**: incremental loads that produce 0 rows or > 3x the trailing
   7-day average must raise a warning, not silently succeed
6. Never delete data-quality tests to make a pipeline pass. Fix the data or the logic;
   if a test is genuinely wrong, explain why before changing it.

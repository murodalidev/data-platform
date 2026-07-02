---
description: Produce a safe backfill plan for a pipeline/model over a date range
---
Create a backfill plan for: $ARGUMENTS

1. Identify the affected DAG/models and their downstream dependencies (`dbt ls -s <model>+`).
2. Verify the pipeline is idempotent for the given range; flag anything that isn't.
3. Estimate volume and warehouse cost/time; recommend batch size (per day/week/month).
4. Produce the exact commands (airflow backfill / dbt run with vars), in order,
   including downstream model rebuilds.
5. Define validation queries to run after: row counts per partition vs source,
   PK uniqueness, spot-check aggregates against a known-good period.
6. Define a rollback plan.
Do NOT execute anything — output the plan only.

---
name: airflow-dag-builder
description: Use when creating or modifying Airflow DAGs, tasks, schedules, sensors, or operators. Covers the project's DAG template, idempotency, backfill parametrization, and retry/SLA defaults. Trigger on any mention of DAGs, Airflow, scheduling, or orchestration.
---

# Airflow DAG Builder

## Hard rules
- DAGs orchestrate ONLY — all logic imported from `src/`. If a DAG file exceeds ~150 lines, logic is leaking in.
- Parametrize by `data_interval_start` / `data_interval_end`. NEVER `datetime.now()`.
- `catchup=False` by default; enable only for pipelines designed for backfill.
- Every task idempotent: re-run of the same interval = same result.

## DAG template
```python
from datetime import timedelta
import pendulum
from airflow.decorators import dag, task

DEFAULT_ARGS = {
    "owner": "data-eng",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": True,
}

@dag(
    dag_id="<domain>__<purpose>",
    schedule="0 3 * * *",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    default_args=DEFAULT_ARGS,
    max_active_runs=1,
    tags=["<domain>"],
    doc_md=__doc__,
)
def pipeline():
    @task
    def extract(data_interval_start=None, data_interval_end=None):
        from src.extract.<source>_extractor import <Source>Extractor
        return <Source>Extractor().extract(start=data_interval_start, end=data_interval_end)
    ...

pipeline()
```

## Checklist before finishing
- [ ] `max_active_runs=1` unless parallel runs are proven safe
- [ ] Audit logging task (row counts → `_meta.pipeline_runs`)
- [ ] `doc_md` explains purpose, source, target, grain, on-call notes
- [ ] Failure alerting configured (callback or SLA)

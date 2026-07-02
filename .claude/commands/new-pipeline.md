---
description: Scaffold a complete new data pipeline (extractor + DAG + dbt staging model + tests)
---
Create a new pipeline for: $ARGUMENTS

Follow these steps in order:
1. Ask me (if not clear from the argument): source type, load frequency, incremental key, target schema.
2. Create the extractor in `src/extract/<source>_extractor.py` subclassing `BaseExtractor`,
   with a pydantic schema in `src/extract/schemas/`.
3. Create the DAG in `dags/<domain>__<purpose>.py` — orchestration only, parametrized by
   `data_interval_start/end`, with retries, SLA, and audit logging.
4. Create the dbt staging model `dbt/models/staging/stg_<source>__<entity>.sql` + YAML
   with tests (unique, not_null on PK) and documented grain.
5. Add source to `dbt/models/staging/sources.yml` with freshness config.
6. Write pytest unit tests for the extractor in `tests/unit/`.
7. Run `make lint` and `make test`, fix any failures.
8. Summarize what was created and what manual steps remain (credentials, Airflow connection).

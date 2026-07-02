# CLAUDE.md — Data Platform

## Project Overview
Data engineering platform: ingestion → transformation → serving.
Stack: Python 3.12, Airflow (orchestration), dbt (transformations), PostgreSQL/Snowflake (warehouse), Docker.

## Architecture
- `dags/` — Airflow DAGs. One file per pipeline. Naming: `<domain>__<purpose>.py` (e.g. `sales__daily_ingest.py`)
- `src/extract/` — source connectors (APIs, DBs, files). Each connector returns raw data + metadata.
- `src/transform/` — Python-level transformations (pre-warehouse cleaning only; business logic lives in dbt)
- `src/load/` — warehouse loaders (idempotent upserts, COPY-based bulk loads)
- `src/utils/` — shared helpers (logging, retries, config, secrets)
- `dbt/models/staging/` — 1:1 with sources, renaming/casting only. Prefix: `stg_`
- `dbt/models/intermediate/` — reusable joins/logic. Prefix: `int_`
- `dbt/models/marts/` — business-facing models. Prefix: `fct_` / `dim_`
- `configs/` — YAML configs per environment (dev/staging/prod)
- `tests/` — pytest. Mirror `src/` structure.

## Commands
- `make setup` — install deps (uv sync)
- `make test` — run pytest
- `make lint` — ruff check + sqlfluff lint
- `make dbt-run` — dbt run --profiles-dir ./dbt
- `make dbt-test` — dbt test
- `make airflow-up` — docker compose up (local Airflow)

## Core Principles
1. **Idempotency**: every pipeline must be safely re-runnable. No blind INSERTs — use MERGE/upsert or delete+insert by partition.
2. **Incremental by default**: full refreshes only when explicitly required.
3. **Schema-on-write**: validate schemas at ingestion (pydantic models in `src/extract/schemas/`).
4. **No business logic in DAGs**: DAGs orchestrate only. Logic lives in `src/` or dbt.
5. **Backfill-safe**: all pipelines parametrized by `execution_date` / `data_interval`, never `datetime.now()`.
6. **Secrets**: only via env vars / secret manager. NEVER hardcode credentials.

## Conventions
- Python: type hints required, ruff formatting, Google-style docstrings
- SQL: sqlfluff (dialect from `.sqlfluff`), lowercase keywords, CTEs over subqueries, one column per line in SELECT
- All timestamps in UTC, column suffix `_at` (e.g. `created_at`), dates suffix `_date`
- Table grain must be documented in dbt model YAML (`grain:` in meta)

## Detailed rules
See `.claude/rules/` — loaded automatically:
- `sql-style.md`, `python-style.md`, `data-quality.md`, `security.md`

## Spec-Driven Workflow
Non-trivial features (new pipeline, new mart, migration) follow: **spec → plan → tasks → implement**.
- `specs/<NNN>-<slug>/spec.md` — WHAT & WHY (data contract, grain, SLA). Written via `/create-spec`.
- `specs/<NNN>-<slug>/plan.md` — HOW (components, data flow, backfill, rollback). Via `/create-plan`.
- `specs/<NNN>-<slug>/tasks.md` — checklist of small reviewable steps. Executed via `/implement`.
Rules: never write pipeline code without an approved spec+plan for non-trivial work.
Never skip from spec straight to code. Small fixes (< ~30 lines, no schema change) don't need a spec.
Templates: `specs/_template/`. Example: `specs/001-example-sales-pipeline/`.

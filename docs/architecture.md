# Architecture

Ingestion (src/extract) → Raw schema → dbt staging → intermediate → marts → BI.
Orchestrated by Airflow (dags/). See CLAUDE.md for conventions.

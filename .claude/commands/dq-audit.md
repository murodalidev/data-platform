---
description: Audit data quality coverage across dbt models and report gaps
---
Audit data-quality coverage for: $ARGUMENTS (default: entire dbt project)

1. List all models and their YAML files.
2. For each model report: has description? documented grain? PK tests (unique+not_null)?
   column-level tests? freshness on sources?
3. Output a coverage table sorted worst-first.
4. For the 5 worst models, generate the missing YAML/tests as ready-to-commit code.

# Plan: <feature name>

> Derived from: spec.md (must be approved first)

## Approach
Chosen technical approach in 3-5 sentences. Alternatives considered and why rejected.

## Components to build/change
| # | Component | Path | Change |
|---|-----------|------|--------|
| 1 | Extractor | src/extract/... | new |
| 2 | DAG | dags/... | new |
| 3 | Staging model | dbt/models/staging/... | new |
| 4 | Mart | dbt/models/marts/... | modify |

## Data flow
source → raw.<table> → stg_<...> → int_<...> → fct_<...>

## Migration / Backfill plan
- Initial load strategy, batch size, validation queries

## Testing strategy
- Unit tests: ...
- dbt tests: ...
- Reconciliation: ...

## Rollout & Rollback
- Feature flag / parallel run period / how to revert

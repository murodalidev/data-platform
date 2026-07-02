# Tasks: <feature name>

> Derived from: plan.md. One task = one reviewable commit/PR.
> Claude: work through these top-to-bottom, check off as completed, stop after each phase for review.

## Phase 1 — Foundation
- [ ] 1.1 Pydantic schema in src/extract/schemas/
- [ ] 1.2 Extractor + unit tests
- [ ] 1.3 Add source to dbt sources.yml with freshness

## Phase 2 — Pipeline
- [ ] 2.1 Staging model + YAML + tests
- [ ] 2.2 DAG (orchestration only)
- [ ] 2.3 Audit logging wired in

## Phase 3 — Serving
- [ ] 3.1 Mart model + YAML + tests
- [ ] 3.2 Backfill per plan.md
- [ ] 3.3 Reconciliation queries pass

## Phase 4 — Hardening
- [ ] 4.1 Alerting configured
- [ ] 4.2 docs/ updated
- [ ] 4.3 /review-pipeline clean

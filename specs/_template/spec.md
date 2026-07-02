# Spec: <feature name>

> Status: draft | approved | implemented
> Owner: <name>
> Created: <date>

## Problem
What business/data problem are we solving? Why now?

## Goal & Success Criteria
- Measurable outcome (e.g. "orders mart updated hourly, freshness < 90 min")
- What does "done" look like?

## Scope
### In scope
- ...
### Out of scope (explicitly)
- ...

## Data Contract
- **Source(s):** system, table/endpoint, auth method
- **Target:** schema.table
- **Grain:** one row per <what>
- **Key columns:** PK, incremental key, partition key
- **Volume estimate:** rows/day, growth
- **SLA:** freshness, availability

## Edge Cases & Risks
- Late-arriving data? Hard deletes at source? Schema drift? PII?

## Open Questions
- [ ] ...

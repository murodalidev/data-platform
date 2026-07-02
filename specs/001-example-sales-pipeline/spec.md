# Spec: Sales orders hourly pipeline

> Status: approved
> Owner: data-eng
> Created: 2026-07-02

## Problem
Sales team sees order numbers with 24h delay; ops needs hourly.

## Goal & Success Criteria
- `marts.fct_orders` freshness < 90 minutes, 99% of hours
- Row counts reconcile with source API daily (±0)

## Scope
### In scope
- Orders endpoint ingestion, staging, fct_orders incremental
### Out of scope (explicitly)
- Refunds endpoint (separate spec), real-time streaming

## Data Contract
- **Source:** Sales API `/v2/orders`, token auth, updated_at cursor
- **Target:** marts.fct_orders
- **Grain:** one row per order_id
- **Key columns:** PK=order_id, incremental key=updated_at
- **Volume estimate:** ~50k rows/day
- **SLA:** hourly, freshness < 90 min

## Edge Cases & Risks
- Late updates up to 48h → lookback window 3 days
- API returns soft-deleted orders with `status='cancelled'` — keep, don't filter
- PII: customer_email → tag in YAML, mask in logs

## Open Questions
- [x] Timezone of updated_at? → UTC, confirmed with API team

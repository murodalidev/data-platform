---
name: data-quality-audit
description: Use when investigating data quality issues - duplicates, nulls, volume drops, freshness lags, or mismatched numbers between reports. Provides a systematic root-cause workflow for data discrepancies. Trigger on "numbers don't match", "duplicates", "missing data", "stale data" type requests.
---

# Data Quality Audit

## Workflow: numbers don't match / data looks wrong
1. **Define the discrepancy precisely**: which metric, which grain, which time range, expected vs actual.
2. **Trace lineage down**: mart → intermediate → staging → source. `dbt ls -s +<model>` for upstream tree.
3. **Bisect the layer**: run the grain-level count at each layer for ONE affected partition:
   ```sql
   select count(*), count(distinct <pk>), min(<ts>), max(<ts>) from <layer_table> where <partition_filter>
   ```
   The first layer where counts diverge is the suspect.
4. **Common root causes to check, in order**:
   - Duplicate PKs (failed merge / re-run of non-idempotent load)
   - Late-arriving data outside incremental lookback window
   - Timezone shift (UTC vs local at a layer boundary)
   - Join fan-out (grain change in an intermediate model)
   - Source-side deletion/update not propagated (hard deletes)
   - Filter drift (a `where` clause someone added)
5. **Prove it** with a minimal query before proposing a fix.
6. **Fix + prevent**: fix the logic, then add a dbt test or audit check that would have caught it.

Never propose "just full-refresh it" as the diagnosis — that hides root causes.

---
name: schema-migration
description: Use when adding, renaming, changing type of, or dropping columns/tables in the warehouse or in dbt models with downstream dependencies. Provides the safe expand-migrate-contract workflow. Trigger on "rename column", "change type", "drop column", "alter table", "breaking change" requests.
---

# Schema Migration (expand → migrate → contract)

Never rename/retype/drop in one step if anything downstream depends on it.

1. **Impact analysis first**: `dbt ls -s <model>+` and grep the codebase + BI layer
   for the column/table name. List every consumer.
2. **Expand**: add the new column/model alongside the old one. Backfill it.
3. **Migrate**: switch consumers one by one to the new column. Each switch is its own PR.
4. **Verify**: for one full cycle, assert old vs new agree:
   `select count(*) from t where old_col is distinct from new_col` → must be 0.
5. **Contract**: only after all consumers migrated and verified, drop the old column.
   Deprecation notice period per team convention (default: 2 weeks).

For source-side changes (upstream team changed their schema):
- Pin staging model to explicit columns (never select *) so breaks are loud and local
- Add a dbt source column test to detect the drift earlier next time

# SQL Style Rules

- Lowercase keywords (`select`, `from`, `where`)
- CTEs over subqueries; each CTE named descriptively (`orders_deduplicated`, not `cte1`)
- One column per line in SELECT; trailing commas style per `.sqlfluff`
- Never `select *` in models — always explicit columns
- Explicit `join` types (`inner join`, `left join`) — never bare `join`
- Qualify all columns in joins with table aliases (short, meaningful: `o` for orders)
- All staging models: rename to snake_case, cast types explicitly, no logic beyond that
- Incremental models must handle late-arriving data: use lookback window pattern
  (`where updated_at >= (select max(updated_at) from {{ this }}) - interval '3 days'`)
- Every mart model must have: unique + not_null test on primary key, documented grain

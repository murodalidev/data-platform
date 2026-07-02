---
name: dbt-model-builder
description: Use when creating or modifying dbt models (staging, intermediate, or mart). Covers layer conventions, incremental patterns, YAML/test requirements, and naming. Trigger on any request mentioning dbt models, stg_/int_/fct_/dim_ files, or SQL transformations in the warehouse.
---

# dbt Model Builder

## Layer decision
- Raw source, 1:1, rename/cast only → `staging/stg_<source>__<entity>.sql`
- Reusable join/derivation used by 2+ marts → `intermediate/int_<entity>_<verb>.sql`
- Business-facing → `marts/fct_<event>.sql` or `marts/dim_<entity>.sql`

## Staging template
```sql
with source as (
    select * from {{ source('<source>', '<table>') }}
),

renamed as (
    select
        id as <entity>_id,
        cast(created_ts as timestamp) as created_at,
        lower(trim(email)) as email
    from source
)

select * from renamed
```

## Incremental template (marts/large staging)
```sql
{{ config(
    materialized='incremental',
    unique_key='<pk>',
    incremental_strategy='merge'
) }}

select ...
from {{ ref('stg_...') }}
{% if is_incremental() %}
where updated_at >= (select max(updated_at) from {{ this }}) - interval '3 days'
{% endif %}
```
The 3-day lookback handles late-arriving data. Adjust per source SLA, document why.

## Mandatory with every model
1. YAML file next to it: description, `meta: {grain: "..."}`, column descriptions
2. Tests: `unique` + `not_null` on PK; `accepted_values`/`relationships` where meaningful
3. Run `dbt parse` and `sqlfluff lint` on the new file before finishing
4. Check downstream impact: `dbt ls -s <model>+`

"""Pipeline run auditing: every ingestion records its counts to _meta.pipeline_runs."""

from dataclasses import dataclass
from datetime import datetime

from psycopg import Connection

from src.utils.logging import get_logger

logger = get_logger(__name__)

DDL = """
create schema if not exists _meta;
create table if not exists _meta.pipeline_runs (
    pipeline        text        not null,
    interval_start  timestamptz not null,
    interval_end    timestamptz not null,
    rows_extracted  bigint      not null,
    rows_loaded     bigint      not null,
    rows_rejected   bigint      not null,
    status          text        not null,
    recorded_at     timestamptz not null default now()
);
"""


@dataclass
class RunAudit:
    """One pipeline run's counts for the audit table."""

    pipeline: str
    interval_start: datetime
    interval_end: datetime
    rows_extracted: int
    rows_loaded: int
    rows_rejected: int
    status: str = "success"


def record_run(conn: Connection, audit: RunAudit) -> None:
    """Insert one audit row. `conn` is a psycopg connection (injected, testable)."""
    with conn.cursor() as cur:
        cur.execute(DDL)
        cur.execute(
            """
            insert into _meta.pipeline_runs
                (pipeline, interval_start, interval_end,
                 rows_extracted, rows_loaded, rows_rejected, status)
            values (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                audit.pipeline,
                audit.interval_start,
                audit.interval_end,
                audit.rows_extracted,
                audit.rows_loaded,
                audit.rows_rejected,
                audit.status,
            ),
        )
    conn.commit()
    logger.info(
        "audit recorded: %s [%s -> %s]",
        audit.pipeline,
        audit.interval_start,
        audit.interval_end,
    )
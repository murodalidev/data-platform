---
description: Systematically debug a failing Airflow DAG or task
---
Debug this failing DAG/task: $ARGUMENTS

Work systematically:
1. Read the DAG file and the task's underlying code in `src/`.
2. Check recent logs: !`docker compose logs --tail 200 airflow-scheduler 2>/dev/null || echo "airflow not running locally"`
3. Form hypotheses ranked by likelihood (schema drift, credential expiry, upstream data change,
   resource limits, dependency version).
4. For the top hypothesis, propose the minimal reproduction/verification step.
5. Propose the fix + a regression test so it can't silently recur.
Never "fix" by widening exception handling or disabling the failing check.

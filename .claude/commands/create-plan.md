---
description: Generate plan.md + tasks.md from an approved spec
---
Create the plan for spec: $ARGUMENTS

1. Read the spec.md in the given specs/ folder. If status is not "approved", stop and tell me.
2. Read CLAUDE.md and relevant .claude/rules/ to align with conventions.
3. Explore existing code (extractors, similar DAGs/models) to reuse patterns — list what you'll reuse.
4. Write `plan.md` from the template: approach, components table, data flow, backfill, testing, rollback.
5. Write `tasks.md`: small tasks (one reviewable commit each), grouped in phases.
6. STOP. Do not implement until I approve the plan.

---
description: Implement tasks from a spec's tasks.md, phase by phase
---
Implement from: $ARGUMENTS (path to specs/<NNN>-<slug>/)

1. Read spec.md, plan.md, tasks.md in that folder.
2. Work through unchecked tasks in order. For each task:
   - implement following .claude/rules/,
   - run `make lint` and relevant tests,
   - check the box in tasks.md with a one-line note.
3. STOP at the end of each phase and summarize for my review before continuing.
4. If reality diverges from plan.md, stop and propose a plan update — don't silently deviate.

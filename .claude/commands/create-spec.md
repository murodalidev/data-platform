---
description: Start a new feature with spec-driven workflow (spec.md first, no code)
---
Create a new spec for: $ARGUMENTS

1. Find the next number: !`ls -d specs/[0-9]* 2>/dev/null | sort | tail -1`
2. Create `specs/<NNN>-<slug>/spec.md` from `specs/_template/spec.md`.
3. Interview me to fill it: ask about source, target, grain, SLA, volume, edge cases —
   one focused question at a time. Push back if my answers are vague (especially grain and SLA).
4. Fill "Open Questions" with anything still unresolved.
5. STOP after spec.md. Do NOT write plan.md or any code until I say the spec is approved.

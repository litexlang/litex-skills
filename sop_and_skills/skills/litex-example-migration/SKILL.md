---
name: litex-example-migration
description: Diagnose unchanged Litex examples that fail after a version change. Use for migration triage and requested repairs, separating contract changes, capability gaps, defects and environment drift.
---

# Litex example migration

Use [the foundation](../litex-basics/SKILL.md) and
[live reading](../litex-reference/SKILL.md) for the actual target version.
A requested scan is read-only; implement repairs only within its authorized scope.

1. Anchor the unchanged failing source, configuration, named old baseline and
   current executable. Dated snapshots stay associated with their own version.
2. Reproduce the first actual failure. Separate syntax, WD, proof, storage/use,
   module-context and environment evidence instead of inferring the cause
   from a final error alone.
3. Read the relevant current Manual/CLI section and matching positive/negative
   example. Use [modules](../litex-basics/references/topics/modules.md) when
   imports/export context explain the difference.
4. Classify intended contract change, intentional limit, migration omission,
   implementation defect, old-example defect, environment drift or unknown.
   State diagnostic confidence separately from repair ownership.
5. Report the smallest real code, observed result, established expected
   behavior and next check. A proof-search miss is not proof of a false goal.
6. For an authorized authoring repair use
   [proof writing](../litex-proof-writer/SKILL.md) and one persistent Session.
   Keep expected-negative controls rejected and verify the actual saved source.

Do not add trust, remove premises or weaken a goal to call migration solved.
A proposed kernel repair belongs to a separate applicable maintainer workflow;
respect its concrete AST/Env/Runtime authorization gates.

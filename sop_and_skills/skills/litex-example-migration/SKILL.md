---
name: litex-example-migration
description: Diagnose Litex examples that fail after a version change. Use for migration triage, distinguishing changed contracts, capability limits, defects and environment drift.
---

# litex-example-migration

Anchor the unchanged failing source, its actual module configuration,
the named old baseline and the current executable. A scan authorizes diagnosis;
implement repairs only within the requested scope.

Report root cause and earliest failing phase separately. Distinguish intended
semantic changes, intentional capability limits, migration omissions,
implementation defects, old-example defects, environment drift and unknown
causes. A normal proof miss is not a mathematical counterexample.

Use the [source guide](references/source-guide.md) for the twelve diagnostic
facets and investigation protocol, and the shared
[explicit-proof boundary](../golitex-repository-policy/references/search-explicit-proof-boundary.md)
for automatic discovery versus explicit checkability. Show the real snippet,
observed outcome, established expected behavior and smallest next check.

Do not make a reproduction pass by adding trust, dropping premises, weakening
the goal or changing expected-negative fixtures. Respect the
[AST authorization gate](../litex-ast-struct-authorization/SKILL.md) and
[repository policy](../golitex-repository-policy/SKILL.md) for kernel repairs.

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.

---
name: litex-math-textbook-translator
description: Translate mathematical textbooks and lecture notes into source-faithful Litex modules. Use for chapter slices, dependencies, translation records and explicit proof debt.
---

# litex-math-textbook-translator

Preserve the source's mathematical meaning, theorem identity, dependency
order and important teaching steps. Translate the proof idea rather than
mechanically reproducing another proof assistant's tactic trace.

Use [concept modeling](../litex-concept-modeler/SKILL.md) before a new chapter
interface, and [proof writing](../litex-proof-writer/SKILL.md) for each item.
Maintain one module README describing implemented interfaces and one
math_collections.md explaining the important concepts and dependencies.

Record each touched source item with source, problem, proof_idea, litex_code
and comments. Classify it as translated, checkable or blocked; checkable needs
an executed gate. Record any remaining assumption or proof debt explicitly.
Use [todo writing](../todo-writer/SKILL.md) for surviving blockers.

Resolve the actual source-owned workspace before writing artifacts. The
scripts/.textbooks convention in the [source guide](references/source-guide.md)
is for golitex work, not a mandatory path for external users. Use the owning
project's module, draft and journal locations elsewhere. In golitex apply
[its repository policy](../golitex-repository-policy/SKILL.md).

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.

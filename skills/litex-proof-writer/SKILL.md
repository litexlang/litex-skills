---
name: litex-proof-writer
description: Write, repair and verify Litex mathematical proofs. Use for ordinary .lit authoring, local proof debugging and dataset problems after the Litex foundation.
---

# Litex proof writer

Start with [the foundation](../litex-basics/SKILL.md) once, including the
[misconception cards](../litex-basics/references/misconceptions.md) when relevant.
This skill owns the proof-writing process; use
[live reference routing](../litex-reference/SKILL.md) to inspect actual source.

1. State the mathematical idea, exact carriers/premises and intended conclusion.
   Preserve the goal; a weaker statement is not a repaired proof.
2. Inspect the existing builtin/module interface and one small matching example.
   Use the [topic index](../litex-basics/references/topics.md) for the next move;
   read a showcase only when the proof needs a larger interface/dependency.
3. Open one live `-session` on accepted context. Submit one complete statement,
   read feedback, then continue. Repair ordinary failures there; earlier accepted
   definitions/facts remain. Never rerun a full file after each small addition.
4. Diagnose the first actual failing phase. Correct syntax, scope or WD before
   searching for missing proof evidence. State a direct routine fact first;
   keep meaningful witnesses, branches, induction and intermediate calculations.
5. Retain exact distinct attempts and accepted source in the owning task's
   notes/journal under its policy. Materialize a contiguous accepted prefix at
   a coherent checkpoint and run a separate clean file gate.
6. Check the intended mathematics, saved source, assumptions/debt and downstream
   use before reporting completion. Use [review](../litex-review/SKILL.md) for
   an independent read-only audit when requested.

Use [algebra](../litex-basics/references/topics/algebra.md) and
[calculation cleanup](../litex-equality-inequality/SKILL.md) for equalities/order;
[existence](../litex-basics/references/topics/existence.md),
[logic/scope](../litex-basics/references/topics/logic-scope.md) or
[induction](../litex-basics/references/topics/induction.md) for those proof moves.
Use [concept modeling](../litex-concept-modeler/SKILL.md) for an unsettled
definition rather than inventing proof scaffolding.

A normal search miss is not a counterexample. Explicit proof debt may be
permitted by the owning task, but never label a proof containing unproved
`trust` fully checkable. Follow that repository's budgets and authorization
rules; do not impose golitex-specific paths on another project.
Use [todo writing](../todo-writer/SKILL.md) for surviving blockers.

Expanded author notes and dated cases remain in this source repository's
`references/` archives. They are optional historical material, not prerequisites
of the lightweight author package or current CLI authority.

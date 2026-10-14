---
name: litex-math-textbook-translator
description: Translate mathematical textbooks and lecture notes into source-faithful Litex developments. Use for chapter slices, source dependencies, item records and explicit proof debt.
---

# Litex textbook translator

Start with [the foundation](../litex-basics/SKILL.md), then preserve the source's
mathematical meaning, theorem identity, order and important proof ideas.
Translate mathematics rather than another prover's tactic trace.

1. Resolve the source-owned workspace, intended slice and actual module
   README/design/configuration. Follow the owning project's artifact policy.
2. Write the natural-language proof spine and dependency order. Use
   [concept modeling](../litex-concept-modeler/SKILL.md) for a new interface.
   Use [live reading](../litex-reference/SKILL.md) level 2 for a relevant
   showcase, not whole unrelated books.
3. Keep a touched item record with `source`, `problem`, `proof_idea`,
   `litex_code` and `comments`. Record commands, assumptions, source caveats
   and the status: translated, checkable or blocked.
4. Reuse builtin/library interfaces faithfully. Keep source-facing theorem
   identity and any pedagogical alternative clear; do not add trusted copies
   of routine builtin-supported facts.
5. Use [proof writing](../litex-proof-writer/SKILL.md) in one live `-session`.
   Submit source-order statements one at a time, keeping accepted context after
   ordinary failure. Save a coherent prefix and check its actual configuration.
6. Track localized proof debt under the owning task's budget/policy with
   [todo writing](../todo-writer/SKILL.md); do not call debt fully checkable.
7. Verify the saved slice and the requested wider checkpoint, reconcile source,
   statements, interfaces and trust, and update module documentation.

Use [modules/context](../litex-basics/references/topics/modules.md),
[existence](../litex-basics/references/topics/existence.md) and
[induction](../litex-basics/references/topics/induction.md) only as needed.
A partial chapter, normalized model or source assumption keeps that exact scope.

Golitex workspace registry, draft/public boundaries and trust budgets belong
to its maintainer profile; they do not prescribe paths for unrelated projects.
Expanded historical source notes remain in the full source edition.

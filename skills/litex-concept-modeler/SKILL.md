---
name: litex-concept-modeler
description: Choose Litex interfaces for mathematical definitions and reusable concepts. Use when carrier, function, predicate, struct, selection or module design must be settled before proof writing.
---

# Litex concept modeler

Use [the foundation](../litex-basics/SKILL.md) first when unfamiliar with Litex.
Start from the intended mathematics and its downstream uses, not the desired
proof output. Keep carrier, value, callable, condition, structure and theorem
as distinct roles.

1. Identify the source meaning, domains, concept-owned nondegeneracy and the
   concrete operations/proofs a caller needs.
2. Inspect the actual target module's README/design/configuration. Use
   [live reading](../litex-reference/SKILL.md) level 2 for a matching reusable
   showcase, level 1 for a small construction and level 3 for exact syntax.
3. Choose the smallest faithful interface: an existing builtin first when
   appropriate; `have` for a value, `have fn` for a callable, `prop` for a
   condition, and a primary structure when values really bundle data with laws.
   A theorem or explicit axiom has a different proof/trust role.
4. Show an intended use and the nearest unsuitable form. For selection, preserve
   quantifier dependencies and prove existence/uniqueness before choosing a
   function. Read [existence](../litex-basics/references/topics/existence.md).
5. Probe the intended declaration/use and a boundary in one persistent Session.
   Record designed, checked, assumed and blocked interfaces distinctly.
6. For a reusable module maintain one README of implemented interfaces and
   one `math_collections.md` of important concepts/dependencies. Reconcile the
   intended design before generating dependent source, then update implemented
   documentation after representative uses pass.

Apply [strict definitions](../litex-strict-definitions/SKILL.md). Use
[sets/functions](../litex-basics/references/topics/sets-functions.md) for carrier
and callable questions, [modules](../litex-basics/references/topics/modules.md)
for dependency context and [proof writing](../litex-proof-writer/SKILL.md) for
the proof loop. Do not preserve an incorrect interface through aliases,
wrappers, abstract predicates or trust.

The source repository retains expanded modeling guides and templates as
optional references. Kernel representations and maintainer authorization are
separate from mathematical modeling.

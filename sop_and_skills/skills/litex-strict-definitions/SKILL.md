---
name: litex-strict-definitions
description: Review or revise Litex definitions so carriers, parameter domains and concept-owned nondegeneracy match the intended mathematics. Use for definition design and dependent-interface alignment.
---

# Litex strict definitions

Use [the foundation](../litex-basics/SKILL.md) and
[sets/functions](../litex-basics/references/topics/sets-functions.md).
Put exact carriers, parameter domains and concept-owned nondegeneracy into the
definition, rather than leaving them to later comments or conventions.
Do not narrow the intended mathematical concept merely to make a proof pass.

1. State the intended domain/value contract and downstream use.
2. Inspect a live declaration and domain/WD positive/negative pair through
   [reference routing](../litex-reference/SKILL.md).
3. For several legitimate formulations use
   [concept modeling](../litex-concept-modeler/SKILL.md) to settle the interface.
4. Align dependent theorem premises, binders, comments and callers with that
   contract. Do not keep incompatible interfaces hidden behind aliases/trust.
5. Probe uses in one live Session. Replacing an already committed declaration
   requires a deliberate restart/replay, not an assumption that an edited file
   changed the running process.
6. Check the saved definition and representative dependent uses separately.

For example, a line determined by two points needs their distinctness, while
a midpoint of an arbitrary pair may intentionally allow coincident points.
Use actual mathematical meaning to decide; strictness is not arbitrary extra
premises. Expanded review notes remain in the full source edition.

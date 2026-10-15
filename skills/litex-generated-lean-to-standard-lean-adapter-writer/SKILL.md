---
name: litex-generated-lean-to-standard-lean-adapter-writer
description: Write handwritten Lean Adapter and Final layers after compiler-generated Litex output exists. Use for a native Lean/Mathlib consumer without changing compiler-owned output or weakening its theorem.
---

# Litex Lean Adapter and Final

Keep four owners distinct: Litex source, compiler-generated Lean, handwritten
`Adapter.lean`, and handwritten `Final.lean`. The generated layer remains
compiler owned. This task starts after actual generated output exists.

1. Read the generated theorem's exact denotations, premises and conclusion.
   Anchor the final native mathematical statement independently.
2. Write an Adapter connecting the generated interface to intended ordinary
   Lean/Mathlib objects. Review semantic conversion and equality specialization
   rather than assuming a generated relation already is native equality.
3. Keep Final's binders, premises and conclusion native. Its proof may use
   native Adapter theorems; the generated theorem must remain a live dependency.
4. Do not reprove unrelated mathematics, invent an axiom, weaken Final or edit
   generated output to force the bridge to work. Report missing conversion
   evidence with the real source and proposed interface.
5. Check Adapter and Final with the intended Lean/Mathlib environment.
   Successful Litex verification alone does not establish Lean acceptance.

For Litex source authoring use [the foundation](../litex-basics/SKILL.md).
For exact supported output read the target-version compiler guide through
[reference routing](../litex-reference/SKILL.md). Compiler implementation belongs
to the separately selected maintainer profile. The full source edition retains
expanded adapter examples and ownership notes.

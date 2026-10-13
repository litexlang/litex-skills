---
name: litex-generated-lean-to-standard-lean-adapter-writer
description: Write handwritten Lean Adapter and Final layers consuming compiler-generated Litex proofs. Use after generated output exists; keep the final theorem native to Lean and Mathlib.
---

# litex-generated-lean-to-standard-lean-adapter-writer

Consume the actual compiler-generated theorem through a handwritten
Adapter.lean, then a real Final.lean consumer. Generated files remain compiler
owned. The Final theorem's binders, premises and conclusion use ordinary
Lean/Mathlib concepts; its proof body may cite native Adapter theorems.

Read the [source guide](references/source-guide.md) before constructing the
bridge. It defines the four ownership layers, reviewed Same-to-Eq
specializations, concrete interface examples and acceptance requirements.

The adapter converts a proved interface; it does not reprove the mathematics
or insert a new axiom to make the desired theorem appear. A generated theorem
citation must be a live proof dependency. If conversion evidence is missing,
report it without weakening the final native statement. Verify Adapter and
Final in the intended Lean environment; Litex acceptance alone is insufficient.

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.

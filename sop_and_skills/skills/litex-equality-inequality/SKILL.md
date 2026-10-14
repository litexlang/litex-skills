---
name: litex-equality-inequality
description: Simplify or repair Litex algebraic calculations, equality chains and order estimates while preserving domains, premises and meaningful proof steps.
---

# Litex equality and inequality

Use [the foundation](../litex-basics/SKILL.md) and the
[algebra topic](../litex-basics/references/topics/algebra.md).
Establish domains, signs and the mathematical argument first.

1. Try the natural direct fact using existing builtin/library interfaces.
2. If it fails, read the exact first phase and inspect a matching live
   `examples/proof_nodes/` or `examples/infer/` case through
   [reference routing](../litex-reference/SKILL.md).
3. Split genuine jumps into justified calculations. Preserve nonzero/sign
   premises and the equality direction/representation needed by the consumer.
4. Compare a shortened candidate and its downstream use in the same context;
   restore only a bridge demonstrated to be necessary.
5. Keep one live `-session` across ordinary failures. Save accepted source and
   use separate clean file gates at coherent checkpoints/final delivery.
6. For cleanup or a claimed improvement, retain the actual source, invalid
   control, command and measured result. Shorter source alone does not establish
   faster execution or globally minimal proof.

Use [proof writing](../litex-proof-writer/SKILL.md) for the overall process.
The full source repository retains the dated case index at
`references/parts-index.md` and its historical evidence. Read only a selected
case when needed; those archives are excluded from the lightweight author pack.
Replay before claiming current support. Kernel improvements require their own
authorized task and applicable maintainer rules.

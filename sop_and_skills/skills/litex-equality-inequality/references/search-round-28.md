# Search round 28 — set-builder consumers depend on fact chronology

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


27 independent strict files: 15 accepted, 12 rejected. Fresh current-source
release snapshot and complete replay sources are preserved. Plain builder
equalities isolate Round 27's template observation without new definitions.

## Existing support and precise difference

```litex
forall E set,p R:
    E={x R: x>0}
    p $in E
    =>:
        p>0
```

This passes. Reversing just the two premises misses; re-stating p in E after
the equality repairs that exact reversed target. Function-valued builder
predicates show the same order distinction. Generic set membership transport
across equality and builder introduction already pass. Thus do not claim all
set aliases are unsupported or add duplicate membership primitives.
[Part 69](part-69-set-builder-fact-chronology.md).

## Carrier boundary and nomination

For p declared in E before E's builder equality becomes available, deriving
p in R directly misses; member replay checks. The literal-member replacement
does not check in the tested variants. Source read-only inspection shows the
builder projection in infer_in_fact_rules, resolving the builder from equal
object values when membership inference runs. Equality inference does not
invoke that projection in the inspected owner. This matches the chronology
observation, but no repair/replay establishes a complete kernel diagnosis.

Nominate bounded goal-directed consumption of already known membership and
set equality/body evidence, with actual citations and capture/domain guards.
Do not globally replay inference, increase recursion or add Env state merely
to make these cases pass. Implementation needs its own scoped verification.

## Controls and evidence

Wrong sign, changed free threshold or function, changed input point and missing
member evidence reject. Renaming a bound builder variable retains the positive
result. A trivial supplied-body probe only checks known-fact use, not new
mathematical capability. Warm results never determine cold support.

[Receipt](evidence/round-28-2026-10-09.summary.json), `evidence/round-28-cases/`, build
identity and inspected source hashes. No canonical/kernel edits, new trust,
full-module or performance claim. Next: independent alias/inference-order
consumers and source equations, keeping structural evidence lookup separate
from public proof style.

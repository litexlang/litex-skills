# Part 69 — Consume known set equality and member facts without order dependence

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and observed order difference

Both orders express the same conjunction about a positive-real builder.

```litex
forall E set,p R:
    E={x R: x>0}
    p $in E
    =>:
        p>0
```

This passes cold. The same target with premises `p in E` followed by the
builder equality misses. Reversing equality direction also misses in that
member-first order. The functional builder predicate f(x) in U has the same
order difference on the source's arbitrary carriers.

## Checked repair of the exact member-first target

```litex
claim:
    ? forall E set,p R:
        p $in E
        E={x R: x>0}
        =>:
            p>0
    p $in E
```

This passes. It is a demonstrated current bridge, not recommended permanent
proof style. Re-stating only the equation or using the literal builder member
instead does not repair the tested variants.

For `p E` introduced before `E=builder`, direct real-carrier extraction also
misses and replaying `p in E` repairs it. This matters for comparison WD:
retain the derived carrier proof separately from the strict-positive target.

## Existing support and read-only owner evidence

Plain set-equality membership transport, builder introduction and definition-
first extraction already work. Binder renaming keeps the positive example.
The inspected membership_projection.rs resolves a builder from equal values
when infer_in_fact_rules runs and projects its carrier and body. The inspected
equality-inference owner does not run that membership projection. These facts
support investigating chronology, without asserting that one change repairs
every source-template or alias consumer.

Consider a bounded truth consumer of actual known membership and equality
evidence. Preserve inherited permission ceilings, body instantiation, free
identifier identity, WD and source citations. No global inference replay,
new Env/Runtime fields or indexes, arbitrary body search or recursion policy
change is justified. Kernel implementation is a separate authorized task.

## Negatives and evidence

Membership in x>a cannot imply p>b for unrelated b. A body using f cannot
justify one using unrelated g, and membership at p does not establish the
body at q. Missing membership or the wrong negative sign are false controls;
all reject. Do not erase free captures when normalizing binder names.

[Round 28 receipt](evidence/round-28-2026-10-09.summary.json) retains the exact order
variants, same-Session repairs, cold strict output and inspected owner hashes.
This refines Part 68's broad consumer nomination. No code/Env/AST change,
new trust, complete causal repair or runtime claim.

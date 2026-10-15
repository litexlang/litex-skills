# Part 58 — Consume product evidence after reassociation

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and source

Multiplication is associative over reals. A known equation `a*b=c` may be used
inside an additional product regardless of grouping. Concrete Mathematics
Chapter 2 `summation_factor_step_210` multiplies a summation-factor equality
by a previous recurrence value. No factor is required nonzero for this step.

## Direct miss and checked positive

```litex
forall a,b,c,d R:
    a*b=c
    =>:
        a*(b*d)=c*d
```

This direct target misses. Replacing the target by `(a*b)*d=c*d` passes.
The same desired target checks with one calculation chain:

```litex
claim:
    ? forall a,b,c,d R:
        a*b=c
        =>:
            a*(b*d)=c*d
    a*(b*d)=(a*b)*d=c*d
```

## Order sibling and boundary

```litex
claim:
    ? forall a,b,c,d R:
        a*b<=c
        d>=0
        =>:
            a*(b*d)<=c*d
    a*(b*d)=(a*b)*d<=c*d
```

This passes; the bare associated comparison misses. The same-direction target
with `d<0` rejects and is false: take `a=0,b=1,c=1,d=-1`.

## Bounded candidate

Consider finite product reassociation that exposes a checked subproduct fact,
with actual equality/order citations and sign guards. Do not add arbitrary
factor cancellation or a source-specific recurrence law. These two grouping
probes isolate a capability difference; they do not yet identify the precise
normalization or consumer owner. Existing author chains are fully checkable.

## Evidence

[Round 20](search-round-20.md), receipt `product-*`. Date 2026-10-09. Normal
text prints both groupings similarly; use the retained literal source. Current
worktree build was unavailable at resumption; outcomes were rechecked on the
original hash-matched snapshot. No kernel changes or performance claim.

# Part 6 — Cancel a common term or factor

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

An additive shift preserves and reflects real order. A nonzero multiplier
reflects equality; positive/negative multipliers reflect order with the
corresponding direction. Anchors: Manual R11 and coordinate-geometry midpoint
calculation in `15_coordinate_geometry_case_study/main.lit` around line 3123.

## Positive and verbose comparison

```litex
claim:
    ? forall a,b,k R:
        a+k = b+k
        =>:
            a = b
    a = (a+k)-k = (b+k)-k = b
claim:
    ? forall a,b,k R:
        k > 0
        a*k <= b*k
        =>:
            a <= b
    a = (a*k)/k <= (b*k)/k = b
```
Both pass. The original geometry proof prints separate multiplied equalities
and their endpoint chain; those are review candidates, not verified removable
chapter code. The reduced additive transport route also passes:
```litex
claim:
    ? forall a,b,c,d R:
        a+d = c+b
        =>:
            a-c = b-d
    a-c = (a+d)-c-d = (c+b)-c-d = b-d
```

## Ideal forms and negative boundaries

The direct a=b from a+k=b+k misses, as does a<=b from a+k<=b+k.
The direct a=b from k!=0,a*k=b*k misses. Positive/negative order cancellation
direct targets also miss; all corresponding one-chain proofs pass.
These are excerpts; complete direct/explicit sources are in the receipt.

Without k!=0, a*k=b*k does not entail a=b: a=2,b=1,k=0.
k>=0 does not suffice for order cancellation, with the same counterexample.
For negative k, preserving rather than reversing the inequality is false:
a=2,b=1,k=-1 gives a*k<=b*k but not a<=b. All were executed and rejected.
Unequal additive offsets cannot cancel: a+k=b+h with a=0,b=1,k=1,h=0.

## Builtin candidate

Match stored relations containing the target endpoints and a shared term or
factor, then check zero/sign requirements. The eliminated k is absent from
the goal; this needs bounded known-fact matching, not a claim that the goal
alone supplies k. Reuse existing visibility/equivalence interfaces and preserve
exact source evidence. Do not introduce a new Env index or unrestricted
intermediate discovery to make this pilot pass.

## Evidence

[Round 3 receipt](evidence/round-03-2026-10-08.summary.json): `additive-*`,
`equal-cancel-*`, `order-cancel-*`. Current working-tree release built
successfully on 2026-10-08; 34 total strict clean-file probes in the round.
No geometry theorem cleanup or kernel implementation performed.

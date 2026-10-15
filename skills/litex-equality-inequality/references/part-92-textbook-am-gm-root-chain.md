# Part 92 — Actual textbook AM-GM: replace contradiction with a root chain

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematics

The high-school chapter02 defines arithmetic_mean=(x+y)/2 and geometric_mean=
sqrt(x*y), with x,y>=0 inside the geometric mean definition. The local theorem
has the same nonnegative premises. Its original proof has16 top-level body
statements, one of which is a contradiction block with three additional inner
statements. The exact isolated original proof passes current strict verification.
Keep the named mean interfaces and their domains; no harmonic mean is needed.

## Positive: four statements, no contradiction block

This exact replacement passes independently with both source definitions:

```litex
claim:
    ? forall x, y R:
        x >= 0
        y >= 0
        =>:
            r52_geometric_mean(x, y) <= r52_arithmetic_mean(x, y)
    ((x+y)/2)^2-x*y=(x-y)^2/4>=0
    x*y<=((x+y)/2)^2
    (x+y)/2>=0
    r52_geometric_mean(x,y)=sqrt(x*y)<=sqrt(((x+y)/2)^2)=(x+y)/2=r52_arithmetic_mean(x,y)
```

[Full runnable short source slice](evidence/round-52-cases/delete-product-sign.lit).
The square certificate gives the squared upper bound, the half-sum is
nonnegative, and native square-root monotonicity plus square-root folding gives
the final chain. The named mean values are exposed inline. A six-statement
version also publishes x*y>=0 and the half-sum square's nonnegativity; those
two publications were deleted in independently passing variants. No stronger
x>0/y>0 assumptions were introduced; the zero diagonal boundary also passes.

## True direct misses and live bridges

The bodyless named theorem and literal sqrt(x*y)<=(x+y)/2 miss cold. A candidate
that publishes the square certificate/bound and jumps directly to that mixed
root/scalar comparison also misses. Publishing the upper sign alone does not
repair that direct jump. Passing through sqrt(((x+y)/2)^2) is the checked route,
consistent with the related generic mixed-root evidence in Part35. No new bt
rule was implemented or justified solely from this consumer.

Deleting the certificate makes the squared upper-bound statement fail. Deleting
that bound makes the root monotonicity link fail at adjacent index1. A variant
with the product sign but without the half-sum sign fails at adjacent index2,
sqrt(((x+y)/2)^2)=(x+y)/2. Different four-statement variants are not equivalent
in verification: retain the tested certificate/bound/radius-sign route. These
failures establish liveness in this route, not a global minimum proof length.

The root-square bridge sqrt(x*y)^2=x*y attempted without the original explicit
product-sign publication missed; that separate failed route does not contradict
the successful monotonicity route with no product-sign echo. Retain contexts
rather than inferring a universal mandatory publication rule.

## Negatives and scope

The strict mean inequality is false on the diagonal and rejects. Calling the
named geometric mean with(-1,-1) violates its retained parameter domains and
rejects; it is not a valid named-function counterexample. Separately, the literal
counterexample not sqrt((-1)*(-1))<=(-1-1)/2 passes, showing why the unrestricted
signed version would be false even with a nonnegative product. The zero mean
identity passes. Mathematical and domain controls are kept distinct.

[Round52 receipt](evidence/round-52-2026-10-09.summary.json):17 independent strict files,
6 accepted/11 rejected, all promoted copies rerun on the fixed current-source
release snapshot. Source hash, build and literal warm journal saved. Session99217
remains live, normal misses repaired there; cold files own direct/deletion claims.
No canonical scripts, kernel, AST/Env/Runtime, trust, whole chapter or performance
change. Next inspect textbook logarithm interfaces and numeric equalities,
preserving base guards and already concise direct forms rather than expanding them.

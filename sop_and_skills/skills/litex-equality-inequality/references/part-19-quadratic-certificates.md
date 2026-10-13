# Part 19 — Orient a certificate as one checked chain

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

The author chooses a mathematically useful square certificate. Put its
nonnegativity first and then equate it to upper-minus-lower so the saved
orientation is exactly the comparison bridge consumed next.
Anchor: Manual R13; 2D geometry dot/determinant identity near line 1597.

## Positive and verbose contrast

Before, both statements pass:
```litex
claim:
    ? forall a,b,c,d R:
        (a*c+b*d)^2 <= (a^2+b^2)*(c^2+d^2)
    (a^2+b^2)*(c^2+d^2)-(a*c+b*d)^2 = (a*d-b*c)^2 >= 0
    0 <= (a^2+b^2)*(c^2+d^2)-(a*c+b*d)^2
```
One checked chain also passes:
```litex
claim:
    ? forall a,b,c,d R:
        (a*c+b*d)^2 <= (a^2+b^2)*(c^2+d^2)
    0 <= (a*d-b*c)^2 = (a^2+b^2)*(c^2+d^2)-(a*c+b*d)^2
```
The same oriented-certificate approach passes for the weighted Young bound
2*a*b<=t*a^2+b^2/t with t in R+, and the squared-sum bound
(a+b)^2<=2*(a^2+b^2). Full sources are in the receipt. All three bare
inequality targets miss.

## Negatives and improvement status

The reverse Cauchy inequality is false (a=1,b=0,c=0,d=1), and rejects.
The weighted bound with t<0 is false (a=1,b=0,t=-1); t=0 is a denominator
WD failure. Both controls reject. Omitting the coefficient 2 in the squared-
sum bound is false at a=b=1 and rejects.

This is already a verified authoring improvement, not evidence that a new
bt rule is necessary to reduce these bodies. Fixed Cauchy/Young native leaves
are optional proposals if direct familiar bounds are desired; unrestricted
polynomial certificate discovery is a different feature. General orientation
consumption should be audited before adding one leaf per rewritten identity.
No canonical geometry/Manual cleanup or runtime improvement is claimed.

## Evidence

[Round 6 receipt](evidence/round-06-2026-10-08.summary.json), `cauchy-two-*`,
`weighted-young-*`, `squared-sum-bound-*`. Current working-tree release build,
strict fresh files, 2026-10-08.

# Part 24 — Rounded and real threshold comparisons

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For integer n, these are the four characteristic threshold equivalences:
```text
floor(x)<n  iff x<n
n<ceil(x)  iff n<x
ceil(x)<=n iff x<=n
n<=floor(x) iff n<=x
```
Anchor: Concrete Mathematics Chapter 3 equation 3.7.
The tested direct directions below miss; their explicit routes pass.

## Positive

```litex
claim:
    ? forall x R,n Z:
        floor(x) < n
        =>:
            x < n
    floor(x) $in Z
    x < floor(x)+1
    floor(x)+1 < n+1
    floor(x)+1 <= n
    x < floor(x)+1 <= n
```
The ceil strict-reflection and both weak rounding directions have checked
explicit proofs in the receipt. Integer successor-gap itself already passes
directly; this is a rounding-to-gap composition observation.

## General real forward directions

The following also pass and do not require integer n:
```litex
forall x,n R:
    x < n
    =>:
        floor(x) <= x < n
forall x,n R:
    n < x
    =>:
        n < x <= ceil(x)
```
Their bare endpoint targets miss. Do not gratuitously require n in Z for
these forward directions; only the converses/weak rounded directions need it.

## Negatives and candidate

Removing integrality from floor strict reflection is false at x=0.8,n=0.5;
ceil strict reflection is false at x=0.2,n=0.5. The weak ceil/floor rounded
directions also fail for those noninteger thresholds. All were executed.

Add bounded threshold leaves with direction-specific domain checks. Each
target supplies x,n and a rounding constructor, so fixed premise generation
can replace integer-gap/translation traces. Avoid a general reverse-monotonicity
rule: floor/ceil lose fractional information. Preserve strict/weak endpoints
and actual premise evidence.

## Evidence

[Round 7 receipt](evidence/round-07-2026-10-08.summary.json), `floor-threshold-*`,
`ceil-threshold-*`, `floor-weak-threshold-*`, `ceil-weak-threshold-*`,
`integer-gap-*`. Strict current working-tree release on 2026-10-08.

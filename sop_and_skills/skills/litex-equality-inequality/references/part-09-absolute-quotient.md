# Part 9 — Absolute value of a quotient

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For real u,v with v!=0, abs(u/v)=abs(u)/abs(v). Derive it by multiplying
u/v by v, applying the existing product-absolute identity and dividing by
the nonzero abs(v). Anchor: Analysis Chapter 6 `reciprocal_abs_diff_bound`,
which uses the multiply-first route around lines 1020–1029.

## Positive — current route

```litex
claim:
    ? forall u,v R:
        v != 0
        =>:
            abs(u/v) = abs(u)/abs(v)
    abs(v) != 0
    (u/v)*v = u
    abs(u/v)*abs(v) = abs((u/v)*v) = abs(u)
    abs(u/v) = (abs(u/v)*abs(v))/abs(v) = abs(u)/abs(v)
```
This passes. It exposes multiplication/cancellation to avoid the unsupported
direct identity, not additional mathematics the final source should always log.

## Ideal form and negative

```litex
forall u,v R:
    v != 0
    =>:
        abs(u/v) = abs(u)/abs(v)
```
Direct target misses. Removing the absolute value from the denominator is
false and rejects: u=1,v=-1 gives 1=-1.

## Candidate and upstream diagnosis

Add a fixed quotient-absolute equality rule for well-defined real quotients.
Verify v!=0 (and derived abs(v)!=0 for RHS WD) without requiring v>0.
Preserve expression-domain evidence and rejection of the signed-denominator
control. This is more general than adding a rule only for reciprocal errors.

For abs(1/x-1/y), the first quotient-chain attempt failed WD of abs(x*y)
in a denominator. Explicit nonzero bridges moved it to a search miss at
abs((y-x)/(x*y))=abs(y-x)/abs(x*y). A multiply-first complete reciprocal
identity then passed. Thus truth support and WD consumption are separate;
adding the identity alone does not prove that every nested RHS will become WD.

## Evidence

[Round 3 receipt](evidence/round-03-2026-10-08.summary.json): `abs-quotient-*`,
`reciprocal-difference-*`, `reciprocal-product-chain`.
Current working-tree release built successfully on 2026-10-08. The failed
intermediate attempts are retained alongside the accepted route; no trust used.

## Dated reciprocal follow-up

Round 16 reproduces the absolute reciprocal identity miss and checks the original Analysis scalar lemma plus a six-statement multiply-first version. Safe-divide zero/nonzero branches are checked separately; no continuity-debt removal is claimed. See [Part 49](part-49-separated-quotient-bound.md) and its receipt for this dated support.

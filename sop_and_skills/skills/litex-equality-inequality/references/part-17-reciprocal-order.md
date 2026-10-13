# Part 17 — Compare reciprocals on one sign region

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

If x<=y and x,y are both positive or both negative, 1/y<=1/x.
The product x*y is positive; using that common denominator preserves order.
Anchor: Analysis Chapter 5 reciprocal-natural sequence around lines 195–196.

## Positive and current bridges

```litex
claim:
    ? forall x,y R+:
        x <= y
        =>:
            1/y <= 1/x
    0 < x*y
    1/y = x/(x*y) <= y/(x*y) = 1/x
```
Passes. Omitting the product sign statement makes this composed route miss.
Replacing both weak comparisons with strict ones also passes with that sign
bridge. Both-negative operands use the same route after publishing 0<x*y;
that weak version passes. Direct positive weak/strict and negative weak
reciprocal targets all miss.

## Negatives and candidate

Nonzero operands alone do not determine the direction across zero:
x=-1,y=1 gives x<=y but 1/y<=1/x is false. Weak order cannot imply strict
reciprocal order: x=y=1. Both were run and rejected.

Add fixed reciprocal antitonicity on either sign region, matching the actual
reciprocal expressions and checking operand order/signs/WD. Do not treat
nonzeroness as a substitute for a same-sign condition. Parent-domain evidence
and strictness must remain explicit in its certificate. This avoids requiring
the author to invent a product denominator.

## Related reusable interface

Analysis's reciprocal error envelope has existing mathematical meaning:
nonzero x,y, |x|,|y|>=c>0 and |x-y|<=c^2*epsilon imply
|1/x-1/y|<=epsilon. The direct target misses; a five-statement reduced
multiply-first proof passes (`reciprocal-envelope-chain`). Reuse or improve
that named interface rather than add a source-shaped bt rule for every epsilon
package. Full chapter replacement remains unverified. The missing-magnitude-
bound variant rejects; x=1/10,y=1/5,c=1,epsilon=1/10 refutes it.

## Evidence

[Round 5 receipt](evidence/round-05-2026-10-08.summary.json), `reciprocal-*`.
Current working-tree release, 2026-10-08; no trust, kernel or canonical edits.

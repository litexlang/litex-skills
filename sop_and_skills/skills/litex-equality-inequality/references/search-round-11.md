# Search round 11 — Square-root bounds and strict square reflection

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current working-tree release build succeeded on 2026-10-08. 33 isolated strict
file probes, exact sources/outcomes retained. No kernel/canonical proof edits.

## Principal recommendations

1. Mixed root/scalar bounds and root order reflection: x<=r^2 implies
   sqrt(x)<=r when x,r>=0; r^2<=x implies r<=sqrt(x) for x>=0 and arbitrary
   real r. Strict variants with strict squared bounds also miss directly,
   while two-statement root-monotone chains pass. Do not impose a lower-bound
   radius sign unnecessarily. [Part 35](part-35-square-root-bounds.md).
2. Nondegenerate root-difference identity: sqrt(x)-sqrt(y)=(x-y)/(sqrt(x)+
   sqrt(y)) misses directly and passes with principal-square/cancellation
   proof. Preserve nonnegative radicands and the nonzero denominator.
   [Part 36](part-36-square-root-difference.md).
3. Strict signed-square reflection: a^2<b^2 and b>=0 should give a<b without
   requiring a>=0. Direct misses; root/magnitude chain passes. The geometry
   strict-triangle dot/product block has this mathematical move, but no
   enclosing-source replacement was executed.
   [Part 3 strict follow-up](part-03-square-reflection.md).

Root-of-sum upper bound sqrt(x+y)<=sqrt(x)+sqrt(y) also misses directly.
A staged square expansion route passes. A fixed bound/interface is optional;
do not label root addition as an equality or as a full Euclidean strict
triangle theorem. [Part 37](part-37-square-root-subadditivity.md).

## Existing support and controls

Weak/strict root monotonicity, root-product identity and sqrt(x^2)=abs(x)
pass directly. Signed sqrt(x^2)=x, negative upper radius, false strictness,
negative radicand, zero rationalization denominator and root-sum equality
controls all reject. Do not add duplicate monotonicity/product rules.

## Coverage and next work

Anchor: coordinate geometry strict_triangle_one_side and root/distance
normalizations, plus native root monotonicity examples. Some scalar error
patterns are adjacent general probes, not directly extracted calculus theorem
replacements. No line-saving claim for the complete geometry module.

Next: examine the earlier high-ranked geometry equality chains in their exact
enclosing interfaces, especially tuple-coordinate/function argument transport;
classify real source redundancies versus missing general consumers. Recheck
current capabilities before using dated recommendations.

Evidence: [receipt](evidence/round-11-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Thirty-seven dated parts exist.

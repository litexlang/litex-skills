# Search round 3 — Cancellation, fractions and product errors

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current-source release build succeeded on 2026-10-08; 34 independent strict
file probes. Existing working-tree changes were preserved; no kernel or
canonical mathematical proof edits were made.

## Recommendations

1. **Absolute quotient identity:** direct abs(u/v)=abs(u)/abs(v) with v!=0
   misses; multiply-first proof passes. This fixed equality rule has explicit
   operands and a nonzero guard. Signed denominator control rejects.
   [Part 9](part-09-absolute-quotient.md).
2. **Common-term/factor cancellation:** direct additive and multiplicative
   equality/order conclusions miss, corresponding chains pass. Zero factors
   and wrong negative-factor directions reject. The eliminated term/factor is
   absent from the target, so bounded stored-relation matching must be designed,
   rather than assuming goal-only structural decomposition can find it.
   [Part 6](part-06-cancellation.md).
3. **Fraction cross multiplication:** direct positive-denominator cross and
   uncross goals miss; chains pass. Both-negative denominators also preserve
   the cross direction and were tested. Merely nonzero denominators are not
   enough. Rule should be guarded by denominator-product sign with valid WD.
   [Part 7](part-07-fraction-order.md).
4. **Product-difference estimate:** direct
   abs(u*v-x*y)<=abs(u)*abs(v-y)+abs(y)*abs(u-x) misses; decomposition chain
   passes. Omitted-error-term control rejects. This is a fixed estimate leaf
   or checked reusable interface, not unrestricted error-decomposition search.
   [Part 8](part-08-product-error.md).

Priority: quotient identity is the smallest fixed shape; cancellation and
cross multiplication are widely reusable. Product-error leaf versus explicit
library interface remains a maintainer design choice.

## Reciprocal boundary

Original reciprocal quotient route first failed denominator WD. After explicit
nonzero bridges, it failed truth search for absolute quotient identity.
Multiply-first reciprocal proof succeeds. Keep the phases distinct: a truth
rule alone does not establish nested RHS domain-evidence consumption.

## Coverage and next work

Anchors: Manual R11/R14; Analysis Chapter 6 reciprocal/product limits and
Chapter 9 product limit; geometry midpoint additive cancellation. Reduced
scalar proofs were checked, not full enclosing chapter cleanup or downstream
consumer compatibility. No speed improvement is claimed.

Next: positive/minimum radius and extremum bound consumers, then power/log
monotonicity and their source-level WD bridges. Earlier 1206 lexical candidates
remain a ranking queue, not individually audited redundancies.

Evidence: [receipt and case replay commands](evidence/round-03-2026-10-08.summary.json),
[release build log](../../../references/sources.md#unbundled-local-material). Exploratory old-binary probes
were superseded by clean current-source reruns before these recommendations.

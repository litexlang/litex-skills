# Search round 5 — Strict absolute bounds, reciprocals and unit powers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Release built successfully from current working tree on 2026-10-08.
30 independent strict file checks, with exact sources, failed shorter routes
and negative controls retained. No kernel or canonical mathematical source edits.

## Rule recommendations

1. Strict absolute/interval equivalence: -r<x<r should directly give |x|<r;
   |x|<r should project both strict endpoints. All direct variants miss, while
   case/chain routes pass. Weak interval introduction already passes and
   should not be duplicated. [Part 15](part-15-strict-absolute-interval.md).
2. Absolute contraction: ||x|-|y||<=|x-y| misses directly but the two
   reverse-triangle bounds and a symmetric-bound fold pass. This fixed metric
   leaf can remove repeated continuity proof scaffolding.
   [Part 16](part-16-absolute-contraction.md).
3. Reciprocal antitonicity on one sign region: x<=y gives 1/y<=1/x when both
   positive or both negative. Direct targets miss; a positive-product bridge
   and one chain pass. Nonzero-only/cross-zero and false strictness controls
   reject. [Part 17](part-17-reciprocal-order.md).
4. Unit-interval power range: 0<=a<=1,n in N+ gives a^n<=a. Direct misses;
   explicit induction passes. Exponent zero and a>1 controls reject. A fixed
   power range rule or checked library interface is more reusable than
   repeating induction. [Part 18](part-18-unit-power-range.md).

## Existing support and interface reuse

Analysis Chapters 6/9 reciprocal error envelope reduces to a checked
five-statement scalar proof without changing its original premises.
Prefer existing named mathematical interface reuse over a bespoke epsilon bt
rule. This probe does not verify replacing the enclosing chapters or removing
their other debt. The old canonical sources were not modified.

## Coverage and next work

Anchors: Manual R10/R15, Analysis Chapter 5 reciprocal-natural Cauchy sequence,
Chapter 9 absolute-value continuity, Chapters 6/9 reciprocal error bounds.
Reduced capability probes are not whole-source acceptance or runtime claims.

Next: review two-dimensional quadratic/dot-product estimates and zero/square
sum consequences in geometry/showcases, retaining valid sign controls and
checking existing native support before recommending new rules.
Earlier corpus inventory is a ranking aid, not proof of exhaustive cleanup.

Evidence: [round receipt](evidence/round-05-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Eighteen dated parts now exist.

# Search round 17 — factorial order and comparison consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


30 independent strict probes: 15 accepted, 15 rejected. Rejections include true capability misses and mathematical/domain controls; counts are not a correctness score. Fresh current-source release build succeeded.

## Recommendations

- Guarded native factorial order/equality reflection from already checked factorial evidence. Preserve 0/1 collision and avoid inverse/forward search cycles. [Part 50](part-50-factorial-reflection.md).
- Reuse intrinsic positivity and known negated/dual order evidence at bounded comparison consumers. Factorial positivity is already direct; ratio needs its explicit sign publication. Exact internal cause unresolved. [Part 51](part-51-native-factorial-consumers.md).
- Optional fixed native growth bound n<=factorial(n), or one reusable checked theorem. Existing predecessor and at-least-one interfaces support a short case proof. [Part 52](part-52-factorial-growth-bound.md).

## Existing support and precautions

Native forward weak/positive-region strict monotonicity, positivity, nonzero and divisibility all pass. Whole author-routes file acceptance does not prove its later repeated forall independent: isolated nested direct misses and inner-order publication passes. No special nested-factorial or user-defined choose_fn builtin is proposed.

[Receipt](evidence/round-17-2026-10-08.summary.json), sources `evidence/round-17-cases/`, build log `evidence/round-17-build.log`. Reflected order, ratio, nested order and growth soft misses are repaired in an unchanged Session; independent files are authoritative. 0/1 collisions, strict growth equality cases and negative factorial-domain controls reject. No kernel/canonical edits, trust or performance claims.

Next: Concrete Mathematics chapter02 finite sums, telescoping boundaries and shifted-index identities. Prefer actual source callers and reuse native sum interfaces before proposing new rules; do not revisit the same factorial family without new source evidence.

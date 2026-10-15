# Search round 16 — separated denominators and magnitude transport

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


32 strict independent file probes: 14 accepted, 18 rejected. Rejections mix true capability misses and mathematical/domain controls. Fresh source release build succeeded; immutable binary used for all probes. The isolated original near-point and reciprocal source theorems both pass.

## Recommendations

- Known magnitude nonzero/positive evidence -> argument nonzero. Zero reflection already works; avoid a search cycle with existing argument-nonzero -> magnitude-nonzero. [Part 47](part-47-magnitude-nonzero.md).
- Bounded affine reverse triangle abs(y)-abs(z-y)<=abs(z), using existing symmetry and affine cancellation. It compresses the source's half-neighborhood case split into two chains. [Part 48](part-48-neighborhood-magnitude-lower.md).
- Magnitude quotient bound from numerator upper and positive denominator lower bounds. Three-statement multiply-first proof passes; direct misses. [Part 49](part-49-separated-quotient-bound.md).

## Reused capability and exclusions

Reciprocal error source passes with a shortened six-statement body; direct still misses. Rational reciprocal difference identity passes, absolute identity repeats the Part 9 gap. No duplicate nomination. Safe divide's nonzero/zero equalities pass, preserving the actual zero branch. No claim of fixing the continuity theorem's separate codomain-restriction trust debt.

[Receipt](evidence/round-16-2026-10-08.summary.json), cases `evidence/round-16-cases/`, build log `evidence/round-16-build.log`. Near/reciprocal, separation, strict-neighborhood and quotient soft misses are repaired in unchanged Sessions; independent files are authoritative. Nonpositive separation, excessive neighborhood, missing denominator separation/sign, strict-from-weak and safe-divide zero controls reject.

Normal outer forall search_proof on the derived-nonzero reciprocal probe does not identify the internal WD phase. No kernel/canonical chapter edits, trust or timing claims; whole registered books were not checked.

Next: return to corpus inventory outside the repeated reciprocal/square families; inspect factorial/binomial/order estimates or finite cardinality-to-numeric interfaces in Concrete Mathematics/high-school examples before proposing new patterns.

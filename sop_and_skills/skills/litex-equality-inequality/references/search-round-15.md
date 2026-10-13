# Search round 15 — weighted means and scalar quotient bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


47 independent strict accepted/rejected probes: 16 accepted, 31 rejected. Rejections include true capability misses and mathematical/domain controls; counts are not a correctness score. One malformed generated candidate is excluded and separately retained as an authoring error; its corrected proof passes. Fresh current-worktree release build succeeded.

## Recommendations

1. Bounded convex/normalized weighted upper/lower comparison, preserving arbitrary real endpoints and exact normalization. Strict variants require a positive weight on a strict component. [Part 44](part-44-weighted-bounds.md).
2. Positive-denominator quotient-vs-scalar forward rule: a/b<=M from b>0,a<=M*b, with strict sibling. Reverse comparison already passes; no duplicate requested. [Part 45](part-45-quotient-scalar-bound.md).
3. Inspect real-base evidence consumption in square nonnegativity when the base involves a declared real-valued function. Variance direct and component/square bridges miss; explicit real carrier facts allow the complete reduced proof. Exact internal cause unresolved. [Part 46](part-46-function-real-square-sign.md).

## Source opportunities and limits

Exact reduced expectation upper interface passes with two proof statements. Least-squares reduced inequality passes with a nonnegative remainder statement and one certificate chain. Weighted scalar squares pass with two component sign facts. These are source-adjacent/interface checks, not verified whole-showcase replacements or runtime improvements. Existing arithmetic, nonnegative, probability and fraction interfaces should be reused rather than replaced with function-name-based builtins.

## Evidence

[Receipt](evidence/round-15-2026-10-08.summary.json), `evidence/round-15-cases/`, build log `evidence/round-15-build.log`. Convex, normalized, quotient and variance Session failures are repaired without restart; independent files are authoritative against contamination. Controls for negative weights/denominator, missing normalization/strictness and zero total reject. No trust, kernel or canonical mathematical source changes.

Next: inspect actual textbook reciprocal/quotient-continuity error estimates and distinguish common denominator/nonzero guards from missing absolute/metric consumers. Registered Analysis/Analysis2 use native safe-division interfaces; preserve their semantics when choosing probes.

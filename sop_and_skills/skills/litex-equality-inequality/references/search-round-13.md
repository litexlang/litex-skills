# Search round 13 — vector and dot-product consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


35 independent strict files: 18 accepted, 17 rejected. Rejections include true search misses, mathematically false controls and invalid-index controls; counts are not a correctness score. Fresh current-worktree release build succeeded and an immutable snapshot was used for the whole probe window.

## Recommendations

1. Priority: bounded arithmetic constructor consumption of literal-pair projection equalities whose coordinates are compound expressions. Two bare projection equations are accepted but their weighted sum still misses; two scaled equations make it pass. This needs precise ownership diagnosis, not general expansion of search. [Part 40](part-40-projection-arithmetic.md).
2. Authoring/interface reuse: dot addition and full real linearity use three proof statements in reduced interfaces. Direct dot coordinate expansion, nested vector expansion, symmetry, nonnegativity and known-vector transport already work. Do not add duplicate or name-based dot bt rules. [Part 41](part-41-dot-interface-reuse.md).
3. Lower-priority investigation only: bounded shallow scalar definition unfolding under arithmetic, with certificates and computation limits; direct dot linearity misses, but checked existing theorem interfaces are available. No implementation proposal is established by this single family.

## Evidence and exclusions

[Receipt](evidence/round-13-2026-10-08.summary.json), runnable `evidence/round-13-cases/`, release log `evidence/round-13-build.log`. Synchronized projection and linearity Sessions retain ordinary failed statements and accepted repairs. Scalar polynomial-alias transport passes directly, narrowing the candidate away from general arithmetic congruence. No trust or premise changes, no canonical proof/kernel edits, no enclosing geometry or broad Rust gates.

Next corpus anchors: geometry `dot_squared_plus_det_squared`, Gram/Cauchy-style quadratic identities and order consumers; compare existing native scalar algebra and nonnegative-square rules before proposing interfaces. Inventory search remains non-exhaustive.

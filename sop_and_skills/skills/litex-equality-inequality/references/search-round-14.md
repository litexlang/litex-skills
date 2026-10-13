# Search round 14 — square identities and magnitude bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


47 independent strict file probes: 23 accepted, 24 rejected. Rejections mix true capability misses and mathematical/domain controls; counts are not a correctness score. Fresh current-worktree release build succeeded. Reduced scalar and dot/det interfaces only; no enclosing geometry rewrite.

## Recommendations

- Priority: guarded absolute-radius squared-order strategy, abs(x)<=r from r>=0 and x^2<=r^2, with a strict sibling. The existing absolute-vs-absolute strategy requires abs syntax on both sides; plain radius direct goals miss but one-chain abs(x)<=abs(r)=r passes. [Part 42](part-42-absolute-square-radius.md).
- Lower priority: bounded composition of square-sum-bound extraction with exact numeric endpoint transport. Standalone extraction and standalone endpoint transport already pass; their composition at c^2<=1^2 misses. Do not duplicate either leaf or broaden global search.
- Existing capability/authoring: Cauchy squared bounds use one nonnegative-square certificate chain; scalar rotation uses one factorization chain; dot/det Gram interface uses four definition equations and one chain. No name-based dot, rotation or Cauchy bt rule recommended. [Part 43](part-43-quadratic-geometry-certificates.md).

## Evidence and corrections

[Receipt](evidence/round-14-2026-10-08.summary.json), cases `evidence/round-14-cases/`, release log `evidence/round-14-build.log`. Synchronized magnitude Session confirms weak/strict failures repaired in the same process. An initial generic numeric-endpoint nomination was discarded after successful isolated transport probes. Negative radius, weak-to-strict, missing nondegeneracy, wrong numeric constant and missing rotation-unit controls reject.

Next: move beyond geometry into rational estimates and weighted nonnegative/convex combinations in registered textbook or actual showcase callers; avoid repeating the existing signed-square/cardinality/root families. Corpus inventory remains heuristic and non-exhaustive.

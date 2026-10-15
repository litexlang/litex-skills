# Search round 18 — finite sums, translation and telescoping

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Completed Oct 9 after starting Oct 8, using one current-source release snapshot. 33 independent strict file probes: 14 accepted, 19 rejected. Rejections include true search misses, one original-source removed-syntax parse error and mathematical/domain controls. Counts are not a correctness score.

## Recommendations

- Canonical affine endpoint/offset evidence in the existing reindex consumer. Literal-plus endpoints pass; simplified subtraction endpoints need explicit equalities/reverse chain. The dispatcher already tries both orientations. [Part 53](part-53-sum-shift-endpoints.md).
- Anonymous singleton callback application/expansion evidence. Named singleton works; even a symbolic anonymous constant/eta callback misses. Naming the difference callable repairs the exact base interface. [Part 54](part-54-singleton-anonymous-sum.md).
- Optional fixed unit-stride telescoping interface, with the complete same-function/domain and inclusive boundary certificate. Exact general identity has a checked named-callback induction proof. [Part 55](part-55-telescoping-sum.md).

## Existing support and source migration

Native range addition, subtraction, scaling, adjacent partition, named singleton/last-term and the existing fixture shift orientation pass. No duplicate rules. Original Concrete Mathematics shift proof has removed $fn_eq syntax; modern fn_extension copy parses and then fails at reindex. The checked wrapper reverse-chain alternative avoids the eta waterfall, but no canonical chapter replacement was performed.

[Receipt](evidence/round-18-2026-10-09.summary.json), runnable `evidence/round-18-cases/`, release log `evidence/round-18-build.log`. Translation, singleton and telescoping failures are repaired in unchanged Sessions; independent files are authoritative. Wrong shift/endpoint, native empty interval and out-of-domain zero index reject; wrapper empty-zero behavior passes. No kernel/canonical source edits, trust or runtime claims.

Next: Concrete Mathematics finite-difference/summation-by-parts identities and rational integer-carrier interfaces, selecting actual unused source callers rather than more replays of this telescope family.

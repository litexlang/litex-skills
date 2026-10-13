# Search round 12 — geometry coordinates and function argument equality

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


31 independent strict file probes: 18 accepted, 13 rejected. Rejections include true search misses and mathematical/domain controls; counts are not a correctness score. A fresh source release build succeeded; all previous 28 snapshot outcomes reproduced, with three new midpoint probes. The synchronized Session confirms ordinary failure followed by successful repair without restart.

## Recommendations

- Priority 1: consume already checked anonymous-function argument equalities in existing congruence matching. Preserve binder scope, free captures and full domains. [Part 39](part-39-function-argument-equality.md).
- Priority 2: bounded arithmetic normalization of corresponding function arguments. Existing ordinary and arithmetic known-equality congruence work; this is narrower than general rewriting. [Part 39](part-39-function-argument-equality.md).
- Optional: finite tuple equality from complete coordinate facts, with known equal lengths and bounded enumeration. Existing reconstruction chain/native enumeration already work. [Part 38](part-38-coordinate-transport.md).
- Authoring first: geometry midpoint scalar calculations can use one chain; the extracted two-coordinate interface passes with two chains. No midpoint-specific bt rule is justified, and the enclosing theorem was not changed or verified.

## Evidence

[Current receipt](evidence/round-12-2026-10-08.summary.json), [initial historical snapshot](evidence/round-12-initial-snapshot-2026-10-08.summary.json), runnable sources `evidence/round-12-cases/`, fresh source build log `evidence/build-round-12-recheck.log`. Normal JSON and exact binary hash retained. No trust introduced, source premises unchanged.

Next corpus anchors: geometrical vector/dot-product equality consumers after main.lit:3155; determine which coordinate expansions are existing interface reuse and which scalar identities under dot/norm require a bounded consumer. No exhaustive corpus claim.

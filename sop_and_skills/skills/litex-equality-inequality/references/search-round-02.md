# Search round 2 — Recommendations, 2026-10-08

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current-source release build succeeded; 24 isolated strict file probes and ten
pilot rechecks were executed. No canonical mathematical source or kernel edits.
The working tree contained existing changes; HEAD alone is not the binary identity.

## Recommended candidates

1. Signed square reflection: a<=b from real domains, 0<=b and a^2<=b^2.
   Direct target misses; `a <= abs(a) <= abs(b) = b` passes. Do not require
   0<=a, and do not infer signed order without controlling b's sign.
   [Part 3](part-03-square-reflection.md).
2. Absolute neighborhood transfer: abs(x)<=abs(L)+r (or x<=L+r) from
   abs(x-L)<=r. Direct targets miss; one explicit chain passes. The goal
   supplies the center/radius, so a bounded rule need not search centers.
   [Part 4](part-04-absolute-neighborhood.md).
3. Structural nonnegative composition: two-square sums pass, three-square
   sums miss without intermediate signs; three already-known nonnegative
   terms pass directly. Audit composition of implicit signs, not all sum
   support, and do not add one special case for each summand count.
   [Part 5](part-05-structural-nonnegative.md).

Priority: the first two are narrowly specified candidates; the third needs
producer/consumer and bounded structural strategy investigation. The earlier
componentwise subtraction candidate still misses on the new binary.

## Existing support, not a new rule recommendation

The long Analysis Chapter 9 `max_lipschitz` theorem is a cleanup candidate:
```litex
forall a,b,A,B R, epsilon R+:
    abs(a-A) <= epsilon
    abs(b-B) <= epsilon
    =>:
        abs(max(a,b)-max(A,B)) <= epsilon
```
This self-contained scalar form passes. The finite-extremum form passes with
both sets' original finite/nonempty/real-subset conditions; dropping them
misses. These probes establish supported interfaces, not that the entire
chapter can already be rewritten or its existing trust removed.

## Search coverage and next work

Inventory covers examples, showcases, public textbooks and registered local
textbook modules: 2260 .lit files and 1206 lexical runs of >=7 relation-like
lines. The heuristic does not parse multiline strings or prove redundancy.
Duplicate/disabled code must be classified during review; raw counts are not
independent evidence.

Reviewed anchors: Manual R09/R10/R12; Analysis Chapter 6/9 product estimates;
middle-school/AM-GM examples; selected coordinate-geometry cancellation runs.
No full chapter cleanup was executed.

Next round: scalar cancellation under sums and division, then product-error
estimates and positive radii/minimum consumption. Reproduce direct targets,
match existing source owners and attach positive/negative controls before
recommending any rule. Full corpus search remains active.

Evidence: [round receipt](evidence/round-02-2026-10-08.summary.json),
[pilot recheck](evidence/pilot-current-recheck-2026-10-08.summary.json),
[inventory](evidence/inventory-2026-10-08.summary.json),
[release build log](../../../references/sources.md#unbundled-local-material).

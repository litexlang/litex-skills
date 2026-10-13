# Search round 10 — Index refinement, finite constructors and consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current working-tree release built on 2026-10-08; 43 valid independent strict
probes. One generated reserved-name parse error was corrected and excluded
before all valid probes. No kernel or canonical mathematical source edits.

## Recommendations

1. Positive integer index refinement available in WD: m in N+,index in Z,
   m<=index should prove index in N+. Direct misses; 0<m<=index chain passes.
   A call-containing goal fails preflight before that chain can run. Supplying
   the refinement or declaring the index N+ makes the call valid. Ordinary
   real positive-lower-bound propagation already passes and needs no duplicate.
   [Part 32](part-32-positive-index-refinement.md).
2. One-sided finite intersection support: direct intersection finiteness
   misses if only one side is finite, though a finite-subset route passes.
   Both-finite case already passes; neither-finite control rejects. Difference
   with finite left side already passes.
   [Part 33](part-33-finite-constructors-wd.md).
3. Finite-constructor WD and cardinality inclusion consumption: standalone
   finite union/intersection/difference facts pass but nested size comparisons
   fail preflight. Supplying finite union resolves its dedicated upper size
   bound. Intersection/difference size bounds additionally need their already-
   true constructor subset facts published. Audit these consumers rather than
   duplicate closure/size mathematics or widen arbitrary subset search.
   [Part 34](part-34-cardinality-consumers.md).

## Existing capability

Finite subset size monotonicity, strict proper-subset cardinality, equal size
plus inclusion giving equal sets, and max/min pointwise bounds pass directly.
They do not justify strict size from mere subset or equality from equal
cardinality alone; both controls reject. Empty maximum also rejects.

## Scope and next work

The aggregate helper's fresh index and assumptions were inspected; complete
producer/consumer causal repair remains unimplemented. Guarded/refined positive
controls are not migrations of original interfaces. No enclosing combinatorial
module cleanup, source trust removal or runtime improvement is claimed.

Next: return to actual higher-ranked geometry/calculus corpus blocks, looking
for sign-constrained square-root bounds and endpoint transport, then compare
function restriction/anonymous-application consumers with existing interfaces.
Maintain distinct math-rule, WD-consumer and authoring classifications.

Evidence: [receipt](evidence/round-10-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Thirty-four dated parts exist.

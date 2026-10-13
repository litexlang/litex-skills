# Search round 21 — finite-product interfaces and wrapper consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


39 independent strict files: 17 accepted, 22 rejected. False conclusions,
invalid domains and true shortcut misses are distinct. The executable is the
verified selected-scalar overlay snapshot, not the currently unbuildable
working tree; the receipt records its hash and exact source manifest and
excludes concurrent Lean compiler/infer changes. No current-worktree or
whole-chapter capability claim is made.

## Recommendations

- Consider composing singleton evaluation with anonymous callback beta
  application: `product(m,m,fn(k Z)R{c})=c` misses, while the same target with
  the intermediate `fn(k Z)R{c}(m)` passes. Named singleton already passes.
  [Part 60](part-60-anonymous-product-singleton.md).
- Inspect existing range and function-definition evidence consumption for
  empty-product wrappers. Native append already passes; source wrapper append
  needs `2<=m+1`, the preceding wrapper definition, and a chain in the best
  checked interior variant. A complete positive-index cases proof passes after
  exporting `m>=1` and, in the boundary case, `m+1=2`.
  [Part 61](part-61-empty-product-wrapper.md).
- A related follow-up is known anonymous application equalities inside a
  product: even explicitly stating both constant callback evaluations did not
  close their multiplied expression; naming the callback and stating its two
  values repairs the two-factor calculation. This isolates another consumer
  shape but does not yet identify its cause or justify global beta unfolding.

## Existing support

Native named singleton, named last-factor append, product eta callback
replacement and wrapper named singleton/empty value pass. Do not duplicate
those rules. Full eta function equality needs the supported explicit
`by fn_extension` route; aggregate eta replacement does not require that
standalone function equality. No `$fn_eq` migration of the registered chapter
was undertaken.

[Receipt](evidence/round-21-2026-10-09.summary.json) and `evidence/round-21-cases/`
preserve all complete sources, commands, exits and Normal outputs. Some long
interactive failures were output-capped; independent file output is complete.
A binder-reuse parse error was excluded, the terminated Session restarted,
and thirteen accepted statements replayed before continuing. Warm results
were never used as evidence of cold direct support.

No source/kernel changes, trust, full chapter gate or runtime claim. Next:
isolate anonymous-call equality consumption under arithmetic from aggregate
expansion, then compare named-head controls and scope/capture boundaries.

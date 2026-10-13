# Part 40 — Tuple projection equalities under arithmetic

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and proof idea

A literal pair returns its first and second entries. Multiplication and addition preserve those equalities. Corpus anchor: dot-coordinate expansion and linearity in `showcases/math_concepts_in_litex/15_coordinate_geometry_case_study/main.lit:3189`, plus `examples/proof_nodes/equal/by_known_special_property/geo_coordinate_expansion.lit`.

## Direct form and known-leaf miss

A true direct weighted projection equality fails:

```litex
forall a,b,c,d,s,t R:
    (a+b,c+d)(1)*s+(a+b,c+d)(2)*t = (a+b)*s+(c+d)*t
```

Publishing each bare projection equality still fails at the combined sum:

```litex
claim:
    ? forall a,b,c,d,s,t R:
        (a+b,c+d)(1)*s+(a+b,c+d)(2)*t = (a+b)*s+(c+d)*t
    (a+b,c+d)(1) = a+b
    (a+b,c+d)(2) = c+d
    (a+b,c+d)(1)*s+(a+b,c+d)(2)*t = (a+b)*s+(c+d)*t
```

This is not absence of projection computation: both projection lines pass. The equivalent scaled leaves pass and allow the sum to close:

```litex
claim:
    ? forall a,b,c,d,s,t R:
        (a+b,c+d)(1)*s+(a+b,c+d)(2)*t = (a+b)*s+(c+d)*t
    (a+b,c+d)(1)*s = (a+b)*s
    (a+b,c+d)(2)*t = (c+d)*t
    (a+b,c+d)(1)*s+(a+b,c+d)(2)*t = (a+b)*s+(c+d)*t
```

The synchronized Session confirms the combined sum misses before and after accepted bare projection equalities, then succeeds after the two scaled equalities, without restart.

## Existing support and verbose comparison

For a scalar-valued literal pair `(a,b)`, explicit bare projection equalities suffice for the weighted sum; a single scaled projection already passes directly. Simple sum-pair definition unfolding also passes in both reduced and unreduced forms. Known polynomial-valued scalar aliases are consumed directly under the same arithmetic shape:

```litex
forall x,y,a,b,c,d,s,t R:
    x = a+b
    y = c+d
    =>:
        x*s+y*t = (a+b)*s+(c+d)*t
```

Thus the observation is narrower than missing arithmetic congruence, missing tuple projection, or inability to transport polynomial equalities in general. Do not recommend a new rule for all arithmetic known equality.

## Negatives

Repeated first coordinate instead of the second rejects (`projection-weighted-wrong-index`); invalid index three of a pair rejects (`tuple-sum-invalid-index`). Missing one alias equation or changing the sign in the supported scalar-alias example rejects. These controls are separate from true capability misses.

## Improvement candidate

Investigate bounded arithmetic-constructor checking that consumes certified literal-tuple projection equalities even when the selected coordinate is itself a compound expression. Trigger a supported arithmetic node with corresponding scalar children; verify exact projection child/index and preserve its WD/equality certificate. Descend through a finite constructor tree with the existing leaf permissions/cost bounds, without reopening unrestricted semantic search. Projection into a known finite tuple must respect its length; no array sampling, arbitrary function evaluation or invalid-index repair.

Read-only owner locators: arithmetic congruence in `search_equal_fact_by_tuple_components.rs`, corresponding-argument matching in `search_equal_fact_proof_by_matching_one_arg_by_one.rs`, and returned finite-coordinate definition evidence. The precise failing producer/consumer is not established yet. This is a local investigation candidate, not an implemented fix or authorization to change shared AST/Runtime state.

## Evidence

Dated 2026-10-08, fresh current-worktree release build succeeded. [Receipt](evidence/round-13-2026-10-08.summary.json) retains exact immutable binary identity, source, commands, exits, Normal JSON and Session transcripts. Runnable cases in `evidence/round-13-cases/` have explicit replay commands. Normal JSON now includes nested failure evidence; conclusions use the actual failed fact, not just the outer claim label.

These are scoped observations, not universal authoring requirements or a demonstrated root cause. No kernel edits, canonical geometry replacement, whole-module check or runtime benchmark.

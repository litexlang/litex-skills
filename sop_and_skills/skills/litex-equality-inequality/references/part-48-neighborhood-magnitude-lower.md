# Part 48 — Affine reverse triangle and neighborhood lower bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and proof idea

A nearby point cannot lose more magnitude than its distance from the reference point: abs(y)-abs(z-y)<=abs(z). If abs(z-y)<=abs(y)/2, this yields abs(z)>=abs(y)/2. Source: Analysis chapter06 `near_nonzero_abs_lower`, whose isolated original case/contradiction proof passes.

## Ideal affine form: observed miss

```litex
forall z,y R:
    abs(y)-abs(z-y) <= abs(z)
```

No nonzero condition is needed for this bare reverse triangle inequality.

## Positive: one continuous chain

```litex
claim:
    ? forall z,y R:
        abs(y)-abs(z-y) <= abs(z)
    abs(y)-abs(z-y) = abs(y)-abs(y-z) <= abs(y-(y-z)) = abs(z)
```

This uses the existing difference symmetry, reverse triangle inequality and exact cancellation endpoint. Do not claim reverse triangle mathematics is wholly absent.

## Actual source cleanup candidate

The original theorem manually reverses the difference, applies a triangle bound, splits weak/strict cases and ends the impossible strict branch. The same original premises and target pass with two chains:

```litex
claim:
    ? forall z,y R:
        y != 0
        abs(z-y) <= abs(y)/2
        =>:
            abs(z) >= abs(y)/2
    abs(z-y) = abs(y-z)
    abs(y)/2 = abs(y)-abs(y)/2 <= abs(y)-abs(y-z) <= abs(y-(y-z)) = abs(z)
```

The strict neighbor interface also passes in the same shape with a strict first bound; its direct target misses. Original/direct/short strict sources are retained. No full registered chapter replacement was checked.

## Negative

The larger neighborhood abs(z-y)<=abs(y) does not imply abs(z)>=abs(y)/2: y=1,z=0 refutes it. The corresponding executable control rejects. Do not treat a weak distance premise as a strict magnitude conclusion.

## Improvement candidate

A bounded affine reverse-triangle strategy could recognize this exact two-argument magnitude/difference shape and assemble evidence from existing symmetry and reverse-triangle primitives plus checked affine cancellation. All arguments must be real and well-defined. Limit algebra normalization to the selected affine residual; no general opaque-function rewriting or intermediate-point search is implied. The source half-radius theorem may remain an explicit library interface rather than a special 1/2 builtin.

## Evidence and limits

Date: 2026-10-08. Current-worktree release build succeeded. [Round 16 receipt](evidence/round-16-2026-10-08.summary.json) retains immutable binary identity, exact complete sources, commands, exits, Normal JSON, Session responses and durable replay commands. Runnable sources are in `evidence/round-16-cases/`.

No kernel/canonical textbook edits, added trust or runtime claims. Only isolated scalar/source-interface checks; registered chapters, continuity theorem dependencies and downstream consumers were not verified. Candidates are not implemented rules or complete causal diagnoses.

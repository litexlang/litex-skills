# Part 20 — A nonpositive real square has zero base

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For real a, a^2<=0 forces a=0, since a nonzero real has a strictly positive
square. Anchor: coordinate geometry `distance_sq_positive_of_ne`, which
projects nonpositive component squares before recovering coordinates.

## Positive and ideal form

```litex
claim:
    ? forall a R:
        a^2 <= 0
        =>:
            a = 0
    by contra:
        ? a = 0
        a != 0
        0 < a^2 <= 0
        impossible 0 < 0
```
Passes; direct universal conclusion misses. The a^2=0 premise already gives
a=0 directly, so no duplicate zero-square rule is needed.

## Boundary and candidate

Extend the zero-square consumer to nonpositive square evidence under an
explicit real-base domain. Nonnegative alone says nothing about zero:
a=1 refutes that false implication. Do not infer a real base merely because
its square is real (complex i has square -1 and is nonzero).
Both false implications were also executed and rejected. The complex control
explicitly supplies a^2 in R and a^2<=0, showing why the proposed leaf must
retain the base's real domain rather than merely its square's domain.

## Evidence

[Round 6 receipt](evidence/round-06-2026-10-08.summary.json), `square-nonpositive-*`,
`square-zero-direct`. Strict current working-tree release, 2026-10-08.

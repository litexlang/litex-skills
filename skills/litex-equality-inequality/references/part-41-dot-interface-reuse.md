# Part 41 — Reuse dot definitions and keep linear calculations short

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

The planar dot product is user-defined by two coordinate products, and vector difference is a user-defined pair. The source already exposes dot symmetry, addition and linearity as mathematical interfaces. Do not add a builtin based only on the user function name `dot`.

## Existing direct support

The complete reduced-coordinate expansion passes:

```litex
have fn vec(A,B cart(R,R)) cart(R,R) = (B(1)-A(1),B(2)-A(2))
have fn dot(u,v cart(R,R)) R = u(1)*v(1)+u(2)*v(2)
forall u,v,w cart(R,R):
    dot((u(1)+v(1),u(2)+v(2)),w) = (u(1)+v(1))*w(1)+(u(2)+v(2))*w(2)
```

Nested vector-difference expansion also passes directly. Dot symmetry, nonnegativity of self-dot, and transporting a known vector equality into a zero dot product all pass in this exact definition context.

## Positive: concise linearity proof

The direct linearity statement misses, but this three-statement proof body passes:

```litex
have fn vec(A,B cart(R,R)) cart(R,R) = (B(1)-A(1),B(2)-A(2))
have fn dot(u,v cart(R,R)) R = u(1)*v(1)+u(2)*v(2)
claim:
    ? forall u,v,w cart(R,R),a,b R:
        dot((a*u(1)+b*v(1),a*u(2)+b*v(2)),w) = a*dot(u,w)+b*dot(v,w)
    dot(u,w) = u(1)*w(1)+u(2)*w(2)
    dot(v,w) = v(1)*w(1)+v(2)*w(2)
    dot((a*u(1)+b*v(1),a*u(2)+b*v(2)),w) = (a*u(1)+b*v(1))*w(1)+(a*u(2)+b*v(2))*w(2) = a*(u(1)*w(1)+u(2)*w(2))+b*(v(1)*w(1)+v(2)*w(2)) = a*dot(u,w)+b*dot(v,w)
```

Addition similarly passes with two coordinate equalities plus one chain. Deleting those two equalities in the addition example makes the single-chain variant miss. More elaborate aliases, explicit scaled dot-product bridges and raw tuple-projection arithmetic are not necessary in these accepted reduced forms.

## Verbose comparison and failed overexpansion

The source linearity theorem introduces a `sum_vector`, asserts its two projections, records scaled coordinate products, releases dot coordinate formula twice, records scaled dot equalities, then ends with a calculation chain. The retained three-statement interface uses the same mathematical definitions and target but is not a verified replacement of the full canonical theorem.

A chain that inserts the unreduced tuple projections between `dot` and expanded arithmetic fails in the same build. Its failed adjacent equality is the projection-weighted sum covered by [Part 40](part-40-projection-arithmetic.md). Direct expanded dot coordinates pass, so adding those projections blindly is counterproductive in this case.

## Negatives

Addition with the wrong minus sign rejects. Self-dot need not be strictly positive (zero vector), and zero dot product does not transfer to an unrelated vector without equality. All controls have runnable sources and failed Normal results in the receipt.

## Improvement status

Prioritize the general projection-equality consumer candidate in Part 40. No dot-specific rule is justified; source-defined dot laws are existing reusable mathematical interfaces. Optional automation for simultaneous shallow unfolding of several transparent scalar definitions would require a separate bounded design and independent evidence, not merely this direct linearity miss. No unrestricted unfolding or function-name special cases are recommended.

## Evidence

Dated 2026-10-08, fresh current-worktree release build succeeded. [Receipt](evidence/round-13-2026-10-08.summary.json) retains exact immutable binary identity, source, commands, exits, Normal JSON and Session transcripts. Runnable cases in `evidence/round-13-cases/` have explicit replay commands. Normal JSON now includes nested failure evidence; conclusions use the actual failed fact, not just the outer claim label.

These are scoped observations, not universal authoring requirements or a demonstrated root cause. No kernel edits, canonical geometry replacement, whole-module check or runtime benchmark.

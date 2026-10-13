# Part 46 — Consume real-valued function evidence in square nonnegativity

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

The probability showcase has a declared real-valued expectation and defines variance as nonnegative-weighted squared centered values. A real scalar square is nonnegative. Function domains are exactly the source's limited two-point vectors; none are replaced by unrestricted functions.

## Direct miss and first failing bridge

The complete reduced variance statement misses:

```litex
let two_point_vector = fn(index N+: index <= 2) R
have fn expectation2(values,probs two_point_vector) R = values(1)*probs(1)+values(2)*probs(2)
have fn variance2(values,probs two_point_vector) R = (values(1)-expectation2(values,probs))^2*probs(1)+(values(2)-expectation2(values,probs))^2*probs(2)
forall values,probs two_point_vector:
    probs(1) >= 0
    probs(2) >= 0
    =>:
        variance2(values,probs) >= 0
```

Trying to expose each weighted component still misses at the first product. Trying to expose its square first then misses at `(values(1)-expectation2(values,probs))^2>=0`.

The base is independently checkably real:

```litex
let two_point_vector = fn(index N+: index <= 2) R
have fn expectation2(values,probs two_point_vector) R = values(1)*probs(1)+values(2)*probs(2)
have fn variance2(values,probs two_point_vector) R = (values(1)-expectation2(values,probs))^2*probs(1)+(values(2)-expectation2(values,probs))^2*probs(2)
forall values,probs two_point_vector:
    values(1)-expectation2(values,probs) $in R
```

This is not mathematical ambiguity or an absent real return declaration.

## Positive: explicit carrier evidence allows the route

```litex
let two_point_vector = fn(index N+: index <= 2) R
have fn expectation2(values,probs two_point_vector) R = values(1)*probs(1)+values(2)*probs(2)
have fn variance2(values,probs two_point_vector) R = (values(1)-expectation2(values,probs))^2*probs(1)+(values(2)-expectation2(values,probs))^2*probs(2)
claim:
    ? forall values,probs two_point_vector:
        probs(1) >= 0
        probs(2) >= 0
        =>:
            variance2(values,probs) >= 0
    values(1)-expectation2(values,probs) $in R
    values(2)-expectation2(values,probs) $in R
    (values(1)-expectation2(values,probs))^2 >= 0
    (values(2)-expectation2(values,probs))^2 >= 0
    (values(1)-expectation2(values,probs))^2*probs(1) >= 0
    (values(2)-expectation2(values,probs))^2*probs(2) >= 0
    variance2(values,probs) = (values(1)-expectation2(values,probs))^2*probs(1)+(values(2)-expectation2(values,probs))^2*probs(2) >= 0
```

The variance Session keeps definitions after the direct soft failure and accepts this repair without restarting. This is an observed bridge, not a recommendation to always echo function return types or a claim of globally minimal proof length.

## Related narrower scalar support

For p,q>=0, direct p*x^2+q*y^2>=0 misses; explicitly publishing each weighted square's nonnegativity passes. That is the earlier Part 5 nonnegative-composition family. The function-based variance requires additional real-base evidence in this build, so do not conflate the two first failures.

## Negatives

A declared real return alone does not supply positive weights. Without their sign guards, variance can be negative: values(1)=1, values(2)=0, probs(1)=-1, probs(2)=0 gives expectation=-1 and this variance formula -4. The unguarded reduced theorem rejects, as does the unguarded weighted scalar square sum.

## Improvement candidate

Inspect how square-nonnegativity child obligations consume real-domain evidence for subtraction involving a declared real-valued function. Trigger an actual real-square sign target, verify the base's complete carrier evidence including function domain guards, and cite it in the square proof. Parent WD/callable metadata must not silently grant unrestricted semantic search. No free carrier assumption or global depth increase is justified. The precise producer/consumer mismatch is unresolved; this is a bounded investigation nomination and an extension of Part 5 evidence, not a causal diagnosis or kernel repair.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 15 receipt](evidence/round-15-2026-10-08.summary.json) retains immutable binary identity, full sources, commands, exits, Normal JSON and synchronized Session responses. Durable sources in `evidence/round-15-cases/` have replay commands. One malformed generated least-squares candidate is separately retained as excluded authoring-error evidence; its corrected version was tested and passes. It is not a kernel miss.

No trust, kernel/canonical source changes, enclosing showcase verification or performance claims. These are scoped cases and nominations, not universal rules or implemented enhancements.

# Part 76 — One evaluated value selects a quadratic parameter

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Actual source and mathematical meaning

The ODE showcase defines `quadratic_solution(c,x)=x^2+c`. Its initial-value
theorem says `quadratic_solution(c,0)=y0` determines `c=y0`. Source inputs are
real and the function is total; no nonzero or distinctness premise is needed.
The isolated probe renames only the function to avoid Session name reuse.

## Positive: shrink the source chain to one value fact

The original body `quadratic_solution(c,0)=0^2+c=c` passes. This shorter body
also passes in its full independent context:

```litex
have fn r36_quadratic_solution(c,x R) R = x^2+c
thm initial_value:
    ? forall c,y0 R:
        r36_quadratic_solution(c,0)=y0
        =>:
            c=y0
    r36_quadratic_solution(c,0)=c
```

The actual task-specific theorem name is in
[the runnable short file](evidence/round-36-cases/initial-short-value.lit).
Deleting the entire body fails cold. Standalone function-value equalities at
zero and one already pass; do not confuse evaluating a value with automatically
discovering that bridge in a different target family.

At input1, the parameter is y0-1; at arbitrary real x, it is y0-x^2. Both direct
parameter targets miss, while publishing the matching function value equation
repairs the unchanged target. Do not erase the input's squared contribution.

## Order consumer: one meaningful chain

This independently checked weak-order control passes:

```litex
claim:
    ? forall c,M R:
        r36_quadratic_solution(c,0)<=M
        =>:
            c<=M
    c=r36_quadratic_solution(c,0)<=M
```

Its direct bodyless counterpart misses. Publishing the source value chain
`f(c,0)=0^2+c=c` also repairs the same target. The strict direct order misses;
the strict claim with that value bridge passes. No strict one-chain variant
was checked here, so do not extend the weak-chain acceptance by analogy.
These are dated scoped bridges, not a general permanent requirement to echo
all function definitions or append the target after them.

## Negatives and remaining scope

Using input1 while concluding c=y0 is false and rejects. A fact about a
different parameter d cannot determine c; that control rejects. A weak bound
cannot imply c<M when equality is allowed; that variant rejects. Preserve
actual function arguments and carriers, rather than identifying calls by
rendered spelling or discarding their parameters.

The bridge is a readable value-evaluation step. The direct consumption misses
may inform a bounded named-value consumer audit alongside Part75, retaining
actual definition/call/domain evidence. They do not justify general unfolding,
global search changes or a universal function-value shortcut. No kernel change
or complete causal repair is claimed.

## Evidence

[Round36 receipt](evidence/round-36-2026-10-09.summary.json):17 unique cold strict files,
9 accepted/8 rejected, all promoted copies rechecked; original source hash,
exact adaptation and fixed fresh binary retained. Initial build failed during
concurrent Lean changes; the successful recheck build supersedes that block.
Warm Session25852 retains earlier theorem facts and uses round29 snapshot;
its bodyless initial theorem success is not independent acceptance. No ODE
showcase/derivative whole-file gate, canonical/kernel/protected-owner edit,
new trust or runtime claim.

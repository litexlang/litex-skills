# Part 102 — Small recursive values: compress the trace, retain its route

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Actual examples and mathematical proof idea

Source examples/test_statements/boundaries contains recursive-equation-explicit-chain
and recursive-increment-explicit-chain. The former repeatedly returns its
predecessor's value from base 0; the latter adds 1 at each successor. Evaluate
the base and one or two recursive equations. Keep the exact induction
definitions and natural-number carriers. The source comments explicitly
classify required explicit steps as a capability limitation, not a verifier bug.

## Constant recursion: seven facts become two chains

```litex
have fn f(n N) N by induc n from 0:
    case n = 0: 0
    case n >= 1: f(n - 1)
f(1)=f(1-1)=f(0)=0
f(2)=f(2-1)=f(1)=0
```

[Complete compressed positive](evidence/round-62-cases/zero-compressed-chains.lit).
The original publishes f(0)=0, 1-1=0, several separate f(1) equations and
finally its f(2) chain. Its seven post-declaration statements pass, but can be
replaced by the two chains above. No mathematical claim or function definition
is weakened. Bare f(2)=0 fails. The second chain alone also fails: the first
chain contributes the value needed downstream. Publishing only f(0)=0 does
not make the bare f(2) endpoint pass. These are separate cold-file controls.

## Increment recursion: keep an internal value bridge

```litex
have fn f(n N) N by induc n from 0:
    case n = 0: 0
    case n >= 1: f(n - 1) + 1
f(1-1)=f(0)=0
f(1)=f(1-1)+1=0+1=1
```

[Complete two-chain positive](evidence/round-62-cases/increment-two-chains.lit).
The source's preceding standalone f(0)=0 is removable; three facts become
two. Collapsing both moves into `f(1)=f(1-1)+1=f(0)+1=0+1=1` without earlier
publication fails. Publishing f(0)=0 before that longer chain also passes,
so the displayed route is not asserted to be the unique or global minimum.

After publishing the first chain, replacing the second with bare f(1)=1 still
fails. Likewise bare f(1)=1 and `f(1)=f(0)+1=1` fail independently.
Keep the recursive expression as the useful intermediate in this context.
[One-chain miss](evidence/round-62-cases/increment-one-chain.lit),
[inner value plus bare miss](evidence/round-62-cases/increment-inner-and-bare.lit),
[alternative base-plus-chain positive](evidence/round-62-cases/increment-base-one-chain.lit).

## Negatives and improvement boundary

Constant recursion f(2)=1 and increment recursion f(1)=2 reject. More
decisively, the accepted increment two-chain route with its final value
changed from 1 to 2 also rejects. A true bare endpoint miss is not that kind
of mathematical negative.
[Wrong two-chain conclusion](evidence/round-62-cases/increment-two-chains-wrong.lit).

No new bt rule is proposed: these examples already have meaningful explicit
routes, and their source user classification is preserved. The observed
search boundary does not establish a missing recursive evaluation theorem,
an internal kernel defect, unrestricted unfolding permission or runtime cost.
No universal closed form or arbitrary-index result was checked here.

## Evidence

[Receipt](evidence/round-62-2026-10-09.summary.json):17 independent strict files,
6 accepted/11 Normal rejections, promoted files checked with the fixed
round62 snapshot after a successful current-source release build. The build
first waited for another process's lock; no competing process was stopped.
Exact source hashes and build log retained. Older round61 snapshot prechecks
agree but do not own current acceptance. Session9174 remains on round61,
with renamed recursive declarations and literal failed/passing attempts
journaled; cold source files use the original name f and own deletion evidence.
No canonical examples, kernel, trust, protected structs or performance claims.

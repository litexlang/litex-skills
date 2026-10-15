# Part 52 — A reusable factorial growth bound

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

For natural n, n<=factorial(n). At n=0 it is immediate; at n>0, factorial(n)=n*factorial(n-1) and factorial(n-1)>=1. This is a native mathematical bound, not automatic unfolding of a user-defined counting function.

## Ideal direct form: observed miss

```litex
forall n N:
    n <= factorial(n)
```

The native denominator-style lower bound factorial(n)>=1 already passes; the stronger comparison with the base does not.

## Positive: use the existing predecessor and sign interfaces

```litex
claim:
    ? forall n N:
        n <= factorial(n)
    n >= 0
    n <= 0 or n > 0
    by cases:
        ? n <= factorial(n)
        case n <= 0:
            n = 0
            n = 0 <= 1 = factorial(0) = factorial(n)
        case n > 0:
            n $in N+
            factorial(n-1) >= 1
            n <= n*factorial(n-1) = factorial(n)
```

This repaired the direct miss in the same Session. A separate induction proof also passes, but its induction hypothesis is unused; the case proof better matches the mathematical spine.

An initial `n=0 or n>0` classification misses directly. The tested proof uses the supported order dichotomy `n<=0 or n>0` and known natural nonnegativity, then identifies the zero case. The failed classification is a true capability observation, not a mathematical negative.

## Negative and domain boundary

Unconditional n<factorial(n) rejects: equality holds at n=1 and n=2. Negative integers are outside native factorial's N domain and reject. Closed 0/1/2/3 values are retained as runnable boundary evidence.

## Improvement status

A fixed native growth lower-bound rule could check the natural domain and return this certified mathematical property. Alternatively keep it as a reusable checked theorem using the case proof above; the direct miss does not require automatic replacement of every induction/case proof. Nomination is optional until actual consumers and cost justify it. Strict-growth variants require a distinct boundary and have not been proved as general interfaces in this round.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 17 receipt](evidence/round-17-2026-10-08.summary.json) retains exact immutable binary identity, complete source, commands, exits, Normal JSON, synchronized Session responses and durable replay commands. Runnable cases are in `evidence/round-17-cases/`.

No kernel/canonical mathematical source edits, trust, whole-textbook gate or performance claims. Cases are dated interface evidence and nominations, not implemented enhancements or universal authoring requirements.

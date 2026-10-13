# Part 18 — Natural powers on the unit interval

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For 0<=a<=1 and positive natural n, a^n<=a. Repeated multiplication by a
does not increase a nonnegative value. Anchor: Manual R15 unit-interval bound.

## Positive

```litex
claim:
    ? forall a R,n N+:
        0 <= a
        a <= 1
        =>:
            a^n <= a
    by induc n from 1:
        ? a^n <= a
        ? from n = 1:
            a^n = a^1 = a
        ? induc:
            a^(n+1) = a^n*a^1 = a^n*a <= a^n*1 = a^n <= a
```
Passes. The same direct universal target without induction misses.

## Negative and candidate

Including n=0 is false for a=1/2: a^0=1>a. Removing the upper bound a<=1
is false for a=2,n=2. Both variants were executed and rejected.

A fixed unit-interval power-range rule or existing checked named interface
can remove repeated induction in callers. Preserve positive-natural exponent
evidence and interval bounds. It does not imply the same statement for
arbitrary real exponents, negative bases, or exponent zero. This differs from
successor monotonicity and from integer parity rules.

## Evidence

[Round 5 receipt](evidence/round-05-2026-10-08.summary.json), `unit-power-*`.
Current working-tree release built on 2026-10-08; strict clean files.

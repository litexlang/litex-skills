# Part 50 — Reflect factorial order and equality

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and existing support

Native factorial is nondecreasing on N, strictly increasing on N+, and has the collision factorial(0)=factorial(1)=1. Existing factorial_monotonicity and factorial_order_author_routes examples are the source anchors; high-school counting uses native factorial alongside a user-defined Pascal/choose function. Native weak/guarded strict forward monotonicity, positivity, nonzero and divisibility all pass in this round. Do not add duplicate forward rules or treat the user function choose_fn as a builtin.

## Ideal direct forms: observed misses

```litex
forall m,n N:
    factorial(m) < factorial(n)
    =>:
        m < n
```
```litex
forall m N,n N+:
    factorial(m) <= factorial(n)
    =>:
        m <= n
```

Strict reflection needs only natural inputs. Weak reflection uses positive right argument; no positive left argument is needed.

## Positive: current contradiction routes

```litex
claim:
    ? forall m,n N:
        factorial(m) < factorial(n)
        =>:
            m < n
    by contra:
        ? m < n
        n <= m
        factorial(n) <= factorial(m)
        impossible factorial(m) < factorial(n)
```
```litex
claim:
    ? forall m N,n N+:
        factorial(m) <= factorial(n)
        =>:
            m <= n
    by contra:
        ? m <= n
        n < m
        factorial(n) < factorial(m)
        impossible factorial(m) <= factorial(n)
```

The initial variants without the explicit integer comparison miss inside factorial monotonicity. Exposing n<=m / n<m under the contradiction supplies that native rule's premise. Both direct misses are repaired in the same later Session without restart.

## Equality on the positive domain

The direct factorial(m)=factorial(n) -> m=n for m,n N+ misses. A self-contained checked reflected-order theorem followed by two applications proves it; see receipt `factorial-equality-reflected-interface`. This is a reusable mathematical interface, not an assumption or trust.

## Negatives

Weak reflection without the right-positive guard rejects: m=1,n=0 gives equal factorials but m<=n is false. Equality reflection on all N rejects for m=0,n=1. Unconditional strict forward monotonicity rejects for 0<1 because their factorials are equal. Full domain and boundary controls are runnable in the receipt.

## Builtin candidate

Consume already checked factorial comparisons to reflect strict order on N, weak order with n>=1, and equality when both arguments are positive. Preserve exact domain/sign evidence and the 0/1 collision. This is not syntax-decreasing descent when a naked argument-order goal queries a larger factorial expression: use bounded known-fact/certificate queries rather than unrestricted truth search, which can cycle with forward factorial monotonicity. No global inverse-function discovery or arbitrary function-name inference is implied.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 17 receipt](evidence/round-17-2026-10-08.summary.json) retains exact immutable binary identity, complete source, commands, exits, Normal JSON, synchronized Session responses and durable replay commands. Runnable cases are in `evidence/round-17-cases/`.

No kernel/canonical mathematical source edits, trust, whole-textbook gate or performance claims. Cases are dated interface evidence and nominations, not implemented enhancements or universal authoring requirements.

# Part 44 — Convex and normalized weighted bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source anchor

Nonnegative weights adding to one preserve a common upper/lower bound. Positive-total weights can be normalized by their sum. Endpoints, observations and the common bound are arbitrary reals; do not require nonnegative observations or M. The probability showcase defines a two-coordinate probability vector and `expectation2(values,probs)` by the weighted sum. These bounds are adjacent use probes of that interface, not existing source theorem rewrites.

## Ideal direct form: observed miss

```litex
forall p,q,x,y,M R:
    p >= 0
    q >= 0
    p+q = 1
    x <= M
    y <= M
    =>:
        p*x+q*y <= M
```

Lower bounds, unit-interval parameter variants and positive-total normalized direct bounds also miss.

## Positive: concise current route

```litex
claim:
    ? forall p,q,x,y,M R:
        p >= 0
        q >= 0
        p+q = 1
        x <= M
        y <= M
        =>:
            p*x+q*y <= M
    p*x+q*y <= p*M+q*M = (p+q)*M = M
```
```litex
claim:
    ? forall p,q,x,y,M R:
        p >= 0
        q >= 0
        p+q > 0
        x <= M
        y <= M
        =>:
            (p*x+q*y)/(p+q) <= M
    p*x+q*y <= p*M+q*M = (p+q)*M
    (p*x+q*y)/(p+q) <= ((p+q)*M)/(p+q) = M
```

The primary Session reproduces both direct misses and their successful chain repairs without restart. Under the source's exact limited two-coordinate function domains, expectation upper bounds likewise pass after one definition equality and one weighted chain:

```litex
let two_point_vector = fn(index N+: index <= 2) R
have fn expectation2(values,probs two_point_vector) R = values(1)*probs(1)+values(2)*probs(2)
claim:
    ? forall values,probs two_point_vector,M R:
        probs(1) >= 0
        probs(2) >= 0
        probs(1)+probs(2) = 1
        values(1) <= M
        values(2) <= M
        =>:
            expectation2(values,probs) <= M
    expectation2(values,probs) = values(1)*probs(1)+values(2)*probs(2)
    values(1)*probs(1)+values(2)*probs(2) <= M*probs(1)+M*probs(2) = M*(probs(1)+probs(2)) = M
```

Direct expectation upper bound misses. This establishes a reduced usable interface, not full-source replacement.

## Strict variants

One strictly bounded component with a strictly positive weight suffices, while the other component may have zero weight. Direct strict and the initial normalized strict chain miss; exposing two component comparisons passes:

```litex
claim:
    ? forall p,q,x,y,M R:
        p > 0
        q >= 0
        p+q > 0
        x < M
        y <= M
        =>:
            (p*x+q*y)/(p+q) < M
    p*x < p*M
    q*y <= q*M
    p*x+q*y < p*M+q*M = (p+q)*M
    (p*x+q*y)/(p+q) < ((p+q)*M)/(p+q) = M
```

The convex strict sibling passes by the same component-bridge pattern with p+q=1.

## Negatives

Negative weights can overshoot: p=-1,q=2,x=0,y=M=1. Nonnegative weights without normalization can overshoot: p=q=x=y=M=1. A strict x<M with p=0 does not force a strict mean bound: q=1,y=M. Zero total is invalid for division. All controls reject; denominator positivity/nonzero and sign conditions are independent obligations.

## Improvement candidates

Bounded weighted-sum upper/lower strategy: recognize the fixed sum form, verify nonnegative weights, exact weight normalization, and each component bound. Strict variants must justify at least one strictly positive weight multiplying a strict bound; weak components cannot create strictness. Generate finite child obligations and keep WD/citations; do not assume M>=0. The normalized version may reuse the positive-denominator scalar strategy nominated in Part 45 plus a checked numerator bound.

No causal diagnosis or performance claim from these probes. Broader finite-sum support requires independent domain/callback evidence.

## Existing source authoring opportunity

The least-squares reduced inequality passes with one explicit nonnegative remainder fact and one certificate chain, while the certificate without that fact misses. See receipt `mean-least-squares-nonnegative-bridge`. This is related to existing nonnegative-composition evidence in Part 5; do not introduce a mean-specific builtin.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 15 receipt](evidence/round-15-2026-10-08.summary.json) retains immutable binary identity, full sources, commands, exits, Normal JSON and synchronized Session responses. Durable sources in `evidence/round-15-cases/` have replay commands. One malformed generated least-squares candidate is separately retained as excluded authoring-error evidence; its corrected version was tested and passes. It is not a kernel miss.

No trust, kernel/canonical source changes, enclosing showcase verification or performance claims. These are scoped cases and nominations, not universal rules or implemented enhancements.

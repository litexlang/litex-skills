# Part 55 — A bounded telescoping-sum interface

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and proof idea

For a nonempty integer interval, summing f(k+1)-f(k) leaves f(b+1)-f(a). Inclusive endpoints matter. Native last-term and singleton interfaces give an induction proof; a fixed telescoping rule could avoid repeating it at callers.

## Ideal direct form: observed miss

```litex
forall a,b Z,f fn(k Z) R:
    a <= b
    =>:
        sum(a,b,fn(k Z) R {f(k+1)-f(k)}) = f(b+1)-f(a)
```

The full Z-to-R callback domain makes both f(a) and f(b+1) legal. No nonnegativity or monotonicity of f is needed.

## Positive: check the exact general identity

```litex
claim:
    ? forall a,b Z,f fn(k Z) R:
        a <= b
        =>:
            sum(a,b,fn(j Z) R {f(j+1)-f(j)}) = f(b+1)-f(a)
    let delta_terms = fn(j Z) R {f(j+1)-f(j)}
    by induc m from a:
        ? sum(a,m,delta_terms) = f(m+1)-f(a)
        ? from m = a:
            delta_terms(a) = f(a+1)-f(a)
            sum(a,m,delta_terms) = sum(a,a,delta_terms) = delta_terms(a) = f(a+1)-f(a) = f(m+1)-f(a)
        ? induc:
            a <= m
            delta_terms(m+1) = f((m+1)+1)-f(m+1)
            sum(a,m+1,delta_terms) = sum(a,m,delta_terms)+delta_terms(m+1) = (f(m+1)-f(a))+(f((m+1)+1)-f(m+1)) = f((m+1)+1)-f(a)
    sum(a,b,delta_terms) = f(b+1)-f(a)
    sum(a,b,fn(j Z) R {f(j+1)-f(j)}) = sum(a,b,delta_terms) = f(b+1)-f(a)
```

This proves the exact same a,b,Z real-valued-function interface and repairs the direct miss in the same Session. A 1..n positive-index variant also passes. The initial all-literal-callback induction failed at the singleton base; Part 54 isolates that earlier consumer gap. The successful induction keeps one named difference callable and avoids unnecessary affine simplification under opaque f during the step.

## Negative

The endpoint f(b)-f(a) is wrong for an inclusive range; f(k)=k gives one on a=b but the wrong endpoint gives zero. The executable off-by-one universal rejects. Callback domain guards and nonempty interval conditions remain obligations; this rule does not assign a native empty sum convention.

## Builtin candidate

Recognize a difference summand of the same checked function at index+1 and index (or a separately specified predecessor-oriented sibling), with unit integer stride and correct inclusive boundary values. Consume the existing range/callback WD evidence, retain free-capture identity and a typed telescoping certificate; do not accept unsupported mixed functions without equality evidence, wrong endpoint/stride or invalid domain. No arbitrary recurrence discovery or arbitrary cancellation of differently indexed functions is implied.

A reusable checked theorem is also a valid current interface. A direct miss does not mandate eliminating every mathematical induction; prioritize actual repeated callers and the narrower singleton/translation consumers before extending default search.

## Evidence and limits

Completed 2026-10-09; started 2026-10-08. The successful source release build and all probes use one immutable binary snapshot; individual wall timestamps were not captured. [Round 18 receipt](evidence/round-18-2026-10-09.summary.json) retains source, exact command/exit/Normal JSON, binary identity, synchronized Session responses and durable replay commands. Sources are in `evidence/round-18-cases/`.

No kernel/canonical textbook edits, trust, whole-book gate or performance claims. These are dated scoped observations and nominations; current-syntax source probes are independent copies, not registered chapter repairs.

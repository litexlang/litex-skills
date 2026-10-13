# Part 54 — Singleton sums with anonymous callbacks

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

A nonempty singleton interval sum equals its one legal callback value. For named callbacks the direct interface already works. Anonymous callbacks with an outer symbolic capture are an observed checking boundary in this build.

## Existing named support

```litex
forall a Z,f fn(k Z) R:
    sum(a,a,f) = f(a)
```

Named last-term expansion, range addition/subtraction/scaling and adjacent partition also pass directly in independent probes. Their long induction fixtures do not justify duplicate builtin rules.

## Direct anonymous misses

A simple constant callback misses:

```litex
forall c R:
    sum(1,1,fn(j Z) R {c}) = c
```

Eta callback sum(1,1,fn(j Z)R{f(j)})=f(1) also misses. For the difference callback, raw application, expanded f(2)-f(1) and affine f(1+1)-f(1) endpoints all miss. Thus this is not merely the final telescoping cancellation.

## Positive: name the callable once

```litex
claim:
    ? forall f fn(k Z) R:
        sum(1,1,fn(j Z) R {f(j+1)-f(j)}) = f(2)-f(1)
    let h = fn(j Z) R {f(j+1)-f(j)}
    sum(1,1,h) = h(1)
    h(1) = f(1+1)-f(1)
    1+1 = 2
    h(1) = f(2)-f(1)
    sum(1,1,fn(j Z) R {f(j+1)-f(j)}) = sum(1,1,h) = h(1) = f(2)-f(1)
```

The raw-application miss is followed by this successful proof in the same Session. This is an observed interface bridge, not a permanent instruction to name every lambda or claim global minimality. Exact callback, free capture and domain are retained.

## Boundaries and improvement candidate

Inspect the singleton-sum consumer's application construction and callback expansion evidence for an anonymous function value. For equal legal interval endpoints, use exactly one callback application with its domain/guard, binder/free-capture and beta/WD certificates. Do not require evaluating an opaque captured f numerically or invent a value for it. Reuse the existing named-singleton law; no new anonymous constant-specific rule is justified.

Zero outside a declared N+ callback domain remains invalid. Empty native intervals must not be treated as singletons or default zero. These controls are in the receipt. The complete internal producer/consumer cause is not yet established.

## Evidence and limits

Completed 2026-10-09; started 2026-10-08. The successful source release build and all probes use one immutable binary snapshot; individual wall timestamps were not captured. [Round 18 receipt](evidence/round-18-2026-10-09.summary.json) retains source, exact command/exit/Normal JSON, binary identity, synchronized Session responses and durable replay commands. Sources are in `evidence/round-18-cases/`.

No kernel/canonical textbook edits, trust, whole-book gate or performance claims. These are dated scoped observations and nominations; current-syntax source probes are independent copies, not registered chapter repairs.

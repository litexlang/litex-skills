# Part 60 — Evaluate anonymous singleton products through the callback endpoint

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and source

The product of one legal term equals that term. Concrete Mathematics Chapter 2
uses singleton products in `finite_coefficient_product_211` and adds eta
functions/equalities around named source functions. Native named singleton
`product(m,m,f)=f(m)` already passes on the tested legal domains.

## Direct miss and shortest checked route

```litex
forall c R,m Z:
    product(m,m,fn(k Z) R {c})=c
```

The direct target misses, whereas this one-chain author passes:

```litex
claim:
    ? forall c R,m Z:
        product(m,m,fn(k Z) R {c})=c
    product(m,m,fn(k Z) R {c})=fn(k Z) R {c}(m)=c
```

The first equality alone already passes. The nonconstant callback variant
`fn(k Z)R{k+1}` likewise needs the explicit application endpoint before `m+1`.
The source eta callback `fn(k N)R{f(k)}` has the same singleton shape.

## Negatives and nomination

The wrong target `c+1` rejects. A callback declared only on N+ cannot be used
at the singleton index zero. Native reversed intervals reject at their own
range guard; the source wrapper's empty-product value remains a separate
interface.

Consider a bounded composition of the existing singleton law and the one
checked callback application, retaining complete index/callback WD. Do not
add a duplicate named-singleton rule or unrestricted anonymous-body unfolding.
Product eta replacement already passes even when standalone full eta equality
misses; the latter checks via `by fn_extension`.

## Two-factor follow-up

The direct constant two-factor calculation and a chain with both anonymous
application value equations still miss at the multiplied anonymous calls.
The [named callback repair](evidence/round-21-cases/product-anonymous-two-factor-named-bridge.lit)
passes. This is a known-equality consumer observation, not proof that the
singleton nomination alone repairs general anonymous products.

## Evidence

[Round 21 receipt](evidence/round-21-2026-10-09.summary.json), `product-singleton-*`,
`product-native-singleton-eta*` and `product-anonymous-two-factor-*`.
Exact selected-scalar overlay source manifest and binary hash are recorded.
Current worktree build is blocked elsewhere. No canonical edits or performance
claim; all positive authors have independent strict file acceptance.

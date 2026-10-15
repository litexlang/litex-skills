# Part 61 — Reuse native product laws across an empty-product wrapper

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and convention

Concrete Mathematics Chapter 2 defines `finite_coefficient_product_211` to
return a native product on first<=last and 1 otherwise. Native `product`
requires a nonempty interval. Keep this distinction and the declared N index
domain; do not silently change either convention.

The exact current-syntax wrapper is included in each relevant
[round-21 source](evidence/round-21-cases/product-wrapper-append-no-first-range.lit).
Named singleton and empty value already pass directly through the wrapper.

## Interior append: best checked variant

After that exact definition, the following complete claim passes:

```litex
claim:
    ? forall f fn(k N) R,m N:
        m>=2
        =>:
            finite_coefficient_product_211(2,m+1,f)=finite_coefficient_product_211(2,m,f)*f(m+1)
    2<=m+1
    finite_coefficient_product_211(2,m,f)=product(2,m,f)
    finite_coefficient_product_211(2,m+1,f)=product(2,m+1,f)=product(2,m,f)*f(m+1)=finite_coefficient_product_211(2,m,f)*f(m+1)
```

The native append equation itself passes directly. The bare wrapper goal,
one-chain author, variant deleting the last-endpoint bound, and variant
deleting the previous definition fail. An additional `2<=m` line is removable.
Do not call this a globally minimal proof.

## Empty boundary and complete positive-index route

On m N+, split m=1 and m>1. The bare disjunction misses until `m>=1` is
explicitly stated. In the m=1 branch, even the wrapper argument equality
misses until `m+1=2` is exported. The complete
[case proof](evidence/round-21-cases/product-wrapper-append-cases-index-bridge.lit)
passes with those bridges. The mathematical split remains author-owned.

Removing positive-index/range coverage is false: at m=0 and f(1)=2, the
wrapper left side is 1 while the proposed right side is 2. Empty-wrapper
value zero is also false. Native empty product syntax is outside the current
native interface, rather than a counterexample to the standard convention.

## Recommendation and evidence boundary

Inspect bounded consumption of known affine index equalities, index bounds
and previous definition equations. Do not recognize this user function's name
in the kernel or add a second native append rule. The original registered
chapter still has legacy `$fn_eq` spellings; this round tests extracted current
interfaces, not a chapter migration or full solution theorem.

[Round 21](search-round-21.md) retains independent strict file receipts,
same-Session attempts, actual first failed facts and explicit source snapshot
limits. No kernel/canonical source change, trust or measured speed claim.

# Part 31 — Pointwise estimates for finite products

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For finite S and real functions with 0<=f(x)<=g(x) on S, product f<=product g.
Nonnegative factors are essential; multiplication does not preserve arbitrary
signed pointwise order. Anchor: Concrete Mathematics finite products and the
native aggregate identity/function interfaces.

## Positive two-factor control

```litex
claim:
    ? forall f,g fn(x {1,2}) R:
        forall x {1,2}:
            0 <= f(x)
            f(x) <= g(x)
        =>:
            finite_set_product({1,2},f) <= finite_set_product({1,2},g)
    0 <= f(1)
    0 <= f(2)
    f(1) <= g(1)
    f(2) <= g(2)
    finite_set_product({1,2},f) = f(1)*f(2) <= g(1)*g(2) = finite_set_product({1,2},g)
```
Passes. The analogous two-factor nonnegative-product proof also passes.
For arbitrary finite S, direct monotonicity/nonnegative-product targets miss;
no complete general finite-set induction was accepted in this round.

## Existing equality route

Given pointwise f(x)=g(x) on their identical complete domain S, the claim
product(S,f)=product(S,g) closes with only `by fn_extension f = g`.
The explicit repeated product equality can be deleted; this was checked.
Do not add a new equality rule just to replace this supported route.

## Negatives and candidate

Pointwise order without nonnegative factors is false at f=(-2,-3),g=(-1,-2):
products are 6 and 2. The variant rejects. Empty product remains 1; its
explicit identity passes, so weak monotonicity must allow empty S.

Consider a native product comparison interface analogous to the existing sum
comparison call, checking complete pointwise order and nonnegative terms.
That is a proposal, not an installed theorem name. The two-factor control
does not prove general runtime support; a general mathematical certificate,
domain contract and positive/negative gates are needed before implementation.
Do not infer a positive total from a possibly empty product/sum analogy.

## Evidence

[Round 9 receipt](evidence/round-09-2026-10-08.summary.json), finite-product cases,
two-factor routes, function-extension liveness and empty identity.
Current working-tree release, strict independent files, 2026-10-08.

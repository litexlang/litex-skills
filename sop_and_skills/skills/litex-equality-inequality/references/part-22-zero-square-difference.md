# Part 22 — Endpoint equality from a zero squared difference

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

A real difference with zero square is zero, and its endpoints are equal.
Anchor: Manual R13 equality cases for completed-square and Cauchy certificates.

## Positive and ideal form

```litex
claim:
    ? forall a,b R:
        (a-b)^2 = 0
        =>:
            a = b
    a-b = 0
```
Passes. The same direct universal statement without the bridge misses.
In the Cauchy equality case the checked route publishes
(a*d-b*c)^2=0 through its determinant identity, then a*d-b*c=0. In the
two-variable AM-GM equality case it publishes (a-b)^2=0 then a-b=0.
Both complete routes pass; both direct equality-case conclusions miss.

## Negative and candidate

a^2=b^2 alone does not imply a=b; a=1,b=-1 refutes it and the direct variant
rejects. A non-strict Cauchy bound does not force zero determinant; the
corresponding equality-case variant rejects at a=1,b=0,c=0,d=1.

Add a fixed endpoint-equality strategy consuming known (a-b)^2=0 under real
domains, reusing square-zero and zero-difference certificates. The target
supplies both endpoints; no unknown factorization is needed. The author still
supplies the polynomial identity that produces that squared difference. Do
not claim generic Cauchy equality recognition or arbitrary factorization from
this narrowly tested primitive.

## Evidence

[Round 6 receipt](evidence/round-06-2026-10-08.summary.json), `difference-square-*`,
`cauchy-equality-*`, `am-gm-equality-*`, `equal-squares-sign-false`.
Strict current working-tree release, 2026-10-08; no kernel changes.

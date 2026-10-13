# Part 3 — Recover signed order from squares

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and proof idea

For real a,b, squared order controls magnitudes. To conclude a<=b, it is
sufficient that b is nonnegative; a need not be nonnegative. Use a<=abs(a),
then square-order comparison of magnitudes, then abs(b)=b.
Anchors: Manual R12; AM-GM in the middle-school showcase and
`examples/proof_nodes/order/am_gm.lit`. These are isolated capability probes;
the enclosing AM-GM theorem has not been rewritten or reverified for brevity.

## Positive — one checked chain

```litex
claim:
    ? forall a,b R:
        0 <= b
        a^2 <= b^2
        =>:
            a <= b
    a <= abs(a) <= abs(b) = b
```

## Verbose contrast

Manual's square-root route, with both bases nonnegative, also passes:
```litex
claim:
    ? forall a,b R:
        0 <= a
        0 <= b
        a^2 <= b^2
        =>:
            a <= b
    0 <= a^2
    0 <= b^2
    a = sqrt(a^2) <= sqrt(b^2) = b
```
The one-chain route avoids root-domain bridges. Do not add a>=0 to callers
that do not have or need it; existing theorem interfaces remain unchanged.

## Ideal direct form and capability gap

```litex
forall a,b R:
    0 <= b
    a^2 <= b^2
    =>:
        a <= b
```
This direct form misses `search_proof`; the version additionally assuming
0<=a also misses. The chain above passes.

## Negative boundaries

Without the sign condition, squared order does not imply signed order:
```litex
forall a,b R:
    a^2 <= b^2
    =>:
        a <= b
```
Rejected; a=1,b=-2 is a counterexample. Weak squared order also cannot imply
a<b even when both bases are nonnegative: a=b=1 is a counterexample. That
strictness variant was executed and rejected in the receipt.

## Builtin candidate

A bounded signed-square reflection rule for goal a<=b may check real domains,
0<=b and a^2<=b^2. It need not search square-root intermediates. Existing
magnitude comparison provides the mathematical route; preserve its proof
evidence rather than asserting a sign-free monotonicity of squaring.
This is a proposal, not an implemented rule or a universal source workaround.

## Evidence

[Round 2 receipt](evidence/round-02-2026-10-08.summary.json), cases
`square-reflection-right-sign-direct`, `square-reflection-abs-chain`,
`square-reflection-direct`, `square-reflection-chain`,
`square-reflection-no-sign`, `square-reflection-strict-false`.
Strict clean files, fresh contexts, release built from current working tree
on 2026-10-08; binary hash and exact source in receipt. Full-chapter shortening
and performance were not tested.

## Strict variant — round 11 follow-up

The direct a<b from 0<=b,a^2<b^2 also misses. This checked route passes:
```litex
claim:
    ? forall a,b R:
        0 <= b
        a^2 < b^2
        =>:
            a < b
    0 <= a^2
    0 <= b^2
    abs(a) = sqrt(a^2) < sqrt(b^2) = abs(b)
    a <= abs(a) < abs(b) = b
```
Without the sign guard, a=1,b=-2 refutes the conclusion and the probe rejects.
The geometry strict-triangle dot/product comparison uses this mathematical
move through a contradiction; a strict signed-square reflection sibling could
remove that block once its exact squared endpoint is supplied. Enclosing
geometry replacement remains unverified.
Evidence: [round 11](evidence/round-11-2026-10-08.summary.json), `square-strict-*`.

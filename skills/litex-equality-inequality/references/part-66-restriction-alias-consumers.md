# Part 66 — Generic restriction aliases and empty graph consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and direct miss

With the exact topology showcase restriction template:

```litex
forall X,Y set,f fn(x X) Y,K power_set(X),result fn(x K) Y,p K:
    result=\restricted<X,Y,f,K>
    =>:
        result(p)=f(p)
```

This generic alias target misses. The immediate equation
result(p)=restricted(p) passes. Composition aliases, real-valued restriction
aliases and the full-R alias variant also pass; do not claim all function
aliases are unsupported.

## Same-target checked route

```litex
claim:
    ? forall X,Y set,f fn(x X) Y,K power_set(X),result fn(x K) Y,p K:
        result=\restricted<X,Y,f,K>
        =>:
            result(p)=f(p)
    result(p)=\restricted<X,Y,f,K>(p)=f(p)
```

One definition-result chain to the literal callback also passes. Supplying or
stating p in X does not repair the direct target; the standalone membership
checks but the final equality remains the failed fact. Inspect the generic
equality/definition consumer with actual intermediate citations; no broad
carrier strengthening, alias cache or function-name special case is justified.

## Empty restriction: reuse its checked function type

The direct empty graph target misses, while this complete author passes:

```litex
claim:
    ? forall f fn(x R) R:
        \restricted<R,R,f,{}> = {}
    have h fn(x {}) R=\restricted<R,R,f,{}>
    h={}
    \restricted<R,R,f,{}> = h = {}
```

The type fn(x {}) R already checks directly. A literal-function chain instead
fails first at restricted=fn(x {})R{f(x)}. Inspect whether the existing empty
signature/graph interface consumes this template expression's checked type;
do not add a second named empty-function law. General root cause or a repair
has not been established.

## Boundary and evidence

The empty restriction cannot be called at zero. General restricted arguments
still require membership in K, and wrong composition order remains false.
Full-R function identity checks via explicit extension. Keep WD and the
function's complete input domain separate from value equality.

[Round 25](search-round-25.md) retains complete strict file sources, actual
failed subfacts, live-session attempts and source/binary identities. The
template-close whitespace parse error is excluded from mathematical findings.
No kernel/canonical edits, added trust or runtime claims.

## Refined author and nomination

Round 26 verifies a shorter same-premise author: stating only
`\restricted<X,Y,f,K>(p)=f(p)` closes the generic alias goal. The full chain
above remains valid but is no longer the shortest checked variant here.
General and mixed-domain equality transitivity already pass; the nomination
concerns obtaining the definition link, not adding transitivity. See
[Part 67](part-67-restriction-definition-link.md).

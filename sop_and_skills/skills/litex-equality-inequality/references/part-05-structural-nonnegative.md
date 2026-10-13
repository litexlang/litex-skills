# Part 5 — Nonnegative expression trees

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

An explicit certificate is a sum of real squares divided by a positive number.
Its sign follows by inspecting the expression tree; finding a certificate for
an arbitrary polynomial is separate mathematical work.
Anchor: Manual R09 three-variable sum-of-squares proof.

## Positive and current bridge

```litex
forall a,b,c R:
    (a-b)^2+(b-c)^2 >= 0
    (a-b)^2+(b-c)^2+(c-a)^2 >= 0
    ((a-b)^2+(b-c)^2+(c-a)^2)/2 >= 0
```
This strict file passes. The first two statements seed saved signs for the
final one; they are current bridges, not independent mathematical insights.

## Ideal form and precise observed boundary

```litex
forall a,b,c R:
    ((a-b)^2+(b-c)^2+(c-a)^2)/2 >= 0
```
Direct target misses. Even a^2+b^2+c^2>=0 misses while a^2+b^2>=0 passes.
However, with explicit premises 0<=u,0<=v,0<=w, the direct target
0<=u+v+w passes. Therefore the evidence is not that all three-term sums are
unsupported; composition of implicit square signs is the narrower observation.

Manual's full endpoint chain also passes. A single polynomial identity with
an appended >=0 does not suffice in the tested certificate variant. Do not
claim that automatic polynomial certificate discovery already exists.

## Negative

```litex
forall a,b R:
    a^2-b^2 >= 0
```
Rejected; a=0,b=1 refutes it. A subtract node cannot inherit the sign rule for
an add node. Real domains and positive/nonzero denominators remain mandatory.

## Improvement candidate

Audit the owner of bounded nonnegative composition before adding another
ad-hoc rule for exactly three squares. A structural sign strategy could descend
through sums, products of proved nonnegative factors and division by a proved
positive denominator, consuming strictly smaller expression children and
preserving leaf permissions/proof evidence. Unsupported leaves must miss.
Do not increase global search depth or silently discover SOS decompositions.
The current source already has a sum-of-nonnegatives rule; the precise failing
producer/consumer still needs a kernel investigation before implementation.

## Evidence

[Round 2 receipt](evidence/round-02-2026-10-08.summary.json): `sos-two-direct`,
`sos-three-direct`, `sos-nonnegative-direct`, `sos-nonnegative-chain`,
`sos-certificate-direct`, `sos-complete-chain`, `sos-false`,
`sum-three-known-direct`, `sum-three-known-chain`. Current-source release built
successfully on 2026-10-08. Case sources and exact outputs retained. This is
a capability proposal; no new rule or performance improvement is claimed.

## Dated follow-up: weighted/function-valued squares

Round 15 retains an additional weighted scalar square sum and the probability showcase's variance interface. Component sign facts solve the scalar sum; the function-based squared centered values additionally require explicit real-base facts in that build. These refine the first failing obligation rather than establish a universal workaround. See [Part 46](part-46-function-real-square-sign.md) and [round 15 receipt](evidence/round-15-2026-10-08.summary.json).

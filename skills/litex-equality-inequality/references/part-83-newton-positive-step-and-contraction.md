# Part 83 — Positive Newton step and a local contraction certificate

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

The numerical-analysis showcase proves newton(x)>1 for x in R+ with twelve
body statements, then uses that result in induction and quadratic contraction.
This card checks the positive-step theorem with the short Part81 prefix, and
separately checks the scalar mathematics behind contraction. It does not yet
verify the recursive sequence interface or the full contraction theorem.

## Positive: twelve source statements to five

With the retained positive update definition and Part81 residual dependencies,
this body passes independently:

```litex
r43_newton_sqrt_two(x)=(x+2/x)/2
r43_newton_sqrt_two(x)-1=(x+2/x)/2-1=((x-1)^2+1)/(2*x)
(x-1)^2+1>0
2*x>0
r43_newton_sqrt_two(x)-1=((x-1)^2+1)/(2*x)>0
```

[Full runnable slice](evidence/round-43-cases/greater-delete-square-nonnegative.lit).
The six-statement version with a separate square nonnegative fact also passes;
that fact is removable here. The bodyless theorem and standalone literal
`forall x R+: (x+2/x)/2>1` miss independently. An accepted warm universal
positive-step theorem hides the bodyless miss; the cold files own this result.
The certificate makes positivity explicit rather than assuming a new lemma.

## Local scalar contraction: four statements

The exact scalar premise family is x in R+, a,b in R, x>=1, b>=0,
4*x^2*b=a^2. It expresses the source's lower iterate bound, nonnegative next
gap and one-step identity, but does not prove those recursive premises.

```litex
thm r43_scalar_four:
    ? forall x R+,a,b R:
        x>=1
        b>=0
        4*x^2*b=a^2
        =>:
            b<=a^2/4
    x^2-1=(x-1)*(x+1)>=0
    x^2>=1
    4*b=1*(4*b)<=x^2*(4*b)=4*x^2*b=a^2
    b=(4*b)/4<=a^2/4
```

[Runnable scalar slice](evidence/round-43-cases/contraction-four-statements.lit).
A six-statement candidate first proved x^2>=1, then missed the adjacent
`4*b<=4*x^2*b`. Reassociation through the same nonnegative factor 4*b checks
that multiplication explicitly. Additional x-1>=0, x+1>=0 and 4*b>=0
publications were deleted in accepted independent variants. No general product
normalization rule or permanent publication requirement is inferred.
The direct scalar target and direct square-lower target miss cold.

## Negative boundaries and capability limits

The lower bound x>=1 is mathematically necessary: x=1/2,a=b=1 gives
4*x^2*b=a^2 but not b<=a^2/4. The concrete control checks all three numeric
facts. Without b>=0, x=2,b=-1,a=0 refutes the product-order move itself;
the deletion fixture rejects at that move, not a false final conditional.
Indeed the identity and x>0 imply b>=0 mathematically, so the final conditional
without its explicit b-sign premise is still true; its rejection is a capability
miss, not a counterexample. Keep this distinction when interpreting that case.
The stronger positive-step claim formula>2 is false (x=1); x=0 has undefined
division. Both reject. Missing lower-bound and b-sign variants are labeled by
these distinct mathematical reasons.

## Evidence and next consumer

[Round43 receipt](evidence/round-43-2026-10-09.summary.json):20 independent strict files,
10 accepted/10 rejected; every promoted copy rerun on the fixed current-source
release snapshot. Source and warm journal are retained beside the receipt.
Session25852 remains on the older round29 snapshot and can inherit universal
facts; do not treat its later successes as cold support. No canonical source,
kernel, trust, AST/Env/Runtime, whole showcase or performance change.
Next verify the exact recursive iterate, induction lower bound and downstream
source contraction using these checked bodies and unchanged definitions.

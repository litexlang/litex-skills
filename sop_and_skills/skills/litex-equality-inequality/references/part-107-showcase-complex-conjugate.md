# Part 107 — Actual complex modulus and conjugate consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and interface

The middle-school showcase computes the modulus of 3+4*i and then conjugates
it. Keep the exact C carrier and builtin re/img/C_abs interfaces:

```litex
have fn complex_conjugate(z C) C = re(z) - img(z) * i
```

The modulus is sqrt(3^2+4^2)=5; conjugation retains real part3 and changes
imaginary part4 to -4. The isolated source section passes; this does not claim
the whole showcase or a new complex-number implementation.

## Direct scalar and complex values

```litex
C_abs(3+4*i)=5
complex_conjugate(3+4*i)=3+(-4)*i
```

Each passes independently with the declaration.
[Modulus endpoint](evidence/round-67-cases/abs-direct.lit),
[conjugate endpoint](evidence/round-67-cases/conjugate-direct.lit).
The source's i^2, real/imaginary-coordinate facts, modulus unfolding and sum
calculation are unnecessary for this modulus endpoint. Its explicit modulus
chain also passes without the coordinate publications. The source conjugate
chain passes, but its intermediate function expansion is removable here.

## Numeric real/imaginary consumers: one value plus two chains

```litex
complex_conjugate(3+4*i)=3+(-4)*i
re(complex_conjugate(3+4*i))=re(3+(-4)*i)=3
img(complex_conjugate(3+4*i))=img(3+(-4)*i)=-4
```

[Complete consumer route](evidence/round-67-cases/numeric-consumer-chains-after-value.lit).
The source additionally publishes re(3+(-4)*i)=3 and img(3+(-4)*i)=-4 before
those chains; both publications are removable together. Deleting the conjugate
value from the three-fact route fails. Bare consumer endpoints miss even after
the conjugate value is published. Publishing the two canonical coordinate
values as well makes those bare endpoints pass, but that five-fact route is
longer than the checked three-fact route.
Do not turn this nested consumer boundary into a universal coordinate-echo rule.

## Symbolic values: retain canonical form, omit reconstruction

```litex
forall z C:
    complex_conjugate(z)=re(z)-img(z)*i=re(z)+(-img(z))*i
    re(complex_conjugate(z))=re(re(z)+(-img(z))*i)=re(z)
    img(complex_conjugate(z))=img(re(z)+(-img(z))*i)=-img(z)
```

[Complete shortened symbolic block](evidence/round-67-cases/symbolic-without-reconstruction.lit).
The source first publishes z=re(z)+img(z)*i; this body fact can be removed.
Deleting the remaining conjugate-form chain fails, and the two bare symbolic
consumer endpoints also miss. Preserve the useful canonical a+b*i expression
in this source-scoped route. No global minimum or arbitrary outer-function
substitution capability is claimed.

## Negative controls and evidence

Wrong modulus6 rejects even with the full accepted expansion chain. Wrong
conjugate sign3+4*i rejects after the input coordinate values. Wrong imaginary
part4 rejects in the same value-plus-consumer chain context that accepts -4.
These controls are separate from the true bare nested-consumer misses.
[Wrong modulus chain](evidence/round-67-cases/wrong-abs-chain.lit),
[wrong consumer chain](evidence/round-67-cases/wrong-consumer-chain-after-value.lit).

[Receipt](evidence/round-67-2026-10-09.summary.json):20 strict cold files,
11 accepted/9 Normal rejections; promoted file paths checked on the fixed
snapshot after successful current-source release build. Source hash and build
log retained. Historical round66 prechecks agree but do not own acceptance.
Session9174 stays on round61 and journals the renamed conjugate declaration
and accepted numeric direct values. Cold files own deletion evidence. No
canonical source, kernel, trust, protected owner, timing or whole-showcase
change. This one source family does not justify a new permanent rewrite rule.

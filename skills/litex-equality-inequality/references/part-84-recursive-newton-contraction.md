# Part 84 — Actual recursive Newton contraction, 27 statements to eight

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematical spine

The numerical-analysis showcase defines its positive recursive iterate from
x_0=1, gaps |x_n^2-2|, proves x_n>=1 by induction, and proves
4*x_n^2*g_(n+1)=g_n^2. Those interfaces imply g_(n+1)<=g_n^2/4.
This round retains the actual recursive definitions, domain claims, iterate
step theorem and gap step proof, with the checked short Part81–83 upstream
proofs. It verifies actual downstream composition, not a scalar substitute.
Names are prefixed r44 only to avoid Session collisions. The extractor and
closed-form comparison bound are excluded from this slice.

## Positive: contraction body27 to eight

[Complete checked recursive slice](evidence/round-44-cases/contraction-delete-identity-call.lit)
contains all dependencies and the eight-statement contraction body. The steps
are: publish the lower-bound theorem; publish both factor signs; check the
square certificate; state x_n^2>=1; expose the next gap magnitude/nonnegativity;
compare using the same multiplier; divide by four.

Exact excerpts from that body:

```litex
r44_sqrt_two_newton_iterate(n)-1>=0
r44_sqrt_two_newton_iterate(n)+1>=0
r44_sqrt_two_newton_iterate(n)^2-1=(r44_sqrt_two_newton_iterate(n)-1)*(r44_sqrt_two_newton_iterate(n)+1)>=0
```

```litex
4*r44_sqrt_two_newton_gap(n + 1)=1*(4*r44_sqrt_two_newton_gap(n + 1))<=r44_sqrt_two_newton_iterate(n)^2*(4*r44_sqrt_two_newton_gap(n + 1))=4*r44_sqrt_two_newton_iterate(n)^2*r44_sqrt_two_newton_gap(n + 1)=r44_sqrt_two_newton_gap(n)^2
r44_sqrt_two_newton_gap(n + 1)=(4*r44_sqrt_two_newton_gap(n + 1))/4<=r44_sqrt_two_newton_gap(n)^2/4
```

The nine-statement candidate separately releases the gap step theorem; that
call is removable because the established theorem checks the identity link.
Its definition remains in the prefix. Deleting the lower-bound release fails
at the subsequent certificate route. No dependency removal or globally minimal
proof claim follows from this local shortening.

## Actual induction needs the recursive representation bridge

The lower-bound induction originally writes the successor equation, releases
newton(x_k)>1 and repeats that conclusion. The final repeated conclusion can
be deleted, retaining the actual successor equation and theorem call.
Removing both the equation and repeat makes the inductive successor goal miss
in an independent file, despite warm success after the original theorem was
published. Keep this meaningful recurrence bridge in the tested context.
Original lower-bound and gap step proofs pass; their bodyless controls miss.
The iterate step theorem itself also misses bodyless. The gap step body was
retained unchanged here; it is not counted as a shortened proof.

## Scalar-to-source boundary and negatives

Part83's scalar square certificate needed no separate factor-sign facts. The
corresponding source expression first passes its polynomial equality and then
misses `(iterate(n)-1)*(iterate(n)+1)>=0`. Adding the two factor signs above
repairs the actual consumer. Do not infer a universal sign-echo requirement.
A shortened source candidate without those facts fails cold even after its
scalar analogue passes. Record the distinct expression/context evidence.

The false strengthened conclusion with denominator8 rejects; at n=0 the
actual gaps are g_0=1 and g_1=1/4, exceeding1/8. The first authored fixture
accidentally retained /4 due to an indentation mismatch in the generator;
that duplicate-positive result is excluded and the corrected /8 fixture is
independently checked. This was an author fixture error, not verifier acceptance
of the stronger false theorem. No new trust or premise was inserted.

## Evidence and remaining scope

[Round44 receipt](evidence/round-44-2026-10-09.summary.json):14 independent cold strict
files,7 accepted/7 rejected; promoted paths rerun with the fixed current-source
release snapshot. Exact source hash and source-order warm journal retained.
Warm Session25852 remains on round29 and contains accepted universal theorems;
its deletion successes do not establish standalone capability.
The short positive update, residual/gap identities, actual recursive induction
and eight-statement contraction compose in the checked full slice. No canonical
showcase/kernel/AST/Env/Runtime edit, whole-showcase, extractor, closed-form
error-bound or performance acceptance. Next check the actual comparison-bound
recurrence and final bound induction before claiming that later estimate.

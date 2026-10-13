# Part 114 — Actual coordinate difference quotients: two function values suffice

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Round79 continuation: actual numeric tuple consumer

The source's numeric gradient calculation needs an explicit coordinate theorem
followed by its result chain in the independent small slice:

```litex
release thm tuple_equal_from_coordinates((2*(3,4)(1),2*(3,4)(2)),(2*3,2*4))
quadratic_gradient((3,4))=(2*3,2*4)=(6,8)
```

[Complete numeric slice with gradient definition](evidence/round-79-cases/numeric-source-slice.lit).
Bare gradient((3,4))=(6,8) and the chain without the native theorem call miss.
Publishing the two input coordinate values does not repair the bare endpoint.
Even after the native coordinate theorem, replacing the result chain by only
its endpoint misses. Retain the meaningful coordinate interface and chain;
extra input-coordinate echoes are unnecessary in the accepted source route.

The complete round78 short theorem prefix followed by the original numeric
demonstration passes. The final gradient predicate assertion after its native
theorem call is removable. This completes a current gate through the source's
numeric demonstration with the shortened proof prefix; it is not an audit of
the original unmodified full file or every multivariable operation.
[Short source with predicate echo removed](evidence/round-79-cases/short-demo-delete-predicate-echo.lit).
Wrong numeric tuple(6,9) rejects after the same coordinate theorem and input
coordinate publications. No conclusion about Part99's separate direct tuple
consumer gap follows from this numeric native-route acceptance.

[Round79 receipt](evidence/round-79-2026-10-09.summary.json):9 strict files,
4 accepted/5 Normal rejections, promoted paths rerun after successful current-
source release build on the fixed snapshot. Exact source/binary identity
retained. Session66922 on round68 accepted the coordinate call and result
chain, but already held symbolic gradient-coordinate facts; it cannot own
deletion necessity. Cold isolated files do. Same source family, no new Part,
kernel/trust/canonical change or unrestricted direct tuple equality claim.

## Round78 continuation: four-step gradient packaging

With round77's shorter derivative prefix, the original coordinate-gradient
theorem body can shrink from ten statements to four:

```litex
thm quadratic_gradient_is_coordinate_gradient:
    ? forall point cart(R,R):
        $is_coordinate_gradient_at(quadratic_surface,point,quadratic_gradient(point))
    quadratic_gradient(point)(1)=2*point(1)
    quadratic_gradient(point)(2)=2*point(2)
    release thm quadratic_surface_has_x_partial_derivative(point)
    release thm quadratic_surface_has_y_partial_derivative(point)
```

[Complete preferred source and exact definitions](evidence/round-78-cases/direct-coordinate-facts.lit).
Two theorem-result echoes, two transported partial-derivative facts, the final
coordinate-gradient fold and the separate tuple-value publication are jointly
removable. Both coordinate projection chains shorten to their direct endpoints.
The native calls and original gradient function remain intact.

Deleting both coordinate-value publications from this four-step route fails;
the remaining native calls do not close the gradient target unaided. Changing
the gradient target to the input point itself also rejects, with the baseline
and short routes. This is a false gradient in general, distinct from the true
missing-publication consumer miss.
[False short gradient](evidence/round-78-cases/short-wrong-gradient.lit).

[Round78 receipt](evidence/round-78-2026-10-09.summary.json):11 strict files,
8 accepted/3 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary identities
retained. Session66922 on round68 checked only the gradient definition and
source coordinate slice; cold round78 owns complete packaging deletion.
No numeric gradient demo, whole-showcase, timing or global-minimum claim.
Rounds76–78 remain one source family; no new bt/canonical/kernel/trust change.

## Round77 continuation: two-step local derivative error proofs

After round76's two-value quotient theorems, each original partial-derivative
proof's innermost claim can use only a native call and one mixed error chain.
For the original x binder, retain:

```litex
release thm quadratic_surface_x_difference_quotient(point,x)
|(quadratic_surface((x,point(2)))-quadratic_surface(point))/(x-point(1))-2*point(1)|=|(x+point(1))-2*point(1)|=|x-point(1)|<epsilon
```

This is an excerpt under x!=point(1) and abs(x-point(1))<epsilon. The y
proof mirrors it with the original coordinate expressions. Four local proof
statements become two: the repeated quotient result is removable, while the
real-error equality is incorporated as an intermediate inside the absolute
chain. Deleting that equality without adding the intermediate still fails.

Both delta-controlled predicate folds and both final derivative predicate
folds can also be removed jointly in this route. The original epsilon-delta
claims and witness delta=epsilon stay intact; native witness and claim closure
check their remaining obligations. Do not generalize this to every by-def
action or existential construction.
[Complete preferred derivative source](evidence/round-77-cases/combined-short-route.lit).

The accepted original-baseline and shortest source through the actual
quadratic_gradient_is_coordinate_gradient theorem both pass. Its gradient
definition, coordinate facts and calls are untouched. This extends the older
round76 downstream scope below; the numeric gradient demonstration is still
excluded. Changing the x derivative slope to 2*point(1)+1 rejects with the
short route as well as with the baseline.
[Short source through coordinate gradient](evidence/round-77-cases/short-through-coordinate-gradient.lit).

[Round77 receipt](evidence/round-77-2026-10-09.summary.json):15 strict files,
10 accepted/5 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Source/binary identities and
literal journal retained. Session66922 on round68 checked only the local x
error claim using its earlier renamed quotient; full current cold files own
derivative/gradient and joint-deletion evidence. Rounds76/77 are one source
family, not independent promotion evidence. No canonical/kernel/trust edits,
new mathematical premises, performance or full-showcase claim.

## Source mathematics and exact interface

The multivariable-calculus showcase defines quadratic_surface(p)=p(1)^2+p(2)^2
on cart(R,R). Its coordinate quotients hold one coordinate fixed, cancel the
common square and factor the other difference of squares. Keep the exact
surface definition, tuple carriers and nonzero coordinate-difference premises.
No scalar replacement function or changed derivative predicate is introduced.

## Checked two-fact x proof

```litex
have fn quadratic_surface(p cart(R,R)) R = p(1)^2+p(2)^2

thm quadratic_surface_x_difference_quotient:
    ? forall p cart(R,R), x R:
        x!=p(1)
        =>:
            (quadratic_surface((x,p(2)))-quadratic_surface(p))/(x-p(1))=x+p(1)
    quadratic_surface((x,p(2)))=x^2+p(2)^2
    quadratic_surface(p)=p(1)^2+p(2)^2
```

[Full source](evidence/round-76-cases/x-values-only.lit).
The original has eight body facts: denominator nonzero, two tuple-coordinate
values, two surface values, numerator simplification, factorization and final
quotient chain. The two displayed values alone close the same theorem goal.
The y proof likewise needs only surface((p(1),y))=p(1)^2+y^2 and the same
surface(p) value under its original y!=p(2) premise.
[Both short theorems together](evidence/round-76-cases/both-values-only.lit).

## Meaningful chain alternative and deletion boundaries

A longer but checkable single quotient chain passes after the two surface
values, even when the denominator and coordinate-value publications are
removed together. That chain exposes numerator cancellation, difference-of-
squares factorization and division by the known nonzero coordinate gap.
It is useful explanatory algebra, but machine-removable after the two values.
[Three-fact route](evidence/round-76-cases/x-combined-short.lit).

A chain-only theorem without those value publications misses. Removing both
surface values from the otherwise expanded x route also misses. The separate
coordinate and denominator publications are removable; the original premise
x!=p(1) remains. Do not infer that all function values can be omitted merely
because the functions are transparent definitions.

## Actual derivative consumers and negative controls

The original source through both quadratic_surface_has_x_partial_derivative
and quadratic_surface_has_y_partial_derivative passes. Replacing only the two
quotient theorem bodies by the two-value proofs also passes through those
same derivative theorems. Their predicates, epsilon-delta witnesses and native
quotient calls stay untouched.
[Short source through both partial derivatives](evidence/round-76-cases/short-through-partial-derivatives.lit).
Coordinate-gradient theorem and later numeric tuple outputs are outside this
gate; no full-showcase or general gradient acceptance is inferred.

Wrong x quotient x-p(1), instead of x+p(1), rejects both with the original
body and the short two-value body. Removing the original nonzero-coordinate
premise also rejects; the quotient is undefined when x=p(1). These controls
are distinct from the true chain-only capability miss.
[Short wrong conclusion](evidence/round-76-cases/short-wrong-x-conclusion.lit).

## Evidence

[Receipt](evidence/round-76-2026-10-09.summary.json):19 strict files,
14 accepted/5 Normal rejections, all promoted paths rerun on a fixed snapshot
after successful current-source release build. Exact source/binary hashes
and log retained. Session66922 remains on round68; it accepted the exact
surface definition and renamed two-value x theorem. Cold round76 owns joint
shortening and derivative-consumer evidence. No canonical source, kernel,
trust, protected owner, performance or global-minimum claim. No new bt needed.

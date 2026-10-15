# Part 80 — Assemble the actual derivative uniqueness proof, 61 to 29 lines

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source theorem and preserved interface

The maintained ODE showcase's derivative_value_unique theorem takes a real-
valued function and two derivative candidates at the same real point, and
concludes the slopes coincide. This round extracts its two actual epsilon-
delta definitions and the complete theorem into a strict standalone file.
Only definition/theorem names are namespaced. The original theorem passes.

The short native-radius version preserves both derivative hypotheses, real
domains, positive epsilon/delta witnesses, sample nondegeneracy and the target
equality. It changes the auxiliary radius choice to native min and supplies
the same mathematical proof. No source assumption, trust or new lemma is added.

## Complete short proof and scope of the line comparison

[Full runnable short slice](evidence/round-40-cases/native-combined-short.lit)
contains both definitions and the accepted theorem. The original theorem has
61 nonblank source lines; the short theorem has29, including its signature
and by-contra header. The unchanged definition prefix is excluded from both
counts. This is tested source reduction, not global minimality or runtime data.

The short proof combines the already checked positivity/tolerance, common-
radius, named-sample, quotient, triangle and separation routes. For example,
the native radius and sample section retains:

```litex
have radius R+ = min(delta1,delta2)
0 < radius / 2
have sample R = x0 + radius / 2
sample = x0 + radius / 2 > x0
sample - x0 = radius / 2
|sample - x0| = |radius / 2| = radius / 2 < radius
```

The later error chains themselves supply the needed radius-to-delta bounds;
separate preceding radius<=delta publications can be deleted in this combined
native proof. Actual witness acquisition and the quotient declaration pass,
so these are full theorem-slice results, not only scalar subgoal checks.

## Actual have-defined quotient alias differs from the equation probe

After the real source declaration of difference_quotient, these two error
chains suffice without separately publishing their unaliased right-hand errors:

```litex
|difference_quotient-slope1| = |(f(sample)-f(x0))/(sample-x0)-slope1| < epsilon
|difference_quotient-slope2| = |(f(sample)-f(x0))/(sample-x0)-slope2| < epsilon
```

The complete theorem passes with those two raw error statements removed.
Deleting only the alias chains, or deleting all four error publications, fails.
This refines Part79's independently supplied equation-alias context: it does
not establish that all alias representations have identical consumption.

## Closing facts and finite/native boundaries

The short route keeps reflexive `|slope1-slope2|>=|slope1-slope2|` before
impossible. Deleting that fact fails; the separate explicit not-self-< fact
can be removed. Deleting both closing facts also fails in the short variant.
The original full source proof passes without this inserted closing bundle;
do not turn a particular short-route dependency into a universal by-contra
requirement or claim an implementation repair.

The finite-radius short route also passes. Its two singleton-union member
bridges cannot be deleted in the tested variant. The native min version can
omit those finite-member steps. Neither result repairs every nested finite
extremum WD gap from Part72, and neither justifies adding new kernel rules.

## Negative and deletion controls

The bodyless full theorem misses cold. Removing the second derivative
hypothesis makes the general conclusion false and rejects. Missing explicit
sample!=x0 remains harmless in the accepted short theorem, since the retained
point-order route is sufficient for its actual consumers. The explicitly
restored sample!=x0 variant passes too; it is not required by this acceptance.
Combined deletion of raw errors, bound publications and the explicit negative
closing fact was independently checked, not inferred from individual removals.

## Evidence and remaining corpus work

[Round40 receipt](evidence/round-40-2026-10-09.summary.json):16 unique cold strict files,
9 accepted/7 rejected; all promoted files rerun with the fixed fresh binary.
Original source hash and exact theorem/definition slices retained. Warm Session
25852 uses the older round29 snapshot and abs spelling, whereas cold files
retain current source bars. Its bodyless theorem success is not acceptance.

This completes standalone acceptance of the assembled derivative uniqueness
slice. It does not verify the rest of the showcase, later derivative selector,
whole registered module or chapter. Canonical source and kernel are untouched;
no AST/Env changes, trust or performance claim. The broader corpus search stays
active; apply the same real-context deletion checks to further source families.

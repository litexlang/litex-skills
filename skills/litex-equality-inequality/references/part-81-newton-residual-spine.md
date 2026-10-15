# Part 81 — Four statements prove the actual Newton residual identity

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and domains

The numerical-analysis showcase defines residual(x)=x^2-2 and the positive
Newton update newton(x)=(x+2/x)/2. Its one-step identity is
4*x^2*residual(newton(x))=residual(x)^2. The same identity, together with the
positive factor4*x^2, proves the new residual is nonnegative.
Probes preserve the actual positive input/function domains and rename only
function/theorem identifiers. No recursive iterate, extractor or final global
gap estimate is verified in this round.

## Positive update carrier: two sign bridges before the real definition

The original five-statement positive-carrier claim passes. It can be reduced
to these two statements in its actual forall x R+ claim:

```litex
2/x>0
x+2/x>0
```

The resulting full file also accepts the actual have-fn definition returning
R+. Direct bodyless `(x+2/x)/2 in R+` misses cold. Both original type/sign
echo deletion controls and their combined deletion pass; no supplied positive
input or division-domain guard is removed.

## Exact identity: twelve source statements to four

The original next_value alias is unnecessary. This four-statement body passes
with the actual residual/update definitions and unchanged identity target:

```litex
r41_newton_sqrt_two(x)=(x+2/x)/2
r41_square_root_two_residual(x)=x^2-2
r41_square_root_two_residual(r41_newton_sqrt_two(x))=r41_newton_sqrt_two(x)^2-2=((x+2/x)/2)^2-2
4*x^2*r41_square_root_two_residual(r41_newton_sqrt_two(x))=4*x^2*(((x+2/x)/2)^2-2)=(x^2-2)^2=r41_square_root_two_residual(x)^2
```

[Full four-statement identity](evidence/round-41-cases/identity-four-statements.lit)
contains the self-contained constructor prefix. Bodyless and function-values-
only variants miss cold. Removing either the update value fact or the old
residual value fact also fails. The fully literal rational/polynomial identity
passes directly; do not treat that result as proof that named-function value
bridges can all be deleted. No extra nondegeneracy beyond the source R+ input
is introduced.

## Nonnegative residual: fourteen source statements to five

Calling the identity alone does not close the nonnegative target. This shorter
body uses its actual mathematical implication:

```litex
release thm r41_newton_sqrt_two_residual_identity(x)
x^2>0
4*x^2>0
r41_square_root_two_residual(x)^2>=0
r41_square_root_two_residual(r41_newton_sqrt_two(x))=r41_square_root_two_residual(x)^2/(4*x^2)>=0
```

The original fourteen-statement consumer passes too. A combined independent
file uses the two-statement positive constructor, four-statement identity and
five-statement nonnegative consumer together; it passes. This proves actual
dependency reuse rather than assuming isolated reductions compose.
[Combined short slice](evidence/round-41-cases/combined-short-identity-and-sign.lit)
is the preferred review artifact for this round. No global minimum or speed
claim follows from the proof-body statement counts.

## Negatives and bounded gap distinctions

The literal x=0 update is undefined and rejects. Changing the right residual
from(x^2-2)^2 to(x^2-3)^2 makes the identity false and rejects. Direct literal
new-residual nonnegativity misses as a true unsupported target, separate from
those controls. Positivity, named value publication and nonlinear identity
consumption are different proof phases; do not duplicate polynomial algebra
rules or broaden arbitrary function unfolding to close one case.

Any future reflection shortcut must retain the actual positive multiplier
and real/square evidence. Merely nonnegative multiplication would not justify
division or recovering the factor's sign. This scan makes no kernel change or
complete internal-cause claim.

## Evidence

[Round41 receipt](evidence/round-41-2026-10-09.summary.json):19 unique cold strict files,
10 accepted/9 rejected, all promoted copies rerun with the fresh fixed binary.
Exact source hash and function definitions preserved. A final-newline deletion
generation error was corrected before submission, not counted as a verifier
failure. Warm Session25852 on round29 snapshot can reuse the original theorem;
cold bodyless/function-value/consumer controls determine liveness. No canonical
source/kernel/AST/Env edit, new trust, whole recursion/showcase or runtime claim.

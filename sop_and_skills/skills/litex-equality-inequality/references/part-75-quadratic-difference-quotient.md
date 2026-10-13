# Part 75 — Shorten a real ODE showcase's difference-quotient proof

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics

The maintained ODE showcase uses `ode_solution(x)=x^2+1` and proves its
derivative is2*x0 by factoring the numerator of the difference quotient.
The isolated algebra slice preserves real inputs and `x!=x0`. Only the
function name is renamed to keep persistent Session probes separate.

## Checked four-statement algebra spine

```litex
have fn r35_ode_solution(x R) R = x^2+1
thm quadratic_quotient_error:
    ? forall x,x0 R:
        x!=x0
        =>:
            (r35_ode_solution(x)-r35_ode_solution(x0))/(x-x0)-2*x0=x-x0
    r35_ode_solution(x)=x^2+1
    r35_ode_solution(x0)=x0^2+1
    r35_ode_solution(x)-r35_ode_solution(x0)=(x^2+1)-(x0^2+1)=x^2-x0^2=(x-x0)*(x+x0)
    (r35_ode_solution(x)-r35_ode_solution(x0))/(x-x0)-2*x0=((x-x0)*(x+x0))/(x-x0)-2*x0=(x+x0)-2*x0=x-x0
```

The actual checked name is task-specific; the full file is
[four-line route](evidence/round-35-cases/values-and-two-chains.lit).
The six-statement original spine also passes. Its explicit `x-x0!=0` echo can
be deleted, and its separate quotient-only equation can be merged with the
offset chain. This is the tested short route, not a globally minimal proof.

## Deletion boundaries and supported downstream inequality

The bodyless named target misses cold. Function-values-only, nonzero-only and
one chain expanding the whole quotient directly miss. Literal polynomial
quotient arithmetic already passes; the named-function consumer is distinct.
Removing the two function value facts, the difference bridge, or the final
offset chain fails. Even shortening the difference bridge to
`f(x)-f(x0)=x^2-x0^2=(x-x0)*(x+x0)` fails at its first adjacent equality.
Retain the exact literal subtraction bridge; do not infer its removability
from the mathematical equivalence of those expressions.

For the source strict error goal, use the four algebra statements and one
final checked consumer:

```litex
abs((r35_ode_solution(x)-r35_ode_solution(x0))/(x-x0)-2*x0)=abs(x-x0)<epsilon
```

With the unchanged premises `x!=x0` and `abs(x-x0)<epsilon`, this five-statement
body passes. Deleting the abs bridge fails cold. The source's original seven-
statement error spine passes too. This checks the downstream inequality slice,
not the full derivative predicate, witness, ODE solution theorem or showcase.

## Negatives and nomination scope

Using3*x0 instead of2*x0 makes the identity false in general and rejects.
Dropping nondegeneracy produces an undefined zero-denominator case and rejects.
These are not true capability misses. No trust or extra mathematical premise
is used. Do not erase `x!=x0` merely because its derived echo is removable.

The evidence nominates investigating checked named-function value consumption
under arithmetic/quotient contexts, while keeping exact WD and fact citations.
It does not justify duplicating already supported polynomial identities,
global function unfolding or search-depth expansion. The necessary current
bridge is diagnostic, not a permanent authoring mandate.

## Evidence

[Round35 receipt](evidence/round-35-2026-10-09.summary.json):22 unique cold strict files,
7 accepted/15 rejected, with promoted copies rerun on the same fresh release
build as round34. Exact showcase source path/hash and subgoal adaptation are
retained. Warm Session successes after original theorem publication cannot
establish deletion liveness; cold bodyless/final-offset/abs controls disagree.
No canonical/kernel/AST/Env changes, full derivative acceptance or runtime claim.

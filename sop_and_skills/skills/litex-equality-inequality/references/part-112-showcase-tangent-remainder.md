# Part 112 — Actual quadratic tangent remainder and a short order consumer

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and exact definitions

The calculus showcase's final theorem says that x^2 minus its tangent formula
9+6*(x-3) equals (x-3)^2. Preserve the exact two named functions and real
carrier. This is an isolated algebraic source slice; no derivative-predicate
or whole-calculus acceptance is inferred from it.

```litex
have fn square_function(x R) R = x^2
have fn square_tangent_at_three(x R) R = 9 + 6 * (x - 3)

thm square_tangent_error_at_three:
    ? forall x R:
        square_function(x)-square_tangent_at_three(x)=(x-3)^2
    square_function(x)=x^2
    square_tangent_at_three(x)=9+6*(x-3)
```

[Full two-value positive](evidence/round-73-cases/values-only.lit).
The original then repeats the difference as a two-edge polynomial expansion
chain. That last proof-body fact is removable; three facts become two.
The displayed body exposes the exact source formulas, from which the final
polynomial identity closes. A teaching version may retain the expansion to
show why the error is quadratic; it is machine-removable here.

## Deletion boundaries

The original theorem passes. Bare equality, empty theorem and chain-only
proof miss. Deleting either function-value fact from the original also fails.
Do not turn this result into a rule to remove all formula publications or to
prefer a single chain regardless of context. The two-value route is verified
shorter than this source, not asserted to be globally minimal.

## Derived order consumer: theorem call plus square certificate

The following is a new consumer probe, not a theorem copied from the source:

```litex
thm tangent_lower_bound:
    ? forall x R:
        square_tangent_at_three(x)<=square_function(x)
    release thm square_tangent_error_at_three(x)
    0<=(x-3)^2
```

[Full shorter theorem plus consumer](evidence/round-73-cases/short-theorem-lower-bound-no-echo.lit).
The error equality and nonnegative square close the weak order target.
A repeated target fact after the square certificate can be omitted. The
call alone and a bare order target miss. The alternative certificate chain
0<=(x-3)^2=square_function(x)-square_tangent_at_three(x) also passes with the
shorter remainder theorem, but is not needed for this consumer.

## Numeric checks and negatives

Both source functions equal9 at3; these direct value checks pass. Therefore
the claimed strict inequality for every real x is false, and its probe rejects.
The theorem with error -(x-3)^2 rejects too. At4, the correct difference1
misses as a bare numeric target, but publishing square_function(4)=16 and
square_tangent_at_three(4)=15 first makes that same endpoint pass.
[Contact values](evidence/round-73-cases/numeric-contact.lit),
[positive gap with values](evidence/round-73-cases/numeric-gap-with-values.lit).
The numeric difference miss is true-but-unsupported, not a negative value check.

## Evidence and scope

[Receipt](evidence/round-73-2026-10-09.summary.json):17 strict files,
7 accepted/10 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Source/binary hashes retained.
Historical round72 prechecks agree but do not own current acceptance. Session66922
stays on round68: after a normal chain-only miss it accepted the original
theorem in the same process, then the short order consumer. The failed warm
transcript is marked partial if the tool truncated it; cold receipt is complete.
No canonical source, kernel, trust, protected owner, global minimality, timing
or derivative-interface change. No new bt proposed from this source slice.

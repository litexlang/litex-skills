# Part 115 — Actual quadratic initial value: publish the relevant formula once

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and interface

The ODE showcase defines quadratic_solution(c,x)=x^2+c and evaluates it at0
to identify its integration constant. Keep its real parameters and exact
initial-value premise. This algebra slice does not validate its derivative
predicate, differential-equation proof or full showcase.

## Checked short source theorem

```litex
have fn quadratic_solution(c,x R) R=x^2+c

thm quadratic_initial_value_selects_parameter:
    ? forall c,y0 R:
        quadratic_solution(c,0)=y0
        =>:
            c=y0
    quadratic_solution(c,0)=c
```

[Complete positive](evidence/round-82-cases/value-only.lit).
The original one-statement proof chain is
quadratic_solution(c,0)=0^2+c=c. The intermediate polynomial expression can
be removed, retaining one formula-value fact. Statement count stays one;
no runtime or large proof-size saving is claimed. Bare implication and an
empty named theorem body both miss. Keep the useful bridge rather than
expanding zero arithmetic or asserting every direct hidden-function query works.

## Derived arbitrary-point consumer

The following is separately authored from the same formula, not a source
theorem or an assumed library interface:

```litex
thm arbitrary_initial_parameter:
    ? forall c,x0,y0 R:
        quadratic_solution(c,x0)=y0
        =>:
            c=y0-x0^2
    quadratic_solution(c,x0)=x0^2+c
```

[Complete arbitrary-point consumer](evidence/round-82-cases/arbitrary-initial-point-consumer.lit).
Its one value fact closes the algebraic target without changing the formula
or requiring nonzero/positive x0. Do not infer general inverse-function or
ODE solution-uniqueness support from this scalar parameter calculation.

## Negatives and evidence

Wrong conclusion c=y0+1 rejects with the short body. Omitting the initial
condition rejects with the original body. Numeric values at0 for c=3 and
c=-2 pass directly, illustrating that no positivity assumption on c is needed.
These controls are distinct from the true bare-parameter search miss.

[Receipt](evidence/round-82-2026-10-09.summary.json):8 strict files,
4 accepted/4 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary hashes and
log retained. Session66922 stays on round68 and accepted the renamed formula
and local parameter claim; current cold files own source/deletion/negative
evidence. No canonical source, kernel, trust, protected owner, performance,
full-ODE or global-minimum claim. No new bt required for this checked route.

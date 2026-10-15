# Round102 — school algebra: equation and factored roots follow-up

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


The original ordered source prefix through its algebra numerical consumers
checks with two earlier simplifications together: `solve_linear_equation`
keeps only `a*x=c-b`; `factored_quadratic_roots` keeps factor-zero case
headers with no branch-body facts and no colon. The former was already an
isolated alternative in Part104; the latter was already Part105's shorter
case route. This round checks their combination in the source order and adds
negative-coefficient, repeated-root, and signed-root consumers.

Seventeen promoted strict Normal files: 8 accepted and 9 rejected. An
empty-body `case ...:` fixture produced a parser error and is excluded from
proof counts. Bare theorem bodies, direct root disjunction and root-equality
case guards reject; removing `a!=0` or the zero-product premise and writing
false conclusions reject. Normal failures have null Session errors. All
promoted paths were rerun and match their recorded outcomes.

[Part104](part-104-showcase-linear-equation.md),
[Part105](part-105-showcase-factored-roots.md),
[receipt](evidence/round-102-2026-10-10.summary.json), and
[preferred ordered prefix](evidence/round-102-cases/preferred-both-short.lit).
The receipt records exact source/binary hashes and commands. Successful
round88 fixed snapshot reused; no moving-kernel, whole-showcase, new bt or
performance claim. No canonical or kernel edits.

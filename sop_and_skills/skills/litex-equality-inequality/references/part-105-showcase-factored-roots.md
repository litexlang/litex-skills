# Part 105 — Factored quadratic roots: keep cases, omit branch echoes

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

The middle-school showcase defines factored_quadratic_roots from
(x-r)*(x-s)=0 to x=r or x=s. A zero product has a zero factor; each factor's
vanishing identifies its root. Preserve the real carrier and disjunctive
conclusion. The isolated source slice does not claim whole-showcase acceptance.

## Checked source simplification

```litex
thm factored_quadratic_roots:
    ? forall r,s,x R:
        (x-r)*(x-s)=0
        =>:
            x=r or x=s
    by cases:
        ? x=r or x=s
        case x-r=0
        case x-s=0
```

[Complete shortened theorem](evidence/round-65-cases/bodyless-factor-cases.lit).
The original has a colon and x=r or x=s fact inside the corresponding branch.
Both branch-body facts are removable together. Native case syntax without a
colon expresses an empty body, which still has to close the declared goal.
The same shortened theorem followed by
`release thm factored_quadratic_roots(2,3,3)` passes.
[Checked consumer](evidence/round-65-cases/bodyless-theorem-native-call.lit).

Round102 rechecked this form inside the original ordered school-showcase prefix,
alongside the one-step linear-equation proof. The combined strict file passes.
Native repeated-root `(2,2,2)` and signed-root `(-3,4,-3)` consumers also
pass after this prefix. [Joint short prefix](evidence/round-102-cases/preferred-both-short.lit),
[repeated root](evidence/round-102-cases/preferred-repeated-root-consumer.lit),
[signed root](evidence/round-102-cases/preferred-negative-root-consumer.lit).

## Direct forms and case coverage

The bare implication to x=r or x=s misses, and an empty-body named theorem
also misses. The bare implication to x-r=0 or x-s=0 passes. Keep the factor
expressions in the case guards: using only cases x=r and x=s fails at
coverage/search_proof before checking their trivial branch conclusions.
This is an expression-specific explicit route, not a proof that the two
mathematical disjunctions differ.

Removing the second factor case also fails at coverage. Changing the theorem
and case target to x=r, while keeping both factor cases, fails at second
branch closing_then. Empty bodies do not waive branch checking.
[Missing case](evidence/round-65-cases/missing-second-case.lit),
[wrong first-root target](evidence/round-65-cases/bodyless-cases-wrong-first-root.lit).

## Double root and concrete demonstration

The true bare (x-r)^2=0 implies x=r target misses, but this local bridge passes:

```litex
claim:
    ? forall r,x R:
        (x-r)^2=0
        =>:
            x=r
    x-r=0
```

[Complete double-root bridge](evidence/round-65-cases/double-root-local-zero.lit).
No second repetition of x=r is needed. This isolated observation does not
establish unrestricted normalization of disjunctions or polynomial equations.

The source numeric demonstration's three statements
`(3-2)*(3-3)=0`, `3=3`, `3=2 or 3=3` pass; the final disjunction alone also
passes. Those first two facts are removable for this numerical assertion,
though a reader may retain the product to illustrate the theorem.

## Negatives, receipt and scope

The false implication to both roots and the false implication to the first
root alone reject, as does root disjunction without the zero-product premise.
The checked facts (3-2)*(3-3)=0 and 3!=2 give a concrete counterexample to
the first-root claim. Distinguish these from the true direct-disjunction miss.

The round102 variant `case x-r=0:` with an empty indented body was a parser
error, excluded from proof outcomes. The checked empty-body syntax omits the
colon. In the same full prefix, replacing factor-zero case guards by `x=r`
and `x=s` rejects at coverage; a direct root disjunction also rejects. Missing
zero-product premise and false `x=r and x=s` reject as semantic controls.

[Receipt](evidence/round-65-2026-10-09.summary.json):17 strict files,
8 accepted/9 Normal rejections. All promoted paths rerun on the fixed snapshot
after successful current-source release build. Source hash, build log and
literal Session journal retained. Session9174 remains on round61 and accepted
the renamed bodyless-case theorem; current cold files own deletion evidence.
No canonical source, kernel, trust, protected owner or performance change.
The natural case route already exists; no new bt is proposed from this case.

[Round102 follow-up receipt](evidence/round-102-2026-10-10.summary.json):17 normal
strict files, 8 accepted/9 rejections, plus one excluded parse-error fixture;
promoted paths rerun with matching outcomes. This is the same source family as
Parts104–105, on the successful fixed round88 binary snapshot, not an
independent rule or whole-showcase acceptance.

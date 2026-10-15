# Part 104 — Actual showcase linear equation: one proof fact and a native call

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

The middle-school showcase defines solve_linear_equation from a!=0 and
a*x+b=c, then demonstrates its call at (3,-6,0,2). Subtract b and divide by
the nonzero coefficient. Keep the exact theorem name, domains and premises.
This isolated source slice does not claim acceptance of the whole showcase.

## Checked one-chain theorem

```litex
thm solve_linear_equation:
    ? forall a,b,c,x R:
        a!=0
        a*x+b=c
        =>:
            x=(c-b)/a
    x=(a*x+b-b)/a=(c-b)/a

release thm solve_linear_equation(3,-6,0,2)
```

[Complete theorem and caller](evidence/round-64-cases/short-chain-bare-caller.lit).
The chain follows the source equality through a common subtraction and
division. No helper definition or additional mathematical assumption is needed.
Keep the named theorem because the source demonstrates native theorem reuse.

## Source comparison and deletion controls

The original two proof-body facts are:

```litex
a*x=c-b
x=(a*x)/a=(c-b)/a
```

Both pass together. Surprisingly, each alone also suffices in a cold theorem
file: retaining only a*x=c-b closes the theorem, and retaining only the
original division chain also closes it. The displayed combined chain is
therefore one clear checked route, not a global minimum or the only repair.
[Intermediate-only theorem and call](evidence/round-64-cases/intermediate-bare-caller.lit),
[division-chain-only theorem](evidence/round-64-cases/theorem-division-chain-only.lit).

Round102 rechecked the original ordered school showcase prefix through its
algebra consumers. Its preferred joint short file keeps only `a*x=c-b` in
this theorem and also uses Part105's bodyless factor cases. The source's
numeric consumer still passes. A separate negative-coefficient consumer
checks `solve_linear_equation(-2,7,1,3)` and the resulting quotient. This is
a second dated source-prefix check of the same situation, not a new rule.
[Joint short prefix](evidence/round-102-cases/preferred-both-short.lit),
[negative coefficient](evidence/round-102-cases/short-linear-negative-coefficient.lit).

The original concrete demonstration publishes 3!=0 and 3*2+(-6)=0, invokes
the theorem, then repeats 2=(0-(-6))/3. Removing those three surrounding
facts leaves the native call accepted after either the original theorem or
the shortened one. These are numeric call-premise checks; they do not prove
that arbitrary symbolic callers can omit their premises. The theorem call
also serves the source's pedagogical purpose even if its numeric conclusion
could be calculated independently.

## Direct miss and negatives

The bare guarded forall endpoint misses. An empty-body named theorem with
the same goal also rejects at conclusion/search_proof. At least one useful
proof-body route is retained in these checked examples.

The wrong-sign x=(b-c)/a claim rejects. Removing a!=0 from the otherwise
same chain fails earlier at goal_wd/Div: the quotient needs a!=0. This is a
domain guard boundary rather than validation of a well-defined false quotient.
The numeric facts 0*7+2=2 and 7!=0 pass, illustrating that the zero-coefficient
equation cannot determine x. The valid chain with the additional premise a<0
passes; no positive-coefficient restriction was invented.
[Wrong sign](evidence/round-64-cases/wrong-sign-conclusion.lit),
[missing guard](evidence/round-64-cases/missing-nonzero-chain.lit).

## Evidence and scope

[Receipt](evidence/round-64-2026-10-09.summary.json):14 strict cold files,
10 accepted/4 Normal rejections. All promoted paths rerun on the fixed
snapshot after successful current-source release build. Exact source hash,
build log and Session journal retained. Session9174 uses round61 and accepted
the renamed one-chain theorem and its native call; cold round64 owns deletion
and negative evidence. No whole-showcase, performance, protected-owner or
kernel change. In particular, this audit does not implement the common-factor
cancellation bt candidate the user excluded from the selected rule task.

[Round102 follow-up receipt](evidence/round-102-2026-10-10.summary.json) shares its
17 normal strict files and one excluded parse fixture with Part105. It reuses
the successful round88 fixed binary snapshot; it is not moving-kernel or
whole-showcase acceptance.

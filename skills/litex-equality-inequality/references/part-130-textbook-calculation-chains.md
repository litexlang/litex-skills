# Part130 — Textbook calculation chains: retain the useful algebraic bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

Chapter 1, §1.1 of *The Mechanics of Litex Proof* presents four explicitly
step-by-step equality calculations. Its own comments say this is a teaching
style and some intermediate links may be omitted. Keep each example's
original rational/real/integer carrier, premises and final result. The
checked source prefix stops before §1.2; it is not whole-chapter acceptance.

## Positive: two shorter chains

For rational `a,b` with `a-b=4` and `a*b=1`, the source has four equal
expressions. Three suffice in this fixed snapshot:

```litex
(a+b)^2=(a-b)^2+4*(a*b)=20
```

For real `r,s` with `r+2*s=-1` and `s=3`, the source has five equal
expressions. Three suffice:

```litex
r=(r+2*s)-2*s=-7
```

The two shortened statements pass together in the original ordered prefix;
the remaining two original calculations also pass there. The first retained
middle expression exposes the square identity; the second exposes subtraction
of `2*s`. [Joint checked prefix](evidence/round-103-cases/joint-first-two-short.lit).

## Direct misses and tested boundaries

Each of the four §1.1 conclusions, when written as only the final equality
under the same premises, rejects at `search_proof`. For the first two, an
alternative bridge jumping straight to the substituted numeric expression
also rejects. Thus their successful bridge has a specific useful shape;
the observed direct miss is not a false mathematical conclusion.

The third, conditional Brahmagupta calculation, passes as written. Deleting
either of its two middle expressions individually rejects. The fourth,
`d*(a*f-b*e1)=0` from `a*d=b*c` and `c*f=d*e1`, also passes as written.
Each of its four intermediate expressions was deleted in a separate cold
file; all four deletions rejected. Three newly written shorter candidate
chains rejected too. These finite probes do not establish global minimum or
an internal cause. Keep the source chains for these two situations until an
actual shorter accepted route is found.

False first/second endpoints (`21` and `-8`) reject. Removing `a*b=1` from
the first shortened problem or `s=3` from the second rejects. These are
premise/false-goal controls, distinct from the true direct-form misses.

## Evidence and scope

[Receipt](evidence/round-103-2026-10-10.summary.json):24 promoted strict cold files,
4 accepted/20 Normal rejections, matching reruns, null Session errors and
recorded source/binary hashes. The fixed binary is the successful round88
snapshot. This is a source-specific authoring recipe, not a new bt or a
universal demand to include algebraic bridges. No canonical textbook, kernel,
AST, trust, performance or moving-kernel claim/change.

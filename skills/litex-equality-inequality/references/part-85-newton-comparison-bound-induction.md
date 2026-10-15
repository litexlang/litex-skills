# Part 85 — Comparison recurrence and the actual final Newton bound

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and retained mathematics

The numerical-analysis showcase defines B_n=4*(1/4)^(2^n) with positive
codomain, proves B_(n+1)=B_n^2/4, and proves g_n<=B_n by induction using
Part84's actual quadratic contraction. This round retains the positive-bound
proof and all recursive interfaces, replacing only candidate proof bodies.
No scalar surrogate or extra premise replaces the source theorem.

## Positive: recurrence eight statements to four

The accepted body uses a local positive t, one value bridge, one power chain,
and one final calculation:

```litex
have t R+ = (1/4)^(2^n)
r45_sqrt_two_newton_gap_bound(n)=4*(1/4)^(2^n)=4*t
(1/4)^(2^(n+1))=(1/4)^(2^n*2)=((1/4)^(2^n))^2=t^2
r45_sqrt_two_newton_gap_bound(n+1)=4*(1/4)^(2^(n+1))=4*((1/4)^(2^n))^2=4*t^2=(4*t)^2/4=r45_sqrt_two_newton_gap_bound(n)^2/4
```

[Full recurrence slice](evidence/round-45-cases/bound-step-delete-exponent.lit).
The earlier four-statement candidate published the exponent equation but
omitted the power chain; its final calculation missed. Restoring the power
chain gives a five-statement proof, then deleting the separate exponent
publication passes. These different four-statement candidates are not
interchangeable: the explicit intermediate power expression is live.
The direct bodyless recurrence and bodyless positivity proof miss cold.
The original positive-bound proof remains in the short combined prefix.

## Positive: final induction33 branch statements to twelve

The original induction has eight base-case calculations and25 successor
calculations. The checked replacement has four base calculations and eight
successor statements. Count excludes induction headers and goal lines.

Base calculations retain iterate(0)=1, combine residual evaluation into one
chain, evaluate g_0 through its magnitude, and evaluate B_0=1. Successor proof
retains g_k>=0, the two factor signs for B_k-g_k and B_k+g_k, a difference-of-
squares certificate, the resulting square order, two recurrence calls and a
single comparison chain. Exact final excerpt:

```litex
release thm r44_sqrt_two_newton_gap_contracts_quadratically(k)
release thm r45_sqrt_two_newton_gap_bound_step(k)
r44_sqrt_two_newton_gap(k+1)<=r44_sqrt_two_newton_gap(k)^2/4<=r45_sqrt_two_newton_gap_bound(k)^2/4=r45_sqrt_two_newton_gap_bound(k+1)
```

[Combined four-statement recurrence and twelve-statement final induction](evidence/round-45-cases/combined-four-step-and-short-final.lit)
contains every retained source definition and short upstream proof through the
actual final bound. The five-statement recurrence also composes independently.
No global minimality or speedup is claimed.

## Negatives, deletion and capability boundaries

Removing the successor g_k magnitude/nonnegative publication makes this short
induction fail. The final theorem bodyless also misses. The false strengthened
conclusion g_n<=B_n/2 rejects: g_0=B_0=1 refutes it. Its proof body still proves
the original bound, so the rejection occurs at the stronger final conclusion.
The source's positive B codomain and N index domain are unchanged. None of
these misses justifies a new universal power/sign rule from this single case.
Warm Session already knows the original recurrence and final theorem; independent
cold files own deletion and composition evidence.

## Evidence and next checkpoint

[Round45 receipt](evidence/round-45-2026-10-09.summary.json):14 strict independent files,
8 accepted/6 rejected, all promoted paths rerun using the fixed fresh release
snapshot. Source hash and warm journal retained. No canonical source, kernel,
AST/Env/Runtime, trust, whole-showcase, extractor or timing change.
The actual symbolic closed-form bound is accepted in the combined slice. The
source's final n=2 numeric checkpoint and broader corpus searches remain next;
no whole numerical showcase acceptance is inferred from this selected slice.

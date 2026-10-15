# Part 91 — Actual textbook exponential bound with a two-step induction

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and migration boundary

The high-school chapter16 states forall n in N,2^n>=n+1. Its original claim
puts a base calculation and a conditional forall m in Z inside by induc,
without explicit structured branches. The exact isolated source parses under
the current binary but fails the induction successor goal2^(n+1)>=n+1+1.
This is a normal proof-execution/search failure, not a parser failure or a
counterexample. No old binary acceptance baseline is available; the migration
cause is undetermined. No whole chapter or source-prefix dependency is claimed.

## Positive: current structured induction has two calculation statements

This checked standalone proof preserves the exact N domain and conclusion:

```litex
claim:
    ? forall n N:
        2^n>=n+1
    by induc k from 0:
        ? 2^k>=k+1
        ? from k = 0:
            2^0=1>=0+1
        ? induc:
            2^(k+1)=2^k*2>=(k+1)*2=k+1+(k+1)>=k+1+1
```

[Runnable short proof](evidence/round-51-cases/modern-short.lit).
The successor chain uses the active induction hypothesis directly, doubles its
comparison and uses k>=0 from the natural binder. No separate hypothesis echo,
nonnegative-index publication or doubled inequality is required in this route.
A generated expanded current-form reference with five calculation statements
also passes; those are generated variant counts, not a deletion saving from an
already passing original textbook proof. The original isolated claim did not
pass and remains untouched in the source workspace.

## True direct misses, mathematical negatives and syntax controls

Bare forall n N:2^n>=n+1 and a bodyless claim miss cold. After the original
expanded current proof is published, warm direct success is contaminated.
Keeping a successor branch containing only k>=0 fails cold, showing the actual
successor calculation is live. The direct integer extension also misses, but
is mathematically true: negative integers have n+1<=0 and2^n>0. It is a separate
capability probe, not a false or domain-negative example.

The strict natural bound2^n>n+1 is false at0 (also1), and the proposed stronger
2^n>=2*n+1 is false at1; both reject. A numeric not2^0>0+1 control passes.
An empty successor branch and a missing base branch are separate parser
controls. Current structured induction requires both ?from and ?induc and
nonempty syntax bodies. Those parser errors do not establish mathematical
rejection of the underlying bound; the accepted short proof keeps the meaningful
base calculation rather than inserting a dummy proof statement.

## Evidence, restart and remaining scope

[Round51 receipt](evidence/round-51-2026-10-09.summary.json):12 independent files,
3 accepted,7 normal proof rejections,2 intentional parser controls. All promoted
paths rerun with the fixed current-source release snapshot; parsed errors are
classified separately from Normal success/session_error=null outcomes.
Source hash, build and literal warm journal retained. A missing-base warm syntax
probe ended Session42453. New Session99217 replayed the accepted modern-short
file on current release and reached its prompt. No unrelated historical
contexts were claimed replayed. Ordinary proof misses did not cause restart.
No canonical scripts source, kernel, trust, AST/Env/Runtime or whole-book edit.
The original mathematical theorem is now explicitly checkable in the isolated
current form; the old source's internal failure cause is not claimed repaired.
Next source family: chapter02's local AM-GM proof, retaining x,y>=0 and the
named arithmetic/geometric means before testing square-root comparison bridges.

# Part 67 — Publish only the missing restriction definition link

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematical spine

For p in K subset X, result=restricted implies result(p)=restricted(p), and
the restriction definition implies restricted(p)=f(p). Round 26 checks which
link the generic target lacks without changing its arbitrary X/Y carriers.

## Shortest checked author in this round

With the exact showcase template, this complete claim passes:

```litex
claim:
    ? forall X,Y set,f fn(x X) Y,K power_set(X),result fn(x K) Y,p K:
        result=\restricted<X,Y,f,K>
        =>:
            result(p)=f(p)
    \restricted<X,Y,f,K>(p)=f(p)
```

The direct zero-body form remains the Round 25 miss. The one statement above
is shorter than the previously accepted full result(p)=restricted(p)=f(p)
chain. An extra final result(p)=f(p) line passes but is unnecessary.

## Diagnose the right boundary

Stating only result(p)=restricted(p) does not close the original target.
Stating both links separately, or supplying both as diagnostic premises, does.
The immediate head-congruence equation itself already passes. Generic objects,
arbitrary-carrier function calls and mixed-domain calls also support direct
equality transitivity. Do not add a duplicate transitivity rule.

The bounded candidate is obtaining/consuming an existing function definition
equation through a supplied equal function value, retaining its actual alias,
definition and domain evidence. The precise implementation owner and a causal
repair remain unproved; no unrestricted function-body search or Env cache is
justified by these observations.

## Negative controls

f(p)=g(p) alone cannot imply f(p)=h(p). Two links at p cannot imply equality
at an unrelated q. A definition result about restricted(p) does not determine
an unrelated result function without result=restricted. All three false controls
reject. Mixed-domain positives explicitly retain legal memberships; they are
diagnostic interface probes, not new assumptions for the main author.

## Evidence

[Round 26 receipt](evidence/round-26-2026-10-09.summary.json) preserves all exact sources,
strict cold envelopes and current executable/build identity. Same-Session
attempts and deliberate current-binary adoption are retained. No canonical
proof/kernel changes, trust, whole-module, global-minimality or speed claim.

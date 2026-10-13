# Part 79 — Derivative error application and the closing triangle estimate

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source interface and hypotheses

The ODE showcase's derivative_delta_controlled definition bounds the difference
quotient error when the input is distinct from x0 and within its positive
delta. The isolated definition is renamed r39_derivative_delta_controlled;
its real-valued function domain, real inputs and positive epsilon/delta remain.
Source absolute-bar notation is written as the equivalent abs(...) form in
these probes. This is a caller/scalar slice, not full uniqueness acceptance.

## Direct application already works; alias needs its actual value bridge

The original unaliased error follows directly from the supplied predicate and
both sample conditions. Missing distance and changed-slope controls reject.
For an independently supplied q=quotient equation, direct abs(q-slope)<epsilon
misses. The tested claim body needs these two statements:

```litex
abs((f(sample)-f(x0))/(sample-x0)-slope)<epsilon
abs(q-slope)=abs((f(sample)-f(x0))/(sample-x0)-slope)<epsilon
```

Publishing only the raw error does not repair that alias target. This receipt
tests the equation-premise alias context; it does not establish identical
behavior for every have-initializer alias. Do not duplicate the working raw
derivative application or infer that its numeric bound is unavailable.

## Five source algebra statements reduce to two triangle statements

With the source errors abs(q-slope1)<epsilon and abs(q-slope2)<epsilon:

```litex
abs(slope1-q)=abs(q-slope1)<epsilon
abs(slope1-slope2)<=abs(slope1-q)+abs(q-slope2)<epsilon+epsilon=2*epsilon
```

The original five-statement scalar triangle spine passes, and this two-
statement route passes cold. Bodyless closure and the second chain alone miss.
The first statement publishes the needed orientation of the actual error.
Missing the second error is false; weak errors cannot imply the strict final
bound, and that false control rejects. No intermediate point discovery or
unbounded triangle search is justified by the short explicit route.

## Separation margin: keep the visible one-factor endpoint

From distinct slopes and the source epsilon=abs(slope1-slope2)/3, the direct
margin misses. Even after publishing nonzero difference and absolute positivity,
the chain ending in `(2/3)*abs(...)<abs(...)` misses. Adding the closed factor
comparison 2/3<1 alone does not repair that last adjacent link.

This checked three-statement claim body passes instead:

```litex
slope1-slope2!=0
abs(slope1-slope2)>0
2*epsilon=2*(abs(slope1-slope2)/3)=(2/3)*abs(slope1-slope2)<1*abs(slope1-slope2)=abs(slope1-slope2)
```

The explicit 1* endpoint exposes the common positive factor to the existing
comparison route; no kernel, global search or extra source premise is changed.
The longer source-shaped factor spine also passes. This is a dated bridge,
not a permanent mandate to expand every scalar to1 times itself.

## Scalar contradiction: closing evidence remains a separate consumer

Combine the short triangle and margin inside by contra. The short scalar
equality proof misses at `closing / negated_impossible`: it cannot establish
`not abs(slope1-slope2)<abs(slope1-slope2)` in that closing attempt.
The independently checked version additionally publishes:

```litex
abs(slope1-slope2)>=abs(slope1-slope2)
not abs(slope1-slope2)<abs(slope1-slope2)
impossible abs(slope1-slope2)<abs(slope1-slope2)
```

Then the conditional scalar equality proof passes. These are proved facts,
not trusted premises. The bundle is a sufficient checked route; no claim
that both added facts are minimal or universally mandatory is made. The
missing-error control remains rejected. The standalone closing limitation
does not authorize changing by-contra contracts or search ceilings.

## Evidence and remaining integration

[Round39 receipt](evidence/round-39-2026-10-09.summary.json):21 unique strict files,
7 accepted/14 rejected, all promoted copies rerun on the fixed fresh binary.
Exact source path/hash and full failures retained; source spelling changes
are declared above. Warm Session25852 on round29 snapshot accepts bodyless
triangle after theorem reuse; cold files own liveness.

This verifies raw derivative caller, equation-alias bridge, scalar triangle,
margin and a conditional scalar closing proof separately. Actual have-defined
quotient aliases and the assembled original derivative uniqueness theorem are
not accepted by this receipt. No canonical/kernel/protected-owner edit, new
trust, whole-showcase or performance claim. Next verify those real integration
boundaries before claiming the entire source proof can be replaced.

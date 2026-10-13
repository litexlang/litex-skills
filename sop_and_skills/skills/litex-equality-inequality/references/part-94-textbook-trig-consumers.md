# Part 94 — Trig conclusions, named secant consumers and numeric limits

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematical interfaces

High-school chapter05 defines deg(theta)=theta*pi/180 and secant(theta)=
1/cos(theta) with cos(theta)!=0 inside its domain. Its guarded forall exports
five identities: tangent quotient, secant reciprocal, and three successive
square identities. These are theorem conclusions, not redundant proof-body
statements. Preserve their mathematical content and the singularity guard.

## Positive: combine related conclusions without claiming an endpoint shortcut

The exact five-conclusion source passes independently. This combined form also
passes, retaining the first two conclusions and every adjacent square identity:

```litex
forall x R:
    cos(x)!=0
    =>:
        tan(x)=sin(x)/cos(x)
        r54_secant(x)=1/cos(x)
        1+tan(x)^2=1/cos(x)^2=(1/cos(x))^2=r54_secant(x)^2
```

[Complete combined slice](evidence/round-54-cases/trig-combined-conclusions.lit).
It has three conclusion entries instead of five, but no source fact is deleted
merely as unused. No canonical interface or stored-fact contract was changed.
The bare transitive endpoint misses even after either original or combined
forall is published; publication plus transitive discovery is not established
by their own acceptance. Do not promise automatic endpoint consumption.

## Actual endpoint consumer: two explicit body statements

This separate same-domain endpoint claim checks independently with just the
source definitions. Its body is:

```litex
r54_secant(x)=1/cos(x)
1+tan(x)^2=1/cos(x)^2=(1/cos(x))^2=r54_secant(x)^2
```

[Full endpoint claim](evidence/round-54-cases/endpoint-value-and-chain.lit).
Deleting the value publication makes the chain's final adjacent equality
(1/cos(x))^2=secant(x)^2 miss. Earlier chain links pass. Warm chain-only success
after preceding publication is not cold support. This is a consumer bridge in
this context, not permission to remove mathematical conclusions from the source.

## Numeric degree and cosine-law observations

Original degree chains all pass. Direct deg(180)=pi passes, while direct90,60,
45 conversions miss. The checked mixed variant shortens only180 and retains the
other three original arithmetic chains. All four source items already use one
statement each; this is chain shortening, not fewer statements or a speedup.

The source cosine-law squared-side example has cos(pi/2)=0 and a chain to25.
This checked shorter route retains that cosine value and combines its calculation:

```litex
cos(pi/2)=0
r54_cosine_law_third_side_sq(3,4,pi/2)=3^2+4^2-2*3*4*cos(pi/2)=25
```

[Runnable numeric slice](evidence/round-54-cases/cosine-value-and-short-chain.lit).
Removing the cosine publication makes that chain miss. Keeping the cosine
publication but jumping directly from the named function to25 also misses.
The original longer literal-zero chain passes. Do not infer general arithmetic
or trigonometric evaluation behavior from one named-function consumer.

## Negatives and evidence

Wrong minus-sign secant identity and numeric24 reject. Missing cos!=0 leaves
tangent/secant domains unsupported; secant(pi/2) explicitly violates its domain
and rejects. Arguments remain real and no positive-cosine restriction is added.

[Round54 receipt](evidence/round-54-2026-10-09.summary.json):19 independent strict files,
7 accepted/12 rejected; all promoted paths rerun on the fixed current-source
release snapshot. Source hash, build and exact warm journal saved. Session99217
remains live. No canonical scripts/kernel/protected-owner/trust, whole-chapter,
consumer-equivalence beyond tested outcomes, or performance claim.
Next chapter06: trigonometric bounds/parity/periodic interfaces and transformed
sine numeric definition consumers, preserving callable singularity guards.

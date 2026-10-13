# Part 95 — Actual trig periods: explicit formulas and one argument bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and already concise support

High-school chapter06 directly states sine/cosine ranges, parity,2*pi periods
and two pi-period tangent spellings. Ranges and parity pass directly; do not
expand those working interfaces. The bare two-pi and tangent interfaces miss
independently under the freshly built release. Preserve every source conclusion
and the tangent's original three cosine-nonzero guards in the principal repair.
A one-spelling/two-guard source variant is only a separately labeled probe.

## Positive: four-step sine/cosine two-pi proof

With the exact source two conclusions as the claim target, this body passes:

```litex
cos(2*pi)=1
sin(2*pi)=0
sin(x+2*pi)=sin(x)*cos(2*pi)+cos(x)*sin(2*pi)=sin(x)
cos(x+2*pi)=cos(x)*cos(2*pi)-sin(x)*sin(2*pi)=cos(x)
```

[Full source-domain proof](evidence/round-55-cases/two-pi-addition-proof.lit).
Deleting either closed sine/cosine value makes this route fail. The calculation
is an explicit meaningful addition-formula proof, not a new periodicity axiom
or an unbounded search strategy. No source theorem was weakened.

## Positive: both original tangent spellings in four steps

This body checks both tan(x+pi)=tan(x) and tan(x+1*pi)=tan(x), with all three
source cosine guards unchanged:

```litex
cos(x+pi)=-cos(x)
tan(x+pi)=sin(x+pi)/cos(x+pi)=(-sin(x))/(-cos(x))=sin(x)/cos(x)=tan(x)
x+1*pi=x+pi
tan(x+1*pi)=tan(x+pi)=tan(x)
```

[Complete two-conclusion proof](evidence/round-55-cases/tangent-delete-sin-value.lit).
An initial addition-formula proof reached its final spelling-conversion step
and failed tan(x+1*pi)=tan(x+pi). Publishing the exact argument equality repairs
that step. A separate sin(x+pi)=-sin(x) publication is removable in the checked
full route; deleting the cosine equation instead fails. The one-conclusion
proof also passes, but it is not acceptance of both source conclusions.
Direct anti-period statements at x+1*pi fail in the separately tested route.
This is dated expression/consumer evidence, not a permanent requirement to
publish every trivially equal function argument or a settled kernel cause.

## Amplitude and actual numeric function use

The source transformed-sine definition and amplitude abs spelling both work
under the current release; no syntax migration is needed here. The amplitude
example shortens to r55_sine_scale_amplitude(-3)=3. Its original abs(-3) chain
also passes. Both forms remain one statement; only the intermediate is removed.

The source transformed-sine example exposes its definition, which passes.
A downstream exact-value probe r55_transformed_sine(2,3,pi/6,0)=1 misses.
This explicit route checks that value:

```litex
sin(pi/6)=1/2
r55_transformed_sine(2,3,pi/6,0)=2*sin(3*0+pi/6)=2*sin(pi/6)=2*(1/2)=1
```

[Full numeric slice](evidence/round-55-cases/transformed-short-chain.lit).
The exact value1 is an additional evaluation use probe, not a claimed repair
of a failing original definition equation. Wrong amplitude-3 and transformed
value2 reject; sine's false pi-period and tangent's singular pi/2 value reject.
No positive-amplitude or frequency assumptions were added to the real source
functions; no source singularity guards were silently removed.

## Evidence and baseline correction

[Round55 receipt](evidence/round-55-2026-10-09.summary.json):23 independent strict files,
9 accepted/14 rejected, all promoted copies rerun on the fixed fresh release
snapshot. Build52713 completed before that acceptance snapshot was copied.
Initial probes accidentally copied the pre-build binary while compilation was
running; those observations and executable are retained only in the task draft,
explicitly excluded from current acceptance. Every source probe reran after the
build. Source hash and incremental warm journal retained. Session99217 still
runs the older round51 executable; its responses are labeled, and cold current
files own all acceptance/deletion claims.
No canonical scripts/kernel/protected-owner/trust, whole chapter, global
periodicity discovery, or performance change. Next chapter04 identity/negative-
identity order consumers, separating source conclusions from proof traces.

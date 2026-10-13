# Part123 — Actual scalar product/sum laws: inline the needed argument bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The linear-algebra showcase proves the scalar-product and scalar-sum laws for
plane_smul on cart(R,R). Preserve the exact real_field multiplication/addition,
real scalar carrier, vector carrier, operations and both conclusions. Use
Part122's shortened preceding source. The field adapter supplies the actual
real_field operation equations used by these coordinate calculations.

## Checked short route

[Complete preferred source](evidence/round-95-cases/chains-include-field-arguments.lit)
reduces sixteen immediate proof statements to nine. Keep the adapter call, four
scalar coordinate facts, two outer result expansions and two final chains.
The five plain tuple function-value facts and two standalone argument-rewrite
facts are removed; the needed argument rewrites become steps in the final chains:

```litex
plane_smul(real_field.mul(a,b),x)=plane_smul(a*b,x)=((a*b)*x(1),(a*b)*x(2))=(a*(b*x(1)),a*(b*x(2)))=plane_smul(a,plane_smul(b,x))
plane_smul(real_field.add(a,b),x)=plane_smul(a+b,x)=((a+b)*x(1),(a+b)*x(2))=(a*x(1)+b*x(1),a*x(2)+b*x(2))=plane_add(plane_smul(a,x),plane_smul(b,x))
```

These are excerpts inside the original forall claim, after the preserved
coordinate/outer expansion facts. All carriers and premises remain in the linked
complete source. The count concerns immediate proof statements, not scalar
operations, runtime cost or a global minimum.

## Independent deletion is insufficient for a combined proof

The original standalone bridge is:

```litex
plane_smul(real_field.mul(a,b),x)=plane_smul(a*b,x)
```

Deleting both such argument rewrites passes when the five tuple-value facts
remain. Deleting all five tuple-value facts passes when the two rewrites remain.
Deleting both groups together rejects. This is why the preferred final chain
retains `plane_smul(a*b,x)` and the sum counterpart as intermediate expressions.
It shortens the source without claiming those mathematical bridges are absent.
A second checked route retains product/sum tuple values instead of the standalone
argument rewrites; it is longer than the nine-statement route.

## Boundaries and consumers

Direct forall, removing the adapter call, deleting all four coordinate facts,
removing final chains and replacing them by bare endpoints reject. The short
proof also rejects without its adapter call or with all coordinate facts removed.
These are true facts with unsupported tested routes, not false mathematics or
an internal-cause diagnosis. No individual necessity claim for each coordinate
fact follows from the group-deletion probe.

False product and sum conclusions equaling x reject separately. Exported
product/sum facts can be consumed by an ordinary forall after the preferred
proof. Source continuation through the following vector-addition distributivity
claim also passes; this is not a claim that it directly depends on the shortened
claim, nor complete plane-vector-space acceptance.

## Evidence

[Receipt](evidence/round-95-2026-10-10.summary.json):17 strict files,
7 accepted/10 Normal rejections; all promoted paths rerun with matching exit
codes, Normal envelopes and null session errors. Exact source/binary identities
recorded; fixed snapshot from successful round88 build reused. Cold files own
combined-deletion evidence. Same showcase family, not independent permanent-rule
promotion. No canonical/kernel changes, trust, new bt, performance or whole-module
claim.

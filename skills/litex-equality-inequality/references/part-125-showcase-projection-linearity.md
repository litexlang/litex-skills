# Part125 — Actual projection linearity: twenty-eight calculation facts to ten

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The showcase projects (x,y) to (x,0) in the constructed real_plane. It proves
preservation of addition and scalar multiplication, then folds is_linear_map.
Keep the exact projection function, actual first-class plane operations, real
scalar/cartesian carriers and linearity goal. Use Part124's short instance prefix.

## Checked route

[Complete short theorem](evidence/round-97-cases/merged-delete-all-input-coordinate-values.lit)
uses five calculation statements per nested claim: operation alias, left expansion,
two scalar calculations and right expansion. Original nested calculation facts
twenty-eight become ten; both claim scopes and final definition action remain.
All five input tuple-value publications and eight bare coordinate facts can be
omitted together in this merged route.

The addition claim keeps these scalar calculations:

```litex
projection_x_axis(u)(1)+projection_x_axis(v)(1)=u(1)+v(1)
projection_x_axis(u)(2)+projection_x_axis(v)(2)=0+0=0
```

Its right expansion combines the original function expansion, tuple transport
and resulting plane operation equation:

```litex
real_plane.add(projection_x_axis(u),projection_x_axis(v))=plane_add(projection_x_axis(u),projection_x_axis(v))=(projection_x_axis(u)(1)+projection_x_axis(v)(1),projection_x_axis(u)(2)+projection_x_axis(v)(2))=(u(1)+v(1),0)
```

The scalar claim keeps `a*projection_x_axis(v)(1)=a*v(1)` and
`a*projection_x_axis(v)(2)=a*0=0`, with the analogous merged result chain.
Actual operation aliases remain `real_plane.add=plane_add` and
`real_plane.smul=plane_smul`.

## Deletion boundaries

Deleting five input tuple values alone passes. Deleting eight bare coordinate
facts alone also passes in the original source. A first broader deletion filter
included two scalar-product equations as well as those eight coordinates; it
rejects and is explicitly relabeled in the receipt. It cannot establish that
bare coordinate facts alone are necessary.

After merging right-side chains, retaining the four scalar calculations passes
with neither input tuple values nor bare coordinate facts. Merging without
those scalar calculations rejects even with coordinate publications. Replacing
the four scalar calculations by three whole projection values also rejects in
the tested alternative. A route retaining five whole input values instead of
eight bare coordinates passes, but is longer than the ten-calculation route.

Deleting both operation aliases rejects in the original source. Removing the
final is_linear_map fold rejects in both original and shortened proofs. These
are true mathematical targets with incomplete tested routes; no internal-cause
or individual alias-necessity claim is made. False additivity to projection(u)
and false scalar compatibility to projection(v) reject separately.

## Complete shortened standalone showcase

[Full short draft](evidence/round-97-cases/short-through-complete-showcase.lit)
continues through the original native linearity and kernel-subspace calls,
(0,7) kernel membership and final projection noninjectivity theorem. It passes
from the beginning to the end as one strict standalone file. Prior Parts document
the prefix's proof/interface changes; this is not a claim that the canonical
module has been edited or every incidental exported fact is unchanged.
The original actual source remains untouched. No canonical module/release or
moving-kernel-wide acceptance claim.

## Evidence

[Receipt](evidence/round-97-2026-10-10.summary.json):16 strict files,
7 accepted/9 Normal rejections, all promoted paths rerun with matching exit,
Normal envelope and null session error. Actual mathematical source and fixed
binary identities recorded; snapshot from successful round88 build reused.
Cold files own deletion evidence. The broad coordinate/scalar deletion control
is relabeled with its exact removed set; no parse error is counted as a verifier
miss. Same source family as Parts116–124, not independent general-rule promotion.
No canonical/kernel edits, trust, new bt, performance or global-minimum claim.

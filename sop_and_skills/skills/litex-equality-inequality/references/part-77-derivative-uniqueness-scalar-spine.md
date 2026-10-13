# Part 77 — Positivity, common radius and sample point in derivative uniqueness

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Actual source and retained conditions

The ODE showcase's derivative uniqueness proof assumes distinct real slopes
inside its outer contradiction. It chooses a positive error tolerance from
their separation, a common positive radius, and a nearby point. These probes
isolate those exact scalar substeps, preserving distinct slopes and positive
radius inputs. They do not verify the whole uniqueness theorem or showcase.

## Replace the nested positivity contradiction by one nonzero bridge

The source's full positivity contradiction passes. This shorter claim also
passes independently:

```litex
claim:
    ? forall slope1,slope2 R:
        slope1!=slope2
        =>:
            abs(slope1-slope2)>0
    slope1-slope2!=0
```

The bare positivity target misses cold. Thus keep the meaningful difference-
nonzero bridge; the existing absolute positivity rule then supplies the target.
Do not duplicate that forward magnitude rule or infer direct support from the
warm Session after its original universal theorem has been accepted.

## Error tolerance typing: preserve two mathematical bridges

The source's two carrier/order echoes before its binding can be deleted:

```litex
slope1-slope2!=0
abs(slope1-slope2)>0
have epsilon R+=abs(slope1-slope2)/3
```

This three-statement body passes in the full isolated distinct-slope claim.
Direct quotient-positive typing and the claim publishing only difference-
nonzero miss cold; the two mathematical facts suffice even without the binding
when the target is merely positive membership. Original five-statement typing
spine passes too. Do not erase a needed argument positivity fact just because
the derived real-typing echo is removable.

## Common radius: constructor membership already works

Both `min(delta1,delta2) in R+` and
`finite_set_min(union({delta1},{delta2})) in R+` pass from positive inputs.
Both typed-binding claim controls also pass. For the finite source spelling,
the original subset/member/real-member chain before this binding is removable:

```litex
have radius R+=finite_set_min(union({delta1},{delta2}))
```

This is positive carrier/binding acceptance. It does not repair every nested
finite-extremum comparison WD from Part72. Native min's two immediate operand
bounds pass independently; no corresponding blanket finite-wrapper bound
claim or full downstream consumer is inferred here.

## Sample point: a tested three-statement error route

With x0 real and radius positive, the tested literal sample-expression route is:

```litex
claim:
    ? forall x0 R,radius R+:
        abs((x0+radius/2)-x0)<radius
    0<=radius/2
    (x0+radius/2)-x0=radius/2
    abs((x0+radius/2)-x0)=abs(radius/2)=radius/2<radius
```

Direct absolute equality, distinctness and strict-radius targets miss.
Publishing only the difference equation and abs chain fails specifically at
`abs(radius/2)=radius/2`; its preceding congruence link passes. The explicit
nonnegative-half fact repairs both equality and strict-error variants. This
localizes a sign consumer, not a generic failure of abs congruence.

Sample distinctness separately passes after `0<radius/2` and
`x0+radius/2>x0`; the positive-half fact alone is insufficient in the tested
claim. No combined minimal proof, actual named-sample alias integration or
automatic strict-to-weak half-sign bridge is claimed by these separate probes.

## Negatives and scope

Omitting distinct slopes cannot imply positive separation. Nonnegative radius
inputs cannot guarantee a positive minimum. A minimum need not exceed its
first operand. All three false controls reject. Keep the original positive
and nondegenerate conditions; no trust or convenient additional premise is used.

Existing forward absolute/nonzero and positive-minimum support should be reused.
Any consumer nomination must distinguish direct search misses from required
mathematical value/sign steps, retain actual guard evidence and inherited
permissions, and avoid global unfolding/search changes. No kernel implementation
is authorized or made by this card.

## Evidence

[Round37 receipt](evidence/round-37-2026-10-09.summary.json):26 unique cold strict files,
14 accepted/12 rejected, promoted copies independently rerun. Fresh release
build and immutable snapshot identity, literal sources and full output retained.
Warm Session25852 remains on round29 snapshot; cold gates own capability and
deletion results. Exact source: the maintained ODE showcase derivative uniqueness
positivity/radius/sample spine. No canonical/kernel/AST/Env edit, whole-theorem,
trust-removal or runtime claim.

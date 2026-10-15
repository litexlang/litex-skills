# Part 78 — Four sample-point statements support both guards and a quotient

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Actual source and joint acceptance

Derivative uniqueness in the maintained ODE showcase defines
`sample=x0+radius/2` with x0 real and radius positive. Its later derivative
guard needs sample!=x0 and its error guard needs abs(sample-x0)<radius. The
following quotient declaration then needs a nonzero denominator and a
real-valued callable. This round tests all these consumers, not just one error
bound in isolation. Inputs, sample equation and function domain are preserved.

## Checked short spine: source eight statements to four

```litex
thm nearby_sample:
    ? forall x0 R,radius R+,sample R:
        sample=x0+radius/2
        =>:
            sample!=x0
            abs(sample-x0)<radius
    0<radius/2
    sample=x0+radius/2>x0
    sample-x0=radius/2
    abs(sample-x0)=abs(radius/2)=radius/2<radius
```

The actual task-specific theorem name is in
[the runnable four-statement file](evidence/round-38-cases/joint-five-delete-nonnegative.lit).
The original eight-statement and five-statement variants pass too. The
explicit `0<=radius/2` in the five-statement variant is removable after the
positive-half fact; do not turn Part77's independently tested nonnegative-half
bridge into a permanent extra echo in this combined context.

The named joint bodyless target, the separate direct error/distinctness targets,
positive-half deletion and final abs-fold deletion all miss cold. A different
four-statement route recording only sample-x0>0 fails its sample!=x0 conclusion.
Keep the actual point-order bridge needed by this checked joint route; proof
length alone does not establish equivalent evidence consumption.

## Downstream: actual declaration-flow quotient carrier

A fresh independent file declares arbitrary x0, positive radius, and
f in fn(t R)R; binds sample to the exact source expression; runs the four
statements; then successfully checks the source-shaped declaration:

```litex
have r38_quotient R=(r38_f(r38_sample)-r38_f(r38_x0))/(r38_sample-r38_x0)
```

[Full four-statement declaration flow](evidence/round-38-cases/quotient-four-order-flow.lit)
retains every declaration, function carrier and name. Original and five-
statement flows pass. Omitting all point facts fails quotient WD. The alternate
difference-positive four-statement flow also types the quotient despite failing
the explicit joint distinctness theorem: these are different target consumers.
Do not claim that quotient WD acceptance automatically publishes every
logically equivalent point relation for derivative-predicate guards.

## Negatives, limits and next consumer

At radius0 the defined sample equals x0, so nonzero point distance is false and
rejects. The chosen distance is exactly radius/2, so a strict error bound below
radius/2 is false and rejects. Positive radius and the real-valued function
carrier are not optional assumptions. No extra source premise or trust is used.

This is joint scalar and actual quotient carrier acceptance. It does not yet
verify derivative_delta_controlled applications, the final slope contradiction,
the whole uniqueness theorem or showcase. Any future inference nomination
must preserve real WD, actual alias/order/sign evidence and their citations;
no global rewrite/search or protected-owner change is authorized by the scan.

## Evidence

[Round38 receipt](evidence/round-38-2026-10-09.summary.json):19 unique cold strict files,
8 accepted/11 rejected; promoted copies independently rechecked with a fixed
fresh release binary. One root-indented author flow error is separately
[excluded](evidence/round-38-authoring-errors.summary.json); it did not kill the live
Session or establish a kernel miss. Corrected sources own acceptance.
Warm Session25852 on round29 snapshot accepts deletions that fail cold; cold
files alone determine liveness. Exact source hash/adaptation retained. No
canonical/kernel/AST/Env edit, whole-theorem or runtime claim.

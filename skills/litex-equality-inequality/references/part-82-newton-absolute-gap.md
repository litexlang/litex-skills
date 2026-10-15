# Part 82 — Two statements prove the actual Newton absolute-gap identity

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source target and retained dependencies

The numerical-analysis showcase's one-step gap theorem has positive input x
and target4*x^2*|residual(newton(x))|=|residual(x)|^2. Use the accepted short
positive update definition, residual identity and nonnegative residual theorem
from Part81 as the actual prefix. Their functions/domains and conclusions are
unchanged; namespace renaming only. No recursive iterate or final bound is used.

## Positive: source ten statements to two

This two-statement body passes independently with the full short prefix:

```litex
release thm r42_newton_sqrt_two_residual_nonnegative(x)
4*x^2*|r42_square_root_two_residual(r42_newton_sqrt_two(x))|=4*x^2*r42_square_root_two_residual(r42_newton_sqrt_two(x))=r42_square_root_two_residual(x)^2=|r42_square_root_two_residual(x)|^2
```

[Full runnable two-statement slice](evidence/round-42-cases/gap-sign-call-chain.lit)
contains every upstream definition/proof. The original ten-statement gap proof,
three-statement identity-plus-sign-call proof and explicit abs-fold variant
also pass. The separate identity call can be deleted: its exact middle equality
is checked using the already defined identity interface, not an added assumption.
Its theorem remains in the prefix; this is not an identity-dependency deletion.

Real-carrier echoes, repeated nonnegative conclusions, reverse zero-bound echo
and separate abs-square identity are unnecessary in this combined target.
The absolute conversion remains a meaningful step. Two theorem calls without
the final chain, nonnegative call alone and a bodyless theorem miss cold.
Identity call plus the chain without publishing the sign theorem also misses.
Keep the actual sign evidence needed for folding the new residual magnitude.

## Existing absolute-square support and an independent scalar control

The source's `|residual(x)|^2=residual(x)^2` is already supported by the direct
real interface `forall a R: |a|^2=a^2`; do not add duplicate absolute-square
mathematics or teach a mandatory real-type echo for every call.

For arbitrary real a,b,p with b>=0 and p*b=a^2, the corresponding direct scalar
gap identity still misses. This tested two-statement claim body repairs it:

```litex
|b|=b
p*|b|=p*b=a^2=|a|^2
```

This is an independent value/sign consumer control, not a new premise in the
Newton source. The source complete chain can check its abs-fold link inline;
do not extrapolate one consumer's publication requirements to all expressions.

## Negatives and scope

Without b>=0, arbitrary p can be negative: p=-1,b=-1,a=1 satisfies p*b=a^2
but refutes p*|b|=|a|^2. That executable control rejects. A Newton coefficient3
instead of4 makes the generic gap identity false and rejects. x=0 is an
undefined denominator and rejects, not a true unsupported arithmetic goal.
Positive x and the real residual/update domains are preserved.

These are explicit authoring improvements using existing interfaces. No broad
absolute rewriting, arbitrary intermediate discovery or new kernel rule is
implemented or justified solely by the scalar direct miss. Retain exact sign,
function/domain and identity evidence in any future bounded consumer audit.

## Evidence

[Round42 receipt](evidence/round-42-2026-10-09.summary.json):14 unique cold strict files,
6 accepted/8 rejected, all promoted files rerun on the fixed fresh binary.
Every gap file includes the combined short Part81 constructor/identity/sign
prefix, so real downstream composition is checked. Exact source hash retained.
Warm Session25852 on round29 snapshot accepts bodyless/call-only variants after
earlier gap theorem publication; cold files determine capability/deletion.
No canonical/kernel/protected-owner edit, trust, whole recursion/extractor/
numerical showcase or runtime claim. Next check the actual contraction and
positive-step bound consumers before claiming a full iterative estimate.

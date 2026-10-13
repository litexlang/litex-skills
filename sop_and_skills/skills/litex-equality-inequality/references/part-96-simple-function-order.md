# Part 96 — Actual simple-function order endpoints need no value chain

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and scope

High-school chapter04 defines identity(x)=x, neg_identity(x)=-x and
constant_five(x)=5 on R. Its weak/strict order blocks expose function values
in chains and then state the central comparison. This card checks those exact
source forms and separately checks central-comparison-only use probes. It does
not remove public source conclusions, imported HighSchoolCite properties, or
inverse/range interfaces from the canonical chapter.

## Positive: direct central comparisons from definitions alone

With only the three function definitions, these forms pass independently:

```litex
forall x,y R:
    x<=y
    =>:
        r56_identity(x)<=r56_identity(y)

forall x,y R:
    x<=y
    =>:
        r56_neg_identity(y)<=r56_neg_identity(x)

forall x,y R:
    x<y
    =>:
        r56_neg_identity(y)<r56_neg_identity(x)
```

[Identity endpoint](evidence/round-56-cases/identity-endpoint-definitions-only.lit),
[weak negative endpoint](evidence/round-56-cases/negative-weak-endpoint-definitions-only.lit),
[strict negative endpoint](evidence/round-56-cases/negative-strict-endpoint-definitions-only.lit).
The original chain-plus-comparison forms also pass. If the intended result is
the comparison alone, the value chain is unnecessary in these exact simple
functions. Both earlier source-wide value publications are also unnecessary
for these independent endpoints. This is not a general rule for complicated
named function bodies; previous cards retain live value/coordinate bridges.

The constant function's two weak comparisons also pass without its source
value chain or any separate value publication:

```litex
forall x R:
    r56_constant_five(x)<=r56_constant_five(0)
    r56_constant_five(0)<=r56_constant_five(x)
```

[Constant consumer](evidence/round-56-cases/constant-comparisons-definitions-only.lit).
Keep both mathematical comparison goals if both are required; do not delete
one simply because constancy makes them equivalent. No standalone library
monotonicity predicate fold was verified here.

## Negatives and evidence

Weak x<=y does not imply a strict identity comparison; x=y refutes it.
Reversing the negative function's decreasing order is false for x<y. Strict
comparison between two constant-five values is false. All three reject in
independent files. No premise, domain or function body was changed for acceptance.

[Round56 receipt](evidence/round-56-2026-10-09.summary.json):15 current-source strict files,
12 accepted/3 rejected; promoted paths rerun on the fixed fresh release snapshot.
Source hash and warm journal retained. Initial current builds failed in unrelated
concurrent compiler result references/match arms; historical round55 observations
were kept as draft evidence only. The later successful build completed before
snapshot/file gates. These fresh outcomes supersede the integration block, not
by assuming that an old binary represented current source. Warm Session99217
still uses the older round51 executable and is explicitly labeled.
No canonical scripts/kernel/protected-owner/trust edit, whole chapter or timing
claim. Next inspect actual nested identity/range consumers separately, retaining
any source false-claim or callable-domain findings instead of hiding them.

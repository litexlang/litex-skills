# Part 109 — Actual group proofs: a concrete inverse law and one chain

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source interfaces and mathematical moves

The abstract-algebra showcase contains a flat GroupSetting predicate with
associativity, two identity laws and two inverse laws on an arbitrary nonempty
carrier A. Preserve this existing source interface, its parameters and laws;
do not replace it with real multiplication or redesign it during a proof audit.
This source slice does not validate all later abstract-algebra theorems.

For left cancellation, apply inv(a) on the left. For inverse uniqueness,
insert the right inverse of a and associate the known product mul(b,a)=one.
Both original two-fact proofs pass independently.

## Checked concise inverse proof

```litex
thm group_inverse_unique:
    ? forall A nonempty_set, mul fn(x,y A) A, one A, inv fn(x A) A, a,b A:
        $GroupSetting(A,mul,one,inv)
        mul(b,a)=one
        =>:
            b=inv(a)
    mul(a,inv(a))=one
    b=mul(b,one)=mul(b,mul(a,inv(a)))=mul(mul(b,a),inv(a))=mul(one,inv(a))=inv(a)
```

[Full source with GroupSetting declaration](evidence/round-70-cases/inverse-source.lit).
The source cancellation proof analogously publishes mul(inv(a),a)=one and
uses one chain from b through inv(a)*a*b and inv(a)*a*c to c.
[Complete cancellation source](evidence/round-70-cases/cancel-source.lit).
Avoid expanding these chains into a waterfall of associativity facts.

## Deletion and explicit-definition boundary

Deleting the concrete inverse-law fact makes each chain fail at adjacent
index1: mul(one,b)=mul(mul(inv(a),a),b) for cancellation, or
mul(b,one)=mul(b,mul(a,inv(a))) for inverse uniqueness. The first identity
edge already passes. Do not describe the whole group interface as unavailable.

Replacing the concrete fact with `by def $GroupSetting(A,mul,one,inv)` does
not repair either theorem. That action succeeds, but proof-body index1—the
following chain—still fails at the same adjacent edge. Opening the universal
laws alone does not substitute for the tested concrete value publication in
these nested expressions. Internal cause remains unestablished.
[Inverse definition-action probe](evidence/round-70-cases/inverse-by-def-and-chain.lit).

Empty-body cancellation and inverse theorems also miss. The source identity
uniqueness proof `identity=mul(one,identity)=one` passes; deleting that chain
does not. No shorter accepted body was found in these bounded probes, and no
global minimality is claimed.

## Negative controls and scoped follow-up

Changing cancellation's conclusion from b=c to b=one rejects. Omitting
GroupSetting from inverse uniqueness rejects, as does omitting mul(b,a)=one.
These missing-law/premise statements are false in general, distinct from the
valid-but-unsupported chain-only forms. Existing source mathematics and all
generic carrier assumptions are retained for the accepted routes.

If investigating automation later, inspect how a known universal law's
instance is consumed inside an outer mul call. The bridge here is a concrete
law value, not a new mathematical axiom. No new bt is proposed or implemented
from this one source family; the separately excluded scalar-cancellation
candidate is not reintroduced by this audit.

[Receipt](evidence/round-70-2026-10-09.summary.json):14 strict files,
4 accepted/10 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source hash/build log
retained. Session66922 remains on round68; it accepted the exact GroupSetting
declaration and renamed original inverse theorem. Cold round70 owns deletion
and negative evidence. No canonical source, kernel, trust, protected owner,
performance or whole-showcase claim.

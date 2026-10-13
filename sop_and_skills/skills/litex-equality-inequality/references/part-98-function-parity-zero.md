# Part 98 — Actual function parity and zero equations: endpoints and a local bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and scope

High-school chapter04 defines identity(x)=x, square(x)=x^2 and shifted_zero(x)=
x-2. Its equations precede imported HighSchoolCite odd_fn/even_fn/zero_of folds.
This card checks the exact equations with those definitions and candidate short
forms. It does not include or claim acceptance of the imported predicate folds
or the whole registered chapter. All function domains remain R.

## Positive: even square and a numeric zero have direct endpoints

The source square(-x)=(-x)^2=x^2=square(x) and shifted_zero(2)=2-2=0 chains
pass. Their direct forms also pass independently:

```litex
forall x R:
    r58_square(-x)=r58_square(x)

r58_shifted_zero(2)=0
```

[Square endpoint](evidence/round-58-cases/even-direct.lit),
[zero endpoint](evidence/round-58-cases/zero-direct.lit).
These remove intermediate equality states, not statements. No extra value,
real-carrier, sign or type publication is needed for these exact consumers.

## Isolated identity oddness needs one local value fact

The isolated source identity(-x)=-x=-identity(x) and bare endpoint both miss
under the fresh binary with only these definitions. This same mathematical
equation checks with one proof-body statement:

```litex
claim:
    ? forall x R:
        r58_identity(-x)=-r58_identity(x)
    r58_identity(x)=x
```

[Complete local-value proof](evidence/round-58-cases/odd-local-value-only.lit).
The version with that value plus the original chain also passes, so the chain
can be deleted from the claim body. Publishing forall identity(x)=x globally
before the bare endpoint does not repair it; the local fact is the demonstrated
bridge. Do not infer an internal cause, general odd-function rule, or permanent
obligation to echo function values. This is a repair of the isolated equation
route, not a claim that the full imported chapter had the same failure.

[Combined local odd claim plus direct even/zero equations](evidence/round-58-cases/combined-local-odd-direct-even-zero.lit)
passes independently with the unchanged definitions. The combined all-bare
candidate misses at oddness; its failure is not an even/zero consumer defect.

## Mathematical negative controls

Identity is not even, square is not odd, and shifted_zero(3) is not0. Those
three positive false assertions reject. No changed definition, nonzero-input
restriction or trusted fact was introduced to obtain positive results.

## Evidence and build boundary

[Round58 receipt](evidence/round-58-2026-10-09.summary.json):14 current-built strict files,
7 accepted/7 rejected; every promoted path rerun with the fixed fresh release
snapshot. Initial builds failed in unrelated compiler FunctionSpace result
references; historical round57 observations remained draft-only. Build77204
subsequently completed, and all14 probes reran before promotion. Source hash,
exact build log and labeled warm journal retained. Session99217 still uses
older round51 executable; cold current files determine these outcomes.
No canonical scripts/compiler/kernel/protected-owner/trust edit, imported
predicate, whole-chapter or performance claim. Next source family: plane-vector
numeric and commutativity equations with exact cart(R,R) coordinate interfaces.

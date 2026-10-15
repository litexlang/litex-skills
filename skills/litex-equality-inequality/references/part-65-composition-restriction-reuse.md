# Part 65 — Use existing composition and restriction interfaces directly

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and current support

The topology showcase declares composition(x A)=g(f(x)) and restricted(x K)=f(x)
under the original complete function signatures and K in power_set(X). Both
exact template declarations are retained in every
[round-25 original probe](evidence/round-25-cases/restriction-value-original.lit).

## Positive: direct value equation

```litex
forall X,Y set,f fn(x X) Y,K power_set(X),p K:
    \restricted<X,Y,f,K>(p)=f(p)
```

This passes cold with the exact declarations. The original proof separately
states the restriction type, f(p) type, restriction(p) type, template/lambda
equality and the final value equation. All five body statements are removable
for this isolated interface. Preserve a source-facing named theorem when it
has callers; the finding concerns its proof body, not deletion of the theorem.

Composition likewise checks directly:

```litex
forall A,B,CarrierC set,f fn(x A) B,g fn(y B) CarrierC,p A:
    \composition<A,B,CarrierC,f,g>(p)=g(f(p))
```

Both exact function-space membership facts also pass without the original
fn_set_member call. This does not establish release/caller liveness in the
whole topology module, which was not run.

## Negatives and distinct interfaces

Replacing g(f(p)) by f(g(p)) is false even with both functions on R; take
f(x)=x+1 and g(x)=2*x at p=0. Dropping p in K from a restricted call is invalid.
An empty restriction has the checked fn(x {}) R type but cannot be called at
zero. All corresponding independent controls reject.

The complete function identity restricted-to-R=f needs the tested explicit
by fn_extension proof; its pointwise equation alone already passes directly.
Empty graph and generic result alias consumers have separate gaps in Part 66.
No new primitive composition/restriction rule is justified by these positives.

## Evidence

[Round 25 receipt](evidence/round-25-2026-10-09.summary.json), original and direct
type/value cases. Source signatures and conditions are unchanged; no trust,
canonical edits, full-module or speed claim.

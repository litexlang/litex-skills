# Part 72 — Finite singleton unions versus nested extremum WD

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and existing direct support

The preceding legacy interval-intersection consumer needs real extrema of
two singleton unions. Finite union closure is independently justified and
already works without new premises:

```litex
forall a,c R:
    $is_finite_set(union({a},{c}))
```

The following carrier goal also passes cold, as does a bodyless named theorem
with that target. Minimum typing has the same positive result:

```litex
forall a,c R:
    finite_set_max(union({a},{c})) $in R
```

Both-finite generic union closure, singleton finiteness and an explicit
singleton-finiteness claim are checked. Concrete declaration flow publishing
the finite facts before using the maximum also passes. No duplicate union
closure bt or trusted closure axiom is justified by this evidence.

## Preserve the source representation and premises

Replacing the union by a display is not a premise-free repair:

```litex
forall a,c R:
    $is_finite_set({a,c})
```

This fails; the inspected list-set WD owner requires pairwise `!=`. The
variant with the genuine extra premise `a!=c` passes. The original interval
theorem permits equal endpoints, so adding that premise would change it.
Even `a!=c => union({a},{c})={a,c}` misses in this snapshot; do not assert
that display conversion supplies a tested shortcut. List-set finiteness has
an intrinsic builtin after WD, which is distinct from object WD itself.

## Remaining nested consumer gap

The exact source consumer target excerpt remains:

```litex
finite_set_max(union({a}, {c})) <= z
z <= finite_set_min(union({b}, {d}))
```

Publishing the proven generic union-finiteness fact before the exact original
source slice does not repair it. Publishing the proven generic max/min real
carrier facts as well still fails. The first failure remains goal WD and its
finite-union requirement, before the original proof body executes.
Generic guarded maximum bounds and their named-theorem variant also miss.
Thus the shallow carrier positive does not establish nested comparison WD.

The inspected requirement owner verifies each atomic requirement's WD then
truth using the supplied VerifyState; max/min retain finite, nonempty and
real-valued obligations. These owner observations do not establish which
permission, recursion or context boundary causes the full failure. Next audit
that boundary with exact evidence rather than increasing global search or
inserting redundant theorem premises. No kernel/AST/Env change is authorized
by this evidence card.

## Negatives and evidence

An arbitrary set unioned with a finite one need not be finite; that target
rejects. Empty-set maximum typing rejects, and a displayed maximum is not
always at most one chosen input. The latter symbolic display control also
hits missing distinctness WD, so it is not evidence of a reached false-bound
truth check. Numeric union-size equality misses and is a true unsupported
goal; it is not classified as mathematically false.

[Round 31 receipt](evidence/round-31-2026-10-09.summary.json): 27 unique strict files,
11 accepted and 16 rejected; promoted copies rerun with immutable fresh release
snapshot. Owner hashes, actual sources and full Normal failures are retained.
Iteration Session 25852 uses round29 snapshot; cold results alone establish
recorded capability. No source textbook/kernel edits, new trust, full repair,
complete downstream acceptance or performance claim.

## Round 32 refinement: comparison-domain requirement ceiling

Independent cold files distinguish equality from comparison on the exact same
maximum. The reflexive equality below passes, including a bodyless named
theorem; its weak-order variant fails during named-theorem goal WD:

```litex
forall a,c R:
    finite_set_max(union({a},{c}))=finite_set_max(union({a},{c}))
```

Diagnostic premise controls locate successive missing obligations. Adding only
finite union status moves the first failure to nonempty status. Adding both
moves it to the real-subset requirement. Adding all three allows the reflexive
weak order. A known real-carrier premise also repairs that diagnostic target.
Those premises are NOT a suggested change to the original source theorem.
Putting the same bridges inside its claim body fails preflight before the
body runs. Standalone finite, nonempty and real-subset targets already pass.

The inspected predicate-domain owner contains:

```rust
let domain_state = verify_state.capped_at(VerifyStateLevel::BuiltinRule);
let result = self.verify_fact(&requirement, domain_state)?;
```

The finite union constructor lives in the Strategy owner and delegates both
finite-child requirements through the bounded strategy verifier. Object WD
for max/min still requires finite, nonempty and real-valued evidence. This
locates a relevant permission boundary that agrees with the nested failure;
it does not authorize resetting the ceiling or claim a repaired causal path.
Any proposed use of already checked parent evidence must preserve citations
and the inherited contract; do not change global permissions to close one case.

Singleton maximum typing passes, while `a<=finite_set_max({a})` fails at truth
search in the named control rather than at the union's finite requirement.
Keep that separate from the nested union WD diagnosis. Singleton cardinality
reflexive order passes; union cardinality reflexive order needs finite status.
False strict self-order with all requirements and nonreal maximum controls
reject. No new rule or source mathematics modification has been made.

[Round 32 receipt](evidence/round-32-2026-10-09.summary.json) records 25 unique strict
files and promoted rechecks, 12 accepted/13 rejected, with named phase controls,
owner hashes and the fresh executable snapshot. The release build completed
after a shared Cargo lock wait. Iteration retained live Session 25852 on the
round29 binary; capability results use the independent round32 binary.
Next test native scalar max/min formulations of the source mathematics, without
claiming that equivalent source spelling repairs the exact legacy expression.

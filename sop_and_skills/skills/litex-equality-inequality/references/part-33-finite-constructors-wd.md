# Part 33 — One-sided finite intersections and constructor WD

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

An intersection is finite if either operand is finite; a difference A\B is
finite if A is finite; a union generally needs both finite operands.
Anchors: finite subset/size examples and combinatorial set-size consumers.

## One-sided positive route

```litex
claim:
    ? forall A finite_set,B set:
        $is_finite_set(intersect(A,B))
    $is_finite_set(A)
    intersect(A,B) $subset A
```
Passes. Direct left-finite and right-finite intersection targets both miss.
Both-finite intersection closure passes directly. Difference closure with
only finite left operand already passes; no duplicate rule needed.

## Constructor property versus WD use

```litex
forall A,B finite_set:
    $is_finite_set(intersect(A,B))
    $is_finite_set(set_minus(A,B))
    $is_finite_set(union(A,B))
```
Each individual family was checked independently and passes. In contrast,
direct cardinality comparisons containing these constructed sets miss;
the intersection/difference claim attempts fail preflight at their finite-set
WD requirement before proof-body subset statements run.
Publishing finiteness before use in a declaration-flow control passes.
This does not mean the finiteness facts are missing mathematically.

## Negatives and recommendations

No finite operands implies no finite intersection guarantee: A=B=N refutes it;
the variant rejects. A finite union with arbitrary second operand is also
false, at A={},B=N; that variant rejects.

Add the missing one-sided intersection constructor support, preserving an
actual finite-operand proof. Separately audit existing constructor-finiteness
proof availability in WD instead of adding duplicate closure axioms or changing
theorem statements to require redundant finiteness. Do not use union's rule
with only one finite input.

## Evidence

[Round 10 receipt](evidence/round-10-2026-10-08.summary.json), finite closure and
one-sided cases, size declaration-flow/preflight controls. Current working-tree
release, strict independent files, 2026-10-08. No kernel edits.

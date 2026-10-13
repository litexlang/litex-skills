# Search round 22 — anonymous application atoms in arithmetic

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


25 independent strict files: 11 accepted, 14 rejected. This round removes
finite-product expansion from round 21's anonymous-call consumer observation.
The same verified selected-scalar snapshot and source-manifest limits apply:
the current worktree still cannot build because of unrelated compiler changes.

## Recommendation: inspect the earlier alpha/atom boundary

```litex
forall c,d R,m Z:
    fn(k Z) R {c}(m)*d=d*fn(k Z) R {c}(m)
```

Even this pure commutative calculation misses. Named `f(m)*d=d*f(m)` passes,
and standalone alpha equality of two equivalent anonymous applications passes.
A read-only parser/normalizer probe exposes:

```text
left IR:  fn (#4#k Z) R{#1#c}(#3#m) * #2#d
right IR: #2#d * fn (#5#k Z) R{#1#c}(#3#m)
rational normalization: false
```

`rational_expression::helper::obj_key` uses `obj.ir().display_string()`, and
monomial collection retains those keys for opaque atoms. Distinct inner binder
IDs therefore distinguish alpha-equivalent applications in this isolated
calculation. The existing structural alpha comparator handles these heads,
but that alone does not canonicalize their algebraic keys.

Inspect binder-aware algebraic atom equivalence before adding a formula-specific
product rule. Preserve free captured identifiers, argument groups, carrier and
guard structure. No stripping names/IDs globally, beta-body search or AST/Env
changes are authorized. Whether this same boundary explains every stored-value
consumer still needs a checked repair and replay; no such repair is claimed.
[Part 62](part-62-anonymous-arithmetic-atoms.md).

## Checking and negative boundaries

Known anonymous-call values still fail under multiplication, scaling and
addition in the tested direct forms. Generic checked scalar congruence or
commutativity theorem calls prove the exact scaled/product/commutative targets.
Those interfaces are diagnostic proof routes, not proposed permanent authoring
scaffolding. Direct callback beta equality and zero multiplication already pass.

Wrong result, different free captures, different arguments and invalid-domain
controls reject. Identity lambdas without free captures also show the direct
product miss; it is not solely a captured-variable phenomenon.

[Receipt](evidence/round-22-2026-10-09.summary.json), complete `evidence/round-22-cases/`,
and the read-only Rust probe/output preserve source correspondence and commands.
The Rust introspection is not counted as a Litex proof file. A reserved-name
`e` parser error is excluded; the Session restarted and replayed 26 accepted
statements, then corrected the variable spelling. No kernel/canonical edits,
new trust, runtime claim or complete causal repair.

Next: further binder-bearing atoms and known-equality consumers, using held-out
callers and free-variable/domain controls; current-source recheck when the
worktree compiler is buildable.

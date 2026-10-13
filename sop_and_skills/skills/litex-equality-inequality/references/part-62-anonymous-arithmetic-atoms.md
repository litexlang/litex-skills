# Part 62 — Alpha-equivalent anonymous calls as algebraic atoms

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and source

Round 21's two-factor anonymous callback calculation missed even after both
call values were stated. Before nominating another product rule, isolate pure
arithmetic on those calls from fold expansion and from function evaluation.

## Direct misses versus existing support

```litex
forall c,d R,m Z:
    fn(k Z) R {c}(m)*d=d*fn(k Z) R {c}(m)
```

This commutative target misses. In contrast, named `f(m)*d=d*f(m)`, anonymous
call beta equality, zero multiplication and standalone alpha equality pass.
The direct distribution and value-substitution targets also miss, including
identity lambdas without free captures and closed indices.

## Checked same-target proof route

This complete diagnostic interface and author pass independently:

```litex
thm scalar_commutative_probe22:
    ? forall lhs,rhs R:
        lhs*rhs=rhs*lhs

claim:
    ? forall c,d R,m Z:
        fn(k Z) R {c}(m)*d=d*fn(k Z) R {c}(m)
    by thm scalar_commutative_probe22(fn(k Z) R {c}(m),d) => fn(k Z) R {c}(m)*d=d*fn(k Z) R {c}(m)
```

Checked generic one-factor and two-factor congruence interfaces likewise repair
the exact targets with known callback-value premises. These show explicit
checkability; do not prescribe extra helper theorems for routine arithmetic.

## Earlier boundary exposed by read-only inspection

The parser assigns separate bound IDs to the repeated lambda parameter:

```text
fn (#4#k Z) R{#1#c}(#3#m) * #2#d
#2#d * fn (#5#k Z) R{#1#c}(#3#m)
```

The snapshot's `obj_key(obj)` is `obj.ir().display_string()`. Monomial atom
keys thus differ, and the pure rational-normalization query returns false.
Structural anonymous-call alpha equality already passes elsewhere. This is
direct evidence for the isolated algebraic-key boundary, not a completed fix
or a causal proof for all stored-value consumption misses.

## Nomination and nearest negatives

Inspect a bounded binder-aware atom comparison/canonical key that retains free
identifier identity and full domain/guard/return shape. Do not normalize away
free captures: `fn(k Z)R{c}(m)=fn(k Z)R{d}(m)` is false without c=d. Different
arguments of the identity lambda also remain distinct. Applying an N+ callback
at zero remains invalid. All three controls reject in executable files.

No global ID/name stripping, arbitrary function unfolding, recursion increase,
new AST fields or Env caches is justified by this probe. First replay pure
commutativity after any local candidate repair, then independently audit the
known-value multiplication/addition consumers and every negative boundary.

## Evidence

[Round 22 receipt](evidence/round-22-2026-10-09.summary.json),
[inspection source](../../../references/sources.md#unbundled-local-material) and
[literal IR output](../../../references/sources.md#unbundled-local-material). Proof files are
in `evidence/round-22-cases/`. The library and executable come from the exact
verified selected-scalar overlay; current-worktree build is blocked elsewhere.
No semantic edits, whole-module or performance claims.

## Current-source follow-up

Round 23's fresh current-source release rechecked all 25 round-22 files with
the same outcomes. Pointwise coordinate callbacks provide held-out beta/entry
positives and arithmetic misses, with explicit same-target repairs; see
[Part 63](part-63-pointwise-coordinate-interfaces.md). The prior worktree build
block is historical. No atom-key or equality-consumer repair was implemented.

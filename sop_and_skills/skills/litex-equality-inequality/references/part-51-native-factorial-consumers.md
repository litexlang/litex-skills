# Part 51 — Native factorial evidence at comparison consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

A factorial ratio with m<=n is at most one because numerator order and positive denominator are established native properties. Nested factorial comparison applies the same monotone operation twice. Source: factorial_order_author_routes.lit and existing factorial intrinsic-sign examples.

## Positive denominator bridge

The initial ratio chain misses at its first common-denominator comparison even after factorial(m)<=factorial(n) is published. Explicit denominator positivity repairs it:

```litex
claim:
    ? forall m,n N:
        m <= n
        =>:
            factorial(m)/factorial(n) <= 1
    factorial(m) <= factorial(n)
    factorial(n) > 0
    factorial(m)/factorial(n) <= factorial(n)/factorial(n) = 1
```

Direct factorial(n)>0 and factorial(n)>=1 already pass on N. Do not add a duplicate positivity theorem. The failed ratio chain and repaired variant are checked in the same Session and independent files.

## Nested-order context trap

The original author-routes file passes as a whole, but its later bare forall follows an identical successful claim. That does not establish independent direct support. The clean isolated target misses:

```litex
forall m,n N:
    m <= n
    =>:
        factorial(factorial(m)) <= factorial(factorial(n))
```

Publishing its inner order first passes:

```litex
claim:
    ? forall m,n N:
        m <= n
        =>:
            factorial(factorial(m)) <= factorial(factorial(n))
    factorial(m) <= factorial(n)
    factorial(factorial(m)) <= factorial(factorial(n))
```

Independent files are authoritative; a later repeated target can merely reuse the earlier universal result.

## Contradiction comparison bridge

The reflected-order proof in Part 50 must expose the positive comparison arising from the negated order goal before native factorial monotonicity can consume it. The source factorial_order.rs already checks forward and reverse-written positive order premises, but this does not establish consumption of every negated-order equivalent at its inherited ceiling.

## Improvement nominations

- Inspect the common-positive-denominator consumer's access to intrinsic native scalar positivity. Reuse/cite the already supported factorial sign evidence instead of inventing another factorial sign property or reopening unrestricted parent search.
- Inspect bounded known negated-order conversion at native comparison premises. Preserve real/natural domain, exact negative/dual fact citations and current budgets; do not insert a factorial-specific exception into generic orchestration.
- Nested monotone composition may remain an explicit meaningful inner step. Its miss alone does not require broader recursion or a special double-factorial rule.

Current source/reproduction identify consumers but not complete internal causes. Nearest domain/0–1 boundary controls are in Part 50. Any actual repair needs focused producer/consumer and proof-evidence checks; no shared Runtime/AST redesign is authorized here.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 17 receipt](evidence/round-17-2026-10-08.summary.json) retains exact immutable binary identity, complete source, commands, exits, Normal JSON, synchronized Session responses and durable replay commands. Runnable cases are in `evidence/round-17-cases/`.

No kernel/canonical mathematical source edits, trust, whole-textbook gate or performance claims. Cases are dated interface evidence and nominations, not implemented enhancements or universal authoring requirements.

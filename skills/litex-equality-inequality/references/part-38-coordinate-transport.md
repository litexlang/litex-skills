# Part 38 — Coordinate equality and midpoint transport

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and proof idea

For two real pairs, corresponding coordinates determine the pair. For equal midpoints, multiply each midpoint coordinate equation by two and cancel the shared terms. Source anchor: `showcases/math_concepts_in_litex/15_coordinate_geometry_case_study/main.lit:3115`.

## Positive: existing interfaces

One reconstruction chain passes:

```litex
claim:
    ? forall p,q cart(R,R):
        p(1) = q(1)
        p(2) = q(2)
        =>:
            p = q
    p = (p(1),p(2)) = (q(1),q(2)) = q
```

The native theorem also passes after explicit finite enumeration:

```litex
claim:
    ? forall p,q cart(R,R):
        p(1) = q(1)
        p(2) = q(2)
        =>:
            p = q
    by enumerate finite_set:
        ? forall coordinate_index 1...2:
            p(coordinate_index) = q(coordinate_index)
    release thm tuple_equal_from_coordinates(p,q)
```

Literal tuple constructor equality, reconstruction and projections from pair equality already pass; do not propose duplicate rules for those supported forms.

## Ideal direct form and capability gap

The following true direct statement fails in search:

```litex
forall p,q cart(R,R):
    p(1) = q(1)
    p(2) = q(2)
    =>:
        p = q
```

Calling `release thm tuple_equal_from_coordinates(p,q)` alone in a claim also fails: its universal coordinate premise is not established from the two separate facts automatically. This is an interface-consumption boundary, not an absent tuple theorem.

## Actual long-chain authoring opportunity

A reduced midpoint scalar interface passes as one chain:

```litex
claim:
    ? forall a,c,d,f R:
        (a+d)/2 = (c+f)/2
        =>:
            a-c = f-d
    a-c = 2*((a+d)/2)-c-d = 2*((c+f)/2)-c-d = f-d
```

The same scalar conclusion without a proof body misses. The full extracted coordinate interface needs only two proof statements in this probe; separately asserting `m(1)=n(1)` and `m(2)=n(2)` is unnecessary:

```litex
claim:
    ? forall a,c,d,f,m,n cart(R,R):
        m = n
        m(1) = (a(1)+d(1))/2
        m(2) = (a(2)+d(2))/2
        n(1) = (c(1)+f(1))/2
        n(2) = (c(2)+f(2))/2
        =>:
            (a(1)-c(1),a(2)-c(2)) = (f(1)-d(1),f(2)-d(2))
    a(1)-c(1) = 2*((a(1)+d(1))/2)-c(1)-d(1) = 2*m(1)-c(1)-d(1) = 2*n(1)-c(1)-d(1) = 2*((c(1)+f(1))/2)-c(1)-d(1) = f(1)-d(1)
    a(2)-c(2) = 2*((a(2)+d(2))/2)-c(2)-d(2) = 2*m(2)-c(2)-d(2) = 2*n(2)-c(2)-d(2) = 2*((c(2)+f(2))/2)-c(2)-d(2) = f(2)-d(2)
```

The original geometry code separately records multiplication, simplification and subtraction for both coordinates. This reduced interface demonstrates those calculations can be combined; it does not verify replacement of the entire enclosing theorem or its downstream vector consumers.

## Negatives and boundaries

Missing second coordinate, unequal tuple lengths and two coordinates of infinite functions all reject. First two coordinates do not establish equality of arbitrary functions on `N+`. Midpoint wrong-direction conclusion `a-c=d-f` rejects; `a=1,c=0,d=0,f=1` is a counterexample.

## Improvement candidate

Optional bounded tuple-coordinate strategy: only for proven finite tuples of equal known dimension, generate each coordinate equality over the entire domain, preserve WD and each child certificate, and impose a size/cost bound. Prefer reuse of existing complete-domain/tuple interfaces; no heuristic equality from a partial coordinate sample.

Midpoint-specific bt rules are not recommended from this one source. Scalar affine cancellation overlaps earlier cancellation candidates. Existing reconstruction/finite-enumeration routes already give concise authoring.

## Evidence and scope

Date: 2026-10-08. Fresh current-worktree release build succeeded. Immutable binary identity, full commands, Normal JSON, cases and synchronized Session transcript: [round 12 receipt](evidence/round-12-2026-10-08.summary.json). Each case has a durable replay command. All positives require exit 0, Normal `kind: run`, `success: true`, `session_error: null`.

Earlier snapshot experiments and an unrelated failed source build are historical evidence only. This fresh build supersedes their source-correspondence limitation. No kernel or canonical geometry source was changed. No performance comparison or universal minimality claim.

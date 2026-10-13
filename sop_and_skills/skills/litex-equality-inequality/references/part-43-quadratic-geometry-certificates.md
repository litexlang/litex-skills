# Part 43 — Quadratic certificates and geometric identity reuse

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The planar identity (ac+bd)^2+(ad-bc)^2=(a^2+b^2)(c^2+d^2) is polynomial algebra. Dropping its nonnegative determinant-square term proves the squared Cauchy bound. A unit rotation preserves squared norm by factoring out c^2+s^2. Anchors: geometry main.lit:1595–1645. These are mathematical certificate choices, not function-name-based builtin facts.

## Positive: a one-chain certificate

The raw Gram polynomial identity passes directly, but the Cauchy inequality alone misses. This complete certificate passes:

```litex
claim:
    ? forall a,b,c,d R:
        (a*c+b*d)^2 <= (a^2+b^2)*(c^2+d^2)
    (a*c+b*d)^2 <= (a*c+b*d)^2+(a*d-b*c)^2 = (a^2+b^2)*(c^2+d^2)
```

Its strict form also passes, using the determinant nonzero guard:

```litex
claim:
    ? forall a,b,c,d R:
        a*d-b*c != 0
        =>:
            (a*c+b*d)^2 < (a^2+b^2)*(c^2+d^2)
    (a*d-b*c)^2 > 0
    (a*c+b*d)^2 < (a*c+b*d)^2+(a*d-b*c)^2 = (a^2+b^2)*(c^2+d^2)
```

The corresponding direct strict target misses. Supplying a meaningful nonnegative-square certificate is concise current authoring; no unrestricted sum-of-squares solver is implied.

## Rotation: direct miss, one chain passes

```litex
claim:
    ? forall c,s,x,y R:
        c^2+s^2 = 1
        =>:
            (c*x-s*y)^2+(s*x+c*y)^2 = x^2+y^2
    (c*x-s*y)^2+(s*x+c*y)^2 = (c^2+s^2)*(x^2+y^2) = 1*(x^2+y^2) = x^2+y^2
```

The same target without the chain misses. Its unit condition is essential. This is an exact reduced algebraic interface; the full point-coordinate rotation theorem was not replaced.

## Source dot/det identity: concise checked body

With the source's exact reduced definitions, direct dot(u,v)^2+det(u,v)^2=dot(u,u)*dot(v,v) misses. Four definition equalities plus one continuous chain pass:

```litex
have fn dot(u,v cart(R,R)) R = u(1)*v(1)+u(2)*v(2)
have fn det(u,v cart(R,R)) R = u(1)*v(2)-u(2)*v(1)
claim:
    ? forall u,v cart(R,R):
        dot(u,v)^2+det(u,v)^2 = dot(u,u)*dot(v,v)
    dot(u,v) = u(1)*v(1)+u(2)*v(2)
    det(u,v) = u(1)*v(2)-u(2)*v(1)
    dot(u,u) = u(1)*u(1)+u(2)*u(2)
    dot(v,v) = v(1)*v(1)+v(2)*v(2)
    dot(u,v)^2+det(u,v)^2 = (u(1)*v(1)+u(2)*v(2))^2+(u(1)*v(2)-u(2)*v(1))^2 = (u(1)*u(1)+u(2)*u(2))*(v(1)*v(1)+v(2)*v(2)) = dot(u,u)*dot(v,v)
```

The source separately records the polynomial identity, left expansion, right expansion and final equality; the reduced interface merges those into one chain. No full canonical theorem replacement/whole-module result is claimed.

## Negatives

Strict Cauchy without determinant nondegeneracy rejects (parallel or zero vectors give equality). Rotation without c^2+s^2=1 rejects (c=2,s=0,x=1,y=0). Do not strengthen an ordinary weak Cauchy statement just to use the strict proof.

## Improvement status

Polynomial identity checking and nonnegative-square shifts already suffice when the author exposes the certificate. Prefer existing dot/det theorems at callers; do not add a rule recognizing a user function called dot. A general bounded certificate checker might be useful only with a separate trigger/cost/evidence design; discovery of arbitrary squares or polynomial invariants is not justified by this one family. The concrete priority rule nomination for this round is the guarded absolute-radius strategy in [Part 42](part-42-absolute-square-radius.md).

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 14 receipt](evidence/round-14-2026-10-08.summary.json) retains immutable binary SHA-256/version, sources, commands, exits, Normal JSON, Session responses and durable replay commands. Cases are retained in `evidence/round-14-cases/`.

No trust, kernel/canonical proof edits or runtime claims. These are dated reduced interfaces; enclosing geometry replacement and downstream consumers were not checked. New strategies remain proposals, not implemented or causally diagnosed fixes.

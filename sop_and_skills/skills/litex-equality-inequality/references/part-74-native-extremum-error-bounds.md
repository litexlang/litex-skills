# Part 74 — Reuse native min/max error bounds before a calculation waterfall

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Real source and shortest checked formulation

Current Analysis Chapter9 `max_lipschitz` has a 58-statement proof body using
finite singleton-union maxima. Its native max formulation passes with no body:

```litex
thm native_max_error:
    ? forall a,b,A,B R,epsilon R+:
        abs(a-A)<=epsilon
        abs(b-B)<=epsilon
        =>:
            abs(max(a,b)-max(A,B))<=epsilon
```

The equivalent native minimum target also passes bodyless. Runnable full
source slices with task-specific names are in
[maximum](evidence/round-34-cases/chapter09-max-native-bodyless.lit) and
[minimum](evidence/round-34-cases/chapter09-min-native-bodyless.lit).
Preserve the inputs and error conditions, use native binary extrema when
that is the source mathematics, and test deleting the entire waterfall.
No global minimality or performance claim follows from source length.

Keeping all58 statements while replacing the finite maxima by native maxima
still fails at proof_body index22, `max(a,b)<=max(A,B)+epsilon`. The target
alone is already checkable by the existing magnitude rule. This is a held-out
whole-body deletion result, not merely a count of neighboring echoes.

## Exact finite-wrapper boundary and source trust

The exact Chapter9 maximum and minimum-header targets miss at WD without the
explicit finite-extremum guards. Native spelling does not repair those exact
expressions. Chapter6's two original bodyless stability theorems, with their
actual six finite/nonempty/real-subset guards, pass independently; all four
maintained min/max magnitude/weak-order examples also pass.

Chapter9's original minimum proof contains four existing trusts; this round
does not execute or modify that entire proof, remove those trusts, or claim
whole-chapter trust reduction. It checks the exact target header and a native
bodyless formulation independently, without inserting trust. Library debt and
the finite-wrapper WD gap remain separate from native rule reuse.

## Radius, orientation and nearest boundaries

Weak native error conclusions pass with strict coordinate hypotheses, with a
real radius, and at zero tolerance. The real-radius case does not license
ignoring guard consistency; its coordinate error premises imply nonnegativity.

Reversed coordinate differences miss directly, but this checked bridge works
for both minimum and maximum:

```litex
claim:
    ? forall a,b,x,y R,epsilon R+:
        abs(x-a)<=epsilon
        abs(y-b)<=epsilon
        =>:
            abs(max(a,b)-max(x,y))<=epsilon
    abs(a-x)=abs(x-a)<=epsilon
    abs(b-y)=abs(y-b)<=epsilon
```

This is a dated diagnostic route, not a permanent orientation requirement.
The true strict-coordinate-to-strict-output estimate still misses. Weak
coordinate bounds cannot imply a strict output bound; that false control
rejects. Missing one coordinate bound and a max/min mismatch reject too.
Do not merge true strict misses with false weak-to-strict controls.

The existing metric owner checks both corresponding error bounds and equal
extremum kinds. Nominate bounded reversed-error guard consumption and a strict
sibling only with both actual guard proofs and inherited permissions. Do not
duplicate the already working weak magnitude rule or expand global search.
No rule was implemented by this scan.

## Evidence

[Round34 receipt](evidence/round-34-2026-10-09.summary.json):30 unique cold strict files,
18 accepted/12 rejected, all promoted copies rerun. Source anchors/hashes and
fixed executable identity retained. A prior concurrent Lean compiler build
failure is historical; the successful recheck build supersedes it. Warm Session
25852 uses round29 snapshot and is not independent acceptance. A long native
body response crossed a later warm submission boundary; cold files determine
its recorded result. No canonical/kernel/protected-owner edits, new trust,
whole-book or performance claim.

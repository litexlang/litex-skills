# Part 73 — Native max/min for interval-intersection bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and representation choice

Legacy Analysis Chapter 11's member-bound theorem says that a point in the
intersection lies above both lower endpoints and below both upper endpoints.
Its next theorem places that point in the corresponding closed hull. Native
`max(a,c)` and `min(b,d)` express that mathematics without finite singleton
union wrappers. All original endpoint/member/domain hypotheses are retained.

This is an equivalent mathematical formulation, not a verified repair of the
exact `finite_set_max(union({a},{c}))` expression. That expression's recorded
WD gap remains in Part72. No automatic union-extremum-to-scalar bridge is
claimed. The source textbook itself was not changed.

## Four-line checked bound proof

The exact definition and shortened four-case `interval_endpoint_member_is_between`
dependency from Part71 precede this theorem in the checked file:

```litex
thm intersection_native_bounds:
    ? forall I,J power_set(R),a,b,c,d R,z intersect(I,J):
        $has_interval_endpoints(I,a,b)
        $has_interval_endpoints(J,c,d)
        =>:
            max(a,c)<=z
            z<=min(b,d)
    release thm interval_endpoint_member_is_between(I,a,b,z)
    release thm interval_endpoint_member_is_between(J,c,d,z)
    max(a,c)<=max(z,z)=z
    z=min(z,z)<=min(b,d)
```

The two releases expose four useful endpoint bounds. The chains use existing
coordinatewise max/min comparison and diagonal identities. Their cold checked
standalone claim controls preserve the same real domains. Simply switching
the ten-line legacy body to native max/min still misses its final bound, as do
two calls alone, four direct endpoint lines and a bodyless consumer.

The receipt's actual theorem names differ from the explanatory name above;
full runnable context is in
[release-form file](evidence/round-33-cases/native-release-four-lines.lit).
Both existing bare-call and release-call versions were checked. Each chain
deletion and the second-call deletion fails cold. Four lines are the tested
short route, not a global minimality or runtime claim.

## Downstream positive: closed hull with one theorem call

After the checked native bound theorem, its next source-facing target passes
with only this body excerpt:

```litex
by thm r33_native_checked(I,J,a,b,c,d,z)
```

The target is `z in '[max(a,c),min(b,d)]`. The original alias/membership and
bound echoes can all be deleted in this isolated native slice; deleting the
entire body fails cold. The theorem returns both bounds, which are genuinely
used together by the interval member consumer. The maintained file retains
the source bare-call spelling; no independent release-form hull check is claimed.

## Negatives and bounded shortcut nomination

Closed-interval members need not satisfy strict lower bounds; the false strict
intersection bound rejects. Membership in only the first interval cannot bound
the unrelated second endpoint; that control rejects. Equal endpoints remain
legal: `0 in '[max(0,0),min(0,0)]` passes, without any distinctness premise.

The true standalone shortcuts `a<=z,c<=z => max(a,c)<=z` and
`z<=b,z<=d => z<=min(b,d)` miss cold, while the explicit chains pass. A bounded
direct consumer of those actual coordinate inequalities is worth nominating;
keep real WD, both guard citations and inherited permissions. This search does
not implement it or claim it necessary for explicit checkability. Do not mix
it with the separate finite-wrapper WD gap or change global search ceilings.

## Evidence

[Round 33 receipt](evidence/round-33-2026-10-09.summary.json): 25 unique strict files,
8 accepted/17 rejected; promoted copies rerun with the immutable fresh release
snapshot. Three hull variants using an unproved two-call dependency are blocked
dependency controls, not independent hull capability misses. The three later
checked-dependency hull variants establish the actual downstream distinction.
Source path/hash and exact adaptation are recorded. Warm Session25852 accepts
some deletions after scalar lemma publication; only cold files establish liveness.
No textbook/kernel/AST/Env edits, new trust, whole-book or performance claim.

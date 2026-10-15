# Part 108 — Actual Pascal identity: retain table maps, combine the final trace

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Current preferred route: round69 removed the three mapping claims

Further liveness testing of this same source family replaces the historical
round68 nine-step route below with six immediate theorem-body statements.
The definitions, predecessor strategies, N+ binders and original premises stay
unchanged. All three mapping claims can first become direct equalities, then
those three equalities can be removed together: the remaining calculation
checks the function maps where they are actually used.

```litex
thm pascal_identity:
    ? forall n,r N+:
        r<n
        r>1
        =>:
            choose_fn(n,r)=choose_fn(n-1,r)+choose_fn(n-1,r-1)
    n-r>0
    (n-1)-r=n-r-1
    (n-1)-(r-1)=n-r
    choose_fn(n-1,r)=pascal_entry(r,(n-1)-r)=pascal_entry(r,n-r-1)
    choose_fn(n-1,r-1)=pascal_entry(r-1,(n-1)-(r-1))=pascal_entry(r-1,n-r)
    choose_fn(n,r)=pascal_entry(r,n-r)=pascal_entry(r-1,n-r)+pascal_entry(r,n-r-1)=choose_fn(n-1,r-1)+choose_fn(n-1,r)=choose_fn(n-1,r)+choose_fn(n-1,r-1)
```

[Full current source with exact declarations](evidence/round-69-cases/no-map-prepublication.lit),
[same source followed by native call](evidence/round-69-cases/no-map-prepublication-native-call.lit).
The native `release thm pascal_identity(5,2)` passes with this shorter theorem.
Removing n-r>0 from this route rejects; adding1 to the theorem conclusion
rejects. The source's two-way cases also accept empty branch bodies, including
the inconsistent branch, but keeping those cases is unnecessary here because
the direct maps and their joint deletion already pass. This does not prescribe
empty cases for unrelated goals or prove all branches may be dropped generally.

[Round69 receipt](evidence/round-69-2026-10-09.summary.json):15 strict cold files,
11 accepted/4 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Source/binary identity retained.
Session66922 remains on round68 and checked the native consumer of the already
accepted round68 theorem; it is not evidence of the new body deletion.
Rounds68/69 are one source family, not independent evidence for a permanent
agent rule. No canonical/kernel/trust changes or global-minimum claim.

## Source and mathematical proof idea

The discrete-mathematics showcase defines a recursive Pascal table and
choose_fn(n,k)=pascal_entry(k,n-k) inside the usual range, otherwise0.
Keep its three predecessor strategies, exact recursive definitions, N+
theorem binders, r<n and r>1 premises. The proof unfolds one Pascal step and
identifies its two summands with neighboring binomial coefficients.
No replacement factorial quotient or stronger premises are introduced.

[Complete shortened source](evidence/round-68-cases/combined-short-route.lit)
contains the definitions and all proof context. The original full standalone
showcase and its preceding definition prefix pass independently.

## Historical round68 checked shortening

The original theorem body has16 immediate statements:five boundary facts,
three case-based mapping claims and eight tail facts. The checked route has9:
one positive-gap fact, the same three mapping claims and five tail facts.
Retain n-r>0. Three weak-order publications and r>0 can be deleted together.
The source case claims keep their original goals and branches.

After those claims, use:

```litex
(n-1)-r=n-r-1
(n-1)-(r-1)=n-r
choose_fn(n-1,r)=pascal_entry(r,(n-1)-r)=pascal_entry(r,n-r-1)
choose_fn(n-1,r-1)=pascal_entry(r-1,(n-1)-(r-1))=pascal_entry(r-1,n-r)
choose_fn(n,r)=pascal_entry(r,n-r)=pascal_entry(r-1,n-r)+pascal_entry(r,n-r-1)=choose_fn(n-1,r-1)+choose_fn(n-1,r)=choose_fn(n-1,r)+choose_fn(n-1,r-1)
```

This is an excerpt of the linked full theorem. The last chain combines
recursive unfolding, summand transport and commutation. The separately
published recursive equation, main Pascal sum and sum-transport equality are
not necessary in this combined route. Individual source deletions of those
facts and of its final chain also pass, but only the combined cold file owns
the joint-shortening claim. This is not global proof minimality.

## Boundaries established by failed shorter files

Bare Pascal identity and an empty-body named theorem miss. Deleting both
coordinate-normalization equalities fails the second adjacent equality in
the choose_fn(n-1,r) mapping chain. A single final chain without the two
mapped-value publications fails its third adjacent equality, even if the
coordinate normalizations remain. Its recursive-unfolding edge already passes;
do not misclassify the failure as absence of recursive definition support.

Deleting all five source boundary facts fails later at the standalone
recursive equation, rather than at the earlier mapping claims. In the short
route, deleting n-r>0 also fails at recursive unfolding in the final chain.
The fact follows from the existing r<n premise; its explicit publication is
a checked consumer bridge, not a strengthened theorem assumption.

## Negative and evidence

Changing only the source theorem conclusion by adding1 to the right-hand
sum rejects while the original proof body is retained. This is a false
conclusion control, separate from true direct-target and deletion misses.
[Wrong conclusion](evidence/round-68-cases/wrong-plus-one-conclusion.lit).

[Receipt](evidence/round-68-2026-10-09.summary.json):18 strict cold files,
10 accepted/8 Normal rejections. All promoted paths rerun on the fixed
snapshot after a successful current-source release build. Exact source hash
and build log retained; no timeout or parser controls counted as rejection.

Old Session9174 deliberately ended to adopt the new prefix/binary. The first
4360 submission accidentally retained internal blank lines, ending the theorem
frame early; subsequent indentation caused parse termination. Its partial,
truncated transcript is labelled author transport failure. Fresh66922 replayed
the checked prefix, received the same complete theorem with internal blank
lines removed for framing, and accepted it. Cold acceptance is unaffected.
No canonical showcase, kernel, trust, protected owner or performance change;
no new bt proposed from this existing explicit proof route.

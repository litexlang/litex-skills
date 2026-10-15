# Part 113 — Actual sequence-limit uniqueness: shorten the positive-gap setup

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Current continuation: round75 compressed tail and separation checks

Keep round74's two positive-gap facts and both original tail obtains. The
same full source theorem now uses the following common-index and error route:

```litex
have n0 N+=n1+n2
n1<=n0>=n2
|a(n0)-L2|<|L1-L2|/3
|L1-a(n0)|=|a(n0)-L1|<|L1-L2|/3
|L1-L2|<=|L1-a(n0)|+|a(n0)-L2|<|L1-L2|/3+|L1-L2|/3=(2/3)*|L1-L2|<1*|L1-L2|=|L1-L2|
```

This is an excerpt inside the original differing-limits assumption, after
the two obtains; the original contradiction closures follow unchanged.
[Full preferred theorem](evidence/round-75-cases/combined-short-route.lit).
The two index-bound facts become one checked bidirectional chain. The first
tail-error fact and absolute-symmetry equality become one mixed chain. Five
separation facts become the last single chain. Joint shortening removes six
immediate proof statements from the round74 route, without changing witnesses,
radius, carriers or theorem target.

Deleting both index bounds instead of combining them fails. Deleting symmetry
instead of including it in the mixed chain also fails. Standalone triangle and
2/3<1 publications are individually removable in the older route. Removing the
old sum-bound publication alone fails, yet the new full comparison chain
checks its radius-sum edge explicitly and needs no separate publication.
Do not infer that an individually required fact must remain a separate line.

The chain n1<=n0>=n2 establishes only the two adjacent comparisons. A claim
that it implies n1<=n2 rejects. The combined shortest sequence proof with
wrong final conclusion L1=L2+1 also rejects.
[False common-index endpoint](evidence/round-75-cases/wrong-common-index-endpoint.lit).

[Round75 receipt](evidence/round-75-2026-10-09.summary.json):15 strict cold files,
7 accepted/8 Normal rejections, all promoted paths rerun on a fixed snapshot
after successful current-source release build. Session66922 on round68 checked
only a scalar common-index existence witness; current cold files own the full
sequence theorem. Rounds74/75 remain one source family. No new bt or permanent
cross-context rule, canonical source/kernel/trust edit or timing claim.

## Source mathematics and context

The real-analysis showcase models sequences as fn(index N+)R and defines
epsilon tails, eventual closeness and has_limit. Its uniqueness proof assumes
two limits L1,L2, supposes they differ, and chooses epsilon=abs(L1-L2)/3.
Two tail witnesses give a common index; the triangle inequality contradicts
the positive separation. Preserve those exact predicates, both limit premises,
one-based domain, radius and witness construction.

## Seven setup statements become two

Within the original inner L1!=L2 assumption, retain only:

```litex
L1-L2!=0
0<|L1-L2|
```

Then continue with the original obtains:

```litex
obtain n1 from $has_eventual_closeness_to(a,L1,|L1-L2|/3)
obtain n2 from $has_eventual_closeness_to(a,L2,|L1-L2|/3)
```

These are excerpts. [Full preferred theorem and source prefix](evidence/round-74-cases/nonzero-gap-delete-both-epsilon-facts.lit)
contains every carrier, assumption and unchanged downstream argument.
The original seven immediate setup statements include difference nonzero,
absolute nonnegative/nonzero facts, a zero-or-positive disjunction, its cases,
epsilon positivity and R+ membership. Jointly replacing them by the two
displayed facts passes the complete uniqueness theorem. Explicit epsilon
positive and member facts are both removable in that verified route.

## Direct versus consumer boundaries

Replacing the entire sign setup by only 0<abs(L1-L2) fails. The standalone
scalar implication L1!=L2 implies this positive distance also misses in the
warm tracer. A scalar claim that first publishes L1-L2!=0 closes it; this is
not a need for a new absolute-nonzero rule.

In the full theorem, deleting explicit absolute positivity from the shortest
route fails at the first obtain, after the difference-nonzero fact. Keep both
facts for this consumer. The scalar claim's short closure does not establish
that nested has_limit radius checks can discover the same positivity unaided.
[Consumer deletion](evidence/round-74-cases/only-difference-nonzero-bridge.lit).
Internal cause of that bounded consumer miss remains unestablished.

Two earlier epsilon-deletion probes used the already failing direct-gap route.
Their failures do not show epsilon publications are needed. The successful
nonzero-gap baseline and its individual/joint epsilon deletions own the
removal evidence. Do not infer liveness from an upstream failure.

## Negative controls and evidence

Changing only the theorem's final conclusion to L1=L2+1 rejects, both with
the original route and with the shorter positive-gap route. Omitting the
second limit premise also rejects. These statements are false in general,
distinct from the true positivity/consumer misses above.
[Short wrong conclusion](evidence/round-74-cases/short-route-wrong-shifted-limit.lit).

[Receipt](evidence/round-74-2026-10-09.summary.json):13 strict cold files,
6 accepted/7 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary hashes and
log retained. Source prefix and complete original uniqueness theorem pass.
Session66922 stays on round68 and journals scalar positive/negative attempts
and the accepted local difference-nonzero bridge; it does not own the complete
source theorem's shortening. No later limit-selector, full showcase, canonical
source, kernel, trust, protected owner or performance acceptance is claimed.
No new bt or strengthened mathematical premise was introduced.

# Part 71 — Shorten four interval-endpoint case proofs

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematics

Legacy Analysis Chapter 11 defines `has_interval_endpoints(I,a,b)` by the
disjunction of the four open/closed endpoint forms. A member of any form lies
weakly between its endpoints; a point strictly between them belongs to every
form. The isolated slice preserves this definition, theorem targets, numeric
domains and four cases. It is not a current whole-book acceptance.

## Positive: retain one member bridge per branch

The original member-to-bounds branch:

```litex
case I = '[a, b):
    z $in '[a, b)
    a <= z
    z < b
    z <= b
```

The checked short branch:

```litex
case I = '[a, b):
    z $in '[a, b)
```

The same deletion works in all four branches. The standalone theorem still
exports both `a<=z` and `z<=b`. Deleting the literal-member bridges while
keeping the inequalities fails; deleting the whole proof body also fails.
Keep the four-way case split and exact bracket choices.

For strict-between-to-membership, each branch's literal membership suffices;
the following extra `z in I` echo can be deleted. Another independently
checked variant keeps only `z in I` in each branch. Both pass cold, while
the bodyless theorem fails. These are dated capability observations, not a
recommendation to reproduce goal echoes or add case scaffolding to every proof.

## Nearest negatives

Closed membership does not imply a strict lower bound. The generic
`forall a,b R,z '[a,b]: a<z` rejects, and `0 in '[0,1)` passes. Open endpoint
nonmembership `not 0 in '(0,1)` passes. Missing member and missing upper bound
controls reject; do not manufacture an ordering premise to erase them.

## Downstream boundary: original goal WD fails before its body

The source's next `intersection_of_interval_endpoint_forms_member_bounds`
theorem contains the target excerpt:

```litex
finite_set_max(union({a}, {c})) <= z
z <= finite_set_min(union({b}, {d}))
```

The original dependency plus original consumer, short dependency plus original
consumer, two-call consumer and other body variants all fail at
`def_thm / goal_well_defined / failed_then / predicate_domain`.
The first missing requirement is `$is_finite_set(union({a},{c}))`, required
for the finite maximum's real typing. No proof body has run at that failure.
Thus this round proves the local theorem shortening but cannot establish
successful downstream integration. Do not attribute this earlier WD failure
to the deletion, add trust or weaken the consumer's mathematical statement.

## Evidence and candidate routing

[Round 30 receipt](evidence/round-30-2026-10-09.summary.json) retains 18 unique strict
files and promoted-file rechecks: 7 accepted and 11 rejected, including five
consumer variants blocked at the same upstream WD requirement. Exact source
path/hash and immutable fresh release binary identity are recorded. Warm
Session 25852 uses the round29 snapshot and previously accepted theorem facts;
its bodyless successes do not establish cold capability.

The source slice is from
`scripts/旧版本的textbooks/Analysis/chapter11-riemann-integral.lit`, lines
275, 364, 395 and 437. No source textbook, kernel, AST or Env/Runtime edit,
new trust, complete repair or runtime claim. Next investigate the independently
justified finite union requirement, rather than extend interval search merely
to close one later target. Existing alias-to-literal consumer candidates remain
separate from the confirmed removable comparison echoes.

# Litex Authoring Error Cards

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use these cards after the first failed real-context attempt or during the
mandatory proof-liveness pass. They are mined repair shapes, not substitute
syntax specifications. Match the failure phase and code shape, try the smaller
form in the same persistent session, and keep only bridges whose necessity is
demonstrated by verifier evidence.

The snippets are intentionally small excerpts from larger caller contexts.
Rejected snippets document real failed shapes; accepted snippets were accepted
in their cited journal context unless a card explicitly says that it is
schematic. Confirm exact names and syntax against the current Manual and a
nearby runnable source before copying them elsewhere.

## Rule map

| Rule | Decision |
| --- | --- |
| R1 Phase first | Repair the earliest failing phase; do not change mathematics for a parse, transport, or well-definedness failure. |
| R2 Carrier first | Make every argument, index, return value, divisor, and dependent premise legal before entering the proof. |
| R3 Inside out | Prove the changed inner value or index before rewriting it under an outer constructor. |
| R4 Native surface | Put `by extension`, `by def`, `by thm`, cases, and witnesses only on a grammar surface that accepts proof control. |
| R5 Canonical representation | Keep one exact function/object representation across producers, premises, and consumers; preserve the intended public interface. |
| R6 One recursive step | Expose the branch fact, predecessor carrier, normalized index, one recurrence equation, then the outer calculation. |
| R7 Liveness after success | Delete inference echoes and endpoint logs; retain only proof-spine moves, reader bridges, and failed-deletion verifier bridges. |
| R8 Session versus replay | Distinguish protocol transport, transactional acceptance, and clean registered-file replay. |
| R9 Fresh binders | Never rebind a name that remains active in the current Litex scope. |
| R10 Semantic local names | Name a recurring mathematical atom, keep canonical public boundaries, and reject aliases that hide constructor structure consumed downstream. |

## Code that fails

### F1. Inline extensionality followed by a body

**Symptom:** parsing stops before either inclusion is checked.

**Wrong in this caller:**

```litex
by extension A = B:
    claim:
        ? forall x A:
            x $in B
        ...
```

**Write:**

```litex
by extension:
    ? A = B
    claim:
        ? forall x A:
            x $in B
        ...
```

**Rules:** R1, R4. Long-form extensionality supplies a goal block that can
contain local claims. This does not mean every `by extension A = B` needs the
long form; use it when the proof has an indented body.

**Evidence:** attempt `R243-SUM-TRANSPORT-A1-DIRECT-EXTENSIONALITY` followed by
`A2-LONG-FORM-EXTENSIONALITY` in
`scripts/linear_algebra_done_right2/experience/proof_journals/2026-8-11-chapter2c-result243-sum-transport.json`.

### F2. Proof control inside a bare `forall` fact list

**Symptom:** `Expected operator or $prop in fact` even though the theorem call
would be meaningful in a proof body.

**Wrong shape:**

```litex
forall t R:
    f(t + period) = f(t)
    by thm periodic_value(t)
```

**Write:**

```litex
claim:
    ? forall t R:
        f(t + period) = f(t)
    by thm periodic_value(t)
```

**Rules:** R1, R4. A bare universal declares facts; it is not a command block.
Once the claim goal activates `t`, use that binder directly rather than writing
another `forall t` inside the body.

**Evidence:** attempts `B004-A1` and `B004-A3` in
`scripts/Analysis2/proof_journals/chapter05_basic_periodic_functions_2026_8_11.json`.

### F3. Rewriting an atomic value directly under a binary constructor

**Symptom:** the outer chain reaches the final step, then reports the compound
equality as unknown.

**Failed:**

```litex
mul(add(one, one), a) = add(mul(one, a), mul(one, a)) = add(a, a)
```

**Accepted repair:**

```litex
mul(one, a) = a
mul(add(one, one), a) = add(mul(one, a), mul(one, a)) = add(a, a)
```

**Rule:** R3. Materialize the changed operand once; do not also publish a
separate outer equality. For deeper nesting, lift one layer at a time only
when the next failed step demands it.

**Evidence:** `C02-LIVE-009` in
`scripts/mathematics_in_litex/experiments/chapter02_proof_liveness_2026-8-6.json`.

### F4. Asking the outer function to discover an inner index equality

**Symptom:** a stored recursive value exists at the normalized index, but the
same value at an arithmetically equal expression is unknown.

**Failed shape:**

```litex
# The proof tries to consume the stored value at 1 through the argument 2 - 1.
falling_power_51(-1, 2 - 1) * (-1 - (2 - 1)) = 2
```

**Accepted bridge before the value calculation:**

```litex
falling_power_51(-1, 2 - 1) = falling_power_51(-1, 1)
```

**Rules:** R3, R6. Normalize the index first, then unfold or consume exactly
one stored recursive equation.

**Evidence:** `C5-003` and the independent symbolic repeat `C5-005` in
`scripts/Concrete-Mathematics-A-Foundation-For-Computer-Science/proof_journals/chapter05-binomial-continuation-2026-8-11.json`.

### F5. Relying on transitive carrier information at construction time

**Symptom:** well-definedness fails before the extensionality proof begins.

**Failed declaration shape:**

```litex
? forall W power_set(VSet), A, complement power_set(W):
    $is_subspace(s, VSet, zero, add, smul, W)
    =>:
        ambient_sum(A, complement) = restricted_sum(A, complement)
```

`A` and `complement` are subsets of `W`, but the ambient constructor requires
them to be known directly as subsets of `VSet`.

**Write the exact construction premises:**

```litex
? forall W power_set(VSet), A, complement power_set(W):
    $is_subspace(s, VSet, zero, add, smul, W)
    A $in power_set(VSet)
    complement $in power_set(VSet)
    =>:
        ambient_sum(A, complement) = restricted_sum(A, complement)
```

**Rules:** R1, R2. The proof body cannot repair a term that was rejected while
its parameters were introduced.

**Evidence:** attempt `R243-SUM-TRANSPORT-A5-CARRIER-FIRST-REMOVE-AMBIENT-SUBSET-PREMISES`
in the Result 2.43 journal cited by F1.

### F6. Rebinding an extensionality or claim binder

**Symptom:** `name x is already active in this scope and cannot be rebound`.

**Wrong:**

```litex
claim:
    ? forall x A:
        x $in {x R: lower < x and x <= upper}
```

**Write:**

```litex
claim:
    ? forall x A:
        x $in {y R: lower < y and y <= upper}
```

**Rules:** R1, R9. Choose role-based names such as `point`, `builder_point`,
`period_witness`, and `candidate_period` before writing nested binders.

**Evidence:** `B001-A1` in
`scripts/Analysis2/proof_journals/chapter01_interval_migration_2026_8_10.json`,
with independent `L` and `period` repeats in periodic-functions `B004`.

### F7. Storing immediately callable data behind a set alias

**Symptom:** a struct field has a function-shaped set carrier but projection is
reported as not callable.

**Failed interface shape:**

```litex
struct FiniteVectorSpaceFamily<...>:
    carriers finite_seq(power_set(USet), m)
```

**Accepted interface:**

```litex
struct FiniteVectorSpaceFamily<s nonempty_set, USet nonempty_set, m N+>:
    carriers fn(k N+: k <= m) power_set(USet)
```

**Rules:** R2, R5. If consumers immediately apply the field projection, spell
the exact bounded callable carrier. Do not infer callability, stored graph
facts, and executability from one another.

**Evidence:** `B001` in
`scripts/linear_algebra_done_right/session_records/2026-8-15-chap9d-family-field-callability.json`.

## Code that passes but is poor final style

### P1. A verified transport log around one live equation

This Result 2.43 branch verified:

```litex
obtain a, c from exist selected_a A, selected_c complement st {
    selected_a $in VSet,
    selected_c $in VSet,
    x = add(selected_a, selected_c)
}
add(a, c) $in W
x $in W
\subspace_add<s, VSet, zero, add, smul, W>(a, c) = add(a, c)
x = add(a, c) = \subspace_add<s, VSet, zero, add, smul, W>(a, c)
witness exist selected_a A, selected_c complement st {
    selected_a $in W,
    selected_c $in W,
    x = \subspace_add<s, VSet, zero, add, smul, W>(selected_a, selected_c)
} from a, c
```

The liveness candidate also verified after deleting the two carrier/closure
echoes and endpoint chain:

```litex
obtain a, c from exist selected_a A, selected_c complement st {
    selected_a $in VSet,
    selected_c $in VSet,
    x = add(selected_a, selected_c)
}
\subspace_add<s, VSet, zero, add, smul, W>(a, c) = add(a, c)
witness exist selected_a A, selected_c complement st {
    selected_a $in W,
    selected_c $in W,
    x = \subspace_add<s, VSet, zero, add, smul, W>(selected_a, selected_c)
} from a, c
```

**Rules:** R3, R7. `obtain`, subspace closure, and witness checking already
recover the deleted facts. A second deletion probe proved that the remaining
`subspace_add = add` equation is live, so it must not be removed merely because
it resembles definition replay.

**Evidence:** attempts `A2`, `A3`, and failed deletion probe `A4` in the Result
2.43 journal cited by F1.

### P2. A verifier-friendly implementation that changes the public object

This recursion verified:

```litex
have fn hanoi_moves(n Z: n >= 0) N by induc n from 0:
    case n = 0: 0
    case n > 0: 2 * hanoi_moves(n - 1) + 1
```

It was rejected by the interface audit because the source object is `N -> N`,
not a restricted `Z -> N` function.

**Write toward the intended interface:**

```litex
have fn hanoi_moves(n N) N by induc n from 0:
    case n = 0: 0
    case n > 0: 2 * hanoi_moves(n - 1) + 1
```

Under the recorded verifier boundary, the intended direct form fails to prove
that `n - 1` satisfies the recursive `N` parameter. Preserve the `N -> N`
interface, localize and label the narrow proof debt if the mainline must
continue, and route the repeated predecessor-carrier behavior as a kernel or
builtin opportunity. Do not present the restricted-`Z` version as the fix.

**Rules:** R2, R5, R6. Passing is necessary but not sufficient; the checked
object must still be the intended mathematical object.

**Evidence:** `CM-BUILTIN-C1-B001`, independently repeated by line-regions
`B009`, in
`scripts/Concrete-Mathematics-A-Foundation-For-Computer-Science/experiments/builtin_migration_chapter01.json`.

### P3. Releasing a theorem result and echoing it

**Passing but noisy shape:**

```litex
claim:
    ? P
    by thm p()
    P
```

**Prefer:**

```litex
by thm p() => P
```

**Rule:** R7. Select the one atomic result on the theorem call. Keep a bare
call only when several results are genuinely live or the desired result cannot
be selected as one atomic target.

**Evidence:** the selected-result rule and measured result-echo deletions in
`references/proof-style.md`, backed by
`scripts/Analysis/proof_journals/hot_theorem_liveness_cleanup_2026_08_05.json`.

### P4. Repeating a witness body already proved by substitution

**Passing but redundant:**

```litex
witness exist x cart(Z, Z) st {y = F_Z2(x)} from Finv_Z2(y):
    y = F_Z2(Finv_Z2(y))
```

**Prefer the bodyless witness:**

```litex
witness exist x cart(Z, Z) st {y = F_Z2(x)} from Finv_Z2(y)
```

If a reusable inverse-to-bijection theorem already exists, prefer that higher
interface over rebuilding injectivity and surjectivity locally.

**Rules:** R5, R7. The witness command checks the substituted body; repeat it
only when the body contains genuine intermediate reasoning or a demonstrated
verifier bridge.

**Evidence:** `MEC-C08-SIMPLIFY-003` and `004` in
`scripts/The-Mechanics-of-Litex-Proof/experience/proof_journals/2026-8-5-current-equality-simplification.json`.

### P5. Separate equality states instead of one mathematical chain

**Common passing shape:**

```litex
u = a
a = b
b = c
u = c
```

**Prefer:**

```litex
u = a = b = c
```

The same rule applies to substitution inside a compound expression. Keep the
stored expression as an explicit middle node:

```litex
# Given x = 3/2 and n*x = 96:
n*(3/2) = n*x = 96
```

Do not hide that route behind the endpoint-only assertion
`n*(3/2) = 96`. Likewise, when downstream steps consume several normal forms,
connect the forms in their mathematical order:

```litex
d = 4*c^2*(1-c^2) = c*(4*c-4*c^3) = c*(c-1/2)
```

If one adjacent rewrite needs its own atomic seed, place that seed immediately
before this outer chain; do not scatter the outer forms into unrelated facts.

For mixed order, use the same continuous style when each adjacent relation is
the actual mathematical route:

```litex
lower < x <= middle = normalized < upper
```

**Rules:** R3, R7. This is a nomination, not a mechanical rewrite. If one
inner equality must seed contextual rewriting, keep it immediately before the
continuous outer chain. Never delete comparison lines by regex.

**Evidence:** the miner nominated equality/comparison waterfalls across the
corpus; failed-to-repaired controls include `C02-LIVE-006`, `009`, `010`, and
`016` in the Chapter 2 liveness journal. Independent mathematical shapes are
recorded in MATH-500 source `unfinished/intermediate_algebra__2022.lit`
(substitution under multiplication) and journal
`unfinished__precalculus__989.json` (several consumer-facing normal forms).

### P6. Expanded `by def` when the inline fold is sufficient

**Often passing but unnecessarily expanded:**

```litex
by def:
    ? $P(args)
```

**Try first:**

```litex
by def $P(args)
```

**Rules:** R4, R7. Keep the goal-block form when its surrounding construct or
a real verifier run requires it. One hot-theorem deletion experiment failed
when a required goal block was removed, so this is never a blind formatting
rewrite.

**Evidence:** the expanded-`by def` style nominations from
`scripts/proof_journal_miner.py` and the negative boundary `B003` in
`scripts/Analysis/proof_journals/hot_theorem_liveness_cleanup_2026_08_05.json`.

### P7. Repeating a nontrivial object instead of naming the mathematical atom

**Passing but noisy shape:**

```litex
space.add(\vector_neg<K, field, V, space>(x), x) = space.zero
space.add(\vector_neg<K, field, V, space>(x), space.add(x, y)) =
    space.add(space.add(\vector_neg<K, field, V, space>(x), x), y)
```

**Prefer naming the callable specialization when the operation recurs:**

```litex
let neg = \vector_neg<K, field, V, space>
by thm vector_neg_spec(K, field, V, space, x) =>
    space.add(x, neg(x)) = space.zero
space.add(neg(x), x) = space.add(x, neg(x)) = space.zero
space.add(neg(x), space.add(x, y)) =
    space.add(space.add(neg(x), x), y)
```

Transparent reduction lets function-head resolution and atomic theorem
selection inspect `neg` and expand it to the fixed template specialization, so
this direct form needs no representation bridge. If the proof treats only one
result as the atom, `let nx = neg(x)` remains reasonable. Use typed
`have name S = value` instead when later steps need the carrier `S` itself.

The reduction is local to the inspected object. It does not manufacture
congruence through an enclosing operation. For example, after proving a
pointwise fact about `lc(...)`, do not assume that a later
`space.add(lc(...), lc(...))` goal can reuse the canonical nested fact. Keep
that predecessor chain canonical, prove the required congruence explicitly,
or use a short canonical-to-alias bridge at the exact boundary.

Keep exported statements and structural facts required by a later canonical
fold in canonical spelling. In LADR, storing the nonempty and closure clauses
of `is_subspace(..., subspace_sum_fn(parts))` did not discharge the exported
canonical goal `is_subspace(..., \subspace_sum<...>(parts))`: reduction expands
an inspected alias, but the canonical goal does not search backward for one.
Reject the alias if repairing that direction would duplicate all structural
clauses or create an adapter stack.

A compact final bridge is appropriate when the proof itself naturally uses a
set-valued alias but the public theorem remains canonical:

```litex
let ball = \metric_ball<R, real_distance>
by extension:
    ? ball(5, 2) = I
    # the two pointwise inclusions
\metric_ball<R, real_distance>(5, 2) = ball(5, 2) = I
```

The same distinction applies to existential elimination. When a concrete
named proposition has one ordinary existential body, prefer the concise
`obtain witness from $P(args)`. But keep the source in the canonical argument
spelling for which the atomic proposition or existential evidence was proved.
Replacing a canonical argument by an alias may pass well-definedness and still
fail with “source existence fact not verified”; that is a proof-evidence
failure, not a request to re-prove well-definedness.

**Boundary:** do not hide structure consumed by a native proof action. For
example, this is counterproductive when the next step needs the range
constructor:

```litex
have image_of_K power_set(Y) = fn_range(fn(x K) Y {f(x)})
have by preimage source_point from image_point $in image_of_K
```

`have by preimage` requires an explicit `fn_range(...)` or `replacement(...)`
source. If an alias forces repeated constructor-membership and preimage
adapters, keep the canonical expression rather than naming it.

**Rule:** R10. This is a semantic decision, not a line-length rewrite: name
objects the proof treats as atoms, preserve public/canonical boundaries, and
stop when the alias increases representation transport.

**Evidence:** callable-template promotion journal
`showcases/math_concepts_in_litex/.drafts/proof_journals/callable_template_let_promotion_2026_08_25.json`,
including independent LADR, linear-algebra, and topology positive runs and the
LADR canonical-fold negative boundary. Earlier probability, ODE, numerical,
and constructor-sensitive topology evidence is indexed by
`showcases/math_concepts_in_litex/.drafts/proof_journals/semantic_local_names_promotion_2026_08_24.json`.

### P8. Repeating a theorem then-clause as its whole proof

**Passing but redundant:**

```litex
thm setting_law:
    ? forall [SomeSetting], x S:
        $law(x)
    $law(x)
```

**Prefer after a real-context deletion probe:**

```litex
thm setting_law:
    ? forall [SomeSetting], x S:
        $law(x)
```

The parser intentionally accepts an optional theorem proof body, and theorem
execution still checks every then-clause after running zero or more proof
statements. This form is correct only when setting expansion, binders,
premises, or ordinary verifier rules really supply the conclusion. A bodyless
theorem for an unsupported abstract proposition must continue to fail with
`cannot prove then-clause`.

**Rule:** R7. Do not add a conclusion echo as syntactic padding; do not remove
a body that performs a real derivation or the smallest verified bridge.

**Evidence:** setting-law deletion probes `B001` and `B002` in
`showcases/math_concepts_in_litex/.drafts/proof_journals/bodyless_theorem_cleanup_2026_08_26.json`;
independent bodyless arithmetic theorem `main_541` in
`showcases/math_concepts_in_litex/16_probability_theory/.drafts/proof_journals/transparent_let_full_replay_a3_2026_08_26.json`;
negative kernel control
`definitions_and_runtime.rs::prechecked_goal_certificate_never_stores_the_goal_itself`.

## Fast use protocol

1. Read the first decisive error and choose one F-card by phase and shape.
2. Apply only that card's smallest repair in the existing persistent session.
3. If it passes, compare the proof against P1--P8 and its ordinary-language
   proof spine.
4. Delete one suspected echo class at a time. Restore only the bridge named by
   the first downstream failure.
5. Run the clean registered-file gate. A session result, a schematic snippet,
   or a journal entry alone does not make a new caller checkable.

When the same repair recurs, do not automatically make the workaround longer
or more universal. Route authoring habits to this skill, reusable mathematics
to the standard library, unclear phases to diagnostics, and isolated stable
verifier behavior to a kernel regression.

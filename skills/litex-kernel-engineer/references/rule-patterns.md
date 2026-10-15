# Rule Patterns

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


## Restoring A Rule After A Dispatcher Refactor

When a formerly supported fact stops verifying after dispatcher, recursion,
or verifier-state changes, restore it at its semantic owner. Do not make the
example pass by inserting a matching `if let` before the generic verifier
pipeline.

1. Use history and current callers to find the former route and why it no
   longer fits the current API.
2. Classify the behavior by the fact being proved. Put membership rules in the
   membership dispatcher, equality rules in equality, and multi-child
   constructor decomposition in a bounded strategy. Keep generic orchestration
   limited to search phases and policy.
3. Split mixed helpers. A syntax-directed or alpha-equivalent comparison is a
   pure structural leaf. Equality transport, quantified premises, subset
   reasoning, or any other proof search is a semantic rule/strategy with an
   explicit recursion budget.
4. Do not create a fresh full verifier state, call an unrestricted verifier,
   or bypass the current builtin premise entry merely because the old helper
   needs more context. Adapt or split the rule instead.
5. Preserve the original well-definedness obligation. If success depends on a
   body, argument, return value, or partial operator already being checked,
   encode or document that precondition at the owning route and retain a
   negative regression that fails without it.
6. Preserve known-fact-first ordering, memoization, and provenance. Record
   every semantic premise as a child result; never return an empty child list
   after using equality, forall, subset, or another proved fact.
7. Add a focused architecture regression when the layer boundary is easy to
   violate again, in addition to the positive and negative behavior tests.

Example classification: for
`fn(x E) R {f(x)} $in fn(y E) R`, the membership success belongs to the
`InFact` builtin route, while comparing the two declared signatures modulo
bound names is a structural leaf. Transport from `E = A` is not structural;
it is a semantic premise and must remain bounded and visible in provenance.

## Builtin Rule Checklist

A builtin rule should have:

- a narrow mathematical property;
- explicit applicability conditions;
- predictable failure behavior;
- a runnable example;
- a regression test or covered example;
- verifier output that names the rule clearly enough for debugging.

Example comment shape:

```rust
// Proves nonzero quotients from nonzero numerator and denominator.
// Example: a != 0, b != 0 => a / b != 0.
```

## Infer Rule Checklist

An infer rule should say:

- when it is applied;
- what fact it adds;
- why the inference is mathematically safe;
- an example of the source fact and inferred fact.

Prefer a narrowly targeted inference over a broad one that changes many unrelated proofs.

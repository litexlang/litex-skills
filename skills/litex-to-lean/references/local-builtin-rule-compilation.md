# Compiler Local Builtin Rule Compilation

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Read this reference only when adding or changing the registered local-builtin
rule mechanism or its compiler Lean adapter.

## Scope

A local builtin rule has one finite atomic conclusion pattern, a fixed ordered
list of parameter requirements, and a fixed ordered list of premises. Every
rule variable is determined by matching the conclusion. Applying the rule does
not recursively apply another local builtin rule.

Keep these mechanisms outside this catalog:

- numeric evaluation or normalization;
- equality rewrite or representation transport;
- definition unfolding;
- recursive constructor strategies;
- binder/body synthesis or variable-size premise search;
- known-forall theorem search.

Adding a mathematical rule over supported syntax must not require another
verifier evidence enum, IR enum, or ad hoc proof search branch.

## Source identity and certificate

Give each rule a stable string ID and a fingerprint of its canonical semantic
schema. A successful application retains:

```text
RegisteredRuleApplication {
    rule_id,
    semantic_fingerprint,
    ordered_bindings,
    ordered_parameter_requirement_proofs,
    ordered_premise_proofs,
}
```

Do not use a diagnostic label, rendered fact, theorem display name, or source
text as semantic identity. Do not silently reuse an ID after changing the
schema.

Match conclusion structure with a pure, bounded matcher. It must not receive a
`Runtime`, mutate an environment, unfold definitions, calculate values, widen
standard sets, or consult equality classes. Bind one complete object subtree
at each schema variable and compare repeated bindings structurally.

Validate the certificate before emission:

1. resolve the exact rule ID and fingerprint;
2. reinstantiate the conclusion and require the exact target fact;
3. reinstantiate parameter requirements and premises in source order;
4. require each child proof to target the exact instantiated fact;
5. validate binding count, child count, order, IDs, and scope availability;
6. reject unknown IDs, stale fingerprints, cycles, missing children, or
   proposition drift.

## Compiler Lean adapter ABI

Write adapters against the compiler native-carrier ABI from
`lean/Litex/Core.lean`. Never use `LitexObject`, `Litex.Object`, or
`Set.univ` as a Litex-set encoding.

The current registered order tracer is:

```litex
forall a, b R:
    a < b
    =>:
        a <= b
```

Its source binders currently lower to complex values with separate membership
proofs, while the atomic propositions remain heterogeneous:

```lean
∀ (a : ℂ) (haR : Litex.In a Litex.R)
  (b : ℂ) (hbR : Litex.In b Litex.R)
  (hab : Litex.Lt a b),
  Litex.Le a b
```

After validating the exact `order.less_equal_of_less` certificate, compiler
emits the proved core theorem:

```lean
Litex.Lt.toLe hab
```

Parameter-membership proofs remain explicit even when the selected theorem
does not consume them. They are part of the source theorem signature and may
be required by another rule or WD route.

All definitions that explain Litex through Lean or Mathlib belong in
`lean/Litex/Core.lean`. Put only concrete certificate-selected theorems in
`lean/Litex/Rules.lean` or a rules module imported by it. Do not create a
feature definition header such as `Order.lean`.

For a future generic adapter registry, use this fixed application order:

```text
bound native Lean terms in Litex parameter order
  -> exact parameter-membership/typing evidence
  -> semantic premise proofs in source order
  -> translated conclusion
```

The adapter theorem may use ordinary checked Mathlib results or tactics inside
its proof. The compiler emitter must not use those tactics to rediscover which
rule applies.

## Evidence and scope

Keep rule applications in the verifier-owned proof tree/DAG. Preserve
`FactId`, statement ownership, ordered children, and local binder scope. A
statement-local rule proof is emitted inside its owning Lean theorem after the
relevant binders and hypotheses; never hoist it to the top level by
generalization.

The compiler emitter must:

1. validate the registered certificate;
2. resolve every cited child by exact identity;
3. render each binding using the reviewed native carrier choice;
4. call the exact proved adapter theorem;
5. fail closed if any route or carrier is unsupported.

Do not rerun Litex proof search, find a fact by printed proposition, use
`assumption`, or launch Lean automation to choose an adapter.

## Tests

For a new registered rule, require:

- one exact positive verifier/certificate regression;
- the nearest structural mismatch or forged-certificate negative regression;
- a numbered compiler `.lit/.lean` tracer if this is a public compiler
  capability;
- an assertion that generated output contains the expected theorem call;
- assertions that it contains no `LitexObject`, `Litex.Object`, `Set.univ`
  source-set encoding, `sorry`, or compiler-invented `axiom`;
- a real Mathlib kernel check of the complete generated file.

Use the focused commands selected by the repository impact policy. The normal
compiler contract gates are:

```sh
cargo test --release --test litex_to_lean_compiler_tracers
cd lean && ./compiler.sh check examples
```

Run `lake build` as well when `Core.lean`, `Rules.lean`, or their import graph
changes.

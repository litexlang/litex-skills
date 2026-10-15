
> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.

---
name: litex-to-lean
description: Design, implement, review, or debug the Litex-to-Lean compiler and its semantic wrapper layer over Lean's native type system. Give every supported Litex object and statement an explicit Lean representation, Litex wrapper contract, verifier-owned evidence path, and proof-driven unwrapping route to Mathlib; use heterogeneous Litex.Same, exact-carrier Litex.Set, Litex.In membership, FactId citations, registered-rule certificates, generated .lit/.lean example pairs, and real Lean kernel gates. Use whenever Litex syntax such as N/Z/Q/R/C, sets, `$in`, equality, order, `forall`, numeric expressions, functions, facts, trust, or verifier builtin rules must be represented or compiled in Lean. Treat the old universal LitexObject/Litex.Object ABI as deprecated and forbidden for new work, and never introduce project axioms or proof holes.
---

# Litex to Lean — Compiler

Build and extend the compiler. Replay the exact successful Litex verification
route in Lean while representing values with ordinary Lean/Mathlib carriers.
Never revive the deprecated universal-object target.

## Derive compilation forward from source semantics

Construct compiler support in this direction: Litex source semantics and
independently verified runtime evidence; explicit host carriers and wrapper
invariants; typed statement/proof result contracts; scope and identity
dependencies; lowering and emission; generated Lean; native consumer and Lean
kernel validation. A desired generated term, Mathlib theorem, or passing
`.lean` file is an acceptance target, not evidence from which to invent the
source representation or proof route.

Use backward reasoning only to inventory consumer requirements and audit
whether the emitted program preserves the verified source route. If generated
Lean fails, trace the failure to the earliest missing semantic contract,
evidence node, carrier decision, or proved bridge and repair that upstream
boundary. Do not add target-side theorem search, special-case emission,
axioms, casts, or wrappers merely to make the current output compile. If the
tracer's final theorem were hidden, every ABI object, evidence field, rule
adapter, and bridge must still be justified by a source-semantic invariant and
an explicit owner.

## Organize the work around three design problems

Treat the following as the compiler's long-term design agenda. Every
substantial compiler design, implementation, review, tracer, and document
should identify which problem it solves and how its choice constrains the
other two. Do not let a locally convenient emitter case silently settle one
of these architectural questions.

### 1. Map Litex mathematics into Lean without isolating either ecosystem

A Litex mathematical object or statement can often be represented by several
extensionally similar Lean terms or propositions. Those encodings are not
interchangeable as compiler designs: the choice determines later theorem
reuse, elaboration, coercions, proof obligations, generated-code readability,
and compatibility with Mathlib and ordinary Lean developments.

Design the recurring foundations first, especially functions, sets,
membership, equality, binders, application, and well-definedness. Litex and
Lean organize these concepts differently, so never choose an encoding merely
because it prints the current example. Prefer native Lean/Mathlib carriers
with explicit Litex semantic wrappers and proved elimination paths. For each
object and statement family, record the alternative Lean encodings considered,
the chosen compatibility boundary, and the consequences for future features.
Once these few foundational contracts are sound, extend the many remaining
`Obj` and `Stmt` cases by the established pattern rather than inventing a new
semantic ABI per case.

### 2. Reify the successful Litex verification route as Lean proof evidence

Litex verification searches by decomposing a goal along a tree. When one
branch succeeds, the successful information must return compositionally from
the leaves to the root: which rule was selected, which subgoals were proved,
which facts and objects were used, and how the child results discharge the
parent result.

Make that returned information explicit, stable, and typed before emission.
The compiler must consume the verifier-owned successful route as structured
proof evidence and translate it into Lean declarations and proof terms. It
must not reconstruct the route from display text or ask Lean to rediscover a
different proof. When a proof rule cannot return enough information for exact
replay, treat that as an evidence-contract gap in the verifier/IR boundary,
not as permission to add target-side search.

### 3. Reify successful statement execution, not only fact verification

Litex statements also produce information while their nested operations
return: declarations, introduced symbols, stored facts, scopes, object values,
well-definedness results, and other environment effects. Preserve this
statement-result structure through the same compositional return discipline.

The recursive `StmtResult` must say what the statement established, what
evidence owns each result, which results persist, which remain local, and in
what source and dependency order Lean must recreate them. Do not infer these
effects later by diffing environments or reparsing rendered statements. The
hard compiler boundary is therefore not only
`Litex proposition -> Lean proposition`; it is the coherent transformation of
semantic mappings, proof-search results, and statement-execution results into
one replayable Lean program.

## Governing thesis: a Litex semantic wrapper layer over Lean

Treat Lean's type system as the host representation layer, not as Litex's
source-level classification system. Litex semantics live one layer above it
through wrappers such as `Same`, `Set`, `In`, `AsReal`, `Lt`, and `Le`.
Therefore, saying that Litex does not primarily reason in terms of Lean types
means that membership, semantic equality, and order are not identified with
Lean typing. It does **not** mean that generated Lean terms are untyped.

Use these stable names and distinctions in designs, reviews, and documentation:

- **Membership-oriented, representation-independent semantics** names the
  Litex object model. Source-level mathematical classification accumulates as
  propositions such as `In x S`; it is not exhausted by one fixed host type.
- **Heterogeneous semantic equality across representations** names
  `Litex.Same`. It may relate `x : α` and `y : β` when reviewed bridges prove
  that the representations denote the same Litex mathematical value.
- Lean `Eq` is homogeneous propositional equality. It requires both endpoints
  in the same carrier and provides native substitution, rewriting, and
  dependent transport.
- `Same` is not merely `HEq`. `HEq` is term identity inside dependent type
  theory; `Same` intentionally includes mathematical identifications between
  approved native representations such as compatible `ℕ`, `ℤ`, `ℚ`, `ℝ`,
  and `ℂ` values.

Use an equivalence class of pairs `(host type, host value)` under `Same` as a
conceptual model of one Litex mathematical value. State explicitly that the
implementation does not construct this quotient: it preserves concrete
representatives, `In` witnesses, and bridge proofs for Lean's kernel to check.
Read `In x S` precisely as: the semantic value represented by `x` has a
`Same` representative in the exact carrier `S.Carrier`. A new membership fact
refines knowledge about `x`; it never retypes, casts, narrows, or replaces it.

Keep equality elimination asymmetric:

```text
Lean Eq ⊆ Litex.Same  via Same.ofEq
Litex.Same --reviewed same-carrier, injective observation--> Lean Eq
```

Treat `Lean Eq ⊆ Litex.Same` as a global semantic invariant. Never add or
assume a global `Same x y → x = y`. Equality of the endpoint Lean types is
necessary for writing `x = y`, but it is not sufficient for proving it from
`Same`: two `Litex.Set` values may be extensionally `Same` while packaging
different exact carriers. Recover native equality only through a proved
specialization whose common carrier has a faithful/injective semantic
observation, such as `Same.complexNativeEq` for `x y : ℂ`, or through
explicitly supplied observations such as `Same.complexEq`. Arbitrary `Same`
evidence is not a Lean rewrite certificate.

For every supported Litex `Obj` and `Stmt`, define an explicit wrapper
contract containing all of the following:

1. the native Lean term, type, proposition, or declaration used as its host
   representation;
2. the Litex wrapper proposition or structure expressing its source
   semantics;
3. the verifier evidence required to construct and use that wrapper;
4. a definition or fully proved elimination theorem that unwraps it into
   Mathlib-native data or results whenever the mathematics permits this; and
5. fail-closed behavior for source shapes whose wrapper contract has not yet
   been implemented.

Require wrapper transparency to Mathlib. Generated Lean must open wrappers
through definitions, witnesses, and proved bridge theorems, never through
unsafe casts or erased membership assumptions. For example, `In x R` exposes
a real representative through `AsReal`; native equality lifts through
`Same.ofEq`; `Lt` and `Le` eliminate through real representatives; and an
exact `Set.Carrier` exposes the native carrier. A wrapper is incomplete until
the generated proof can use ordinary Mathlib theorems through such a proved
unwrapping path.

Keep `Core.lean` closed at the project boundary: it may contain definitions,
abbreviations, structures, inductives, classes, instances, and fully proved
theorems, but no project-declared `axiom`, `sorry`, `admit`, or unsafe proof
placeholder. This requirement does not claim that Lean or Mathlib has no
foundational dependencies; it says compiler adds no unproved foundation of
its own.

## Read the current source of truth

Before making a semantic decision, inspect the current repository artifacts:

- `lean/Litex/Core.lean`: the single compiler semantic bridge header;
- `lean/Litex/Rules.lean`: concrete theorems used by checked certificates;
- `src/result/`: the recursive statement Results, typed verifier evidence,
  FactIds, well-definedness trees, and execution provenance returned by the
  Litex kernel;
- `src/stmt_result_to_lean_compiler/README.md`: the three-problem design agenda that
  every substantial compiler addition must answer;
- `src/stmt_result_to_lean_compiler/`: the active compiler implementation;
- `lean/examples/<N>_<Feature>.lit` and the same-name `.lean`: executable
  source/output ledger;
- `lean/README.md` and `lean/math_collections.md`: implemented scope and
  pending design boundaries.

Treat `tmp/compile_to_lean_legacy/` as a local archive only. It is not part of
the build, is not an evidence provider, and is never a design authority. Do
not make active code depend on it. Both `litex -lean` and `litex -lean-ledger`
must call `src/stmt_result_to_lean_compiler/`: source execution returns a
recursive `Vec<StmtResult>`, the `Runtime` is dropped, and the compiler consumes
only those completed Results.

When modifying registered local builtin rules or their Lean adapters, also
read [references/local-builtin-rule-compilation.md](../../../references/sources.md#unbundled-local-material).

## Use the compiler semantic worldview

Every emitted value is an ordinary Lean term of a real Lean type. There is no
single type containing all Litex objects.

The semantic core has this shape:

```lean
universe u
abbrev Litex.u := Type u

class Litex.BridgeRule (α β : Type u) where
  relation : α → β → Prop

Litex.Bridge : α → β → Prop
Litex.Same : α → β → Prop

structure Litex.Set where
  Carrier : Type u

Litex.In : α → Litex.Set → Prop
```

Interpret the pieces as follows:

- `BridgeRule` is the reviewed primitive relation between native carriers.
- `Same` is heterogeneous semantic equality generated by primitive bridges,
  reflexivity, symmetry, and transitivity.
- Native Lean equality implies `Same` through `Litex.Same.ofEq`.
- `Litex.Set` packages the set's exact element carrier.
- `Litex.In x S` means that `x` is `Same` as some value of `S.Carrier`.
- Membership never changes, casts, narrows, or replaces the Lean type of `x`.
- One value may retain independent membership proofs for several sets.
- Lean universes remain Lean universes. `Litex.u` is only an abbreviation for
  `Type u`, not a separate Litex universe.

Standard numeric sets use native Mathlib carriers:

```lean
Litex.N : Litex.Set := Litex.Set.ofType ℕ
Litex.Z : Litex.Set := Litex.Set.ofType ℤ
Litex.Q : Litex.Set := Litex.Set.ofType ℚ
Litex.R : Litex.Set := Litex.Set.ofType ℝ
Litex.C : Litex.Set := Litex.Set.ofType ℂ
```

The current Adapter-facing real/complex source convention lowers `R` and `C`
binders to `ℂ`. A binder declared in `R` therefore remains a complex-valued
Lean term with a separate real-membership proof:

```litex
forall a R:
    a = a
```

```lean
∀ (a : ℂ) (ha : Litex.In a Litex.R), Litex.Same a a
```

Do not change `a` to `ℝ` merely because `ha` exists. The exact carrier of
`Litex.R` is used by the definition of `In`; it is not the binder's Lean type.
Choose the host carrier from the statically resolved binder domain when the
binder is declared, never from later premises or inferred consequences.
Adapter-facing `R` and `C` binders use the reviewed native `ℂ` convention plus
explicit membership; binders over arbitrary source sets retain their own
implicit host carrier plus `In`. A later premise such as `x = 1` or a later
proof of `x $in R` adds evidence only and must not retroactively specialize a
generic `x : α` to `x : ℂ`.

### Preserve `set` as a parameter kind

Do not confuse a parameter kind with an ordinary object domain. The source
runtime and recursive Result already make this distinction:

```text
forall x S    -> ParamType::Obj(S) -> InFact(x, S)
forall A set  -> ParamType::Set    -> IsSetFact(A)
```

`set` is not a universal Litex set, and `Litex.Set` is a Lean host type rather
than a source set whose members are all sets. Therefore reject both
`Litex.In A Litex.Set` and the current-v2 shortcut that emits
`(A : Litex.Set)` while lowering the retained `IsSetFact(A)` to `True`.

The target ABI must expose a representation-independent set predicate and a
reviewed exact-carrier elimination:

```lean
Litex.IsSet.{u} {α : Type (u + 1)} (A : α) : Prop
Litex.IsSet.rep (A : α) (hA : Litex.IsSet A) : Litex.Set.{u}
Litex.IsSet.same_rep (A : α) (hA : Litex.IsSet A) :
  Litex.Same A (Litex.IsSet.rep A hA)
Litex.IsSet.own (S : Litex.Set.{u}) : Litex.IsSet S
```

For the universe-zero set slice, lower:

```litex
forall A set, x A:
    x = x
```

to the target shape:

```lean
∀ {αA : Type 1} (A : αA) (hA : Litex.IsSet A)
  {αx : Type} (x : αx)
  (hx : Litex.In x (Litex.IsSet.rep A hA)),
  Litex.Same x x
```

Register `hA` under the retained `IsSetFact`'s exact FactId. Every later set
operation must use `Litex.IsSet.rep A hA`; every ordinary `x A` parameter must
retain its independent `InFact` proof against that representative. Apply the
same hierarchy to `nonempty_set` and `finite_set`: each implies `IsSet` and
adds its property on the selected representative.

Distinguish universal binding from compiler-owned construction. A
`forall A set` binder is representation-polymorphic. A checked
`have A set = E` definition may choose the exact host representation
`A : Litex.Set := E`, but it must still construct and register
`IsSet.own A` for the retained source fact. Bare `have A set` must remain
fail-closed until there is a kernel-checked fresh-set construction that exposes
only `IsSet A`; never implement it by a transparent choice of `empty` or an
invented axiom.

Require representative coherence before implementing this API. If
`ha : IsSet A`, `hb : IsSet B`, and `h : Same A B`, Core must prove that
membership in `IsSet.rep A ha` and `IsSet.rep B hb` is equivalent. A bare
definition `IsSet A := ∃ S, Same A S` is not by itself enough while general
set-membership transport from `Same` is unavailable. Treat this as one Core
and compiler contract, not as target-side proof search.

This replacement is ABI-incompatible. When implementing it, bump
`abiVersion`, migrate all `ParamType::Set`, `NonemptySet`, and `FiniteSet`
paths together, regenerate the affected example pairs, and pass the real Lean
gates. Until then, describe it as the target contract and describe
`(A : Litex.Set)`/`True.intro` honestly as current migration debt.

## Reject the deprecated universal-object ABI

Never introduce or emit any of these for compiler:

```lean
axiom LitexObject : Type
axiom Litex.Object : Type
Litex.In : LitexObject → LitexObject → Prop
```

Also reject:

- an indexed `LitexObject (α : Type)` wrapper;
- treating all values, sets, functions, or numeric domains as terms of one
  invented object type;
- representing a Litex set as `Set.univ` over an ambient carrier;
- using native Lean typing as a replacement for source membership;
- silently coercing a value after proving another membership;
- compiler-invented axioms, `sorry`, or `admit`;
- using the legacy universal emitter or old generated ledger as an acceptance
  oracle for compiler.

The only acceptable use of `Set.univ` is an internal ordinary Lean theorem
whose mathematics genuinely needs it. It must never encode the source meaning
of a Litex set.

## Keep one semantic bridge header

Put every definition that explains a Litex concept through Lean or Mathlib in
`lean/Litex/Core.lean`. This includes `BridgeRule`, `Bridge`, `Same`, `Set`,
`In`, numeric sets, subset carriers, real representatives, and heterogeneous
order.

Do not create feature definition headers such as `Order.lean`. Keep
`lean/Litex/Rules.lean` for concrete proved rules selected by verifier
certificates. A generated file imports `Litex.Rules`, which imports the single
core header.

Core bridge declarations must be definitions, structures, inductives,
classes, instances, or proved theorems. Do not postulate their desired laws as
axioms. If an open bridge registry requires a coherence invariant, expose it as
an explicit certificate such as `RealCoherence`; do not install an inhabitant
silently.

## Follow the current lowering contract

Use these mappings unless a later reviewed compiler tracer changes them:

| Litex source | Compiler Lean |
| --- | --- |
| `have A set = R` | `abbrev A : Litex.Set := Litex.R` |
| `x $in S` | `Litex.In x S` |
| `x = y` | `Litex.Same x y` |
| `x < y` | `Litex.Lt x y` |
| `x <= y` | `Litex.Le x y` |
| numeral `n` | `(n : ℂ)` in the current numeric slice |
| `2 + 3` | `((2 : ℂ) + (3 : ℂ))` |
| `forall a R` | `(a : ℂ)` followed by `Litex.In a Litex.R` |

For example:

```litex
forall a R, b C:
    a = b
    =>:
        b $in R
        a $in C
```

lowers conceptually to:

```lean
∀ (a : ℂ) (haR : Litex.In a Litex.R)
  (b : ℂ) (hbC : Litex.In b Litex.C)
  (hab : Litex.Same a b),
  Litex.In b Litex.R ∧ Litex.In a Litex.C
```

Use `Litex.In.congr hab` to transport membership. Do not turn `hab` into a
native cast or erase either original membership fact.

For predicate-defined subsets, use an exact subtype carrier:

```lean
Litex.setBuilder base predicate
```

Do not use the same carrier for a proper subset and its base set. Higher-order
sets are not forbidden: universe-polymorphic `Litex.Set` may itself be the
carrier of a higher-universe set. Only claim source-level support after the IR
and emitter have an executable tracer for the relevant statement form.

## Preserve verification evidence and scope

Treat the runtime environment and verifier output as semantic compiler input:

```text
Stmt/source order
  -> runtime environment tree
  -> StmtResult and verifier-owned evidence
  -> StmtResult-to-Lean compiler declaration/proof nesting
```

Preserve all of the following:

- source statement and sibling order;
- persistent versus statement-local scope ownership;
- `SymbolId` and `FactId` identity;
- verifier-selected proof rules and ordered child proofs;
- well-definedness object IDs, fact IDs, source occurrences, DAG edges, and
  target-requirement roles;
- exact registered-rule ID, semantic fingerprint, bindings, parameter
  requirements, and premises.

Emit only persistent source facts as top-level theorems. Emit statement-local
WD facts after the owning theorem binders and premises, in child-before-parent
order. Never hoist them by generalizing over visible variables.

Register every emitted source theorem by its `FactId`. A
`KnownFactCitation { source_fact_id }` must resolve that exact theorem or local
hypothesis. Never locate a citation by rendered proposition, `assumption`, or
fresh Lean proof search.

The recursive Result remains source-semantic evidence. Do not add a
universal-object target field to it. Carrier/lowering choices must be explicit
and validated by compiler for each supported source construct; do not infer
them later from pretty-printed text.

## Replay proofs without target-side rediscovery

Map only reviewed verifier evidence:

- object reflexivity → `Litex.Same.refl`;
- native equality already proved by a checked route → `Litex.Same.ofEq`;
- equality-based membership rewrite → `Litex.In.congr`;
- closed complex membership → a proved theorem such as
  `Litex.Rules.complexInC`;
- registered order rule → the exact allowlisted theorem after validating its
  ID, fingerprint, bindings, and child evidence;
- direct known fact → its registered `FactId` name.

A Lean tactic may appear inside a fixed proof adapter only after the verifier
has selected a structured certificate and compiler has validated its target.
For example, emit `Litex.Same.ofEq (by norm_num)` only for checked rational
normalization after independently confirming the exact rational equality.
Never launch `simp`, `aesop`, `norm_num`, or theorem search to discover a proof
route that the verifier did not provide.

Fail closed on every unsupported statement, object, fact, proof rule,
certificate shape, carrier choice, or scope reference. Do not emit a partial
file with `sorry`.

## Treat functions as an open compiler design decision

Compiler does not yet define the source function ABI. Do not copy the old
`LitexObject`, `Litex.Applicable`, `Litex.apply`, or `FnSpec` design merely
because it exists in legacy notes.

When adding functions:

1. start from native Lean carriers, `Same`, exact set carriers, and retained
   membership proofs;
2. preserve the exact Litex application layers and arity;
3. decide explicitly how function values respect heterogeneous `Same`;
4. preserve verifier-owned applicability and result-membership evidence;
5. add a numbered `.lit/.lean` tracer and a nearest rejected application
   shape before generalizing.

Return any consequential function-representation choice to the user rather
than hiding it in the emitter.

## Keep trust explicit

Compiler currently declares no new Lean axioms. Never invent one to bridge an
unsupported Litex construct or verifier rule.

If explicit source `trust` is later supported, its Lean representation must be
an exact, visible trust boundary for that proposition and nothing else. Until
that adapter is reviewed, fail closed. Trust must never manufacture carriers,
sets, memberships, bridge instances, coherence certificates, WD evidence, or
builtin laws.

A downstream user may install another `BridgeRule`; that is an explicit ABI
extension. The compiler must only emit/import allowlisted bridge instances.
Ordinary source equality never registers a new bridge.

## Use executable compiler tracers

Every compiler feature gets a checked-in same-name pair:

```text
lean/examples/<N>_<Feature>.lit   authoritative verified source
lean/examples/<N>_<Feature>.lean  generated output; never hand-edit
```

Keep one primary tracer per change and record before/now/boundary/evidence in
the `.lit` comments. Add the nearest executable negative Rust regression for a
widened route.

The current base tracers are:

1. `1_SetSystem`: exact-carrier set aliases, heterogeneous `Same`, and
   membership transport;
2. `2_OrderSystem`: `Lt`/`Le` through real representatives and a validated
   registered-rule certificate;
3. `3_AtomicEquality`: top-level reflexive and closed numeric equality with
   named WD facts.

Use the next numbered pair for a genuinely new feature. Do not add handwritten
Lean examples that claim compiler support.

## Verify in three distinct stages

Do not classify a source as a compiler gap until that exact source passes
ordinary Litex verification.

1. Verify Litex:

   ```sh
   target/release/litex -compact -strict -runner -f lean/examples/<file>.lit
   ```

   Require process exit `0` and the runner envelope's top-level `ok: true`.

2. Compile with compiler:

   ```sh
   ./lean/compiler.sh compile ./lean/examples/<file>.lit
   ```

   A failure here is an IR/certificate/lowering/emission gap only if stage 1
   passed on the exact source.

3. Check generated drift and real Lean:

   ```sh
   cd lean
   ./compiler.sh check examples
   ```

   This recompiles every `.lit`, compares the generated `.lean` byte for byte,
   and submits it to the real Mathlib Lean kernel.

For focused Rust coverage, use:

```sh
cargo test --release --test litex_to_lean_compiler_tracers
cargo test --release --bin litex_to_lean_compiler
```

When `Core.lean`, `Rules.lean`, or the import graph changes, also run
`cd lean && lake build`. Select broader gates only through the repository
impact policy.

Assert the forbidden old ABI in relevant tests: generated compiler output
must not contain `LitexObject`, `Litex.Object`, a compiler-invented `axiom`,
`sorry`, or source-set encodings based on `Set.univ`.

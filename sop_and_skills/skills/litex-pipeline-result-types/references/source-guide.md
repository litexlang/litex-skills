# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Pipeline Result Types

Use this skill whenever designing, reviewing, or migrating return types for
`src/` verify/exec functions. Apply it alongside
`golitex-repository-policy` and `litex-kernel-engineer`.

Two complementary rules:

1. Pipeline function return values mirror the function's stage order.
2. Dispatcher function return values mirror the input enum structure.

## Critical: only `exec_stmt` runs statements

Hard rule for `src/` statement execution:

```text
Outside `crate::execute`:
  call Runtime::exec_stmt only

Inside `crate::execute`:
  exec_stmt may call exec_xxx_stmt / execute_fact_statement
  nobody else may call those branch functions
```

- Do **not** call `execute_fact_statement`, `exec_let_obj`, `exec_have_*`,
  `exec_def_prop_stmt`, `exec_def_abstract_prop_stmt`, `exec_unsafe_stmt`, or
  any other `exec_*_stmt` from runners, REPL, tests, verify helpers, or other
  crates/modules.
- Branch `exec_xxx_stmt` functions stay `pub(in crate::execute)`
  (or tighter). Do not re-export them from `execute/mod.rs` for outer use.
- Nested proof/WD work uses `verify_*` / `store_*` on the current top env, not
  another `exec_stmt` and not a direct `exec_xxx_stmt`.
- Reason: `exec_stmt` owns the transactional temp `ExecEnv` (push → run →
  Failed discard / Success `merge_from`). Bypassing it writes the parent env
  without the Success|Failed contract.

Detailed worked examples live in
[`references/examples.md`](examples.md). Current-repo alignment notes
live in [`references/current-code.md`](current-code.md).

## Formal rules

### File ownership and declaration ordering rule

Every Litex implementation file has one center of gravity: either one main
data structure or one main algorithm pipeline. The filename names that main
responsibility, rather than an incidental helper, result wrapper, or collection
of similarly themed functions. Data-structure files use the structure's
snake-case name; algorithm files use the main operation and subject's
snake-case name (`exec_stmt.rs`, `verify_equal_fact.rs`, or
`verify_non_equational_fact.rs`).

An algorithm file's main entry function should have the same stem as the file.
Place that main function first, then place its direct sub-pipeline functions in
the order they are called. Continue recursively: helpers for an earlier stage
come before helpers for a later stage, and branch-specific implementations stay
grouped under their own branch module/file. A data-structure file places the
primary struct/enum first, followed by constructors, invariants, and operations
in dependency order. Rust type declarations may precede a function only when
forward references or mutually recursive types require it; unrelated helpers
must not appear before the file's main responsibility.

For example, `verify_non_equational_fact.rs` should read conceptually as:

```text
verify_non_equational_fact
  -> verify_non_equational_fact_well_definedness
  -> search_non_equational_fact_proof
      -> search_by_cache
      -> search_by_builtin_rule
      -> search_by_known_fact
```

The same rule applies to dispatchers: `exec_stmt.rs` owns `exec_stmt`, then its
direct branch functions or modules appear in enum/source order. Do not split one
main algorithm across files merely because helpers have similar names; split
only when a data structure or branch owns an independent responsibility.

### Pipeline result rule

For every non-trivial pipeline function `f_xxx`, define a dedicated
`FxxxResult` struct. Its fields must appear in the same order as the
successful stages executed by `f_xxx`. Each field must contain the typed
result or evidence produced by that stage.

Use a struct field when a stage is mandatory.
Use an enum when the stage selects one mutually exclusive route.
Use a nested result type when a selected route has its own sub-pipeline.

The outer `Result<T, E>` represents operational failure.
The inner `T` represents a successfully completed pipeline.
Do not encode stage failure as a successful status variant.

### Dispatcher result rule

For every dispatcher `dispatch_xxx` or `exec_xxx` whose input is an enum,
define a result enum that mirrors the input enum recursively. Every input
constructor must have a corresponding result constructor containing the
dedicated branch function's result type.

Do not flatten branch-specific results into one generic struct.
Do not use a wildcard branch in the final exhaustive dispatcher.

## Critical: Proof vs Result

Hard naming and ownership rule for soft-success / soft-fail outcomes
(WD, search-proof, verify, exec):

```text
*Proof   = success evidence only (never embeds soft-fail)
*Result  = Success(*Proof | *SuccessResult) | Failed(...)
           (or an enum with explicit Fail* variants, e.g. Obj WD)

Do not put Fail inside a *Proof and scan with is_failed() on that Proof.
is_failed() is only a thin match on a real *Result enum.
```

Examples in `src/`:

- `AtomicFactWellDefinedProof` — success-only parameter WD evidence
- `VerifyAtomicFactWellDefinedResult` — `Success(Proof) | Failed(reason)`
- `FactWellDefinedProof` / `VerifyFactWellDefinedResult` — same split
- `VerifyObjWellDefinedResult` — `ByKnown | ByDef | FailToVerifyWellDefined`
- `ExecFactStmtResult` — `Success(...) | Failed(...)`

Soft `Failed` is not `RuntimeResult::Err` (SessionError).

## Builtin rule result ownership

Hard convention: **one Builtin rule ↔ one dedicated success-evidence struct.**

```text
*SearchProofByBuiltinRule  = enum dispatcher only
  VariantA(RuleAEvidenceStruct)
  VariantB(RuleBEvidenceStruct)

Do not share one payload struct across several rules.
Do not use “same math + order/tag field” to collapse rigid surface matchers.
Nested premises climb as typed fields on that rule’s struct (often VerifyFactResult).
```

Example: three or-trichotomy branch orders are three unrelated builtins and
three structs, even though the underlying real-line fact is the same.

## Decision criteria

```text
all stages must run              => struct field
mutually exclusive strategies    => enum variant
one strategy with required steps => struct
```

- Stage failure returns `Err`; later stages do not run.
- Do not replace real stage results with a vague `status` field.
- Name `...WellDefinedResult` when the stage carries cache hits, expansion,
  allocated IDs, or other typed stage data.
- Name `...WellDefinedProof` only when the value is a pure proof object.
- `searched_proof` means the finally selected successful proof route.
  If failed attempts must be retained, add a separate `search_trace`; do not
  overload `searched_proof`.
- Unable-to-search / unknown outcomes belong in `Ok(VerifyFactResult::Unknown(...))`,
  not in `Err`. `Err` is reserved for real operational / invariant failures.
  Top-level statement proof failure is `Ok(ExecStmtResult::Failed)` after the
  temp env is discarded (no merge). Nested must-prove checks inside a stmt
  still reject verify `Unknown` at their boundary and must not `?`-propagate
  it as proven evidence. Callers outside `execute` must go through `exec_stmt`
  only — never call `exec_xxx_stmt` directly.

## Subject inclusion

```rust
// Result consumed only on the current call chain: do not duplicate the subject
pub struct VerifyNonEquationalFactResult {
    pub verify_well_defined_result: VerifyAtomicFactWellDefinedResult,
    pub searched_proof: NonEquationalFactSearchedProof,
}

// Result cached, printed, persisted, or used without the original input: keep subject
pub struct VerifyNonEquationalFactResult {
    pub fact: AtomicFact,
    pub verify_well_defined_result: VerifyAtomicFactWellDefinedResult,
    pub searched_proof: NonEquationalFactSearchedProof,
}
```

## Minimal shapes

Sequential pipeline:

```rust
pub struct VerifyNonEquationalFactResult {
    pub verify_well_defined_result: VerifyAtomicFactWellDefinedResult,
    pub searched_proof: NonEquationalFactSearchedProof,
}
```

Search stage (one successful route):

```rust
pub enum NonEquationalFactSearchedProof {
    ByCache(CacheSearchProof),
    ByBuiltinRule(NonEquationalFactSearchProofByBuiltinRule),
    ByKnownAtomicFact(NonEquationalFactSearchedProofByKnownAtomicFact),
    ByBuiltinStrategy(NonEquationalFactSearchProofByBuiltinStrategy),
    ByKnownForallFact(NonEquationalFactSearchedProofByKnownForallFact),
    ByBuiltinAlgebraicRewrite(
        NonEquationalFactSearchProofByBuiltinAlgebraicRewrite,
    ),
}
```

Dispatcher mirroring input:

```rust
pub enum ExecStmtResult {
    Fact(ExecFactStmtResult),
    Definition(ExecDefinitionStmtResult),
    Unsafe(ExecUnsafeStmtResult),
}
```

Fact verification mostly mirrors `Fact`; atomic facts are flattened so
`Equality` and `AtomicExceptEquality` sit directly on `VerifyFactResult`
(no intermediate `AtomicFact` / `VerifyAtomicFactResult` layer). Consumers
match the same equality-vs-other split as `verify_atomic_fact`.

## Implementation constraints

- Keep implementation stage order identical to result field order.
- Each input enum constructor calls one dedicated `exec_xxx` / `verify_xxx`
  function whose return type fills the matching result constructor.
- `_ => Unsupported` is allowed only as a temporary tracer-phase placeholder,
  never as final architecture.
- Do not keep long-lived parallel Draft and final result type families for the
  same pipeline. Distinguish temporary draft types only while migrating; delete
  or rename them to the canonical names when the pipeline stabilizes.
- Unify naming across well-defined and object-verification results; prefer one
  vocabulary (`Verify*Result`, `*WellDefinedResult`, `*SearchedProof`) instead
  of mixing Proof/Result/Draft names for the same role.

## Checklist

When adding or changing a pipeline/dispatcher return type:

- [ ] Result type name matches the owning function.
- [ ] Struct fields match successful stage order one-to-one.
- [ ] Search/route selection is an enum, not a bag of options.
- [ ] Nested routes that are themselves pipelines have nested result types.
- [ ] Dispatcher result enum recursively mirrors the input enum.
- [ ] No wildcard catch-all in the final exhaustive dispatcher.
- [ ] Stage failures that are true operational errors are `Err`.
      Unable-to-prove is `Ok(VerifyFactResult::Unknown)`, not `Err`.
- [ ] Subject is included only when the result outlives the call-chain input.
- [ ] `searched_proof` is the winning route only; traces stay separate if needed.

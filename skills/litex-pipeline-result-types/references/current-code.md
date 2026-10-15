# Current-code alignment notes

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


These notes record the audit that produced this skill. Update them when the
repository converges on the canonical shapes.

## Already aligned

- `verify_non_equational_atomic_fact` already follows WD-then-search as a
  stage-ordered pipeline result.
- `exec_stmt` is the only public statement entry: temp ExecEnv, then
  `Success|Failed` with merge-on-success; branch `exec_xxx_stmt` stay
  execute-module private.
- Leaf exec `*Result` uses `Success | Failed` (soft miss stays Failed).
- Atomic/fact WD follows Proof vs Result: `*WellDefinedProof` is
  success-only; `VerifyAtomicFactWellDefinedResult` /
  `VerifyFactWellDefinedResult` are `Success(Proof) | Failed(...)`.
- Object WD top-level is already an enum with Fail variant
  (`VerifyObjWellDefinedResult`).

## Needs unification

- File layout does not yet consistently follow the main-responsibility rule.
  Several pipeline entry points live in files named
  `verification_and_result.rs`, `well_defined.rs`, or `result.rs`; these names
  describe a role rather than the file's main algorithm or data structure. The
  target layout is one main responsibility per file, with algorithm filenames
  matching their main operation and direct sub-pipeline functions following it
  in call order.
- `execute_let_stmt.rs` contains `exec_let_obj` rather than the canonical
  `exec_let_obj_stmt` name, so its filename and entry function are not yet an
  exact match.
- `verify_equal_fact.rs` is already closer to the target naming; its function
  ordering should still be checked against the WD-then-search call sequence.

- Distinguish temporary draft types from final types. Do not keep
  `DraftVerifyEqualityResult` and `VerifyEqualityResult` as long-lived parallel
  families for the same pipeline.
- Unify naming among temporary draft WD types toward
  `...WellDefinedResult` / `Verify*Result` vocabulary; keep `*Proof` only
  for success-only evidence (see Proof vs Result in `SKILL.md`).
- `ParamTypeWellDefinedProof` and `ObjWellDefinedProofByDef` still allow
  Fail to sit under a Proof-shaped name / bag; fold them into the same
  Proof vs Result split in a later pass.
- Soft miss for fact verify is `FailToVerifyWellDefined` /
  `FailToSearchProof` on `VerifyFactResult` (not a legacy `Unknown` name).
  Search aggregators return `Ok(None)` on exhaustion; verify entry points
  map that to `Ok(FailToSearchProof)`. Must-prove exec/WD callers reject
  soft miss at their boundary.
- Keep `searched_proof` as the finally selected proof route. If failed attempts
  must be retained later, add `search_trace` separately.

## Direction

The current direction is correct. Subsequent work should make every non-trivial
verify/exec pipeline and every enum dispatcher follow the formal rules in
`SKILL.md`, using the examples in `examples.md` as the target shapes.

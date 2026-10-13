# Test Matrix

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Choose tests by semantic impact. Do not treat repository-wide testing as the
default endpoint of every kernel change.

## Required impact card

Record before testing:

```text
Change class: <L0-L5 and name>
Affected domain: <domain>
Shared contracts changed: <none or exact contracts>
Focused tracer: <path/test>
Selected gates: <commands or suite names>
Explicitly skipped: <broader gates and why>
Escalation: <none or evidence-backed reason>
```

## Impact levels

| Level | Change shape | Required gates |
| --- | --- | --- |
| L0 | Documentation/comments only | Touched snippet/document gate only |
| L1 | One leaf builtin/infer/matcher/diagnostic | Exact positive, nearest executable negative, direct tracer `.lit` |
| L2 | One subsystem or rule family | Focused tests for that module/family and directly affected artifacts |
| L3 | Shared producer/consumer contract | Focused tests on both sides plus the exact contract suite |
| L4 | Core representation/global control flow/public syntax/test harness | Full-kernel gate |
| L5 | Version/dependency/toolchain/package/release | Full-release gate |

Classify by fan-out, not changed-line count. Do not promote L1/L2 to L4 without
a concrete changed contract. A one-line shared-enum or dispatcher change may
be L4; a large implementation inside one isolated leaf may remain L1/L2.

## L1 leaf builtin or infer rule

Treat the change as L1 only when it changes a leaf handler or rule schema and
rule-specific tests/artifacts, while leaving dispatcher/search order,
recursion/fuel, memo/transaction state, evidence types, compiler IR, and
public output unchanged.

Run only:

1. the exact positive Rust regression or generated rule-contract test;
2. the nearest executable negative boundary;
3. the corresponding persistent `.lit` tracer directly, for example:

   `target/release/litex -compact -isolated -runner -f examples/02_builtin_math/<rule>.lit`

If the tracer is a registered project file, use
`target/release/litex -compact -runner -f <file.lit>` instead. Require top-level
`ok: true` and exit code `0`.

Do not run `run_examples`, the docs harness, `run_all`, all Rust tests, or the
To-Lean suite for this L1 case. If a catalog rule has a required paired Lean
adapter, run only its generated adapter contract and exact real-Lean check.

## Escalation triggers

- Several rules or shared helpers within one family: L2; run that family's
  module filter and directly affected examples.
- Dispatcher, search order, recursion/fuel, or family ownership: L3/L4.
- Runtime environment, memoization, rollback, WD IDs/DAGs, or `FactId`: L3;
  run focused producer/consumer contracts.
- `BuiltinRuleEvidence`, compiler capture, Litex-to-Lean IR/lowering/emission,
  shared Lean theorem, or ABI: L3; run the focused To-Lean domain gates.
- Core `Stmt`/`Fact`/`Obj` representation, module system, public syntax, or
  test harness: L4; run full-kernel.
- Version/dependency/toolchain/package/release: L5; run full-release.

If focused failures expose a wider dependency, update the impact card and
escalate one justified level. Do not escalate merely because the changed file
lives under `src/verify/` or because a larger command feels safer.

## Command routing

- Build once with `cargo build --release`; never use `target/debug/litex` or
  default-profile `cargo test` for this workflow.
- Standalone scratch tracer:
  `target/release/litex -compact -isolated -runner -f <allocated-draft-file.lit>`.
- Registered project file:
  `target/release/litex -compact -runner -f <file.lit>`.
- Examples harness, only when selected by L2-L4 impact:
  `cargo test --release run_examples -- --nocapture`.
- Mechanics textbook, only when touched or selected by a shared-contract
  escalation:
  `python3 scripts/textbook_gate.py The-Mechanics-of-Litex-Proof`.
- MATH500 local snippets, only for that dataset/domain:
  `cargo test --release run_math500_litex_simple -- --nocapture`.
- Complete Litex module:
  `target/release/litex -compact -runner -r <module>`.

Do not call the current `run_all` a full repository gate without auditing its
implementation. State exact commands and coverage until a canonical
full-kernel/full-release runner exists. Do not report bare `cargo test` timing
as user-facing Litex performance. Report strange diagnostics even when a proof
succeeds.

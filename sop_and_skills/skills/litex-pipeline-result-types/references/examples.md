# Pipeline and dispatcher result examples

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


These examples are the canonical shapes for Litex `src/` result types.

## Sequential pipeline: non-equational atomic fact

Function:

```rust
fn verify_atomic_except_equality(
    &mut self,
    fact: &AtomicFact,
    state: VerifyState,
) -> RuntimeResult<VerifyFactResult>
```

Stages:

```text
1. verify well-definedness
2. search proof  (Ok(None) on exhaustion → VerifyFactResult::Unknown)
```

On success the payload is `VerifyFactResult::AtomicExceptEquality(...)`
carrying the stage-ordered struct `VerifyAtomicExceptEqualityFactResult`.
Unable-to-prove is `Ok(VerifyFactResult::Unknown(...))`, not `Err`.
## Search stage: mutually exclusive routes

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

pub struct NonEquationalFactSearchedProofByKnownAtomicFact {
    pub cite_fact_id: FactId,
    pub proof_that_parameters_match: Vec<VerifyFactResult>,
}
```

## Other pipelines

Equality:

```rust
pub struct VerifyEqualityFactResult {
    pub verify_well_defined_result: VerifyAtomicFactWellDefinedResult,
    pub searched_proof: EqualityFactSearchedProof,
}
```

And-fact (every conjunct must be proved; no strategy-selection enum):

```rust
pub struct VerifyAndFactResult {
    pub verify_well_defined_result: AndFactWellDefinedResult,
    pub proof_of_each_conjunct: Vec<VerifyFactResult>,
}
```

Exist-fact outer dispatch, then plain-exist pipeline:

```rust
pub enum VerifyExistFactResult {
    Plain(VerifyPlainExistFactResult),
    Unique(VerifyExistUniqueFactResult),
    NotExist(VerifyNotExistFactResult),
}

pub struct VerifyPlainExistFactResult {
    pub verify_well_defined_result: ExistFactWellDefinedResult,
    pub searched_proof: PlainExistFactSearchedProof,
}
```

## Dispatcher: mirror input enum

Top-level statement entry is **only** `exec_stmt` (temp env + merge). Branch
`exec_xxx_stmt` functions are execute-module private.

```rust
pub enum ExecStmtResult {
    Success(ExecStmtSuccess),
    Failed(ExecStmtFailed),
}

pub enum ExecStmtSuccess {
    Fact(ExecFactStmtResult),
    Definition(ExecDefinitionStmtResult),
    Unsafe(ExecUnsafeStmtResult),
}

pub enum ExecDefinitionStmtResult {
    LetObj(ExecLetObjStmtResult),
    DefProp(ExecDefPropStmtResult),
}

// exec_stmt: push temp → match Stmt → exec_xxx on current top →
// Failed discard / Success merge_from(temp)
```

Rule:

```text
Input enum has N semantic branches => result enum has N corresponding branches.
Each branch calls one dedicated exec_xxx_stmt function.
Final code must not hide unconnected branches with `_ => Unsupported`.
```

Early development may use `_ => Unsupported` only as a temporary tracer-phase
state, never as final architecture.

## VerifyFactResult mirrors Fact, with atomic flattened

Atomic facts are split at the top level (no intermediate AtomicFact layer):

```rust
pub enum VerifyFactResult {
    Unknown(UnknownVerifyFactResult),
    Equality(Box<VerifyEqualityResult>),
    AtomicExceptEquality(Box<VerifyAtomicExceptEqualityFactResult>),
    AndFact(Box<VerifyAndFactResult>),
    ChainFact(Box<VerifyChainFactResult>),
    OrFact(Box<VerifyOrFactResult>),
    ExistFact(Box<VerifyExistFactResult>),
    ForallFact(Box<VerifyForallFactResult>),
    ForallFactWithIff(Box<VerifyForallFactWithIffResult>),
    NotForall(Box<VerifyNotForallFactResult>),
}
```

Type tree:

```text
Fact
└── VerifyFactResult
    ├── Equality
    ├── AtomicExceptEquality
    ├── AndFact
    ├── ChainFact
    ├── ExistFact
    │   ├── Plain
    │   ├── Unique
    │   └── NotExist
    └── ...
```

Consumers process results along the same structure as the AST; they should not
guess what a generic result bag contains.

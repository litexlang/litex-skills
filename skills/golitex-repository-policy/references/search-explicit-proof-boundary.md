# Search and explicit proof boundary

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


This records the maintainer's working agreement approved on 2026-10-04:
authors supply meaningful proof steps; Litex checks them with bounded local
reasoning. Default automation must balance author effort, verifier cost and
maintenance. The examples demonstrate the agreement, not universal fixes
mined from a single failure. This document does not authorize kernel, AST,
Env/Runtime, search-policy or test-expectation changes.

Read this when deciding whether a failed goal needs an explicit proof, missing
structural support, reusable mathematics or a verifier repair. Use current
source and fresh evidence for implementation claims. Numerical stage ceilings,
CLI flags and supported constructors are version-dependent and do not belong
in the permanent decision rule.

## Separate three capabilities

1. **Expression:** can the intended object/fact and its domains be represented?
2. **Checking:** can an explicit proof of that same statement be verified?
3. **Discovery:** can the default search find that proof without the explicit
   steps in the current context and permissions?

A discovery miss alone proves neither falsity nor a kernel defect. An accepted
explicit route proves checkability, not that the shorter route works. Keep
intentional limits, unresolved causes and violated contracts distinct. A
workaround does not by itself establish that the implementation is correct.

## Divide responsibility by the work, not by step count

- The verifier should reliably consume available facts and checked equality
  paths, perform supported exact computations and handle supported uniform
  structural obligations. Keep WD, scope, provenance and rollback intact.
- Authors choose meaningful intermediate expressions, witnesses, cases,
  induction parameters, recursive unfoldings and semantic lemmas. Verify that
  the proposed steps work; do not ask search to invent every missing route.
  Fixed-shape builtin rules may already solve particular instances of these
  tasks; do not infer a prohibition from a syntax category such as `exist`.
- Repeatedly needed mathematics may justify a checked theorem, domain library
  or bounded strategy. Naming a theorem does not automatically make it a
  background search candidate. Use its actual supported invocation interface.
- Uniform descent through strictly smaller supported constructors may justify
  structural automation. Parent and child fact families need not match.
  Inspect the entire proof tree, leaf permissions and certificate assembly.
  Repetition alone, or changing mathematical families, is not decisive.
- Treat structural automation as a design criterion, not a promise that every
  build supports every nesting. An existing explicit route may remain the
  accepted authoring interface. Propose any convenience enhancement separately.

There is no general "one automatic step" rule. A long deterministic traversal
can be appropriate; one mathematically short sentence can require expensive
choices. Strict descent establishes a termination argument for that traversal,
not a bound on candidate count, expression expansion, integer size, enumeration
or the whole runtime.

## Diagnose before choosing a repair

Preserve the target, premises, carriers and relevant context. Locate the first
failed phase: expression/binding, WD, truth search, explicit proof execution,
publication/use, scope, computation or output/evidence.

Try the shortest reader-meaningful explicit route for the same mathematics:
an equality endpoint, named theorem, witness or supported proof structure.
Do not add unproved assumptions, weaken the goal, change a return carrier or
insert `trust` to demonstrate checkability.

If that route checks and the maintainer accepts it, a missing shortcut is not
a mandatory kernel repair for that task. Preserve the original input as an
automation-capability observation; do not turn a true but unsupported goal
into a mathematical must-reject test or silently reverse its existing manifest
expectation. Missing conditions and false conclusions are separate controls.

Inspect each added step's role. Selecting a mathematical move generally
belongs in the proof. Repeating mechanical carriers or transporting already
checked evidence can reveal missing shared support or a consumer defect.
Do not immediately immortalize such workarounds as authoring style.

If the explicit route fails, identify the earliest unsupported obligation and
its producer/consumer before proposing broader search. An outer `search_proof`
label cannot determine the cause. Incorrect acceptance, broken evidence,
crashes, leakage or output misreporting require their own contract diagnosis;
they cannot all be explained by limited automation.

Follow existing repair ownership and protected-structure gates. New
mathematics, a missing local evidence consumer and a global representation or
search change are different interventions.

## Three representative examples

These complete snippets were checked independently in the 2026-10-04
documentation task, with one release binary and unchanged Rust source during
the probe window. They contain no trust. Repository-relative origins and the
receipt are listed below; these dated results are not promises about later
versions. Do not prescribe their names or exact spelling for unrelated tasks.

### Supported structural typing

```litex
have n N
((n+1)+1)+1 $in N
```

The verifier handles the supported addition tree without asking the author to
publish a carrier at every layer. That does not justify arbitrary natural
subtraction: `have n N` followed by `n - 1 $in N` was rejected in the same
window. Missing leaf/domain evidence must remain a miss.

### Supply an equality endpoint, then reuse it

```litex
have x R = 2
have y R = x + 1
y = x + 1 = 3
y^2 = 9
```

The author exposes the definition-to-value route. The checked chain's endpoint
is available to the following fact; do not repeat the derivation solely to
reuse it. The corresponding false chain `y = x + 1 = 4` was rejected.

### Supply a recursive unfolding

```litex
have fn f(n N) N by induc n from 0:
    case n = 0: 0
    case n >= 1: f(n - 1) + 1
f(0) = 0
f(1 - 1) = f(0) = 0
f(1) = f(1 - 1) + 1 = 0 + 1 = 1
```

The function is user-defined; its final value is not an intrinsic builtin fact.
The proof gives the recursive equation, the established child value and the
arithmetic residual. With the same definition and `f(0) = 0`, the bare
`f(1) = 1` probe was rejected. Changing the explicit chain's final value to
`2` also rejected. The explicit proof is the accepted interface; this example
does not require an unrestricted recursive evaluator or search expansion.

## Evaluate proposed automation

State the trigger, exact generated obligations, decreasing measure when
applicable, leaf permissions, candidate/computation limits and proof evidence.
No child WD/helper should silently restore broader permissions. Do not add
one Obj/Stmt/caller exception for each new example.

Measure both costs: meaningful author steps, and verifier work as context and
objects grow. Do not claim a performance or maintenance improvement without
comparison evidence. A finite Boolean normalization can still expand
exponentially; a closed exact calculation can still be large.

For an actual implementation, verify the promised direct route and the
explicit route, nearby false/missing-premise/invalid-domain controls, failed
publication and actual provenance. Maintain unsupported compiler/replay
boundaries separately. This agreement alone is not evidence that an untested
enhancement works, nor a reason to upgrade a local task to full-release testing.

## Evidence and destinations

Resolve these paths against the active golitex checkout when available:

- `examples/proof_nodes/atomic/direct_structural_membership.lit`
- `examples/proof_nodes/chain/named_definition_endpoint.lit`
- `examples/test_statements/boundaries/recursive-increment-explicit-chain.lit`
- `examples/test_statements/experience/problem_notes/K004-explicit-recursive-increment-chain.md`
- `docs/audits/search-boundary-skill-blueprint-2026-10-04.json`
- `plan/搜索与显式证明边界.md` (broader evidence synthesis; recommendations
  there are not blanket implementation promises)

The public explanation belongs in the collapsed example discussion in section
1.1 of both Litex Blueprints. Keep dated failures, internal search schedules
and raw receipts in working references; public prose should explain the
mathematical division of labor and its cost tradeoff.

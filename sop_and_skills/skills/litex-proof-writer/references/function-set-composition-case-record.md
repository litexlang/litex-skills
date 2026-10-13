# Function-set composition: checked case record

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Recorded 2026-10-04 in golitex. This is a worked case record with dated
acceptance, not a permanent kernel contract or permission to change semantics.
Historical limitations can disappear. Prefer an already supported shorter
proof when current execution accepts it; recheck a proposed bridge in its real
caller before adopting it. The canonical repository policy owns execution,
authorization and promotion gates.

Contents: scope and decisions; worked examples; controls and receipts;
remaining boundaries; test-entry correction.

## Scope and decision procedure

The user explicitly accepted a few meaningful proof steps instead of broader
automatic search for this function-set task. Preserve that scoped preference
when continuing this work. It does not authorize trust, weakening a theorem,
changing carriers, or declaring a kernel defect solved by a workaround.

The examples illustrate existing proof-style decisions:

| Earliest boundary | What the record establishes |
| --- | --- |
| Object/field WD | A field equation cannot repair an expression that is itself illegal. A checked typed binding supplied the field view in this case. |
| Membership/signature | Function-space membership supplies the signature, not the concrete function value. Application still needs its domain/guards. |
| Equality/search | An explicit intermediate value or carrier equation can select the intended proof route without broad unfolding. |
| Numeric evaluation | Known, checked function bodies allowed bounded substitution followed by exact arithmetic; false values and bad domains remained rejected. |
| Diagnostics | A failed template's outer phase alone did not identify the failed obligation; existing child results needed output projection. |

These are examples of existing principles, not new unconditional requirements
to use typed aliases or rewrite every direct call. Broader technical rule
promotion still needs independent evidence and held-out behavioral validation.

## Checked worked examples

### Template and returned-function aliases

```litex
template<a R>:
    have fn shift(x R) R = x + a
let shift_two = \shift<2>
shift_two(3) = \shift<2>(3) = 5
```

P01/T05 accepted the explicit specialization in the chain. P03/H05 accepted
`add_two(3) = add(2)(3) = 5` for a typed returned-function binding. This does
not establish that all aliases require such chains; earlier callable-alias
evidence in `authoring-error-cards.md` remains relevant to its own callers.

The separately authorized numeric enhancement accepted direct curried calls
and returned-function membership:

```litex
have fn add(x R) fn(y R) R = fn(y R) R {x + y}
add(2) $in fn(y R) R
add(2)(3) $in R
add(2)(3) = 5
add(1 / 3)(1 / 6) = 1 / 2
add(0.1)(0.2) = 0.3
```

H01/E01 cover direct behavior; N17/N21 reject false results and a nearby
decimal. The recorded implementation checks applications, selected bodies and
guards, retains source evidence, and bounds normalization. It does not execute
algorithms or broaden global proof-search permissions.

### Selected function-space carrier

```litex
template<A, B nonempty_set>:
    have maps set = fn(x A) B
$is_set(\maps<R, Z>)
\maps<R, Z> = fn(x R) Z
fn(x R) Z {0} $in \maps<R, Z>
have f \maps<R, Z> = fn(x R) Z {0}
f(2) = 0
```

P05/T03/D05 accepted the concrete carrier equation before membership and
binding. It preserves the selected interface and final value.

### Callable struct field

```litex
struct Box:
    op fn(x R) R
    tag N
have fn step(x R) R = x + 1
template<a R>:
    have box &Box = (step, 0)
\box<2> = (step, 0)
have selected &Box = \box<2>
selected.op = step
selected.op $in fn(x R) R
selected.op(3) = step(3) = 4
```

P02/D08 accepted all steps; P06/D09 cover a function-returned struct and its
result-membership goal. Both raw `\box<2>.op = step` and raw field membership
failed WD in either premise order: the receiver lacked a definition-time
struct view. This typed route was accepted by the user; it did not repair that
view propagation. Removing the tuple equation caused the field equation/call
to fail search in the recorded deletion probe.

### General constructor fact before a captured closure

With the same Box declaration, P07/S07 and P08/S08 first checked:

```litex
forall f fn(x R) R:
    (f, 0) $in &Box
```

The closure-valued template/function then retained
`(fn(x R) R {x + a}, 0)` and carrier `&Box`, using the same tuple/typed-view
route. The original closure-specific `forall a R` claim had verified, but its
later definition use failed. The general fact supplied a working interface;
the original capture/binder matching cause was not diagnosed or repaired.
Do not turn this single matching observation into a ban on closure-specific
lemmas. N25 rejected tag -1 even after the general constructor fact succeeded.

### Fixed signature with an exact output property

Independent Round14 migration retained the singleton construction while
moving a parameter-dependent output property outside the fixed signature:

```litex
have fn singleton(x R) power_set(R) = {x}
forall y R:
    singleton(y) $in power_set({y})
have a R = 1
singleton(a) $in power_set(R)
singleton(a) $in power_set({a})
```

The whole file passed and an incorrect universal `power_set({0})` property
rejected. This preserved the exact output specification without restoring
dependent-return signature syntax. In contrast, old `let F = fn(x R) x` was
an invalid positive; its replacement deliberately tested a different valid
family interface and N27 retained the original rejection.

## Acceptance and retained evidence

Resolve these paths from the current golitex Git root, not this skill folder:

- `examples/test_function_sets/proof_journals/numeric_evaluation_2026-10-04.json`
  records checked evaluation and domain/precision boundaries.
- `examples/test_function_sets/proof_journals/explicit_bridges_2026-10-04.json`
  records explicit routes and deletion controls.
- `examples/test_function_sets/proof_journals/cleanup_2026-10-04.json` records
  twenty session frames and clean-file outcomes, including both field-premise
  orders. Replayed/copied instances are one evidence family, not independent
  confirmations.
- `examples/test_function_sets/cleanup_2026-10-04.json` records 85/85 supported
  cases: 58 accepted positives and 27 correctly rejected negatives. N22–N24
  reject false chain values; N25 rejects a bad tag; N26 checks the actual
  nested template membership failure; N27 rejects the invalid old signature.
- `examples/test_function_sets/cleanup_tests_2026-10-04.json` records 42 passing
  focused Rust tests and stable source/binary identity at that gate.
- `examples/test_function_sets/capabilities_2026-10-04.json` separately records
  ten rejected direct claims with `matches: null`. Rejection of a true claim
  is an observation, not a passing mathematical negative.
- `plan/迁移的plan/proof_journals/example-authoring-round14-2026-10-04.json`
  records the independent fixed-carrier migration and wrong-property control.
- `examples/test_function_sets/acceptance.md`,
  `examples/test_function_sets/todo.md` and
  `examples/test_function_sets/summary_observations_2026-10-04.json` own the current disposition and method
  corrections. Prefer them to a stale skill snapshot.

Focused corpus commands recorded by this task:

```sh
python3 examples/test_function_sets/run.py
python3 examples/test_function_sets/run.py --capabilities
python3 examples/test_objs/run.py --object fn_set
cargo test --release --lib json_output::template_failure_tests
```

The then-current CLI used `-strict`, `-f`/`-e`, `success` and `session_error`.
Persistent proof probes used discarded `sketch:` frames because `try:`,
`-before`, `-runner` and `-compact` were unavailable. Check the current CLI
before copying older command conventions. Each positive needs the successful
envelope and expected statement statuses; each negative needs successful setup
followed by the intended rejection, rather than a crash or protocol error.

## Boundaries and confidence

No false acceptance was observed in the recorded controls. This does not
prove that the whole verifier has no bugs or soundness vulnerabilities. The
user's priority is correct proofs and rejected false claims; optional direct
shortcuts must not be obtained by bypassing WD, guards or proof evidence.

Raw selected/returned field views, captured-closure matching and selected
shortcuts remain dated capability boundaries with usable authoring routes.
Do not silently mark the original interfaces repaired.

An accepted diagnostic-test draft left an input-domain question:

```litex
template<a power_set(1)>:
    have item R = 0
```

The inspected PowerSet WD owner checked child WD without an explicit
`$is_set` requirement. No soundness bug was established. Keep it
unclassified until the intended input contract and real public behavior are
audited; do not change a rule just to make a diagnostic fixture fail.

A subsequent shared-source build was blocked by concurrent eval/JSON edits.
The prior stable receipt is historical acceptance, not evidence that later
source currently compiles. Do not use a stale binary as a current-source gate.

## Public-entry correction

The test helper called `Runtime.parse` and `Runtime.exec_stmt` separately.
It observed a reserved name after execution failure, so same-name parsing
failed. That path bypassed `Runtime.run_litex_code`'s parse-name transaction.
The production owner already rolls parse bindings back on failed execution
and errors. The helper observation must not be reported as a confirmed CLI
same-name retry defect; the proposed fresh CLI recheck was blocked by the
later shared-source build failure.

Use low-level tests to inspect the corresponding stage or JSON projection.
Use the actual public pipeline for claims about session recovery, name/scope
lifecycle, imports and end-user behavior. The statement execution still goes
through `Runtime::exec_stmt`; invoking it alone does not test wrappers that
begin before parsing.

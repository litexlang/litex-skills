# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Concept Modeler

Model the mathematical world and its usable interfaces before proving facts
inside it. Use the smallest mode that covers the task.

## Repository policy

In the golitex repository, apply `$golitex-repository-policy` alongside this
skill and read its canonical bundled policy completely. Do not restate or
override its verifier, trust, textbook-boundary, documentation, or JSON
proof-block journal rules here.

For interface verification, use the policy's persistent release session and
literal outermost `try:` blocks. Record every materially distinct attempt and
every accepted block in the task's JSON proof-block journal. Do not edit the
target `.lit` file during the inner loop. Materialize only a contiguous
accepted prefix at a coherent checkpoint, then run the clean release
`-runner -f` gate and require top-level `ok: true` plus exit code `0`.

## Definition strictness

When writing or revising definitions, apply `$litex-strict-definitions`.
Prefer the stricter form: put carriers, parameter domains, and concept-owned
nondegeneracy inside the definition itself. Do not leave those invariants to
later proofs, comments, or silent convention even if a slightly looser
surface looks locally fine. After a strength change, align dependent `forall`
goals and comments; do not weaken the definition to spare an old proof.

## Derive the model forward

Model in this direction: source mathematics and independently justified
definitions; carriers and semantic roles; domain invariants; orthogonal
relations, objects, functions, structures, and epistemic status; typed
dependencies; Litex forms and signatures; immediate use probes. The desired
downstream theorem or convenient current syntax may reveal a required use, but
must not determine the upstream definition or smuggle its conclusion into a
predicate, wrapper, premise, or selected value.

Use backward reasoning only to audit whether the model supports its intended
consumers and to locate missing prerequisites. If a use probe fails, return to
the earliest incorrect carrier, role, dependency, or interface and re-derive
the later nodes; do not add an adapter merely to make that probe pass. Apply
the counterfactual check: if the motivating final theorem were hidden, would
each concept and dependency still have its stated mathematical meaning and an
independent reason to exist?

## Tracer bullet

Select one concept whose downstream use exposes the important modeling
decision. Show its ordinary meaning, rejected nearest form, chosen interface,
and one immediate use before explaining the wider ontology or dependency
graph. Tie every abstract modeling term back to the corresponding declaration
or use in that tracer.

Use the minimum of a nonempty natural-number subset as the fixed example:
separate `$is_minimum_of_natural_subset(X, n)` as the relation, prove unique
existence, expose `min_of_N_subset(X)` with `have fn ... by exist!`, and consume
the selected value in the increasing enumeration of the subset. This shows why
the relation is a `prop`, the canonical value is a function, and the use probe
decides whether the interface is usable. Choose an analogous task-specific
concept for real work.

When the modeling work drives a major Litex interface migration, create the
persistent acceptance artifact required by the repository policy. Keep the
rejected former declaration/use as commented Litex and the selected interface
plus immediate use unprefixed; point the note to the registered implementation
and its clean verification command.

## Modes

### Interface mode

Use for one definition, construction, notation, or small group of tightly
related interfaces. Decide the semantic role, Litex form, exact carrier and
signature, immediate downstream use, and verification status. Do not require a
chapter-wide inventory or dependency graph when the local interface is the
whole task.

Read [`references/concept-forms.md`](concept-forms.md) completely.
When the choice is non-obvious, involves a function-versus-prop decision,
unique selection, restricted function, set-valued construction, exact carrier,
or template, also read
[`references/construct-selection.md`](construct-selection.md)
completely.

### Domain mode

Use for a mathematical subject, textbook, chapter, module, or substantial
library surface. Inventory the important concepts, design their ideal
interfaces, build a typed dependency DAG, preserve source order where
possible, and produce an implementation sequence.

Read both
[`references/concept-forms.md`](concept-forms.md) and
[`references/dependency-dag.md`](dependency-dag.md) completely.
Read
[`references/construct-selection.md`](construct-selection.md)
when any core interface is ambiguous. When module documentation is in scope,
also read
[`references/module-documentation.md`](module-documentation.md).

## Three independent axes

For textbook concepts that bundle data and laws, use one primary `struct`
interface and put the mathematical laws directly in its definition. This is
the user's explicit 2026-10-09 preference. Do not first create a parallel
law-certificate `prop`, then a struct referencing it, then theorems proving
that struct members satisfy that same certificate. Use native struct opening
for definitional consequences. Retain a separate `prop` only for an
independent mathematical relation or a real unbundled use; constructor
bookkeeping alone does not justify it. Subspace, independence, and basis
relations remain propositions. Keep genuine construction and transport proofs.

Never put `template`, object, `prop`, theorem, and `trust` into one flat
ontology. Record:

1. **Semantic role**: carrier, object, function, canonical selection,
   relation, structure, declaration family, or mathematical result.
2. **Litex form**: builtin, parameter, `have`, `have fn`,
   `have fn ... by exist!`, `prop`, `struct`, `template`, direct fact,
   `claim`, `thm`, or `axiom`.
3. **Epistemic status**: designed, checked, axiomatic, trusted proof debt, or
   blocked by an exact syntax, kernel, library, existence, uniqueness, or
   well-definedness obligation.

`trust` is never a semantic role. Proof moves such as `witness`, `obtain`,
`by cases`, `by contra`, and `by induc` establish facts; they are not concepts.

## Shared workflow

### 1. Set scope and source of truth

Identify the source boundary, included and excluded material, intended
downstream consumers, and existing module documentation. Preserve source
terminology, theorem identity, carrier choices, and pedagogical order.

For an existing top-level module, read its single `README.md` and
`math_collections.md` before changing core interfaces. For a textbook, resolve
its registered workspace through `scripts/.textbooks` and use the one module
under `scripts/<Workspace>/textbook/`.

### 2. State the downstream-use sentence

For every important concept, answer:

> What does the source introduce, and how must later mathematics use it?

Use that answer rather than source grammar to choose the semantic role and
Litex form:

- later code cites a value -> `have`;
- later code applies `f(x)` -> `have fn`;
- later code asserts `$P(x)` -> `prop`;
- later code projects named packaged fields -> `struct`, often with an
  `is_*` law predicate;
- later code instantiates `\Name<S>` and the declaration changes with `S` ->
  `template`;
- later code needs the unique value satisfying a relation -> prove unique
  existence, then expose `have fn ... by exist!`;
- later code should visibly cite an important result -> `thm`;
- a result serves only nearby reasoning -> direct fact or `claim`.

Parameters alone do not make a template. A theorem is not a substitute for
defining the concepts it talks about.

### 3. Inventory when using domain mode

Read the source front to back and collect carriers, objects, functions,
operations, constructors, relations, structures, declaration families,
canonical selections, named results, notation aliases, proof moves, explicit
assumptions, omitted proofs, and source ambiguities. Keep proof moves, examples,
and exercises separate from concepts.

Do not assume one source noun maps to one declaration. Split candidate
relations, existence, uniqueness, and selected values when later mathematics
needs distinct interfaces.

### 4. Draft the ideal interface

Record:

1. ordinary mathematical meaning;
2. semantic role;
3. chosen Litex form and why the nearest alternative is wrong;
4. minimal parameters, domains, codomain, and definition body;
5. exact source anchor or conventional identity;
6. one immediate downstream use probe;
7. direct dependencies; and
8. remaining proof, existence, uniqueness, well-definedness, parser, library,
   or kernel obligation.

Design the mathematically correct interface before accommodating current
implementation limits. If unsupported, keep the ideal form and expose the
exact blocker. Do not call it `checkable` until the real interface and use
probe pass.

### 5. Enforce construction discipline

- Keep a candidate relation and its selected value distinct.
- Preserve source names, domains, codomains, and construction boundaries.
- Build directly in the exact carrier required by the public interface.
- Do not rely on equality, membership, compatibility predicates, or wrappers
  to retype a broader value.
- Pass a larger-domain function through an explicit restricted function value
  when a consumer expects a smaller domain.
- Use `template` only when parameters change the declaration itself.
- Do not smuggle a theorem conclusion into an admissibility predicate.
- Require full dependent-record equality only when a real caller consumes it;
  otherwise prove the weakest payload or projection equality needed.
- Never use `trust`, `abstract_prop`, wrappers, or aliases to preserve a wrong
  semantic role.

### 6. Build the typed dependency DAG in domain mode

Create nodes for important carriers, declarations, canonical constructions,
intermediate results, and main results. Label edges by signature, definition,
well-definedness, law, existence, uniqueness, selection, proof, import, or
trust/source dependency.

Produce both a readable graph and a topological build order chosen to retain
source order as far as possible. Resolve accidental cycles by extracting a
primitive interface or separating a relation from its selected value; do not
hide cycles behind trusted wrappers.

### 7. Compare with existing code

Audit semantic kind, carrier, parameters, codomain, source identity,
downstream use, premises, conclusions, dependencies, namespaces, and
proof/trust status. Use available definition, relation, and fact graph output
to compare the actual dependency surface with the planned one.

Classify drift as modeling error, missing interface, implementation
limitation, proof debt, or documentation drift before editing.

### 8. Verify the smallest interface

Test the minimal definition plus one real use probe in the module context.
Follow the repository policy's JSON-first persistent-session workflow. Hand
verified interfaces to the textbook translator or proof writer only after the
foundational form is stable.

Update `README.md` only after the implemented public interface and
representative use probes verify. Keep ideal but unimplemented interfaces in
`math_collections.md`, not in the factual README.

## Required output

In interface mode, return:

1. semantic role;
2. chosen Litex form and rejected nearest alternative;
3. minimal interface;
4. immediate downstream use probe; and
5. checked or blocked status with exact evidence.

In domain mode, additionally return:

1. scope and source-of-truth statement;
2. concept inventory with source anchors and status;
3. ideal interface cards for the mathematical spine;
4. typed dependency graph with legend;
5. source-aware implementation sequence;
6. modeling decisions, blockers, and visible trust boundaries; and
7. next bounded handoff without silently starting unrelated proof work.

When creating `math_collections.md`, adapt
[`assets/math_collections.template.md`](../assets/math_collections.template.md)
instead of inventing a new schema.

## Quality gates

- **Ontology**: no object, function, construction, or structure is disguised
  as a proposition.
- **Usability**: every core interface has a natural downstream use probe.
- **Fidelity**: carriers, theorem identity, source order, and mathematical
  meaning were not silently changed.
- **Dependency**: important prerequisites and trust boundaries are visible;
  the build order is acyclic.
- **Epistemic honesty**: checked, axiomatic, trusted, and blocked work are not
  conflated.
- **Implementation honesty**: verifier limits do not redefine the mathematics.

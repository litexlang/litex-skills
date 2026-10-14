---
name: litex-basics
description: Learn and apply the essential Litex working model, persistent Session, major syntax, common mathematical expressions and misconception checks. Use at the start of ordinary Litex writing or review; specialized tasks build on this foundation.
---

# Litex basics

Use this foundation once when starting Litex work or switching to an unfamiliar
version. Keep the working model available; do not reload every guide after
each statement. This package includes complete starter examples and needs only
a Litex executable to try them. A golitex source checkout is optional.

## 1. Understand what a line contributes

Litex extends a mathematical context. Objects have carriers, definitions give
interfaces, and accepted facts become available to later statements. A fact
must be well-defined before proof verification. An ordinary rejected candidate
does not become a fact and does not erase earlier accepted work.

```litex
have a R = 2
a + 1 = 3
a^2 = 4
```

`have` introduces a real object and its value; the other lines check consequences.
This is mathematical declaration, not a sequence of mutable assignments.

## 2. Run and keep the Session

Check `litex -version` and `litex -help`. These examples were checked with an
existing release executable reporting 1.0.7-beta; a matching source build was
not established. Use the target version's CLI contract for other versions.

```bash
litex -lang en -strict -session -e 'have a R = 2'
```

Enter one complete top-level statement at a time; end an indented block with
a blank line. `a = 3` is rejected, but `a + 1 = 3` still succeeds in that same
process. Read each result before sending another candidate.

Compare two separate commands, each with a fresh context:

```bash
litex -lang en -strict -e 'have a R = 2'
litex -lang en -strict -e 'a + 1 = 3'  # rejected: this process has no a
```

With the Session command above, the same interaction retains the declaration:

```text
litex> a = 3
... rejected; the prompt returns ...
litex> a + 1 = 3
success
```

The diagnostic line is abbreviated; the final success uses the original `a`.

**Open `-session` for authoring, load accepted context once, and repair ordinary
failed statements there. Never rerun the whole file whenever a few lines are
added.** A theorem/claim with its proof is one statement. Several pasted
statements are not one transaction: some may commit while another fails.

Keep accepted source and distinct failed attempts in the owning task's notes
or proof journal; follow its repository policy. Restart when the process is
unusable, the loaded prefix must change, or a committed declaration must be
replaced. To adopt a verified rebuilt executable, save source, restart and
replay accepted statements in order. A normal proof miss is not a restart.

At a baseline, coherent checkpoint or final delivery, check the saved source
separately while retaining the authoring process:

```bash
# Replace the placeholder with the actual saved file.
litex -lang en -strict -f <saved-file.lit>
```

For the measured 1.0.7-beta executable require exit 0 and parsed JSON with
`kind: run`, `run_result: "success"`, `session_terminated: false`,
`termination: null`. An interactive transcript is not one JSON document.
A Session containing rejected input may have an aggregate failure despite
later success; use a clean gate for the accepted saved artifact.

For an existing passing prefix use `litex -lang en -f prefix.lit -session`.
The prefix must pass; this flag does not skip a failing draft. Module/config
details belong to the [module topic](references/topics/modules.md).

## 3. Choose the main syntax by mathematical role

The signatures below are schematic; replace their names/domains with actual
objects. Full runnable instances follow in the examples and math guide.

| Need | Form / meaning |
| --- | --- |
| A value with a carrier | `have x S = value` checks membership and records equality. |
| An arbitrary member | `have x S` requires a nonempty carrier; it does not choose a numeral. |
| An expression alias | `let name = expression` is an equality alias, not mutable assignment. |
| A callable function | `have fn f(x S) T = expression`; conditions may belong to its domain. |
| A mathematical condition | `prop P(x S):` defines vocabulary; `$P(a)` asserts an instance. |
| Universal / conditional law | `forall x S:`; premises precede `=>:`, conclusions follow. |
| Existence / uniqueness | `exist x S st {facts}` / `exist! x S st {facts}`. |
| A local proof | `claim:` with `? goal`; exports the checked goal, not helper names. |
| A reusable named result | `thm name:` with `? goal`; cite it with the supported theorem-call form. |

Use `a $in S`, `A $subset B`, `=`, `!=`, `<`, `<=`, `>`, `>=` for the
corresponding facts. `N`, `Z`, `Q`, `R` are mathematical carriers. In the
measured version `N` includes zero. Put denominators/nondegeneracy in domains
when they belong to the concept, rather than relying on later conventions.

## 4. Express common mathematics

Read [syntax and mathematical patterns](references/math-patterns.md) on first
use. It covers algebra, properties, sets, functions, sequences, quantifiers,
existence and finite cases using the accompanying complete examples.

A function's own domain can guard a partial expression:

```litex
have fn reciprocal(x R: x != 0) R = 1 / x
reciprocal(2) = 1 / 2
```

The [function example](examples/functions.lit) then proves a universal inverse
law and selects one theorem conclusion. The [existence example](examples/existence.lit)
supplies and extracts witnesses. The [logic example](examples/logic.lit)
shows conditional premises and a witness depending on a universal parameter.

| Mathematical move | Action |
| --- | --- |
| Check a routine consequence | State the fact directly with its actual premises. |
| Introduce a defined positive property | `by def $P(args)` checks the defining clauses. |
| Use a named result | `release thm name(args)` publishes conclusions; `by thm ... => fact` selects a returned atomic fact. |
| Prove / use existence | `witness` / `obtain`; preserve the witness's dependency scope. |
| Finite cases | `by enumerate finite_set:` for the displayed finite-domain example. |
| Inductive argument | A base and step with `by induc`; see the [induction topic](references/topics/induction.md). |

Use explicit intermediate facts only when they perform real mathematical work.
Do not wrap every routine builtin-supported consequence in a helper theorem.

## 5. Avoid the common mistaken models

- A rejected goal is not proof of its negation and is not stored knowledge.
- Declaring `prop P` proves no instances; `abstract_prop` gives only a signature.
- Without `=>:`, a universal's listed facts are conclusions, not assumptions.
- A `forall` body lists facts; proof commands belong in a proof body such as a claim.
- `exist!` needs uniqueness as well as a witness; square roots of four are not unique in `R`.
- An arbitrary member has no chosen value. A claim's helpers and universal binders stay local.
- Guarded function inputs must satisfy the guard before a result can be checked.
- Verified source and the intended mathematics are separate checks; inspect domains and any assumptions/debt.

The [misconception cards](references/misconceptions.md) pair concrete rejected
forms with checked alternatives and state their boundaries. Check the relevant
card at the first stopping point; do not read the whole archive.

## Continue at the right layer

Use [the topic index](references/topics.md) for one mathematical difficulty.
When installed, `litex-proof-writer`, `litex-concept-modeler`,
`litex-math-textbook-translator`, `litex-example-migration` and `litex-review`
own task workflows. `litex-reference` locates live docs/examples/showcases by
reading depth. Do not load every task or topic for a small proof.

If a matching live corpus is available, use it for exact contracts and larger
interfaces; resolve it from the task/hub root, not the installed skill folder.
If unavailable, this starter remains usable within its measured example scope.
Kernel development and maintainer authorization policies are a separate layer.

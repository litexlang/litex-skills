# Litex writing preferences and learner guidance

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use this guide for new proofs, documentation examples, and help with a learner's
code. The maintainer's explicit preferences are recorded here; they do not
remove supported syntax. The live repository's Manual, parser, and checked
examples determine actual support. Do not treat older bundled corpus examples
or this guide as a substitute for current execution evidence.

## Separate three kinds of statements

- **Supported:** a spelling is accepted and has the documented semantics.
- **Recommended:** choose it in new agent-authored code for readability and
  consistency; explain the reason, and honor an explicit user choice.
- **Required:** crossing the boundary changes meaning or causes a real parse,
  well-definedness, or verification failure. State that boundary precisely.

Never turn “prefer” into “the language cannot.” Do not mark an accepted spelling
deprecated without an actual deprecation policy. When a user supplies valid
code, explain it before proposing a style rewrite; avoid unrelated mass
migration and retain exact historical failures and receipts.

## Maintainer preferences

| Supported alternative | Recommended for new source | Reason and boundary |
|---|---|---|
| Bare `by thm name(args)` | `release thm name(args)` | Makes publishing all instantiated conclusions explicit. Bare `by thm` remains a compatibility alias. |
| `forall x R: x > 0 => x != 0` | An indented `forall` with premises before `=>:` and conclusions after it | Readers can see the assumption/conclusion boundary and extend each list. Inline syntax remains supported. |
| Documented aliases such as `∀`, `∃`, `ℝ`, `∈`, `≤` | `forall`, `exist`, `R`, `$in`, `<=` | Matches canonical diagnostics and makes source easier to type, search, and copy. Documented Unicode aliases remain supported. |

The theorem preference is about **unselected calls**. Keep
`by thm name(args) => fact` for one selected atomic consequence. Do not replace
it with `release thm`, which publishes all conclusions. `release thm` accepts
no selection arrow or proof body; `by thm ... => fact` does not accept an
existential, conjunction, chain, or universal target. A root `forall` theorem
requires parentheses, even with zero parameters; an ordinary theorem fact uses
its bare name.

The central style comparison is executable in either form:

```litex
forall x R: x > 0 => x != 0
```

```litex
forall x R:
    x > 0
    =>:
        x != 0
```

Do not rewrite an input-alias demonstration to ASCII when its purpose is to
teach Unicode. Do not infer arbitrary symbol support: `×` means Cartesian
product, so arithmetic multiplication is `*`; `⊂` means proper subset, while
`⊆` means non-strict subset.

## Public examples: facts before theorem names

For homepage, README, tutorial, and other introductory examples, prefer the
smallest readable checked source. Do not wrap each ordinary universal fact in
a named `thm`, or add a trivial theorem call to justify that name. When a
short universal and its mathematical equality chain already verify as facts,
write them directly:

```litex
have fn distance_from_zero(x R) R = abs(x)

forall x R:
    distance_from_zero(x) = abs(x) >= 0

distance_from_zero(-3) = distance_from_zero(3) = 3
```

A bare `forall` is a checked fact list, not a proof-command body. If the
argument needs `by def`, witnesses, cases, or other intermediate proof actions,
use an anonymous `claim` with its universal goal. Retain a named `thm` when an
explicit caller or imported interface needs that name, or when a substantial
named mathematical result is the teaching subject. Reuse alone does not force
naming: later facts can also use accepted universal context. Check the whole
shortened example, including later consumers, in the current CLI.

This is the maintainer's explicit example-writing preference from 2026-10-08.
It is not a syntax prohibition or a mandate to rename textbook theorems,
historical receipts, or public library interfaces.

## Existing authoring choices worth teaching

These refine the existing proof-writer guidance, rather than adding new syntax
restrictions. Apply them when they make the actual mathematical move clearer.

| Situation | Preferred form | Boundary |
|---|---|---|
| Universal with no premises | `forall x R:` followed directly by conclusions | Avoid an empty `=>:`. Premise-free universal iff has its own required left-side block. |
| Positive concrete definition whose clauses are established | `by def $P(args)` | Use a larger goal block only for real intermediate reasoning; `by def` is definition folding. |
| Witness whose substituted body already verifies | `witness exist x R st {x = 2} from 2` | Keep a proof body when it performs a real derivation or teaches one. |
| A theorem call already publishes the fact needed next | Continue with its consumer | Avoid repeating its identical conclusion as a proof echo; retain deliberate reader bridges when useful. |
| A useful algebraic transformation | One readable equality chain | Add intermediate equalities when the verifier needs them; do not manufacture a new theorem for routine arithmetic. |
| A member of an already named set | `forall S set, x S:` | Avoid declaring `x set` plus `x $in S` when the intended object is a member. Binder order is significant. |

Read `authoring-error-cards.md` for the existing checked before/repair cases.
These preferences never justify weakening a theorem, removing a necessary
bridge without verification, or disguising a kernel defect as house style.

## Help with the first actual stopping point

Start with the learner's code and the earliest diagnostic. Explain the intended
mathematical move, show a small repaired form, then run it in its required
context. Distinguish an observed failure, an illustrative shape, and a checked
repair. Teach the relevant item below; do not dump the whole list at once.

1. **A bare `forall` is a fact list.** A proof command such as `release thm`,
   `by def`, or `witness` belongs in a `claim`/`thm` proof body. Use the active
   goal binders there; do not introduce a mirror universal with renamed binders.
2. **A definition is vocabulary.** `prop P(x R): ...` does not establish
   `$P(a)`. Prove its clauses and use `by def $P(a)` when explicit folding is
   needed. Use `have fn` for a value the next line must call.
3. **Object expressions have domains.** Diagnose `1 / x`, `f(x)`, or `a(k)` at
   well-definedness before searching for a theorem about the result. Supply
   the justified nonzero premise, argument domain, or index bound; never add
   an arbitrary assumption solely to make the check pass.
4. **Names and premises have scopes.** `forall x R:` does not introduce a
   global `x`. A successful `claim` exports its goal, not its local witness or
   helper definitions. Inspect what was stored before using it later.
5. **Fact nesting is bounded.** An existential or set-builder body cannot
   directly contain `forall`; put the quantified condition in a real concrete
   `prop`. A universal conclusion cannot contain another universal; put those
   parameters in one header. Do not flatten a mathematical dependency if that
   would change the statement's meaning.
6. **Witnesses and uniqueness are different obligations.** `obtain` needs an
   established existential source. `witness exist! ...` must establish
   uniqueness as well as supply a witness; “here is one value” is insufficient.
7. **Search failure does not refute a fact.** `have x R` followed by `x = 0`
   gives insufficient evidence for that equality. It does not establish
   `x != 0`. Check a native explicit route or a genuine missing intermediate
   fact before assigning proof debt or suspecting a kernel problem.
8. **Checked and assumed results differ.** `trust`/`axiom` are assumptions;
   `abstract_prop` is a signature. Do not call a development containing proof
   debt fully checkable. Follow the existing trust policy when a real task is
   blocked, and make the surviving debt visible.

For run instructions, use the live `docs/cli.md`. Do not copy old flags from a
bundled note: current CLI/output contracts may differ from historical runner
or session recipes. Verify tutorial examples independently, with required
declarations and assumptions in the same context; examples must not pass only
because an earlier fence polluted the environment.

## Evidence and ownership

The three spelling defaults are explicit maintainer instructions from
2026-10-05, not conclusions mined from a failed proof. Related authoring and
triage choices already live in the proof-writer skill, its authoring cheat sheet,
and error cards. Do not promote a new technical workaround from this list.

In golitex, the support anchors are `src/parse/fact.rs`,
`tests/unit/parse/input_integrity.rs` (inline universals),
`src/tokenize/symbols.rs` (Unicode aliases), and
`src/parse/statements/release_and_expand.rs` / `by.rs` (theorem calls).
The public teaching home is
`docs/Litex_Learner_Cheatsheet.md#supported-syntax-and-recommended-writing`;
Manual owns the language contract and FAQ explains the choices. Refresh this
guide when those contracts change, rather than preserving outdated restrictions.

Focused verification on 2026-10-05 used the live release CLI and the repository's
`tests/tooling/run_docs_markdown_files.py` fence collector: all eight added or
changed runnable documentation fences passed independently. Nineteen separate
controls confirmed the supported alternative spellings and rejected the nearby
invalid selection, fact-list command, missing divisor condition, unproved
predicate/existential, escaped binder, nested universal conclusion, and numeric
`×` cases. This validates these examples, not the whole documentation corpus.

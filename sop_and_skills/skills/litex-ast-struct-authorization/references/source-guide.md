# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex AST Struct Authorization

## Hard rule (user convention)

**Do not change Stmt / Obj / Fact structs on your own.**

Without the user's explicit authorization for the concrete struct change, do
not modify `Stmt`, `Obj`, `Fact`, or their payload / leaf structs in either
legacy AST or `src/` AST.

Protected examples include (not exhaustive):

- `Identifier`, `AtomObj`, `SetBuilder`, `FnSet`, `AnonymousFn`, and other
  `Obj` payloads
- `EqualFact`, `ForallFact`, `QuantifierFreeFact`, and other `Fact` /
  `AtomicFact` payloads
- `HaveObjEqualStmt`, `LetObjStmt`, and other `Stmt` payloads
- Adding fields such as `display_name` on a shared leaf used everywhere

## What counts as a protected change

Stop and propose before:

- adding, deleting, renaming, moving, or retyping fields
- adding, removing, or reshaping enum variants of `Stmt` / `Obj` / `Fact`
  or of their dedicated payload types
- changing field responsibility so call sites must reinterpret identity,
  display, or binder meaning

A request to implement a feature, fix a bug, plan, or write a tracer does
**not** authorize these edits. Approving a nearby design is not approval of
a struct-field change. If the need appears mid-implementation, pause and ask.

## What remains allowed without new authorization

- Read-only inspection
- `impl` methods, free functions, parse/exec/display code that **uses**
  existing fields
- Constructors / normalize helpers that rewrite **values** inside the
  existing shape (e.g. rename binder strings) without changing the struct
  definition
- Docs/tests/examples that do not alter those struct definitions

## Required proposal format

Before any protected edit, present a prominent **AST Struct Change Proposal**:

1. exact type(s) and field/variant change
2. what the field represents and who will read/write it
3. why it is needed now
4. why existing fields / parallel local data / display-only maps cannot work
5. lifetime, ownership, and coupling consequences (especially if a leaf like
  `Identifier` would affect all atoms)

Wait for explicit user confirmation. Then stay inside the approved scope.

## Relationship to other gates

- Complements the Env / Runtime authorization gate; does not replace it.
- Use alongside `$golitex-repository-policy` and `$litex-kernel-engineer` for
  golitex work.
- Prefer putting binder display vs identity on binder-carrying objects only,
  not on shared leaves, unless the user explicitly authorizes that leaf change.

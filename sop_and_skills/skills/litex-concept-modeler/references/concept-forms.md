# Litex Concept Forms

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use semantic role and downstream use to choose a Litex form. The sketches in
this reference express intended interfaces; verify exact syntax in the active
repository before calling one checkable.

## Selection matrix

| Mathematical role | Primary Litex form | Immediate use | Common wrong form |
| --- | --- | --- | --- |
| Named value, constant, set, or concrete object | `have` | cite the value or membership | `prop` describing a candidate value |
| Formula-defined map, operation, sequence, or set-valued construction | `have fn` | write `f(x)` | relation `P(x, y)` that forces callers to carry the output |
| Canonical value selected by unique existence | `have fn ... by exist!` | apply the selected function | leaving only an existential relation |
| Property, relation, admissibility condition, or candidate specification | `prop` | assert `$P(...)` | function returning a truth-like object |
| Packaged tuple-like data with named fields and laws | `struct` with direct law clauses | instantiate the structure and project fields | parallel law certificate and definition-satisfaction bridges without an independent use |
| Declaration family indexed by a carrier, structure, or hypothesis | `template` | instantiate `\Name<...>` | ordinary function over a fake universal domain |
| Nearby derived result | direct fact or `claim` | use from local context | exported `thm` for every trivial helper |
| Important named reusable result | `thm` | explicit theorem citation | anonymous background fact or global automatic noise |
| Foundational named assumption | `axiom` | explicit background interface | pretending the assumption was derived |
| Temporary exact proof debt | `trust` status on the missing fact | later trace exposes the dependency | wrapping a wrong concept form in `trust` |

## Fast decision questions

1. Must callers refer to a value, apply a function, assert a condition, project
   fields, instantiate a family, or cite a result?
2. Does the source introduce data or merely test supplied data?
3. Do parameters change an ordinary function value, or the declaration/type
   that callers instantiate?
4. Is the desired value canonical only after existence and uniqueness?
5. Is this an important mathematical interface or only a local proof step?

Classify from those answers, not from whether the source sentence contains
parameters or happens to use the word “definition.”

## Decomposition patterns

### Relation, existence, and canonical selection

A single informal noun often needs several interfaces. For sequence limits:

```text
has_limit(a, L)       prop: L is a candidate limit of a
is_convergent(a)      prop: some L satisfies has_limit(a, L)
limit_unique          thm: two candidate limits are equal
limit(a)              have fn by exist!: selected on convergent sequences
```

Do not choose between “limit is a prop” and “limit is a function.” The
candidate relation and the selected value are different mathematical roles.

### Laws and bundled structure

The textbook default is one bundled structure with its laws written directly:

```text
Group<s>                  struct packaging inv, op, e and direct group laws
group_left_cancel         thm about any Group<s>
```

Use native struct opening to obtain those laws. A theorem saying only that a
Group satisfies its own definition adds no mathematics. A separate law
predicate is justified when the source independently studies unbundled
candidate operations; do not manufacture that use by splitting one proof into
an operations theorem and a struct facade. This is the user's explicit
2026-10-09 textbook design preference, not a claim that all propositions are
redundant.

### Set-valued constructions

If later mathematics writes `mZ(m)` and tests membership in that set, `mZ` is
a set-valued function even when its body uses a predicate:

```text
divides_Z(m, x)     prop
mZ(m)               have fn from Z to power_set(Z)
```

Do not replace the construction with only `is_multiple(m, x)` or a predicate
about a proposed set.

### Parameterized families

An ordinary `prop P(x)` or `have fn f(x)` is not a template merely because it
has parameters. Use `template` when instantiation changes the declaration
itself, such as a sequence space over carrier `S`, a structure family over
`s`, or a quotient construction indexed by supplied mathematical data.

## Anti-patterns

- **Proof-first modeling**: writing theorem bodies before deciding what the
  objects and relations are.
- **Prop fallback**: using a predicate because a real construction is harder
  for the current parser or verifier.
- **Template inflation**: turning every parameterized expression into a
  declaration family.
- **Premise smuggling**: putting the target theorem into an admissibility
  condition so the theorem becomes tautological.
- **Carrier drift**: silently narrowing `Z` to `N`, changing a domain, or
  replacing the source object with a convenient surrogate.
- **Status confusion**: treating `trust`, `axiom`, or verifier acceptance as
  the semantic category of a concept.
- **Wrapper preservation**: keeping both a wrong and right interface through
  aliases, compatibility predicates, or trusted wrappers.

# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex strict definitions

When formalizing mathematics in Litex, **definition strictness is first-class**.
A definition that looks only slightly looser is often not harmless: weak
domains and missing nondegeneracy conditions leak into every `prop`, `forall`,
theorem statement, and downstream library interface.

## Core rule

Prefer the stricter definition.

Put into the definition itself:

- exact carriers and parameter domains (e.g. `R+` for a geometric radius)
- nondegeneracy that belongs to the concept (e.g. `a != b` for a segment,
  line through two points, or diameter)
- nonzero / nontrivial arms or denominators that the object presupposes
  (e.g. angle vertex distinct from both arm tips)

Do **not** rely on later proofs, comments, or silent convention to repair a
loose definition.

Slight surface differences between a loose and a strict form may look
acceptable in isolation. Still strictify: the cost of a weak definition
compounds; the cost of stating the invariant once does not.

## When revising definitions

1. Tighten the definition body / premises first.
2. Align dependent `? forall` goals and thm/prop comments to the same
   strength.
3. Do not weaken a definition to make an old proof easier.
4. Proof bodies may lag if the user explicitly says so; statements and
   comments must not.

## Checklist before accepting a def

- [ ] Domain matches ordinary mathematical meaning (not a larger ambient set
      “for convenience”)
- [ ] Degenerate cases the concept excludes are excluded in the def
- [ ] Well-definedness obligations are visible in the signature/body, not
      postponed as folklore
- [ ] Immediate use probes do not need extra silent inequalities the def
      should already own
- [ ] Related goals/comments cite the same constraints

## LitexGeo-style examples

| Concept | Prefer | Avoid silently allowing |
|---|---|---|
| circle radius | `r R+` | `r R` with later `r > 0` folklore |
| segment / line through points | `a != b` in the def | coincident endpoints |
| angle / angle_cos | nonzero arms at the vertex | zero-length arms |
| midpoint of a segment | `a != b` when the object is a segment midpoint | midpoint of a point-pair with no segment meaning |

Intentional narrow predicates (e.g. SSS-only congruence, apex-fixed isosceles)
are allowed when they are **explicit** design choices, not accidental
under-specification.

## Relationship to other skills

- Interface choice and form (`have` / `prop` / `fn` / …): `$litex-concept-modeler`
- Repository trust / release gates: `$golitex-repository-policy`

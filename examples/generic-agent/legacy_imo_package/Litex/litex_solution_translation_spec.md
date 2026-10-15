# Litex Solution Translation Specification

**Historical summary from debugging IMO 1960 Problem 3**

---

## Core principles

### 1. The sole geometry source: Litex/geo/library_final.lit

**Rules:**
- The archived workflow permits only `Litex/geo/library_final.lit` under IMO as its imported geometry source. Existing predicates must come from that file, not another library, a copy, or a hard-link alias.
- Use a matching predicate from that file. If none exists, define it in this problem's `predicate.lit` rather than switching libraries.
- Repair library_final.lit only when its independent strict precheck fails in the library itself. After that precheck passes, handle problem-specific translation or proof difficulties in the problem files.
- Do not expand the main theorem statement directly into coordinate or algebraic expressions; expand inside the proof body.
- Litex `[import]` points to a module directory. Check that its `[export]` refers to the designated source. If that configuration cannot be imported, report the blocker rather than silently using `Litex/library_final_ref`.

**Example:**

**Incorrect: direct expansion.**
```litex
thm imo_1960_problem_3:
    ? forall A, B, C Point, bx, By, cx, cy, a R:
        # Right angle at A, expanded directly.
        bx * cx + By * cy = 0,
        ...
```

**Correct: use the library predicate.**
```litex
thm imo_1960_problem_3:
    ? forall A, B, C Point, bx, By, cx, cy, a R:
        # Right angle at A, expressed with the library predicate.
        $geo::is_right_angle(A, B, C),
        ...
```

**Finding predicates in the library:**
```bash
# Search keywords.
cd <YOUR_WORK_DIR>/IMO
grep -n "prop is_right_angle" Litex/geo/library_final.lit
grep -n "prop distance" Litex/geo/library_final.lit
grep -n "prop collinear" Litex/geo/library_final.lit
```

---

## Main theorem structure

### Standard structure

```litex
thm problem_name:
    # Quantifiers: declare every variable.
    ? forall x, y, z R, A, B, C Point:
        # Premises: predicates without expansion, with one NL comment per clause.
        $geo::is_right_angle(A, B, C),    # Right angle at A
        $geo::distance_sq(B, C, a * a),   # BC² = a²
        ...
        =>:
            # Conclusion: predicate or expression with its NL comment.
            result_expression                 # Natural language description
    
    # Proof: expand predicates and perform the derivation here.
    # Step 1: Expand predicates
    ...
    # Step 2: ...
    ...
```

### Premise requirements

**Rules:**
- Use predicate forms, not expanded coordinate or algebraic expressions.
- Add an end-of-line NL comment while translating each premise and conclusion, using `#` on that same line.
- Comments are the translation alignment: annotate the source wording or meaning immediately, avoiding later omissions or inconsistent reconstruction.
- Put a missing predicate in `predicate.lit`.

### Equivalence when whole-problem wrappers are forbidden

If the source asks for an iff while the interface contract forbids a conditions(...), statement(...), or criterion wrapper, preserve the meaning and expose two direct theorems rather than adding a wrapper premise:

- `..._necessity`: repeat every shared NL premise faithfully; add the left side as a direct annotated premise and conclude the right side.
- `..._sufficiency`: repeat the same shared premises; add the right side directly and conclude the left side.
- Both headers retain all atomic premises. Helpers may support the proof body but must not replace the public translation interface.
- Check both directions in ordinary and strict project modes, confirming both theorem identifiers appear in the trace.

This preserves iff under the no-wrapper contract. When wrappers are allowed, use the universal-equivalence pattern in the syntax reference.

**Illustration:**
```litex
thm criterion_necessity:
    ? forall x S:
        $common_condition_1(x),  # NL common premise 1
        $common_condition_2(x),  # NL common premise 2
        $left(x)                 # NL left side
        =>:
            $right(x)            # NL right side

thm criterion_sufficiency:
    ? forall x S:
        $common_condition_1(x),  # NL common premise 1
        $common_condition_2(x),  # NL common premise 2
        $right(x)                # NL right side
        =>:
            $left(x)             # NL left side
```

**Comparison:**

**Incorrect: expand the premise directly.**
```litex
thm imo_1960_problem_3:
    ? forall bx, By, cx, cy, a R:
        bx * cx + By * cy = 0,  # Direct coordinate expansion.
        (bx - cx) * (bx - cx) + (By - cy) * (By - cy) = a * a,
        =>: ...
```

**Correct: use the predicate in the premise.**
```litex
thm imo_1960_problem_3:
    ? forall A, B, C Point, a R:
        $geo::is_right_angle(A, B, C),  # Library predicate.
        $geo::distance_sq(B, C, a * a),
        =>: ...
```

### Proof-body requirements

**Rules:**
- Predicates may be expanded inside the proof body.
- Use `have` to introduce coordinates and intermediate values.
- Explain each derivation with clear comments.
- Cite helper theorems with `by thm` in this historical syntax.

**Example:**
```litex
thm imo_1960_problem_3:
    ? forall A, B, C Point, a R:
        $geo::is_right_angle(A, B, C),
        =>: result
    
    # Proof: Introduce coordinate system
    have A = (0, 0), B = (bx, By), C = (cx, cy)
    
    # Expand is_right_angle predicate
    # From $geo::is_right_angle(A, B, C), we get:
    bx * cx + By * cy = 0
    
    # Continue proof...
    ...
```

---

## Common errors and repairs

### Error 1: ignoring an existing library predicate

**Historical failure from IMO 1960 Problem 3:**
- The user asked why the existing right-angle predicate was not used.
- The agent wrote `bx * cx + By * cy = 0` instead of `$geo::is_right_angle(...)`.

**Cause:**
- The agent had not consulted library_final.lit first.
- It translated the source directly into coordinate expressions.

**Repair:**
1. Read library_final.lit before translation.
2. Search relevant keywords such as right angle, distance, and collinear.
3. Use the matching predicate when one exists.

### Error 2: expanding a main-theorem premise

**Incorrect code:**
```litex
thm main_theorem:
    ? forall bx, By, cx, cy R:
        # This expanded form should not replace the public premise.
        bx * bx + By * By = cx * cx + cy * cy,
        =>: ...
```

**Preferred form:**
```litex
thm main_theorem:
    ? forall A, B, C Point:
        # A predicate expresses the geometric relation.
        $geo::equal_distance(O, A, O, B),
        =>: ...
```

### Error 3: confusing translation with proof

**Incorrect interpretation:**
- Expand every predicate during translation.

**Correct distinction:**
- Translation, including the statement's premises and conclusion, uses predicates.
- The proof body may expand those predicates.

**Analogy:**
- The main theorem is the mathematical statement: clear and abstract.
- Its proof may be concrete and computational.

---

## Geometry translation workflow

### Step 1: read the natural-language problem

```json
{
  "problem": "In a given right triangle ABC, the hypotenuse BC, of length a, ..."
}
```

### Step 2: consult library_final.lit

```bash
cd <YOUR_WORK_DIR>/IMO
grep -i "right" Litex/geo/library_final.lit
grep -i "triangle" Litex/geo/library_final.lit
grep -i "distance" Litex/geo/library_final.lit
```

**Predicates found:**
```litex
prop is_right_angle(A, B, C Point): ...
prop distance_sq(A, B Point, d_sq R): ...
```

### Step 3: formalize premises with predicates

```litex
thm imo_1960_problem_3:
    ? forall A, B, C Point, a R:
        # Right triangle with right angle at A
        $geo::is_right_angle(A, B, C),
        # Hypotenuse BC has length a
        $geo::distance_sq(B, C, a * a),
        =>: ...
```

### Step 4: expand and derive inside the proof

```litex
    # Introduce coordinate system
    have A = (0, 0), B = (bx, By), C = (cx, cy)
    
    # Expand is_right_angle predicate
    bx * cx + By * cy = 0
    
    # Continue proof...
```

---

## Requirements for new predicates

### When to introduce one

- The designated library lacks the relation.
- The problem repeatedly uses that geometric relation.
- A genuine abstraction improves statement readability.

### Where it belongs

**Rules:**
- Define it in predicate.lit.
- Configure `[export] predicate = "./predicate.lit"` in litex.config.
- Reference it as `$predicate::prop_name(...)` from solution.lit.

**Example:**

```litex
# predicate.lit
prop is_midpoint(M, A, B Point):
    ? forall mx, my, ax, ay, bx, by R:
        M = (mx, my), A = (ax, ay), B = (bx, by)
        =>:
            mx = (ax + bx) / 2,
            my = (ay + by) / 2

# litex.config
[export]
predicate = "./predicate.lit"

# solution.lit
thm main_theorem:
    ? forall M, A, B Point:
        $predicate::is_midpoint(M, A, B),
        =>: ...
```

---

## Best practices

### Translation checklist

- [ ] Consult library_final.lit for the matching predicate.
- [ ] Keep the main theorem's premises in predicate form.
- [ ] Annotate each premise with its natural-language meaning.
- [ ] Place any new predicate in predicate.lit.
- [ ] Expand predicates and perform derivations in the proof body.

### Main theorem readability

**Goal:**
- Its premises and conclusion directly reveal the natural-language problem.
- A reader can identify what is being proved without reading the proof.

**Counterexample:**
```litex
# The geometric theorem is not apparent from this expanded statement.
thm problem:
    ? forall x1, y1, x2, y2, x3, y3 R:
        x1 * x2 + y1 * y2 = 0,
        (x2 - x3)^2 + (y2 - y3)^2 = a^2,
        =>: ...
```

**Positive example:**
```litex
# The statement is immediately recognizable as a right-triangle theorem.
thm problem:
    ? forall A, B, C Point, a R:
        $geo::is_right_angle(A, B, C),
        $geo::distance_sq(B, C, a * a),
        =>: ...
```

---

## Summary

1. Consult library_final.lit before translating.
2. Use predicate-form premises without expansion.
3. Expand and derive in the proof body.
4. Put new predicates in predicate.lit.
5. Keep the main theorem readable.

Translation expresses geometric relations through predicates; it is not their coordinate expansion.

## Implementation experience: explicit bridge theorems

The historical verifier was conservative about algebra. For substantial substitution, scaling, expansion, or coordinate steps, use helpers with clear interfaces and fixed argument order in theorem.lit, then cite them from the main proof as `by thm theorem::name(...)`.

Check every helper's forall parameter count, order, and types exactly. Prefer a few reusable lemmas over problem-specific coordinate expansion in the public theorem statement.



---

## Exact matching of library theorem forms

**Historical observation, Problem 205:** a by-thm call must match the library result's form.

### ⚠️ The Golden Rule

When using by thm, match the library theorem's conclusion form exactly.

**Example: median_inequality_distance**

```litex
# Failure: the library returns an existential, but this goal is a direct inequality.
thm problem_205:
    ? forall a, b, c, d cart(R, R):
        $geom::unified::is_midpoint(d, b, c),
        not $geom::unified::is_collinear(a, b, c)
        =>:
            geom::unified::distance_sq(a, b) + geom::unified::distance_sq(a, c) 
            > 2 * geom::unified::distance_sq(a, d)
    by thm geom::unified::median_inequality_distance(a, b, c, d)
    # Error: "cannot prove then-clause"

# Success: the conclusion matches the library's existential form.
thm problem_205:
    ? forall a, b, c, d cart(R, R):
        $geom::unified::is_midpoint(d, b, c),
        not $geom::unified::is_collinear(a, b, c)
        =>:
            exist d_ab, d_ac, d_ad R st {
                d_ab >= 0, d_ac >= 0, d_ad >= 0,
                d_ab * d_ab = geom::unified::distance_sq(a, b),
                d_ac * d_ac = geom::unified::distance_sq(a, c),
                d_ad * d_ad = geom::unified::distance_sq(a, d),
                d_ab + d_ac > 2 * d_ad
            }
    by thm geom::unified::median_inequality_distance(a, b, c, d)
```

### Why the form matters

1. An existential library conclusion needs an existential target.
2. A direct inequality and an existential form are not automatically interconverted merely because they are mathematically equivalent.
3. A different interface needs a proved bridge, not just the theorem call.

### Strategy

1. Inspect the exact library conclusion first.
2. Preserve its existential/universal binders and constraints.
3. Argument order is part of the interface. Do not assume endpoint swapping is automatic even for a symmetric relation; use the established order or prove symmetry explicitly.
4. Use the geom::unified:: namespace within the existential clauses.
5. Use by thm directly only when the conclusion forms match.

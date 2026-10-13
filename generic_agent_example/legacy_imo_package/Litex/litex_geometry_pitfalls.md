# Litex Geometry Pitfalls and Best Practices

## Overview
This historical note records pitfalls and practices encountered while formalizing geometry in Litex. Its capability claims are scoped to those old cases.

---

## 0. Variable names

### Reserved identifiers

**Critical:** e is reserved in the recorded version, possibly as Euler's number 2.71828.

**Symptom:**
```litex
thm test:
    ? forall a, b, c, d, e, f, g cart(R, R):  # Recorded parse error.
        ...
```
Error: `ParseError: name 'e' is already active in this scope and cannot be rebound`.

Changing the name to pt_e or another descriptive identifier passed parsing.

### Description
Reserved or predefined letters can cause name-already-active errors.

### Names avoided in the original workflow
- Uppercase letters such as A, B, C, D, E, Q, R may be type names or otherwise reserved.
- Lowercase e denotes Euler's number.
- R denotes the real carrier.

### Naming convention
Recommended in this archived workflow:
- Prefer a, b, c, d over A, B, C, D.
- Prefer descriptive multiletter names such as pe, pa, pb, pc.
- Point names can use a pt prefix: ptA, ptB, ptC, ptD.
- Avoid ambiguous single letters except familiar mathematical parameters such as a, b, c, d, p, q, r, s, t, u, v, w, x, y, z.

Recorded incorrect example:
```litex
thm problem:
  ? forall A, B, C, D, E cart(R, R):  # Uppercase-name conflict.
      ...
```
Error: `name 'C' is already active in this scope and cannot be rebound`.

Recorded accepted example:
```litex
thm problem:
  ? forall ptA, ptB, ptC, ptD cart(R, R):  # pt-prefixed point names.
      ...
```

### Debugging
For a name-already-active error:
1. Check uppercase names and use a lowercase or prefixed alternative.
2. Replace a single e with pe or point_e.
3. Prefer descriptive names.

---

## 1. WellDefinedError and the recorded type-environment issue

### Description
The old case found that a complicated nested theorem goal could precede WD errors in later theorems.

### Symptom
```
Error: "obj unified::vec(p1, q1) is not in C"
Phase: verify_well_definedness (domain/type checking).
```

### Cause attributed by the historical note
The note attributed the failure to combining these expression forms in one goal:
- Function applications such as vec(p, q).
- Index operations such as [1] and [2].
- Tuple construction such as (a, b).
- Arithmetic such as + and *.

For example:
```litex
Recorded failing example:
thm vec_add_path:
    ? forall p, q, r cart(R, R):
        vec(p, r) = (vec(p, q)[1] + vec(q, r)[1], vec(p, q)[2] + vec(q, r)[2])
```

The note described a polluted type environment in which a later simple vec(p1, q1) expression was incorrectly judged outside carrier C. This is a historical diagnosis, not a new current-kernel result.

### Workaround

**A: split into coordinate lemmas, the preferred historical repair.**
```litex
Recorded accepted example:
thm vec_add_path_x:
    ? forall p, q, r cart(R, R):
        vec(p, r)[1] = vec(p, q)[1] + vec(q, r)[1]

thm vec_add_path_y:
    ? forall p, q, r cart(R, R):
        vec(p, r)[2] = vec(p, q)[2] + vec(q, r)[2]
```

**B: use a helper function.**
When the library supplies vector addition:
```litex
thm vec_add_path:
    ? forall p, q, r cart(R, R):
        vec(p, r) = vec_add(vec(p, q), vec(q, r))
```

### Investigation
1. Bisect theorem blocks to locate the first WD-triggering theorem.
2. Retain only required definitions and that theorem in a minimal reproduction.
3. Inspect the goal's nested expressions before blaming variable names.

### Historical case
- Triggering theorem: vec_add_path at L478.
- Downstream symptom: cosine_law at L500.
- Investigation: more than 70 bisection rounds.
- Workaround: vec_add_path_x and vec_add_path_y.
- Recorded outcome: the WD errors disappeared.

---

## 2. Historical equality-substitution boundaries

### Description
The old workflow found that some substitutions and larger algebraic changes needed explicit proof steps.

### Symptom
```
Known: a = 5, b = 10.
Known: a + b = c.
Direct target not derived in that case: c = 15.
```

### Workaround
- State the useful intermediate derivations explicitly.
- Use proved theorem interfaces for substitution.
- Do not rely on an untested algebraic shortcut.
- For unknown-result failures under compound function expressions, first prove a scalar real algebra lemma with a stepwise chain, then instantiate it with the compound arguments. The archived cosine_law → dot_from_cosine_law strict case checked this route.

### Wrapping an equality in function context

Given A=B, the old case missed f(A)=f(B) directly, for example under negation or a dot/vec wrapper.

**Symptom:**
```litex
Known: (a-b)*(c-d) + (a'-b')*(c'-d') = -((b-a)*(c-d) + (b'-a')*(c'-d')).
Goal: dot(vec(b,a), vec(c,d)) = -dot(vec(a,b), vec(c,d)).
Outcome: verification failed. The coordinate equality did not directly lift into the function wrapper.
```

**Workaround:** two explicit wrapping bridges, followed by transitivity.
```litex
# Step 1: wrap the left side.
coordinate_expr_left = -coordinate_expr_right
f(left_args) = -coordinate_expr_right       # Left-side substitution.

# Step 2: wrap the right side.
-coordinate_expr_right = -f(right_args)     # Right-side substitution.

# Step 3: transitivity.
f(left_args) = -f(right_args)
```

**Case:** dot_neg_left, KB L688–700.
- Three lines instead of one: wrap left dot, wrap right dot, then compose.
- Recorded outcome: the added intermediate equations replaced the assumed statement with a proved theorem.

---

## 3. Proving compound expressions

### Practices in the original workflow
1. Layer a complicated result over smaller helper theorems.
2. Keep goals simple instead of combining many nested forms.
3. Retain the explicit derivation steps required by the measured verifier.

### Example
```litex
# Not recommended in the old case: one large compound goal.
thm complex_formula:
    ? forall x, y: f((g(x)[1] + h(y)[2], g(x)[2] - h(y)[1])) = result

# Preferred historical route: smaller helper theorems.
thm step1: ? forall x, y: temp1 = g(x)[1] + h(y)[2]
thm step2: ? forall x, y: temp2 = g(x)[2] - h(y)[1]
thm step3: ? forall x, y: f((temp1, temp2)) = result
```

---

## 4. Axiom vs Theorem

### Assumption boundary
- Do not use an axiom merely to avoid checking a proof.
- The historical guide reserved axioms for:
  1. Foundational mathematical assumptions such as commutativity.
  2. Explicit background properties of definitions, such as distance nonnegativity.
  3. Unexpressed supporting reasoning, with its missing proof explained.

### Verification distinction
- An axiom is accepted as an assumption rather than proved.
- Express provable results with thm rather than axiom.

---

## 5. Debugging tools

### Bisection
When a WD error's first cause is unclear:
1. Preserve the current source.
2. Create a test containing the first half of the theorems.
3. Check which half contains the failure.
4. Repeat until one theorem is isolated.

### Minimal reproduction
Keep the reproduction small:
- Required function and carrier definitions.
- The failing theorem.
- Confirm the failure still occurs.

### Local library diagnosis
```bash
# Locate an error in the library; this is not whole-problem acceptance.
litex -f your_library.lit > verify_result.txt 2>&1

grep "WellDefinedError" verify_result.txt
grep '"result": "error"' verify_result.txt | wc -l
```
Whole-problem acceptance follows stage 4 of the archived workflow and checks every export and the JSON trace.

---

## 6. Historical capability summary

### Support recorded in these cases
- Simple algebraic substitution and expansion.
- Unfolding definitions.
- Citing proved theorems.
- Explicit stepwise derivation.

### Misses recorded in these cases
- Larger algebraic transformations without smaller steps.
- Some automatic substitutions across equality sides.
- Certain deeply nested goals.
- Unwritten reasoning that the old verifier did not reconstruct.

### Original guiding principles
1. Keep each goal simple.
2. Supply useful derivation steps explicitly.
3. Build larger results from smaller proved interfaces.
4. Avoid combining the problematic function/index/tuple forms in that old context.

---

## 7. A minimal by-thm-only route in the cosine-law case

### Background
Even after splitting vec_add_path into coordinate lemmas, explicit intermediate tuple equations with vec()[1] still triggered WD errors in the old cosine-law proof.

### Symptom
```litex
Recorded WD-triggering form:
by thm vec_neg(p1, q1)
vec(q1, p1) = (-(vec(p1, q1)[1]), -(vec(p1, q1)[2]))  # Explicit conclusion.
```

The old note attributed this to pre-scanning the explicit equation, even when its cited theorem was valid.

### Historical workaround: theorem calls only

Use by-thm calls without the problematic repeated equations:
```litex
thm cosine_law:
    ? forall p1, q1, r1 cart(R, R):
        distance_sq(p1, r1) = distance_sq(p1, q1) + distance_sq(q1, r1) - 2 * dot(vec(q1, p1), vec(q1, r1))
    
    # Cite the theorem and let its checked consequence support the next step.
    by thm vec_dot_self_is_distance(p1, r1)
    by thm vec_add_path_x(p1, q1, r1)
    by thm vec_add_path_y(p1, q1, r1)
    by thm dot_square_sum(vec(p1, q1), vec(q1, r1))
    by thm vec_dot_self_is_distance(p1, q1)
    by thm vec_dot_self_is_distance(q1, r1)
    by thm vec_neg(p1, q1)
    
    # State the final goal.
    distance_sq(p1, r1) = distance_sq(p1, q1) + distance_sq(q1, r1) - 2 * dot(vec(q1, p1), vec(q1, r1))
```

### Principles scoped to this old case
1. Keep the by-thm calls and final conclusion, omitting the problematic repeated intermediate equations.
2. Reuse the published theorem consequences.
3. Avoid the explicit vec()[1] tuple equations that triggered that pre-scan failure.

### Case record
- Theorem: cosine_law, L516–541, after 27 unsuccessful rounds.
- Attributed trigger: explicit vec()[1] intermediate equations, L533–540.
- Workaround: nine by-thm calls without those equations.
- Outcome: WD passed; the next failure concerned theorem order.

---

## 8. Theorem ordering

### Description
Theorems are checked in source order. A theorem that cites a later declaration can fail as theorem-not-defined.

### Symptom
```
Error: "by thm: theorem `unified::vec_neg` is not defined"
Phase: verify_process (proof execution/checking).
```

This failure occurs during verify_process, not WD: domain checking passed but the theorem citation failed.

### Repair
Put dependencies before their consumers:

```litex
# Dependencies before consuming theorems.
L398:  thm dot_square_sum           # Dependency.
L479:  thm vec_add_path_x          # Dependency.
L491:  thm vec_add_path_y          # Dependency.
L504:  thm vec_dot_self_is_distance # Dependency.
L603:  thm vec_neg                 # Dependency.
L605:  thm cosine_law              # Uses the earlier results.
L634:  thm dot_from_cosine_law     # Uses cosine_law.
```

### Cascading dependencies
Fixing one declaration's order can expose another downstream ordering error:

**Cosine-law example:**
1. cosine_law at L516 preceded vec_neg at L634.
   - Move cosine_law to L620.
2. dot_from_cosine_law at L517 then preceded cosine_law at L620.
   - Move dot_from_cosine_law to L634.

### Debugging
1. Locate declarations with `grep -n "^thm XXX" file.lit`.
2. List every theorem cited with by thm.
3. Move blocks systematically with a script or editor and verify the result.

---

## 9. Complete historical cosine-law repair

### Background
The vector cosine-law theorem depends on several foundational results.

### Repair record: 27 rounds

**Phase 1: WD failure, turns 1–4.**
- Trigger: indexed vec expressions inside tuples.
- Outcome: WellDefinedError.
- Trial: substitute higher-level theorems for handwritten tuples; still failed.

**Phase 2: minimal proof route, turns 5–8.**
- Remove the explicit equations and retain by-thm calls.
- Outcome: WD passed.
- Next error: theorem vec_neg was undefined.

**Phase 3: first ordering failure, turns 9–15.**
- cosine_law at L516 preceded vec_neg at L634.
- Move cosine_law to L620.
- Outcome: cosine_law passed.

**Phase 4: cascading order, turns 16–24.**
- dot_from_cosine_law at L517 preceded cosine_law at L620.
- Move dot_from_cosine_law to L634.
- Outcome: both theorems passed.

### Lessons of the old case
1. The minimal citation route avoided this particular WD trigger.
2. Declaration order mattered for theorem use.
3. Cascading dependencies needed systematic checks.

### Final recorded sources
```litex
thm cosine_law:  # L605–632, using by-thm calls only.
thm dot_from_cosine_law:  # L634–647, consuming cosine_law.
```

---

## 10. Pure algebra in midpoint proofs

### Background
midpoint_equidistant and midpoint_half_distance originally mixed coordinate calculations with theorem calls and lost the derivation chain.

### Failed mixed route
```litex
Recorded failing by-thm bridge:
thm midpoint_half_distance:
    ? forall a, b, m cart(R, R):
        m[1] = (a[1] + b[1]) / 2, m[2] = (a[2] + b[2]) / 2
        =>: distance_sq(a, m) = distance_sq(a, b) / 4
    
    by thm distance_sq_coordinate_formula(a, m)  # The recorded bridge interrupted the chain.
    m[1] - a[1] = (b[1] - a[1]) / 2
# ... Algebraic derivation ...
distance_sq(a, m) = distance_sq(a, b) / 4  # Recorded atomic-fact-unknown failure.
```

**Failure attributed by the old note:**
1. The knowledge introduced by the theorem call did not support the later algebraic chain.
2. The algebraic and function representations were not connected.
3. The final function equality could not be checked directly.

### The successful pure-algebra route

**Principles:**
1. State the function's value equation directly.
2. Keep a complete algebraic chain.
3. State the required subexpression substitution explicitly.
4. Connect the conclusion by transitivity.

**Recorded successful example:**
```litex
Pure-algebra form:
thm midpoint_half_distance:
    ? forall a, b, m cart(R, R):
        m[1] = (a[1] + b[1]) / 2, m[2] = (a[2] + b[2]) / 2
        =>: distance_sq(a, m) = distance_sq(a, b) / 4
    
# Step 1: state the function's value equation without a theorem-call bridge.
    distance_sq(a, m) = (m[1] - a[1])^2 + (m[2] - a[2])^2
    distance_sq(a, b) = (b[1] - a[1])^2 + (b[2] - a[2])^2
    
# Step 2: algebraic substitution chain.
    (m[1] - a[1])^2 + (m[2] - a[2])^2 = ((a[1] + b[1]) / 2 - a[1])^2 + ((a[2] + b[2]) / 2 - a[2])^2
    ((a[1] + b[1]) / 2 - a[1])^2 + ... = ((b[1] - a[1]) / 2)^2 + ((b[2] - a[2]) / 2)^2
    ((b[1] - a[1]) / 2)^2 + ... = (b[1] - a[1])^2 / 4 + (b[2] - a[2])^2 / 4
    (b[1] - a[1])^2 / 4 + ... = ((b[1] - a[1])^2 + (b[2] - a[2])^2) / 4
    
# Step 3: explicit subexpression substitution.
    ((b[1] - a[1])^2 + (b[2] - a[2])^2) / 4 = distance_sq(a, b) / 4
    
# Step 4: connect the endpoint by transitivity.
distance_sq(a, m) = distance_sq(a, b) / 4  # Recorded acceptance.
```

### Technical details

**1. Explicit subexpression substitution**
In the old case the verifier did not automatically identify the required subexpression replacement.

Incorrect assumption:
```
Known: distance_sq(a, b) = (b[1] - a[1])^2 + (b[2] - a[2])^2.
Intermediate: ((b[1] - a[1])^2 + (b[2] - a[2])^2) / 4.
Unverified expectation: automatic equality to distance_sq(a, b) / 4.
```

Recorded accepted approach:
```litex
# State the substitution step explicitly.
((b[1] - a[1])^2 + (b[2] - a[2])^2) / 4 = distance_sq(a, b) / 4
```

**2. Avoid the problematic by-thm bridge in this chain**
In this historical pure-algebra proof the theorem call interrupted the transitive chain.

- Direct value equation: `distance_sq(a, m) = (m[1] - a[1])^2 + ...`.
- Problematic bridge: `by thm distance_sq_coordinate_formula(a, m)`.

**3. Transitivity**
The recorded verifier composed a continuous equality chain:
```
A = B
B = C
C = D
---
A = D  # Derived by transitivity in the old example.
```

The original note required compatible equalities throughout the chain, such as algebraic steps connected to their function endpoints.

### Recorded outcomes
- midpoint_equidistant passed at L516–539.
- midpoint_half_distance passed at L541–565.
- The recorded success count rose from 196 to 229, an increase of 33.

### Relevant situations
The historical pure-algebra route covered:
1. Coordinate proofs using [1]/[2] projections.
2. Multistep algebraic simplification.
3. Proofs relating function and algebraic representations.

### Lessons of the case
1. Every link must be a checkable equality.
2. Expose the substitution that the measured verifier needs.
3. Preserve a continuous chain without unjustified jumps.
4. A theorem call may coexist with algebra when the final chain explicitly connects function endpoints and complete scalar intermediates; publishing an expansion alone did not justify the shortcut.

---

## 11. Auditing a split knowledge base for completeness

Byte equality with a local source proves copying fidelity, not source completeness. If a file stops at a new heading, inspect the package before adding material:

1. Every configured export.
2. The actual module owning the allegedly missing prop, function, or theorem.
3. Declaration inventories and module responsibilities.
4. A fresh remote checkout and a real consumer using only its repository dependencies.

In the recorded case a trailing heading in definitions.lit was a split artifact; is_midpoint already lived in predicates.lit. The repair clarified boundaries and removed the misleading heading instead of duplicating the predicate.

---

## 12. Cancelling a left scalar factor

Given 2*x=2*y, do not first rely on rewriting to x*2=y*2 merely to fit a right-factor cancellation theorem. The old verifier could miss that commutative transport.

Recorded accepted continuous chain:
```litex
x = (2 * x) / 2 = (2 * y) / 2 = y
```

This division chain cancels the left constant directly, useful after a distance formula establishes equality of doubled dot products.

---

## 13. Solving coordinate equations and reversing affine parameters

The old verifier might not rearrange d=a+c-b into c=d+b-a directly. First add the same expression, then use the subtraction theorem within a complete equality chain:
```litex
d + b = (a + c - b) + b = a + c
(d + b) - a = (a + c) - a by thm geo::subtract_equalities(d + b, a + c, a, a)
c = (a + c) - a = (d + b) - a = d + b - a
```

For reversed affine endpoints, prove the new parameter equations coordinate by coordinate, then unfold the definition and use the distance theorem:
```litex
p[1] = (1 - u) * c[1] + u * b[1]
p[2] = (1 - u) * c[2] + u * b[2]
by def $geo::is_affine_combination(p, c, b, u)
by thm geo::affine_combination_distance_sq(c, b, p, u)
```

---

## 14. Positive-real witnesses for a defined ratio

Known squared distances and a ratio equality did not make by def construct the definition's exist ... R+ automatically. Supply all positive witnesses and their body facts explicitly:
```litex
witness exist ab, cd R+ st {
    ab^2 = distance_sq(c, e),
    cd^2 = distance_sq(b, c),
    4 * ab = cd
} from side / 4, side:
    (side / 4)^2 = distance_sq(c, e)
    side^2 = distance_sq(b, c)
    4 * (side / 4) = side
```

Each witness expression must already have verified R+ membership; build it from the positive length witnesses obtained by unfolding.

Match the witness body's expression order. Even known x+y>z may not instantiate y+x>z automatically. Establish the commuted equation and the target-oriented inequality before witness. The historical triangle_inequality case strictly checked this route.

---

## 15. Nested vector expansion and positive scaling

If dot(vec(a,p),vec(d,p)) does not unfold directly, state both vector equations and all four coordinate equations first, then connect their scalar products with the dot definition. If replacing vec(a,a) by (0,0) misses, substitute its coordinate formulas instead.

For a positive scaling target from 0<x, the old case exposed the positive-integer scaling step explicitly:
```litex
0 < 3
0 < 4
0 < 3 * x
0 < 3 * x / 4
```
Then connect the target to 3*x/4 by an equality chain; use the analogous route for x/4.

---

## 16. Common terms in squared equalities and explicit rearrangement

After fully expanding squared coordinate distances, normalize shared terms into A+C=B+C before using addition_cancel(A,B,C); the old verifier did not reliably find a term across different association orders.

From A-X=B-Y, add X to both sides. First establish the sub_add_cancel(A,X) bridge instead of combining every substitution at once, then keep the continuous chain. Subtract the two resulting linearized equations and expose distribution/association as its own step.

The archived power_of_point_difference strict gate checked this pattern for differences of two equal-distance expansions.

---

## 17. Function-value unfolding and angle-ratio cancellation

A value function is not a standalone `by def f(args)` proof command; that old form triggered parsing errors. State its value equation directly, then compose the equality chain.

For squared cosine equations from are_angles_congruent, first work with angle_cos_num/angle_cos_den. Prove denominator proportionality and nonzeroness, cancel their common factor, and use the predicate's same-sign numerator condition to select the scalar root. Only then unfold the numerator as a dot product. Problem 214 recorded this route in an independent zero-error source/archive check.

---

## 18. Separate quotient cancellation from witness substitution

After defining t=target/s, first prove s!=0 and the canonical quotient-cancellation form rather than expecting definition unfolding and cancellation together:
```litex
(target / s) * s = target
t * s = (target / s) * s = target
```
Separate cancelling the quotient from substituting t. The point-construction case with s=sqrt(distance_sq(a,b)) strictly checked this route.

A witness from a concrete tuple may not instantiate a local g equation automatically. Add the concrete-expression bridge:
```litex
distance_sq(g, b) = target^2
distance_sq(<concrete tuple>, b) = distance_sq(g, b) = target^2
```
This aligns the goal with the actual witness. The historical test_point_on_line_with_distance library check confirmed the route.

---

## 19. Compound substitution in AAS and a same-sign scaling bridge
For the AAS squared-cosine chain, reverse edge equalities may not substitute automatically under products and powers. Normalize both sides to one compound RHS and connect them stepwise:
```litex
X * old_rhs = X * normalized_rhs
X * normalized_rhs = new_lhs * normalized_rhs
```
Do not skip the compound term. The archived triangle_congruence_AAS strict gate checked this RHS-to-RHS bridge.

From u*v>=0, first establish 4*(u*v)>=0 and the identity 4*(u*v)=(2*u)*(2*v) before concluding the doubled-factor product is nonnegative. The complete AAS library regression recorded this route.

---

## 20. Ray orientation at a midpoint and separate coordinate products

Check directed rays before translating vertical angles into dot products. If d is the midpoint of a,c, vec(d,a)=-vec(d,c); reversing just one ray changes the sign. Reverse both relevant rays:
```litex
dot(vec(d, b), vec(d, a)) = dot(vec(d, c), vec(b, d))
```
Do not leave vec(d,b) unchanged on the right; a concrete coordinate counterexample detected that error.

If the sum of two double-negated coordinate products misses, prove each scalar equality separately, explicitly connecting commutation and negation, then combine with add_equalities. The vertical_angles_dot_equal prefix and full-library checks recorded this route.

---

## 21. Lift a scalar identity and distribute distance sums

Multiply the scalar identity by the common factor, such as ux^2+uy^2, with multiply_both_sides. Combine distance formulas with add_equalities, expose distribution separately, then connect the target by a continuous chain. Problem 229 recorded 264 entries and no errors for the complete audit.

---

## 22. Directed meaning in a diagram's equal-angle condition

Cosine equality for undirected angles permits both rotation directions. If the source diagram selects one direction and later SAS reasoning depends on it, retain that source condition; do not invent the desired final angle as a premise.

A reusable directed-angle relation retains undirected equality and requires the product of corresponding oriented areas/determinants to be nonnegative, for example:
```litex
$geo::are_angles_congruent(p, q, r, u, v, w)
geo::det(geo::vec(q, p), geo::vec(q, r)) * geo::det(geo::vec(v, u), geo::vec(v, w)) >= 0
```
Use this only when the original wording or diagram supplies the same-direction information, and document its source. The reusable relation may live in translation; problem-specific inference bridges belong in solution.

---

## 23. Cancellation with a common minuend

For c-x=c-y, subtraction_cancel targets a common subtrahend, not this shape. Rather than multiplying by -1 and assuming normalization, use the following continuous subtraction chain:
```litex
thm cancel_same_minuend:
    ? forall c, x, y R:
        c - x = c - y
        =>:
            x = y
    x = c - (c - x)
    y = c - (c - y)
    c - (c - x) = c - (c - y)
    x = y
```
The historical template passed fresh ordinary and full-dependency strict checks.

---

## 24. Historical IMO syntax pitfalls

This section records nine syntax problems found in the IMO 1960 Problem 3 work, across 34 debugging rounds.

### 24.1 Module namespaces

Recorded incorrect form:
```litex
import "../../Litex/geo_module" as geo
geo::is_right_angle(...)  # Missing the intermediate main:: level.
```

Recorded accepted form:
```litex
import "../../Litex/geo_module" as geo
geo::main::is_right_angle(...)  # Complete namespace in that configuration.
```

An export keyed main requires the module_alias::export_key::name shape used in this old module.

### 24.2 The recorded top-level have issue

Incorrect in the old case:
```litex
# File top level.
have x = 5  # The old note restricted this form to proof bodies.
```

Recorded accepted form:
```litex
thm my_theorem:
    ? goal
have x = 5  # Inside the theorem proof body.
    ...
```

Recorded error: `name 'have' is already active in this scope and cannot be rebound`.

### 24.3 prop parameters

Incorrect:
```litex
prop conditions(ptA: cart(R, R), a: R):  # Colon-style declarations.
    ...
```

Correct:
```litex
prop conditions(ptA, ptB cart(R, R), a, h R):  # Group names before each type.
    ...
```

Separate parameter names with commas, group names sharing a carrier, and put their type at the end of each group.

### 24.4 Multiple constraints in a prop

Incorrect in the recorded syntax:
```litex
prop conditions(...):
ptA != ptB and ptB != ptC  # The old note rejected this conjunction spelling.
```

Recorded accepted form:
```litex
prop conditions(...):
    ptA != ptB
ptB != ptC  # One clause per line.
```

The old prop bodies expressed conjunction by separate lines rather than an and keyword.

### 24.5 Calling another prop

Incorrect:
```litex
prop statement(...):
conditions(ptA, ptB, ...)  # Missing $.
```

Correct:
```litex
prop statement(...):
$conditions(ptA, ptB, ...)  # Predicate-call prefix.
```

The same prefix applies to a predicate called in a theorem's universal goal.

### 24.6 Geometry library functions: distance versus distance_sq

Incorrect for that library:
```litex
geo::main::distance(ptA, ptB) = a  # That library has no distance function.
```

Recorded interface:
```litex
geo::main::distance_sq(ptA, ptB) = a^2  # Squared distance.
```

The old geo_module supplies distance_sq, avoiding square roots. Express distance equalities in squared form for that interface.

### 24.7 Geometry predicates: altitude versus foot

Incorrect for that library:
```litex
geo::main::is_altitude(ptH, ptA, ptB, ptC)  # That predicate is absent.
```

Recorded interface:
```litex
geo::main::is_foot(ptH, ptC, ptA, ptB)  # Perpendicular-foot predicate.
```

is_foot(h,p,a,b) means h is the perpendicular foot from p onto ab. Express the altitude through that foot relation.

### 24.8 Nonzero conditions for division and tangent

Incorrect: missing domains.
```litex
prop statement(...):
tan(alpha) = 4 * n * h / ((n * n - 1) * a)  # Missing nonzero conditions.
```

Recorded explicit conditions:
```litex
prop statement(alpha, n, h, a R):
cos(alpha) != 0      # Tangent domain.
n * n - 1 != 0       # Nonzero denominator factor.
a != 0               # Nonzero denominator factor.
    tan(alpha) = 4 * n * h / ((n * n - 1) * a)
```

Recorded errors:
- tan(alpha) is not well defined: cos(alpha)!=0 is missing.
- The divisor cannot be checked nonzero: the denominator constraints are missing.

Check domains for division and partial trigonometric functions. A predicate calling angle_cos_num/den(p,q,r) needs p!=q and r!=q; a second angle similarly needs its own nondegeneracy. Missing conditions can block the full strict library precheck before the problem proof.

### 24.9 Theorem bodies and historical trust syntax

Incorrect in the old note:
```litex
thm problem_1:
    ? forall x R: P(x) =>: Q(x)
# An empty body or a lone trust keyword.
```

Recorded assumed version:
```litex
thm problem_1:
    ? forall x R: P(x) =>: Q(x)
trust $Q(x)  # Trust followed by the assumed fact.
```

Recorded complete-proof version:
```litex
thm problem_1:
    ? forall x R: P(x) =>: Q(x)
# Actual proof steps.
    have step1 = ...
    have step2 = ...
    $Q(x)
```

Rules recorded by the old guide:
- Its ? theorem form required a proof body rather than just a goal.
- When a proof was incomplete, an explicit trust fact marked the assumption.
- trust needed a concrete fact rather than appearing alone.

### Debugging summary

The nine issues were resolved in the recorded 34 rounds. Common categories:
1. Missing namespace levels, especially main::.
2. Missing division/trigonometric domain conditions.
3. Missing $ on predicate calls.
4. Incorrect library-interface names.

Historical debugging order:
1. For fact-not-defined errors, inspect namespaces and the library.
2. For WD failures, establish the justified domain/nonzero conditions.
3. For unexpected-token errors, inspect parameter and clause syntax.
4. Use the old parser tool for its supported recursive error schema.

---

## Version history
- 2026-09-12: added common-minuend cancellation by a double-subtraction chain.
- 2026-09-07: added directed meaning for diagram-specified equal angles.
- 2026-09-05: added common-factor lifting and explicit distance-sum distribution.
- 2026-09-04: added midpoint ray-orientation checks and separate dot coordinates.
- 2026-09-04: added AAS compound-RHS substitution and doubled same-sign scaling.
- 2026-09-21: added section 24 with nine historical syntax/interface topics.
- 2026-09-03: added separate quotient cancellation and concrete witness substitution.
- 2026-09-01: added function-value unfolding and ordinary-angle squared-cosine cancellation.
- 2026-09-01: added common-term cancellation and explicit rearrangement of squared equalities.
- 2026-09-01: added coordinate-wise nested vector unfolding and positive scaling.
- 2026-09-01: added coordinate solving, affine reversal, and positive ratio witnesses.
- 2026-08-31: added the division-chain cancellation of a left constant.
- 2026-08-29: added split-KB completeness auditing.
- 2026-08-28: initial vec_add_path WD case.
- 2026-08-28: added the minimal citation route, ordering checks, and full cosine-law case.
- 2026-08-28: added the pure-algebra midpoint cases.

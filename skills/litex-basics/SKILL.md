---
name: litex-basics
description: Basic Litex competence — Session, core syntax, carriers, cart/tuples/coordinates, small definitions and short proofs. Use first for ordinary Litex writing or any API/agent smoke test; load litex-intermediate or litex-advanced only when this layer is not enough.
---

# Litex basics (basic layer)

Teach an agent or API caller enough Litex to write **small, checkable mathematics**:
objects, functions, props, finite sets, Cartesian products, 1-based coordinates,
and short theorems/claims. Distilled from the golitex Manual / Learner Cheatsheet /
Learn Litex docs. This file is the **API-injectable** core; deeper cards live under
`references/` and `examples/`.

**Not this layer:** induction tactics, module imports, large textbook interfaces,
kernel work — use `litex-intermediate` / `litex-advanced` / task skills.

## 1. Working model

Litex extends a mathematical context. Objects have carriers. Accepted facts become
available later. A fact must be well-defined before proof search. An ordinary
rejection does **not** erase earlier accepted work and does **not** prove a negation.

```litex
have a R = 2
a + 1 = 3
a^2 = 4
```

`have` declares; `=` checks equality (not mutable assignment). Write multiplication
explicitly: `2 * x`, never `2x`.

## 2. Keep one Session

```bash
litex -lang en -strict -session -e 'have a R = 2'
```

Enter one top-level statement at a time; end indented blocks with a blank line.
Repair only the failed statement in the **same** process. Do not restart the whole
file after adding a few lines. Use `litex -lang en -strict -f file.lit` for clean
checkpoints / final delivery.

## 3. Choose syntax by role

| Need | Form |
| --- | --- |
| Value with carrier | `have x S = value` |
| Arbitrary member | `have x S` (nonempty carrier; no chosen numeral) |
| Expression alias | `let name = expression` |
| Callable | `have fn f(x S) T = expression` (guards before `)`) |
| Condition | `prop P(x S):` … then `$P(a)` / `by def $P(a)` |
| Universal / conditional | `forall x S:` ; premises before `=>:`, conclusions after |
| Existence | `exist x S st {facts}` / `exist! …` |
| Local proof | `claim:` with `? goal` |
| Named result | `thm name:` with `? goal` |

Membership / order: `a $in S`, `A $subset B`, `=`, `!=`, `<`, `<=`, `>`, `>=`.
Native carriers include `N`, `Z`, `Q`, `R`, `C`, `R+`, … In current Litex, `N`
includes zero; use `N+` for positive naturals.

## 4. Products, tuples, coordinates (required)

These are the forms that most often break “smart but wrong” answers:

| Mathematics | Litex |
| --- | --- |
| Cartesian product \(A \times B\) | `cart(A, B)` — **not** `A * B`, not bare `R × R` as a product of numbers |
| Ordered pair | `(a, b)` |
| One-based coordinates | `p(1)`, `p(2)` — ordinary function application |
| Subsets of a set | `power_set(S)` |
| Set builder | `{x R: condition}` |

**Forbidden for `cart(R,R)` coordinates:** `p.1`, `p.fst`, `p[0]`, `p[1]`, `p(0)`.
Indexing with `[]` is removed. Unary tuple is `tuple(a)` or `(a,)`; `(a)` is grouping only.

```litex
have points set = cart(R, R)
have fn vec(A, B cart(R, R)) cart(R, R) = (B(1) - A(1), B(2) - A(2))
have p cart(R, R) = (2, 3)
p(1) = 2
p(2) = 3
```

Unicode `×` means Cartesian product of **sets** (`2 × 3` is not numeric multiply).
Numeric multiply is always `*`.

## 5. Small definitions and short proofs

Guarded function + named law + citation:

```litex
have fn reciprocal(x R: x != 0) R = 1 / x
thm reciprocal_product:
    ? forall x R:
        x != 0
        =>:
            reciprocal(x) * x = 1
    reciprocal(x) = 1 / x
    reciprocal(x) * x = (1 / x) * x = 1
by thm reciprocal_product(2) => reciprocal(2) * 2 = 1
```

Proof grain:

1. Split large equality jumps into smaller bridges.
2. Repair only the first rejection.
3. `by thm name(args) => fact` selects a **returned atomic** conclusion; it does
   **not** reverse `a = b` to `b = a`. Prefer `release thm` when publishing all
   conclusions.

Existence:

```litex
witness exist w R st {w^2 = 4} from 2
obtain root from exist w R st {w^2 = 4}
```

`exist!` needs uniqueness; a real square root of 4 is not unique.

## 6. Quick misconception list

- Rejection ≠ negation; Session keeps prior accepts.
- `prop` alone proves no instances — use `by def $P(args)`.
- Without `=>:`, every `forall` body fact is a **conclusion**.
- Proof commands (`witness`, `by def`, …) belong in a proof body (`claim` / `thm`), not a bare fact `forall`.
- Domain guards are checked before the function result.
- Arbitrary `have x S` is not a chosen numeral.
- Claim helpers stay local.
- **Do not encode \(R\times R\) as `R * R`; do not read coordinates with `.` or `[]`.**

Runnable cards: [misconceptions.md](references/misconceptions.md).
Patterns and examples: [math-patterns.md](references/math-patterns.md),
[examples/](examples/README.md).

## 7. Next layers

| Layer | Skill | When |
| --- | --- | --- |
| Basic (this) | `litex-basics` | Learn Litex; smoke tests; small defs/proofs |
| Intermediate | `litex-intermediate` | Cases, induction, richer existence, calculation tactics |
| Advanced | `litex-advanced` | Modules, large interfaces, textbook/agent workflows |

Task skills (`litex-proof-writer`, …) assume this basic layer. Live Manual depth:
`litex-reference` against a golitex checkout.

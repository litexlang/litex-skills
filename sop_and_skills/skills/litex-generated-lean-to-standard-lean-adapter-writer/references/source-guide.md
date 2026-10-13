# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Generated Lean to Standard Lean Adapter Writer

Expose a compiler-generated Litex proof as an ordinary Lean/Mathlib theorem
without leaking the generated ABI into the theorem users actually want.

## Derive the bridge forward from evidence

Construct the adapter from the independently meaningful source theorem, the
exact generated signature, proved Core bridge laws, and the desired native
mathematical semantics. Derive each representation conversion and its owner,
then the native `Adapter` theorem, then the minimal `Final.lean` consumer. The
desired final statement identifies the conversion obligations but does not
justify bridge assumptions, wrapper parameters, casts, axioms, or a second
independent proof.

Use backward reasoning from `Final.lean` only to inventory requirements and
audit the consumer path. When the path fails, trace it to the earliest missing
generated evidence or proved conversion and fix or report that boundary; do
not leak the gap into the final theorem. If the final theorem were hidden,
every public Adapter conversion must still be justified by a sound reusable
representation relation rather than by this one conclusion.

## Preserve the statement/proof boundary

Use this as the governing mental model:

> Write the `Final.lean` theorem statement as if Litex did not exist.
> Call `Adapter` only inside the `by` proof body.

The theorem statement means every binder, hypothesis, and conclusion before
`:= by`. It must use only ordinary Lean/Mathlib objects and propositions. It
must not mention:

- `Litex.*` predicates, objects, sets, relations, or evidence;
- compiler-owned names such as `__Compiler_*`;
- `Adapter.*` types, predicates, wrappers, or bridge parameters;
- an explicit argument such as `(bridge : Adapter.IntegerSameEqBridge)`.

`import Adapter` is allowed because an import is not part of the theorem
statement. Inside the proof body, cite a native theorem exported by
`Adapter`; do not call the compiler-generated declaration directly from
`Final.lean`.

Do not change or weaken the desired native statement merely to match the
generated theorem's ABI. If the representations cannot yet be bridged, report
the missing evidence or Core/compiler interface instead of leaking it into
the final theorem.

## Keep the four layers distinct

Use the following ownership boundary, adapting filenames only when the
project already has a different convention:

1. The `.lit` source owns the mathematics and its proof.
2. `Generated.lean` is compiler-owned proof replay and must never be hand-edited.
3. `Adapter.lean` is the only handwritten representation interface. Use
   `namespace Adapter` by default. Its public theorem statements should
   already be native Lean/Mathlib propositions; its proof bodies may cite
   generated declarations and use `Litex.*` bridge theorems.
4. `Final.lean` declares the theorem the Lean user originally wanted and
   proves it by citing `Adapter`. Do not stop after the Adapter compiles: keep
   this final native consumer as an explicit acceptance file.

The Adapter converts interfaces; it does not perform the mathematical proof
a second time. Its generated theorem citation must be a live dependency. A
binding named `generated` that is never used is not evidence of reuse.

## Treat `Same` to `Eq` as an audited specialization

Litex uses **membership-oriented, representation-independent semantics**.
Lean host types represent values, `Litex.In x S` classifies the mathematical
value represented by `x`, and `Litex.Same x y` expresses heterogeneous
semantic equality across approved representations. `Same` is neither native
Lean `Eq` nor merely `HEq`; a value may acquire several membership facts
without being retyped or replaced.

Keep the conversion direction explicit:

```text
Lean Eq ⊆ Litex.Same  via Same.ofEq
Litex.Same --reviewed same-carrier, injective observation--> Lean Eq
```

Treat `Lean Eq ⊆ Litex.Same` as the global relation. The Adapter is the right
layer for a reviewed reverse specialization, but its location does not make
that arrow automatic. Merely learning that both endpoints have the same Lean
type is insufficient: for example, two values of type `Litex.Set` can be
extensionally `Same` while packaging different exact carriers, so they need
not be Lean-equal structures. Use a public, proved Core eliminator only after
the generated endpoints have reached a canonical native carrier with a
faithful/injective observation. For example, `Same.complexNativeEq` converts
`Same x y` to `x = y` when `x y : ℂ`; `Same.complexEq` can compare explicitly
supplied complex observations. Never treat arbitrary heterogeneous `Same`
evidence as a Lean rewrite certificate, invent a global `Same → Eq` bridge,
or hide missing representation evidence in an Adapter assumption. For sets,
adapt to native equality through a reviewed extensional-membership theorem or
an injective native set observation, not through host-type coincidence.

Choose the public Adapter theorem's native binders from the desired
Lean/Mathlib interface, not merely by copying the generated host carrier. If a
generated `R` binder is represented as `x : ℂ` plus `In x R`, a native real
consumer may require the Adapter to embed `r : ℝ` into `ℂ` and construct the
reviewed membership evidence. Conversely, when generated equality already has
native complex endpoints, eliminate `Same` with `complexNativeEq`. A generic
binder whose numeric status appears only in a later premise remains generic;
the Adapter must not retroactively pretend that its host type was `ℂ`.

## Write the Adapter from evidence, not convenience

1. Freeze the desired native theorem statement from `Final.lean`, including
   its native inputs, hypotheses, and conclusion.
2. Inspect the exact generated theorem signature. Inventory each conversion:
   native input or premise into the generated representation, then generated
   conclusion back into the native proposition.
3. Give the Adapter theorem a native public signature. Keep Litex and
   generated names inside its proof body.
4. Cite the exact generated theorem and consume the returned proof evidence.
   Use public definitions and fully proved elimination theorems to unwrap
   `Litex.Same`, membership, order, casts, sets, or other wrappers.
5. Prefer an existing public Core bridge over a local wrapper. Add only the
   smallest problem-specific conversion that is genuinely missing.
6. Confirm the Adapter would no longer prove its result if the generated
   theorem citation were removed. Do not replace that dependency with an
   independent Mathlib induction, normalization proof, or theorem search.

Never introduce a project `axiom`, `sorry`, `admit`, unsafe cast, or a
primitive relation defined as `True`. Do not install user-supplied bridge
evidence as a hidden theorem assumption. When a sound elimination path is
missing, stop at that exact interface gap.

## Canonical odd-sum example

The positive `Final.lean` shape is:

```lean
import Adapter

theorem firstHundredPositiveOddIntegersSum :
    ∑ k ∈ Finset.Icc (1 : ℤ) 100, (2 * k - 1) = 10000 := by
  exact Adapter.sumFirstOddsNative 100 (by norm_num)
```

The proposition after `:` knows only `Finset`, integers, summation, and native
Lean equality. Litex is absent from the statement. The proof body calls the
native Adapter theorem, whose proof in turn cites the compiler-generated
odd-sum theorem.

Reject shapes like:

```lean
theorem firstHundredPositiveOddIntegersSum
    (bridge : Adapter.IntegerSameEqBridge) :
    ∑ k ∈ Finset.Icc (1 : ℤ) 100, (2 * k - 1) = 10000 := by
  exact Adapter.sumFirstOddsNative bridge 100 (by norm_num)
```

Also reject a `Final.lean` conclusion written as `Litex.Same ...` or one that
mentions `__Compiler_main.*`. Those are generated/Adapter-facing interfaces,
not the standard Lean theorem requested by the user.

## Verify the real consumer path

Use the project's Lake environment rather than bare `lean`:

```bash
lake setup-file Adapter.lean
lake env lean Adapter.lean
lake env lean Final.lean
```

Also run any project-owned generated-drift or compiler gate required by the
repository. Before completion, audit all of the following:

- `Generated.lean` was not hand-edited;
- the Adapter public theorem has a native proposition;
- its proof has a live citation to the intended generated theorem;
- the Final theorem statement contains no Litex, generated, Adapter wrapper,
  or bridge-parameter vocabulary;
- only the Final proof body cites `Adapter`;
- no axiom or proof hole was introduced;
- the exact `Final.lean` consumer passes the real Lean kernel.

Report an unresolved representation conversion honestly. A successful
Adapter build alone is not completion when the native `Final.lean` theorem
still fails or its statement exposes Litex.

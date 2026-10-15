# Runnable foundation examples

These small examples were checked with an existing executable reporting
Litex 1.0.7-beta, using `-lang en -strict`. They need no language-source
checkout. A different executable/version needs its own checks.

Author in one live Session; use a clean file run for a saved checkpoint:

```sh
litex -lang en -strict -session -f functions.lit
litex -lang en -strict -f functions.lit
```

Run these commands from this directory, or pass the actual absolute file path.
Only the module example has a parent `litex.config` and depends on another file.

| File | What it demonstrates |
| --- | --- |
| [quickstart.lit](quickstart.lit) | Declaration, direct arithmetic and a universal identity |
| [functions.lit](functions.lit) | Nonzero function domain, inverse law and theorem selection |
| [logic.lit](logic.lit) | Property instances, conditional premises and dependent witnesses |
| [existence.lit](existence.lit) | Supplying/extracting a witness and proving simple uniqueness |
| [sets.lit](sets.lit) | Finite set membership and exhaustive finite cases |
| [products.lit](products.lit) | `cart(R,R)`, pairs, and `p(1)` coordinates |
| [sequences.lit](sequences.lit) | A function indexed by natural numbers |
| [induction.lit](induction.lit) | Base and induction step for an exponential inequality |
| [modules/](modules/README.md) | Registered exports, canonical names and definition release |

The files below are **expected to fail**. Do not include them in accepted
source or treat their rejection as a test failure. Run each separately and
inspect the actual phase; a missing executable is not a successful rejection.

| Rejected control | Intended boundary |
| --- | --- |
| [function-domain.lit](negative/function-domain.lit) | Zero does not satisfy the reciprocal's domain |
| [property-instance.lit](negative/property-instance.lit) | Defining a property proves no arbitrary instance |
| [missing-premise.lit](negative/missing-premise.lit) | All real numbers are not nonzero |
| [nonunique-witness.lit](negative/nonunique-witness.lit) | One square root is not a uniqueness proof |
| [arbitrary-member.lit](negative/arbitrary-member.lit) | An arbitrary natural number is not necessarily two |
| [local-name.lit](negative/local-name.lit) | A claim's local helper name is unavailable outside it |
| [fact-body-command.lit](negative/fact-body-command.lit) | A universal fact body does not accept proof commands |
| [by-thm-equality-orientation.lit](negative/by-thm-equality-orientation.lit) | `by thm ... =>` does not reverse a returned equality |
| [negative-unqualified.lit](modules/negative-unqualified.lit) | Another export's short object name is unavailable |

The local-name, fact-body and unqualified-name examples cause parse termination
in the measured executable. Ordinary proof/domain rejections are different:
they can return to a live Session while retaining earlier accepted facts.
See the [misconception cards](../references/misconceptions.md) for corrected
forms. Current clean-run evidence and the same-Session failure/repair transcript
live in the source hub's dated validation record, outside lightweight packs.

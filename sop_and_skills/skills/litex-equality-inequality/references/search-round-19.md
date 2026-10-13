# Search round 19 — exact integer division and triangular parity

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


32 independent strict probes: 12 accepted, 20 rejected. Rejections include true capability misses and invalid-domain/mathematical controls; counts are not a correctness score. Fresh source release build succeeded, immutable binary used throughout.

## Recommendations

- Exact quotient integer carrier from zero remainder, with checked integer/nonzero-divisor evidence. Positive-divisor Euclidean proof passes with two equations; signed general implementation requires its own checked route. [Part 56](part-56-exact-integer-quotient.md).
- Integer-multiple witness directly supplies quotient integer carrier. Direct type misses; one equality a/b=q allows existing type transport to finish, including nonzero signed b. Avoid arbitrary witness search. [Part 56](part-56-exact-integer-quotient.md).
- Consecutive-product parity modulo 2, followed by exact-quotient and nonnegative-carrier composition for n*(n+1)/2. The full residue proof and integer/natural consumer interfaces pass without trust. [Part 57](part-57-triangular-parity-carrier.md).

## Existing support and authoring

Native positive-divisor Euclidean decomposition/quotient codomain and direct witness quotient equality already pass. No duplicate Euclidean/type-transport law proposed. Complete residue cases require explicit chain endpoints in this proof. Triangular natural proof has a removable final type echo; numerator sign bridge remains necessary in the tested short variant. Native factorial ratio integer consumer passes through the checked quotient theorem.

[Receipt](evidence/round-19-2026-10-09.summary.json), `evidence/round-19-cases/`, build log `evidence/round-19-build.log`. Positive exact quotient, signed supplied-witness typing and parity misses are repaired in an unchanged Session; independent files authoritative. Missing divisibility, zero/negative-native-quotient divisor, half-integer and natural-positive zero-boundary controls reject; closed signed exact ratios pass.

No kernel/canonical source changes, source definition weakening, trust, whole-module or performance claims. Next: Concrete Mathematics summation-factor recurrence algebra and indexed numeric type/congruence consumers; test source proof helper elimination before proposing new recurrence automation.

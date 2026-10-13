# Search round 8 — Residues, shifts and cancellation

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current working-tree release build succeeded on 2026-10-08. 29 valid isolated
strict probes. Two text-generated variants accidentally changed claim goals;
they are explicitly excluded, retained only as discarded attempts in JSON,
and superseded by corrected original-target probes. No kernel/canonical edits.

## Recommendations

1. Residue equality / zero difference equivalence: a%m=b%m iff
   (a-b)%m=0 for integer operands and positive modulus. Both direct targets
   miss; complete explicit routes pass. An opaque-argument polynomial bridge
   is required by the tested forward chain. [Part 26](part-26-residue-difference.md).
2. Modulo periodicity: (a+k*m)%m=a%m misses directly; a distribution and
   zero-residue chain passes. This fixed shape is a bounded general rule,
   not a special constant calculation. [Part 27](part-27-modulo-additive-cancellation.md).
3. Common additive shift cancellation: equal (a+k)%m,(b+k)%m should give
   a%m=b%m. Direct misses; a corrected proof with explicit dividend identities
   and one native congruence step passes. The hidden k needs bounded stored-
   relation matching. Do not infer unsigned multiplicative cancellation.

Arithmetic normalization under modulo is a related consumer audit, not blanket
authorization to broaden global rewriting. Record exact phase and preserve
integer/positive-modulus WD and proof evidence.

## Existing support and pending interfaces

Add/subtract/multiply congruence and distribution, remainder uniqueness,
nested multiple moduli, positive-divisor gcd Euclid, and positive common-
divisor gcd bound pass directly. No duplicate rule recommendations.
[Part 28](part-28-number-theory-existing-support.md).

Coprime multiplication cancellation misses from gcd(k,m)=1. A separate variant
with supplied Bezout coefficients passes. The coefficient-production interface
was not verified; this is not yet a ready local bt fix for the original target.
Signed gcd Euclid with abs(b) also misses; only positive b route was checked
as supported. Keep those observations separate from confirmed direct/explicit
capability gaps above.

## Coverage and next work

Anchors: Concrete Mathematics Chapter 4 Euclidean/gcd development and native
modulo congruence, remainder and nesting examples. Reduced scalar proofs were
verified, not full chapter/source replacements or runtime savings.

Next: finite sum/product inequalities and pointwise estimate consumers in
Concrete Mathematics Chapter 2 and Analysis; inspect available aggregate
interfaces before reconstructing induction or proposing new bt.
Corpus queue remains unfinished.

Evidence: [receipt](evidence/round-08-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Twenty-eight dated parts exist.

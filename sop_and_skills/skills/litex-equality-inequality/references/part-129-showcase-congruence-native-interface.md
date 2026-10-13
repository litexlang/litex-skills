# Part129 — Actual congruence addition: reuse the linear-combination interface

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The number-theory showcase's congruent_mod(a,b,modulus) means modulus>0 and
an integer divisibility witness for a-b. Preserve the source predicate, all
integer carriers and both congruence premises. Use Part128's short prefix.

## Preferred proof: ten actions become two

Under the original forall a,b,c,d,modulus Z and two congruence premises:

```litex
release thm common_divisor_divides_linear_combination(modulus,a-b,c-d,1,1)
(a+c)-(b+d)=(a-b)*1+(c-d)*1
```

The existing theorem supplies divisibility of its actual linear-combination
expression. The second statement transports exactly that expression to the
required difference. No helper theorem, new witness, modulus weakening or
new bt is introduced. Final definition folding is unnecessary in this route.
[Complete preferred file](evidence/round-101-cases/native-interface-exact-argument-bridge.lit).

## Verbose comparison and alternative

The original proof unfolds both input predicates, obtains two witnesses,
echoes their equations, calculates the combined difference, supplies a witness
with its own repeated proof body, then folds the result. A checked alternative
omits all unfold/echo/proof-body actions and keeps four statements:

```litex
obtain k from $divides_by(modulus,a-b)
obtain m from $divides_by(modulus,c-d)
(a+c)-(b+d)=(a-b)+(c-d)=modulus*k+modulus*m=modulus*(k+m)
witness $divides_by(modulus,(a+c)-(b+d)) from k+m
```

This remains a usable alternative, but does not need to reimplement the existing
linear-combination interface for the preferred case. Deleting that alternative's
calculation or shortening it to a direct factorization/three-term chain rejects.

## Precise interface boundary

A native call alone rejects at the theorem conclusion, not its premises. Adding
after it only `(a+c)-(b+d)=(a-b)+(c-d)` still rejects. Input unfolding, two
explicit divisibility facts or a final congruence fold do not alone resolve that
route. The exact bridge including the native coefficient factors *1 passes,
with or without the final fold. The cause of this transport boundary is not
established; no permanent general obligation to spell *1 is inferred.

## Consumers and negatives

The complete short standalone number-theory source passes. A signed consumer
uses congruent_mod(-8,2,5) and congruent_mod(23,3,5), calls the shortened theorem,
and verifies congruent_mod(15,5,5). Zero modulus, false residue pair (2,3,5),
wrong witness k*m in the alternative, missing second premise and false sum
conclusion b+d+1 reject. The preferred route also rejects zero modulus and
missing-premise/false-sum controls. Mathematical negatives differ from the
true interface/transport misses above.

## Evidence

[Receipt](evidence/round-101-2026-10-10.summary.json):26 strict files,
10 accepted/16 Normal rejections, promoted paths rerun with matching exits,
Normal envelopes and null session errors. Exact source and binary identities
recorded; fixed snapshot from successful round88 build reused. Cold files own
route/deletion evidence. Same source family as Parts127–128, not independent
permanent-rule promotion. No canonical/kernel edits, trust, new bt, performance,
global-minimum, canonical module or moving-kernel acceptance claim.

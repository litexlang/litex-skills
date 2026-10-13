# Part128 — Actual gcd certificate and Diophantine criterion: twenty-seven to eleven

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The number-theory showcase's is_gcd_certificate includes positivity, common
divisibility, greatestness among positive common divisors and a constructive
Bezout witness. Preserve that predicate, both criterion directions and all
integer carriers. A builtin gcd value alone does not replace this interface.
Use Part127's shortened preceding witness proofs.

## Certificate: thirteen proof actions become five

Inside the original theorem for (84,30,6), retain:

```litex
witness $divides_by(6,84) from 14
witness $divides_by(6,30) from 5
claim:
    ? forall common Z:
        common>0
        $divides_by(common,84)
        $divides_by(common,30)
        =>:
            $divides_by(common,6)
    release thm common_divisor_divides_linear_combination(common,84,30,-1,3)
witness exist x,y Z st {6=84*x+30*y} from -1,3
```

Count includes the claim action and its native call. Positive 6>0 is still a
predicate requirement, checked from concrete arithmetic; only its proof echo
is removed. Witness proof bodies, two native-result echoes, the explicit numeric
identity -84+90=6 and final predicate fold are also jointly removable. The
Bézout witness remains necessary in the tested short proof: deleting it rejects.
Wrong coefficients 1,3 reject. No unproved witnesses are supplied.

## Criterion: seven-to-two forward, seven-to-four converse

Forward proof body, under the original certificate and solubility premises:

```litex
obtain x,y from exist x,y Z st {a*x+b*y=c}
release thm common_divisor_divides_linear_combination(d,a,b,x,y)
```

The original two definition unfolds and three result/equation echoes can be
omitted jointly. Converse, under certificate and divides_by(d,c), keeps:

```litex
obtain u,v from exist u,v Z st {d=a*u+b*v}
obtain k from $divides_by(d,c)
c=d*k=(a*u+b*v)*k=a*(u*k)+b*(v*k)
witness $linear_diophantine_soluble(a,b,c) from u*k,v*k
```

The unfold, obtained equality echo and witness body are redundant here.
Deleting the calculation or shortening it to c=d*k=a*(u*k)+b*(v*k) rejects.
Wrong unscaled witness u,v and missing divisibility premise reject.

## Combined acceptance and boundaries

[Full preferred short source](evidence/round-100-cases/certificate-native-only-closure.lit)
uses all three reductions together, twenty-seven actions to eleven, counting
nested witness bodies/claim actions. All original definitions, positivity,
premises and goals remain. The complete standalone source passes through the
later concrete solubility and congruence examples. A native forward-criterion
consumer also passes; false certificate (84,30,5) rejects.

These deletion outcomes are case-specific. Part117's necessary subspace fold
and Part125's necessary linearity fold remain separate verified boundaries.
No general instruction to omit definition actions follows from this case.

## Evidence

[Receipt](evidence/round-100-2026-10-10.summary.json):21 strict files,
14 accepted/7 Normal rejections, all promoted paths rerun with matching exits,
Normal envelopes and null session errors. A malformed missing-premise generator
removed the forward theorem's conclusion instead of the converse premise; its
parse error is recorded separately and excluded. Correct theorem-scoped removal
provides the actual missing-premise control.
Exact source/binary identities recorded; fixed snapshot from successful round88
build reused. Same number-theory family as Part127, not independent general-rule
promotion. No canonical/kernel edits, trust, new bt, performance, global-minimum,
canonical module or moving-kernel acceptance claim.

# Part122 — Actual plane zero and inverse: seventeen steps become eight

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and proof idea

The showcase uses coordinatewise plane_add on cart(R,R). The zero tuple is an
identity; the additive inverse of x is (0-x(1),0-x(2)). Keep the original carrier,
function definition and claim's two conclusions, including the existential
inverse. Use Part121's shortened field/associativity prefix.

## Checked zero route

The original zero proof has ten immediate statements: tuple reconstruction,
zero projections, function expansion, coordinate memberships, scalar zero
calculations, a tuple comparison and the final identity chain. Four suffice:

```litex
x=(x(1),x(2))
(0,0)(1)+x(1)=0+x(1)=x(1)
(0,0)(2)+x(2)=0+x(2)=x(2)
plane_add((0,0),x)=((0,0)(1)+x(1),(0,0)(2)+x(2))=(x(1),x(2))=x
```

Separate zero-coordinate and x-coordinate membership repetitions are removed.
The function expansion and tuple transport are kept as steps inside one final
chain. The shorter attempted chain `plane_add((0,0),x)=(x(1),x(2))=x`
without the two scalar calculations rejects.

## Checked inverse route

The original inverse proof has seven statements: witness value, two coordinate
values, two scalar calculations, result equation and explicit witness. Four
suffice in the same combined context:

```litex
have inverse_x cart(R,R)=(0-x(1),0-x(2))
x(1)+inverse_x(1)=x(1)+(0-x(1))=0
x(2)+inverse_x(2)=x(2)+(0-x(2))=0
witness exist inverse_x2 cart(R,R) st {plane_add(x,inverse_x2)=(0,0)} from inverse_x
```

The inverse coordinate publications and final result equation are redundant
here. Its result equation can first be shortened to the bare endpoint, then
removed entirely: the witness command checks the required equation itself.
Do not infer that the two scalar calculations are redundant; attempted inverse
proofs retaining only value/result/witness, with or without coordinate values,
reject. Deleting the explicit witness rejects in the preferred proof.

[Complete preferred source](evidence/round-94-cases/joint-delete-inverse-result.lit)
combines both reductions, seventeen immediate proof statements to eight. The
same original existential fact is exported. A subsequent ordinary forall
consumer of the zero and inverse conclusions passes. Source continuation through
the following scalar product/sum laws also passes; it is not a direct-dependency
or complete vector-space-instance claim.

## Commutativity and false controls

The original commutativity proof remains:

```litex
plane_add(x,y)=(x(1)+y(1),x(2)+y(2))=(y(1)+x(1),y(2)+x(2))=plane_add(y,x)
```

Direct forall and removing the swapped middle tuple reject. This is a true
identity with unsupported tested routes, not a mathematical negative or kernel
cause diagnosis. The false zero conclusion `plane_add((0,0),x)=(0,0)` and
incorrect generic inverse witness `inverse_x=x` reject separately.

## Evidence

[Receipt](evidence/round-94-2026-10-10.summary.json):20 strict files,
11 accepted/9 Normal rejections. Promoted paths rerun, matching exit/envelope
and null session errors. Source/binary identities recorded, fixed round88
successful build snapshot reused. Original definitions, carriers, statements
and witness value preserved; no new trust, canonical/kernel edits or bt.
Same showcase family, not independent permanent-rule promotion. No performance,
global-minimum, whole-showcase or complete plane-vector-space acceptance claim.

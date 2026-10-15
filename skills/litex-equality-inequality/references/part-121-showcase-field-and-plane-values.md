# Part121 — Actual field adapter and nested plane addition

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The showcase exposes the stored real_field components and operation values,
then verifies coordinatewise addition on cart(R,R). Keep all seven field
adapter conclusions, the same first-class field object, plane_add and plane_smul
functions and exact associativity statement. Use Part120's short field-law
prefix. No canonical mathematics or kernel edits.

## Field adapter: eight proof statements become four

The original body has a full real_field tuple equality, five component facts
and two application chains. The checked short body needs only:

```litex
real_field.add=real_add
real_field.mul=real_mul
real_field.add(x,y)=real_add(x,y)=x+y
real_field.mul(x,y)=real_mul(x,y)=x*y
```

The theorem still concludes zero=0, one=1, add=real_add, neg=real_neg,
mul=real_mul and both operation equations. The tuple equality and zero/one/neg
repetitions can be removed together. Empty body, tuple equality alone, aliases
alone, deleting all five member facts, deleting calculation chains and replacing
the two chains by bare endpoints all reject in tested contexts.
[Field native consumer](evidence/round-93-cases/field-native-consumer.lit)
accepts `release thm real_field_adapter_values(2,3)` and subsequent concrete
addition/multiplication values. A false zero=one adapter conclusion rejects.

## Plane associativity: omit input tuple values, retain seven statements

Original input tuple values are redundant:

```litex
plane_add(x,y)=(x(1)+y(1),x(2)+y(2))
plane_add(y,z)=(y(1)+z(1),y(2)+z(2))
```

Their four scalar coordinate facts remain, along with both outer result
expansions and the final comparison chain. This shortens nine immediate proof
statements to seven. Direct forall, deleting the four coordinate facts, keeping
outer expansions alone, keeping coordinates plus final chain only, and deleting
the final chain all reject in tested contexts. Do not teach universal redundancy
of the outer expansions from these source-specific input-value deletions.

[Combined complete preferred source](evidence/round-93-cases/joint-preferred.lit)
uses both shortened field adapter and plane proof. Source continuation through
the following commutativity claim also passes, with no direct-dependency or
whole-module claim. The false associativity endpoint equals x rejects.

## Native tuple route: exact observed boundary

Calling the native tuple theorem alone, after input tuple values, after input
coordinate facts, or after all original expansions instead of the final chain
rejects for this nested symbolic function expression. The native theorem is
found, with well-defined coordinate applications, but its premise fails:

```litex
forall i closed_range(1,2):
    plane_add(plane_add(x,y),z)(i)=plane_add(x,plane_add(y,z))(i)
```

The observed phase is release_thm premise index0 / forall search_proof. This is
not a syntax/domain error, mathematical negative, or diagnosis of its internal
cause. Part99's literal tuple route remains separate. A future improvement
should inspect this exact universal coordinate premise and its available proof
interfaces; these observations do not authorize global search or a new bt rule.

## Evidence

[Receipt](evidence/round-93-2026-10-10.summary.json):25 strict files,
8 accepted/17 Normal rejections; all promoted paths rerun, with matching exits
and null session errors. All rejected controls include true-but-unsupported
routes or false statements as labeled above; the count does not mean seventeen
mathematical counterexamples. Fixed round88 build snapshot reused with exact
source/binary identity. Same showcase family, not independent general-rule
promotion. No trusts, source/kernel edits, performance/global-minimum claims,
complete showcase or later vector-space construction acceptance.

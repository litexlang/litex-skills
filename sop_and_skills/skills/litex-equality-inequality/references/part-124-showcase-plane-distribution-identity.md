# Part124 — Actual plane distribution and scalar identity: reach the instance

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The [linear-algebra showcase](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/showcases/math_concepts_in_litex/5_linear_algebra/main.lit)
proves scalar multiplication distributes over vector addition and that the scalar
field's identity fixes every vector, then constructs real_plane. Keep the original
cart(R,R) carrier, real_field, plane_add/plane_smul and exact conclusions. Use
Part123's shortened preceding source; no canonical source edits.

## Distribution: sixteen proof statements become nine

Publish six scalar coordinates: two for plane_add(x,y), two for plane_smul(a,x)
and two for plane_smul(a,y). Keep the left result expansion, fold the right result
expansion and tuple transport into one chain, then compare the two expanded sides.

The merged right expansion is:

```litex
plane_add(plane_smul(a,x),plane_smul(a,y))=(plane_smul(a,x)(1)+plane_smul(a,y)(1),plane_smul(a,x)(2)+plane_smul(a,y)(2))=(a*x(1)+a*y(1),a*x(2)+a*y(2))
```

The three separate input tuple values, two coordinate sum facts, separate tuple
transport and repeated right endpoint are omitted in this combined route.
[Complete preferred source](evidence/round-96-cases/identity-one-value-bridge.lit)
keeps all six coordinate statements and both mathematical expansions. Deleting
all six coordinates rejects; individual necessity of each is not asserted.
Direct ordinary forall also rejects in the original context.

## Identity: five proof statements become two

The original proof uses a full real_field_adapter_values call, tuple reconstruction,
argument rewrite, function expansion and final endpoint chain. It can instead use
one field value and one chain:

```litex
real_field.one=1
plane_smul(real_field.one,x)=plane_smul(1,x)=(1*x(1),1*x(2))=(x(1),x(2))=x
```

The explicit x=(x(1),x(2)) statement is unnecessary in the combined route.
The original full adapter call remains a passing alternative. The chain alone
rejects, so retain the tested field-value bridge; do not infer it can be dropped
merely because the stored field is concrete.

## Combined consumer and false controls

Both reductions jointly pass: twenty-one immediate proof statements become eleven.
The original struct_member invocation and real_plane construction pass after them.
The constructed object can consume the existing abstract vector-space theorem:

```litex
real_plane.zero=(0,0)
real_plane.smul=plane_smul
release thm scalar_times_zero_vector(R,real_field,cart(R,R),real_plane,2)
plane_smul(2,(0,0))=(0,0)
```

This [native consumer](evidence/round-96-cases/preferred-plane-native-consumer.lit)
checks the actual instance interface. It does not establish that the native call
is uniquely necessary to compute the numeric endpoint. False distribution to
plane_smul(a,x) and false identity to (0,0) reject separately.

## Evidence and generation boundary

[Receipt](evidence/round-96-2026-10-10.summary.json):15 strict files,
9 accepted/6 Normal rejections, promoted paths rerun with matching exits/envelopes
and null session errors. One initial short-proof generator retained a trailing
top-level comment before appended indented statements, causing unexpected-indent
parse error. Its coordinate filter also included scalar sum facts. The corrected
signature stops before the first proof statement, and the coordinate filter
selects a single function call on the left. The malformed fixture is separately
recorded and excluded from semantic counts.

Exact source/binary identities recorded; fixed snapshot from successful round88
build reused. Cold files own deletion evidence. The real_plane instance and scoped
native consumer pass; the later projection theorem and complete showcase are not
yet claimed. Same source family, not independent permanent-rule promotion. No
canonical/kernel edits, trust, new bt, performance or global-minimum claim.

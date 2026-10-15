# Part126 — Actual projection kernel/noninjectivity: keep scalar contradiction

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

Projection (x,y)->(x,0) has (0,7) in its kernel and is not injective: (0,1) and
(0,0) have equal images. Preserve the exact projection function, real_plane,
carriers, kernel template and theorem goal. Use Part125's shortened full prefix.

## Kernel fragment: ten statements become seven

These three publications are jointly removable:

```litex
(0,7)(1)=0
projection_x_axis((0,7))=(0,0)=real_plane.zero
(0,7) $in {v cart(R,R):projection_x_axis(v)=real_plane.zero}
```

Keep the projected-value expansion chain, real_plane.zero=(0,0), native
set_builder_member and kernel-to-set-builder equality before final membership.
All three original native theorem calls stay. The fragment count includes calls;
retaining these statements does not establish individual necessity of each.

## Noninjectivity: thirteen actions become five

The original by-contra block can retain only:

```litex
projection_x_axis((0,1))=((0,1)(1),0)=(0,0)
projection_x_axis((0,0))=((0,0)(1),0)=(0,0)
(0,1)=(0,0)
1=(0,1)(2)=(0,0)(2)=0
impossible 1!=0
```

These lines are inside the original `by contra` for the negative injectivity
goal; the tuple equality follows under its injectivity assumption. Omit the
injectivity echo/unfolding, two first-coordinate facts, two projected-value
echoes, image equality and separate second-coordinate equality. All deletions
pass jointly with the kernel fragment cleanup.
[Complete preferred short file](evidence/round-98-cases/contra-delete-coordinate-equality.lit).

## Boundaries and false controls

- `impossible (0,1)!=(0,0)` instead of the scalar contradiction rejects.
  Its positive inequality fails search_proof at closing/impossible; syntax and
  WD succeed. No clean-context tuple-inequality diagnosis is established.
- Only `impossible 1!=0` after the tuple equality also rejects. Removing the
  tuple equality or replacing the three projection-value chains by bare
  endpoints rejects. These are incomplete tested routes for true mathematics.
- The false kernel member (1,7) and positive injectivity after the shortened
  source reject. No usable escaped contra injectivity assumption is observed.

[Native consumer](evidence/round-98-cases/preferred-native-noninjective-consumer.lit)
releases the noninjectivity theorem and consumes its negative conclusion.
The complete shortened standalone showcase passes from beginning to end.

## Evidence

[Receipt](evidence/round-98-2026-10-10.summary.json):18 strict files,
12 accepted/6 Normal rejections, all promoted paths rerun with matching exit,
Normal envelope and null session error. Exact math source/binary identities
recorded; fixed snapshot from successful round88 build reused. The prefix's
proof/interface variants remain documented in preceding Parts; no canonical
module, incidental export parity or moving-kernel-wide acceptance claim.
Same source family, not independent general-rule promotion. No canonical/kernel
edits, trust, new bt, performance or global-minimum claim.

# Part131 — Positive expression to nonzero: one explicit sign bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and actual source

*The Mechanics of Litex Proof* chapter 2 §2.2 proves two simple nonzero
facts: `3*x=2 ⇒ x!=1` over Q and `y^2+1!=0` over R. Its third example
`a<=b, b<=a ⇒ a=b` is already a direct forall fact. The exact three proof
statements, with explanatory comments omitted, pass in source order.

## Concise source forms

For the first claim, the original calculation, `x<1` echo and nested
contradiction reduce to the calculation alone:

```litex
claim:
    ? forall x Q:
        3*x=2
        =>:
            x!=1
    x=(3*x)/3=2/3<3/3=1
```

For the second, the `0<=y^2` echo and nested contradiction are removable:

```litex
claim:
    ? forall y R:
        y^2+1!=0
    0<y^2+1
```

Both short claims pass together with the direct two-sided inequality example.
[Combined short source](evidence/round-104-cases/both-short.lit).
The source deliberately teaches explicit proof structure; these are shorter
usable alternatives, not a request to replace its pedagogical presentation.

## Exact small search boundary

Independent cold files establish:

```litex
forall y R:
    0<y^2+1
```

passes, but the equally true direct query

```litex
forall y R:
    y^2+1!=0
```

rejects at `search_proof`. Publishing the sign immediately before nonzero
passes. Likewise, under `a>=0,b>0`, `a+b>0` passes, but the direct
`a+b!=0` rejects; the sign-then-nonzero pair passes. Generic direct
`x<y ⇒ x!=y` and `y>0 ⇒ y!=0` both pass. Thus the final strict-sign to
nonzero step already works when the sign fact is present. The observed gap is
finding that intermediate sign during these direct nonzero searches; this is
an inference from the checked surface behavior, not an internal diagnosis.

In the first claim, the original mixed equality/order calculation remains:
bodyless `x!=1` and direct `3*x=2 ⇒ x<1` reject; the one-chain version passes.
Wrong endpoints (`x=1`, `y^2+1=0`) and deletion of `3*x=2` reject.
No selected bt or kernel change follows automatically from these probes.

## Evidence and scope

[Receipt](evidence/round-104-2026-10-10.summary.json):20 promoted strict files,
12 accepted/8 Normal rejections; promoted reruns match exits, success flags,
Normal envelopes and null Session errors. It records exact source/binary hashes;
the successful round88 fixed snapshot was reused. Source §2.2 statements
were isolated without earlier chapter context; no whole-chapter or moving-kernel
acceptance, performance claim, canonical edit, new trust or bt implementation.

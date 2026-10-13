# Part118 — Actual injective linear map: retain the membership bridges

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

In the linear-algebra showcase, an injective linear map T has kernel equal to
{source.zero}. Preserve both vector spaces, the field, linearity, injectivity,
the native kernel/zero-subspace templates and the exact theorem conclusion.
This case uses round88's shortened preceding source; no canonical source edits.

## Proof idea and checked short route

For x in the kernel, T(x)=T(0), so injectivity gives x=0. Conversely,
x in {0} gives x=0 and then T(x)=T(0)=0. Set extension checks these directions.
The following excerpts remain inside the original two membership claims:

```litex
# Forward: x kernel; goal x in zero_space
T(x)=target.zero=T(source.zero)
x=source.zero
# Reverse: x zero_space; goal x in kernel
x $in {source.zero}
x=source.zero
T(x)=T(source.zero)=target.zero
```

[Complete preferred source](evidence/round-89-cases/preferred-short.lit)
retains the native zero-image theorem call, both canonical template equalities
and the set-extension action. This is a verified short route, not a global
minimum or a claim about automatic discovery in arbitrary contexts.

## Verbose comparison and joint deletion

The source additionally repeats the zero-image theorem result, unfolds the
injectivity definition explicitly, publishes both alias-to-set equalities,
and repeats the final membership target of each direction claim. It also
publishes `x $in {source.zero}` in the forward direction. These seven proof
actions can be removed together in the exact preserved context.

The original forward calculation was:

```litex
T(x)=target.zero=T(source.zero)
x=source.zero
x $in {source.zero}
x $in zero_space
```

The first two lines suffice there. The reverse singleton membership does not
share the same deletion result: removing only that reverse fact rejects.
An initial deletion removed identical singleton lines in both directions;
its rejection does not locate either line separately. Direction-specific
probes establish the distinction.

## Negative and deletion boundaries

- Removing the explicit `x=source.zero` lines rejects; do not replace the
  short route with only the image equality chain on this evidence.
- Removing the reverse singleton membership rejects. This is a true goal
  with an incomplete tested proof, distinct from a mathematical negative.
- Removing the injectivity premise rejects, including in the preferred route
  after explicit definition unfolding was already removed. Linearity alone
  does not imply a trivial kernel.
- Changing the conclusion to kernel inequality rejects.

[Native consumer](evidence/round-89-cases/preferred-native-consumer.lit) calls
the shortened theorem under its original premises and passes. The source
prefix through the following `trivial_kernel_implies_injective` theorem also
passes; this latter gate checks continuation, not a direct dependency.

## Evidence and scope

[Receipt](evidence/round-89-2026-10-10.summary.json):20 independent strict files,
11 accepted/9 Normal rejections with matching exit codes and null session
errors. All promoted paths rerun. Exact source/binary identity recorded;
round89 reuses the fixed snapshot from the successful round88 build rather
than claiming a new build. Old warm universal declarations do not own deletion
evidence. Same linear-algebra source family as Parts116–117; no independent
permanent-rule promotion, complete-module, performance or new bt claim.

# Part 4 — Transfer an absolute-value neighborhood bound

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Given abs(x-L)<=r for real x,L,r, triangle inequality gives
abs(x)<=abs(L)+r. The same premise gives x<=L+r. No independently supplied
r>=0 premise is necessary: the existing bound already forces it.
Anchors: Analysis Chapter 9 product-limit magnitude bound at lines 3831–3846;
Chapter 6 product-limit proof around line 852 gives a separate strict instance.
The following are reduced self-contained scalar probes, not full chapter gates.

## Positive

```litex
claim:
    ? forall x,L,r R:
        abs(x-L) <= r
        =>:
            abs(x) <= abs(L)+r
    abs(x) = abs((x-L)+L) <= abs(x-L)+abs(L) <= r+abs(L) = abs(L)+r
```

For the upper endpoint:
```litex
claim:
    ? forall x,L,r R:
        abs(x-L) <= r
        =>:
            x <= L+r
    x = (x-L)+L <= abs(x-L)+L <= r+L = L+r
```

## Verbose comparison

Chapter 9 builds positive/negative bounds separately. Representative original
**excerpt**, with its enclosing context retained in the original chapter:
```litex
f(y) - L <= abs(f(y) - L)
f(y) - L <= 1
f(y) = (f(y) - L) + L
L <= abs(L)
(f(y) - L) + L <= 1 + abs(L)
f(y) <= 1 + abs(L)
```
It then performs the negative analogue before bounding abs(f(y)). The checked
scalar chain replaces that mathematical pattern; removal of the actual chapter
block and its consumers is not yet verified.

## Ideal direct forms and negatives

Both following conclusions miss in fresh files with the sole premise
abs(x-L)<=r:
```litex
abs(x) <= abs(L)+r
x <= L+r
```
These are excerpts of the self-contained direct probes in the receipt.
The nearest false shortcut, abs(x)<=r, also rejects; x=L=10,r=1 refutes it.

## Builtin candidate

For target abs(x)<=abs(L)+r, generate the single neighborhood premise
abs(x-L)<=r under real WD. A shifted-endpoint sibling can use that same premise
for x<=L+r. The goal supplies L and r; no arbitrary center search is needed.
Support symmetry and addend orientation only through explicit bounded matching.
Strict variants and negative endpoint orientations have not been tested here.

## Evidence

[Round 2 receipt](evidence/round-02-2026-10-08.summary.json), `abs-neighborhood-direct`,
`abs-neighborhood-chain`, `abs-neighborhood-upper-direct`,
`abs-neighborhood-upper-chain`, `abs-neighborhood-false`.
Current-source release build succeeded on 2026-10-08; hash, commands, complete
sources and Normal JSON retained. No canonical proof or kernel changes.

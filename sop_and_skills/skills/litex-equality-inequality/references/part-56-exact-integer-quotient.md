# Part 56 — Integer carrier of an exact quotient

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Later implementation acceptance (2026-10-09)

The user-selected `ExactIntegerQuotient` rule has completed scoped implementation acceptance:

```litex
forall a,b Z:
    b!=0
    a%b=0
    =>:
        a/b $in Z
```

This explicit zero-remainder form is implemented, including checked positive and negative divisor cases. Related witness-only, factorial, triangular and alternate nonzero-domain probes retain their own dates; no broader direct capability is asserted.
See [selected-rule acceptance](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/tests/unit/execute/selected_scalar_bt_rules/acceptance.md) and its paired machine receipt for
actual working-tree strict example and guard/negative tests. Prefer the direct
form in this accepted scope; do not duplicate it as a new kernel candidate.
The sections below retain the earlier pilot's binary/date and describe its
former behavior, not a permanent current proof-step requirement. Current
round36 build failure does not undo that dated acceptance or establish a new
source gate. No full-corpus, Lean adapter or runtime claim is added.

## Mathematical situation and source

For integer a and nonzero integer b, a%b=0 implies a/b is an integer. A known integer-multiple witness a=b*q gives the same conclusion. Ordinary division is not integer truncation; native quot(a,b) has a stricter positive-divisor interface. Source anchors: Concrete Mathematics chapter02 triangular-coefficient carrier comment and chapter04 Euclidean quotient/divisor witnesses.

## Ideal direct forms: historical misses

```litex
forall a Z,b Z*:
    a%b = 0
    =>:
        a/b $in Z
```
```litex
forall a,q Z,b Z*:
    a = b*q
    =>:
        a/b $in Z
```

Restricting the divisor to N+ does not make the zero-remainder type target direct. Pure cancellation (a*b)/b $in Z also misses, and supplying factorial divisibility does not automatically type its exact ratio.

## Positive: existing equality and type transport

With the explicit witness only one equality is needed:

```litex
claim:
    ? forall a,q Z,b Z*:
        a = b*q
        =>:
            a/b $in Z
    a/b = q
```

The equality a/b=q itself already passes directly from a=b*q. Its subsequent integer carrier therefore succeeds; do not claim general equality transport or all integer typing is absent.

For a positive divisor, two equations suffice without echoing the final type or native quotient codomain:

```litex
claim:
    ? forall a Z,b N+:
        a%b = 0
        =>:
            a/b $in Z
    a = b*quot(a,b)+a%b = b*quot(a,b)
    a/b = quot(a,b)
```

Native Euclidean decomposition and quot(a,b) $in Z already pass directly for b N+. The stronger signed-divisor zero-remainder direct target was tested and misses, but this two-equation proof is only for positive b. Do not claim a general signed repair from that narrowed interface.

## Independent consumers

A self-contained checked exact-quotient theorem plus native factorial divisibility proves factorial(n)/factorial(m) $in Z when m<=n. The direct ratio and remainder-only bridge miss. The triangular integer and natural consumer interfaces also pass using the same theorem after parity is established; see Part 57. These are checked mathematical interfaces, not new assumptions.

## Negatives and semantics

Integer operands alone do not imply integer division: 1/2 is a counterexample and executable universal rejects. b=0 remains invalid. Native quot at a negative divisor rejects under its current declared domain; that is not evidence that ordinary signed exact division is false. Closed 6/(-2), (-6)/2 and 0/2 carrier checks pass; not 1/2 $in Z passes.

## Historical candidates and distinct witness-only nomination

- Conditional exact-division carrier rule: checked integer operands, b!=0 and a%b=0, with an exact integer quotient certificate. Signed b must use correct native remainder semantics; do not call positive-only quot(a,b) at negative b. General negative-divisor implementation acceptance needs a separately checked route.
- Known integer-multiple carrier rule: consume a=b*q with q in Z and nonzero b, preserve the known multiplication/equality certificate, and produce a/b in Z. This queries already provided witnesses rather than searching for arbitrary q.
- Reuse bounded guarded cancellation to a known integer representative where available; do not enable unrestricted algebra discovery in all type checks or relabel a rational quotient as an integer.

The complete type-consumer cause is unresolved. No shared AST/Runtime redesign or proof-policy change is implied.

## Evidence and limits

Dated 2026-10-09. Fresh current-worktree release build succeeded; an immutable binary snapshot was used throughout. [Round 19 receipt](evidence/round-19-2026-10-09.summary.json) retains exact sources, commands, exits, Normal JSON, binary identity, synchronized Session responses and durable replay commands. Runnable sources are in `evidence/round-19-cases/`.

No trust, kernel/canonical mathematical source changes, whole-textbook gate or performance claims. These are source-adjacent scoped observations and rule nominations; source comments are not independent verifier evidence.

# Part 70 — Standard-set aliases and sign/bound consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

Membership in a set equal to a standard numeric carrier or interval gives
the same mathematical information as literal membership. Independent strict
files show that current consumption depends on the target family, not just
on the order of the equality and member premises.

## Positive and shortest checked routes

Both premise orders pass for this positive-real comparison:

```litex
forall S set,x R:
    x $in S
    S=R+
    =>:
        x>0
```

Replacing the target by `x!=0` misses. One meaningful sign bridge repairs it:

```litex
claim:
    ? forall S set,x R:
        x $in S
        S=R+
        =>:
            x!=0
    x>0
```

Literal `forall x R+: x!=0` already passes. Do not infer that the alias
supports every signed-carrier consequence merely because `x>0` passes.

For closed intervals, one literal membership bridge passes:

```litex
claim:
    ? forall S set,a,b,x R:
        x $in S
        S='[a,b]
        =>:
            a<=x<=b
    x $in '[a,b]
```

The direct target misses with either premise order and with `x S` typing.
Replaying only `x in S` does not repair it. The literal interval carrier
already provides both bounds. Negative-real and natural-number aliases
likewise miss their direct sign goals, while one literal member bridge works.
These are dated diagnostic bridges, not permanent authoring requirements.

## Verbose comparison and negatives

Once literal interval membership has been established, separately echoing
`a<=x`, `x<=b` and the target chain is unnecessary in this tested context.
Closed membership does not imply strict lower bounds: `0 in '[0,1]` passes,
whereas the generic alias-to-`a<x` target rejects. Positive membership cannot
imply a negative sign, and natural membership cannot imply strict positivity.
Missing membership rejects. `not 0 in R+` passes.

Reversed endpoints are valid empty intervals in the Manual. Concrete
`not 1 in '[2,1]` passes, but `'[2,1]={}` misses in this snapshot. This is a
true unsupported equality, not an invalid-domain control.

## Bounded improvement candidate

Investigate consumption of checked equality-transported membership by sign,
nonzero and interval-bound leaves. Retain the numeric domain, exact endpoint
brackets, actual equality/member citations, and inherited search permissions.
Do not duplicate the already working positive comparison or broaden inference
globally. The inspected signed-standard-set inference owner matches a literal
`Obj::StandardSet`; this is an owner clue, not a complete causal diagnosis.
No kernel, AST or Env/Runtime change is made or authorized by this card.

## Evidence

[Round 29 receipt](evidence/round-29-2026-10-09.summary.json): 30 unique cold strict
files, 17 accepted and 13 rejected, including true misses and false controls.
Every promoted file was rerun with the recorded immutable release snapshot.
Warm Session accepted interval alias variants that fail cold; only cold files
support capability claims. A malformed author `claim` and a non-PTY EOF restart
are excluded; accepted source was replayed into live Session 25852.
Source anchors are the Manual's signed carriers and real interval entries.
No whole-corpus, complete causal repair or performance claim.

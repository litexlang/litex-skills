# Part 63 — Pointwise beta, entry aliases and function extensionality

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and proof spine

Chapter 1A of linear_algebra_done_right defines coordinate operations by
pointwise callbacks. Evaluate one legal coordinate using the callback's
definition. For equality of complete functions, prove the common-domain
pointwise equation with `by fn_extension`. Keep this separate from opaque
anonymous-call arithmetic and from source template/struct-field unfolding.

## Positive: an entry alias needs no waterfall

```litex
forall n N+,u,v,result finite_seq(R,n),idx closed_range(1,n):
    result=fn(k closed_range(1,n)) R {u(k)+v(k)}
    =>:
        result(idx)=u(idx)+v(idx)
```

This direct fact passes. Scalar multiplication has the same checked entry
shape. The operation need not be builtin real addition:

```litex
forall carrier nonempty_set,n N+,combine fn(left,right carrier) carrier,u,v,result finite_seq(carrier,n),idx closed_range(1,n):
    result=fn(k closed_range(1,n)) carrier {combine(u(k),v(k))}
    =>:
        result(idx)=combine(u(idx),v(idx))
```

This also passes. The complete original ScalarSystem/template entry theorem
was not tested, so these facts do not establish that its definition bridges
can all be deleted. They establish a smaller supplied-callback interface.

## Positive: meaningful full-function proof

```litex
claim:
    ? forall u,v fn(t R) R:
        fn(k R) R {u(k)+v(k)}=fn(j R) R {v(j)+u(j)}
    by fn_extension:
        ? fn(k R) R {u(k)+v(k)}=fn(j R) R {v(j)+u(j)}
        forall eval_index R:
            fn(k R) R {u(k)+v(k)}(eval_index)=u(eval_index)+v(eval_index)=v(eval_index)+u(eval_index)=fn(j R) R {v(j)+u(j)}(eval_index)
```

The proof passes; the bare function equality misses. Scalar association checks
with the same route. No source-function-name shortcut is proposed.

## Arithmetic boundary and negatives

The direct scaled target
`fn(k R)R{u(k)+v(k)}(x)*a=(u(x)+v(x))*a` still misses, including when the
unscaled beta equation is supplied. A checked scalar congruence call repairs
it. This is held-out evidence for Part 62's consumer/atom investigation, not
proof that one proposed key change repairs every consumer.

Zero outside closed_range(1,n), a claimed sequence length n+1, changed
coefficient or captured function, and equality of positive-only and full-R
function domains reject. A positive-domain call at x>0 passes. Do not weaken
callback domains or merge free captures to shorten a proof.

## Evidence and source limits

[Round 23 receipt](evidence/round-23-2026-10-09.summary.json) retains complete sources,
independent strict file results, source hashes, immutable binary identities
and Session adoption/replay. Current-source release builds succeeded; source
changes across the verification window are explicitly recorded. No canonical
chapter edit, generic ScalarSystem coverage, global minimum or speed claim.

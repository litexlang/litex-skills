# Part120 — Actual real field: direct laws and one reciprocal value bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The showcase builds Field<R> from real addition, negation, multiplication and a
case-defined reciprocal. Its zero branch is real_inv(0)=0; the multiplicative
inverse law applies only when x!=0. Preserve that total function and guard.
Associativity, distributivity, commutativity and identity laws follow from the
ordinary real operations. No alternate field or stronger premises are used.

## Checked short form

The inverse claim needs only its reciprocal value bridge:

```litex
claim:
    ? forall x R:
        x!=0
        =>:
            real_mul(x,real_inv(x))=1
    real_inv(x)=1/x
```

The original body also published a full multiplication chain:

```litex
real_inv(x)=1/x
real_mul(x,real_inv(x))=x*real_inv(x)=x*(1/x)=1
```

The second statement is removable in the checked combined context. Conversely,
deleting the first while keeping the original chain rejects.

For the other three law blocks use direct ordinary forall facts with the same
binders and conclusions. For example:

```litex
forall x,y,z R:
    real_add(real_add(x,y),z)=real_add(x,real_add(y,z))
    real_mul(real_mul(x,y),z)=real_mul(x,real_mul(y,z))
    real_mul(x,real_add(y,z))=real_add(real_mul(x,y),real_mul(x,z))
```

[Complete preferred source](evidence/round-92-cases/inverse-value-only.lit)
includes commutativity and identity laws in the same direct form and the original
native struct_member call, Field<R> membership and real_field construction.
The four source claims originally contained eighteen immediate proof statements;
this route retains one. Mathematical law declarations still remain and are not
counted as removable proof statements. No speed/global-minimum claim.

## Distinguish interfaces and boundaries

The tested zero-body claim fixture produces a parse_error despite retaining the
printed goal. It is excluded from verifier negative counts. The working direct
forall form is an equivalent mathematical fact with a different statement
interface, not evidence that an empty claim body is supported.

The nonzero inverse fact as a direct forall still rejects. All four laws as direct
forall facts therefore reject at that inverse obligation; this does not negate
the independently passing algebra/commutativity/identity conversions. Combining
them with the one-value inverse claim passes through the original field instance.

Removing x!=0 rejects in that preferred route. The false inverse law equals-zero,
false add-associativity conclusion and field tuple with equal zero/one all reject.
The unchanged zero branch real_inv(0)=0 passes after field construction.
These negative controls differ from true-but-unsupported inverse direct form.

## Evidence

[Receipt](evidence/round-92-2026-10-10.summary.json):16 strict files,
8 accepted/8 Normal rejections; promoted paths rerun with matching exit codes,
Normal envelopes and null session errors. One separately recorded parse observation
is excluded from these counts. Exact actual source and binary hashes recorded;
fixed snapshot from successful round88 build reused. Cold files own deletion and
interface evidence. The field instance is checked, not the whole showcase or later
plane-vector instances. Same linear-algebra source family; no permanent rule,
canonical/kernel edit, new bt or trust.

# Part 116 — Vector-space uniqueness: a directed chain and an exact export

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Round86 continuation: linear maps preserve zero and negatives

Keep the source's is_linear_map predicate and distinct source/target vector
spaces over the same field. The zero-image proof becomes three statements:

```litex
source.add(source.zero,source.zero)=source.zero
target.add(T(source.zero),T(source.zero))=T(source.add(source.zero,source.zero))=T(source.zero)=target.add(target.zero,T(source.zero))=target.add(T(source.zero),target.zero)
release thm add_left_cancel(K,field,W,target,T(source.zero),T(source.zero),target.zero)
```

This is an excerpt under the original linear-map hypothesis. Seven source
body statements become three; the final result echo is unnecessary. Removing
the concrete source zero-addition fact still fails in the nested T argument.

The negative-image proof uses the canonical source function spelling instead
of its local source_neg alias, then combines the product calculation:

```litex
release thm vector_neg_spec(K,field,V,source,x)
release thm vector_neg_spec(K,field,W,target,T(x))
release thm linear_map_sends_zero_to_zero(K,field,V,W,source,target,T)
target.add(T(x),T(\vector_neg<K,field,V,source>(x)))=T(source.add(x,\vector_neg<K,field,V,source>(x)))=T(source.zero)=target.zero=target.add(T(x),\vector_neg<K,field,W,target>(T(x)))
release thm add_left_cancel(K,field,W,target,T(x),T(\vector_neg<K,field,V,source>(x)),\vector_neg<K,field,W,target>(T(x)))
```

[Full preferred source with exact binders and interfaces](evidence/round-86-cases/negative-five-step-chain.lit).
The original fifteen statements become five. Native calls store the exact
specifications and cancellation result. In the alias-retaining alternative,
source.add(x,source_neg(x))=source.zero remains necessary, while target-inverse,
zero-image and final-cancellation echoes can be removed. Do not silently change
an argument to an alias and assume the same consumer behavior. This checked
canonical spelling is a source-level choice, not an alias or kernel repair.

Original and shortened source through linear_map_kernel_is_subspace both pass.
[Actual downstream consumer](evidence/round-86-cases/short-through-kernel-subspace.lit).
Wrong nonzero-image/negative-image inequality and missing linear premise
controls reject. Later injectivity and concrete-space APIs remain outside scope.

[Round86 receipt](evidence/round-86-2026-10-10.summary.json):19 strict files,
13 accepted/6 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary identities
retained. Session66922 on round68 accepted the exact linear predicate and both
short image theorems; its final pending response was consumed through success
and prompt. Current cold files own deletion and kernel-consumer evidence.
Same source family, no new Part, canonical/kernel/trust/interface change,
performance, global-minimum or excluded scalar-cancellation bt claim.

## Round85 continuation: five-step zero-multiplication laws

Keep the source's distinct scalar zero field.zero in K and vector zero
space.zero in V. Distributivity gives p=p+p; left cancellation then gives
p=space.zero. Under the original zero_scalar_times_vector binder, retain:

```litex
have p V=space.smul(field.zero,x)
field.add(field.zero,field.zero)=field.zero
p=space.smul(field.zero,x)=space.smul(field.add(field.zero,field.zero),x)=space.add(space.smul(field.zero,x),space.smul(field.zero,x))=space.add(p,p)
space.add(p,p)=p=space.add(space.zero,p)=space.add(p,space.zero)
release thm add_left_cancel(K,field,V,space,p,p,space.zero)
```

The companion scalar_times_zero_vector proof uses q=space.smul(a,space.zero),
the concrete law space.add(space.zero,space.zero)=space.zero, and analogous
distribution/cancellation chains. Both five-step bodies pass together.
[Complete preferred source](evidence/round-85-cases/combined-five-step-laws.lit).
The original bodies have ten and nine statements respectively; their final
p=space.zero/q=space.zero echoes are unnecessary after the native call.
Intermediate distribution/value equalities are checked inside the full chains.

Deleting the concrete scalar-zero addition law from the first chain fails;
deleting the concrete vector-zero addition law from the second also fails.
These bridges guide nested scalar-action arguments and cannot simply be
discarded. Empty zero-scalar proof and wrong nonzero-vector conclusions reject.
No positivity, characteristic or real-coordinate restriction is introduced.

[Round85 receipt](evidence/round-85-2026-10-10.summary.json):10 strict files,
5 accepted/5 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Source/binary identities retained.
Session66922 on round68 accepted the existing scalar-carrier helper and both
short zero-law theorems; current cold files own deletion and negative evidence.
Same source family, no canonical/kernel/trust/interface edit, new bt, timing
or global-minimum claim. Later linear-map consumers are outside this gate.

## Round84 continuation: unique negative-vector interface and left cancellation

The source defines vector_neg by exist! from additive_inverse_exists_unique,
then states vector_neg_spec without a proof body. That exact prefix passes.
Retain this reusable interface rather than constructing a new inverse witness
inside each cancellation proof.

Under the original premise space.add(x,y)=space.add(x,z), left cancellation
can keep these four body statements:

```litex
let neg=\vector_neg<K,field,V,space>
release thm vector_neg_spec(K,field,V,space,x)
space.add(neg(x),x)=space.add(x,neg(x))=space.zero
y=space.add(space.zero,y)=space.add(space.add(neg(x),x),y)=space.add(neg(x),space.add(x,y))=space.add(neg(x),space.add(x,z))=space.add(space.add(neg(x),x),z)=space.add(space.zero,z)=z
```

[Complete preferred source](evidence/round-84-cases/chain-delete-spec-echo.lit)
owns exact generic binders, structs, unique function and preceding theorems;
the code above is a proof-body excerpt. The original nine statements include
the result echo after vector_neg_spec and four separate associativity/value
calculations. The full directed chain incorporates those calculations, and
the call's right-inverse result needs no echo. The separate left-inverse chain
still matters: deleting it from this route fails. Empty cancellation and wrong
y!=z/missing common-product premise controls also reject.

Both original and shortened source through zero_scalar_times_vector and
scalar_times_zero_vector pass. These actual downstream theorems retain their
interfaces, hypotheses and cancellation calls.
[Short source through zero consumers](evidence/round-84-cases/short-through-zero-consumers.lit).
No later linear-map or concrete-vector instance acceptance is inferred.

[Round84 receipt](evidence/round-84-2026-10-10.summary.json):10 strict files,
6 accepted/4 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary identities
and literal journal retained. Session66922 stays on round68 with the earlier
short uniqueness interface; it accepted vector_neg, its specification and the
short cancellation theorem. Current cold files own deletion and downstream
evidence. Same source family, no new Part, canonical/kernel/trust/struct edit,
timing or global-minimum claim. The excluded scalar-cancellation bt is not
implemented by this authoring audit.

## Actual source and retained mathematical interface

The linear-algebra showcase defines Field and VectorSpace structs and proves
uniqueness of additive identities and inverses. Preserve these exact existing
struct declarations, fields, laws, generic carriers and theorem assumptions.
This isolated source slice does not audit later vector_neg, linear-map or
concrete-coordinate instances. No structure redesign or scalar replacement
is introduced.

## Identity uniqueness: guide one chain to the actual endpoint

Under the original left-identity premise, the two source proof facts become:

```litex
identity_candidate=space.add(space.zero,identity_candidate)=space.add(identity_candidate,space.zero)=space.zero
```

[Full short source](evidence/round-83-cases/combined-short-route.lit).
The chain uses stored-zero identity, commutativity and the candidate's identity
law. Simply deleting the first source fact from its old chain fails: that
remaining chain returns to identity_candidate without explicitly visiting the
candidate law's zero endpoint. The directed replacement is a different,
checked mathematical route, not evidence that any truncated chain suffices.
An empty identity theorem and the wrong conclusion identity_candidate!=space.zero
both reject.

## Inverse uniqueness: export the equation, keep intermediate facts local

The source obtains y from the vector-space inverse-existence law. Its ordinary
forall y1,y2 statement declares two intermediate calculations and y1=y2 as
three conclusions. The later exist! witness consumes the equality conclusion.
Deleting that last conclusion fails: it changes the exported interface and
must not be described as removing an ordinary proof-body echo.

Replace that universal declaration by this local proof, retaining the exact
two inverse-candidate premises:

```litex
claim:
    ? forall y1,y2 V:
        space.add(x,y1)=space.zero
        space.add(x,y2)=space.zero
        =>:
            y1=y2
    space.add(y2,x)=space.add(x,y2)=space.zero
    y1=space.add(space.zero,y1)=space.add(space.add(y2,x),y1)=space.add(y2,space.add(x,y1))=space.add(y2,space.zero)=space.add(space.zero,y2)=y2
```

The source's `witness exist! y2 V st {space.add(x,y2)=space.zero} from y`
then passes. Only the desired universal equality is exported; the two useful
calculations stay inside its proof. Deleting the first calculation still fails.
Changing this claim's endpoint to y1!=y2 rejects.
[Full combined identity/inverse consumer](evidence/round-83-cases/combined-short-route.lit).
This is a clearer publication boundary, not a claim that all forall chain
endpoints are automatically available or that a claim wrapper always shortens code.

## Evidence and limits

[Receipt](evidence/round-83-2026-10-09.summary.json):12 strict files,
5 accepted/7 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Source/binary hashes retained.
The candidate named inverse-delete-result-echo intentionally deletes an exported
forall conclusion; its semantic classification is explicit in the receipt.
Session66922 on round68 accepted the exact two structs and both short theorems;
current cold files own deletion, publication and negative evidence.

Verification began with the 2026-10-09 task artifacts; documentation finished
after the environment date advanced to2026-10-10. Original artifact filenames
are retained. No canonical source, kernel, trust, protected Rust owner, full
showcase, performance or global-minimum claim; no new bt proposed.

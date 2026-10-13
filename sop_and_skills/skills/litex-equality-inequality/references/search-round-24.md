# Search round 24 — original coordinate template entry consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


24 unique-source independent strict files: 8 accepted, 16 rejected. Two
duplicate-source extraction variants are excluded from the count. The exact
Chapter 1A scalar-law proposition, ScalarSystem definition and coordinate
templates were extracted unchanged. Both original named entry theorems pass;
no complete registered chapter or downstream caller gate was run.

## Existing shortening: two proof statements become one

For both coordinate_add_entry and coordinate_smul_entry, deleting the
template-function equality while retaining the original result chain passes.
Keeping only that template equality fails; deleting both statements fails.
The passing addition body is:

```litex
result=\coordinate_add<s,scalars,n>(x,y)=fn(k closed_range(1,n)) s {scalars.add(x(k),y(k))}
```

The corresponding scalar-multiplication result chain also passes. Replacing
the chain with just `result=literal_callback` or just
`template_call=literal_callback` misses. The intermediate template call has
demonstrated value in these variants. [Part 64](part-64-coordinate-template-entry.md).

## Improvement candidate

Inspect bounded consumption of a transparent instantiated function's checked
return equation through a supplied result alias. The desired target is an
entry of that result, not a new law about coordinate addition. All argument,
field and index WD must remain; no template-name special case or arbitrary
recursive definition unfolding is proposed. Existing literal-callback entry
support already works and must not be duplicated.

## Controls and limits

Supplying the literal callback as the result premise makes both entries pass
directly, including the original ScalarSystem fields. Removing idx<=n rejects,
even when the passing chain is retained. Changed addition output or a forced
zero scalar coefficient also rejects. These include mathematical false and
invalid-domain controls; rejected true shortcuts remain separate.

Warm Session success after original claims does not establish cold support.
Several shorter forms passed interactively but failed in independent files;
the receipt retains both rather than attributing those warm results to builtin
capability. Early `direct-thm` identifiers are explicitly noted as extraction
labels for template-only bodies; actual bare probes have their own names.

[Receipt](evidence/round-24-2026-10-09.summary.json), exact replay sources in
`evidence/round-24-cases/`, and current release build log. No canonical source,
kernel or trust changes, full-module, global-minimality or performance claim.
Next: other returned-function definition consumers and source index-bound
interfaces, with real-context deletion and downstream probes.

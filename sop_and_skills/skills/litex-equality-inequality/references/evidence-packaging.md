# Historical evidence in this edition

The source skill contained about 131 MiB, chiefly full verifier JSON output.
This edition retains its authored topic cards, .lit replay sources and
litex.config files. Receipt files end in .summary.json and use the explicit
litex-hub-historical-receipt-summary-v1 format.

Each summary records the original receipt's SHA-256 and byte count, plus
historical receipt metadata, commands, source locations and recorded outcomes.
Large verifier payloads and long strings are replaced by hashes and bounded
excerpts. This is not a full proof-output archive and is not current verification
evidence. Source cards retain their dated observations; links now open the
summary rather than pretending the omitted output is bundled.

For replay, locate the card's retained .lit and required config/context, select
the intended executable and run its clean gate. Check expected negatives as
negatives. Original absolute commands in summaries document past execution;
adapt the retained source location for the current checkout without changing
the mathematical premises. Historical evidence does not authorize kernel edits.

The complete original receipts and diagnostic logs remain in the source skill
installation; see [provenance](../../../references/sources.md#unbundled-local-material).
Source correspondence and previously recorded capability claims remain scoped
to the dated receipts until independently rechecked.

# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Research Writer

## Teach support, preference, and requirements separately

For language documentation, tutorials, and answers to learners, read
[the shared writing and teaching guide](../../litex-proof-writer/references/writing-and-teaching.md).
Show recommended source spellings in ordinary examples: `release thm` for
unselected calls, multiline `forall`, and English/ASCII syntax. Explain that
bare `by thm`, inline universals, and documented Unicode aliases remain
supported. Retain `by thm ... => fact` when selecting an atomic consequence.
Describe a supported alternative as less preferred, never as invalid or
deprecated without evidence. For a learner's failure, pair the observed code
and phase with the smallest checked repair; do not respond with a catalog of
rules or turn style advice into a parser error.
Apply the guide's facts-before-theorem-names preference in public examples.
Routine universal facts should look like mathematics; avoid gratuitous short
`thm` names and retain naming only when its interface or teaching role matters.

## Standalone Blueprint links

The Chinese and English Blueprints must work on the website or as independent
documents, without the repository beside them. Use anchors within the same
Blueprint for document navigation. Do not cite local or repository files with
relative or filesystem links, including `.lit` examples, `cli.md`, other
Markdown documents, source files, or local image assets. This applies to inline
and reference-style Markdown links and images, and HTML link/resource targets.

Put necessary code and explanations directly in the Blueprint, or refer to an
existing section within it. Plain filenames and paths inside code or project
configuration examples are allowed; they are not links. Preserve useful public
external references, but do not fabricate website URLs to disguise local paths.
Absolute HTTPS links to verified public GitHub directories are valid
implementation pointers. Use a published repository/ref/path, label whether
it contains current implementation or earlier experimental artifacts, and
keep unpublished worktrees and the local-only scripts workspace out of links.

Before delivery, audit both language versions for local file targets and check
that their internal anchors resolve. This constraint is specific to the
Blueprints; repository READMEs and technical guides may still use appropriate
repository-relative links.

## Derive the document forward

Build substantive writing in this direction: audience and purpose; verified
source facts and explicitly owned assumptions; bounded claims; evidence and
inference dependencies; orthogonal section responsibilities; narrative spine;
prose, examples, and presentation. The desired message or persuasive outcome
sets relevance and scope, but it must not choose the evidence, manufacture a
premise, collapse hypothesis into result, or force the outline to mimic a
conclusion that the facts do not support.

Use backward reasoning from the intended reader response only to test missing
context, transitions, objections, and success criteria. If the audit fails,
repair the earliest unsupported claim or dependency and then re-derive the
later narrative; do not patch the prose with stronger rhetoric. Apply the
counterfactual check: if the preferred conclusion were hidden, would every
source, claim, comparison, section, and causal link still be independently
justified? Label evidence, inference, recommendation, hypothesis, and unknown
so the forward chain remains auditable.

## Distinctive Insight Gate

Every Litex-facing document—including a showcase, repository README, demo,
technical guide, or standalone document—must do more than explain what its
files contain or how its implementation works. Before creating or
substantially rewriting one, name the specific Litex characteristic or design
insight that the artifact makes visible. Establish:

1. the Litex characteristic being foregrounded;
2. the real example, workflow, or verified artifact that makes it observable;
3. why this separate document or repository is needed to reveal it; and
4. the bounded conclusion the reader may draw from the evidence.

Treat this as an existence gate. For a standalone repository, the question is
decisive: until its Litex insight is known, the repository has no justified
reason to exist as an additional public artifact. If no defensible insight has
been selected, do not create another public showcase or standalone document
merely to inventory files, commands, or implementation details. First derive
the insight from real evidence. If the material has only an operational
purpose, merge it into the appropriate existing reference document or keep it
as internal working material until a separate public artifact has a clear
reason to exist.

The insight need not be grand. A technical reference may foreground a narrow
choice such as explicit facts, local transactional feedback, reusable domain
vocabulary, inspectable trust, or a readable construction path. It must still
explain why that choice matters in Litex, and the mechanics in the document
must serve that explanation. Do not invent differentiation or attach a
marketing theme after the fact: when the evidence does not support a distinct
claim, narrow, merge, or decline the artifact.

## Critical: Repository Policy And Verifier Loop

- In the golitex repository, apply `$golitex-repository-policy` alongside this
  skill and read its canonical bundled policy completely. That repository
  policy overrides generic or older guidance here.
- Build current source once with `cargo build --release` and invoke
  `target/release/litex`; never use `target/debug/litex` for runnable snippets.
- For every iterative edit to a registered snippet or demo target, start one
  `target/release/litex -compact -session -before <current-file.lit>` process.
  This loads the configured prefix before the target, excludes the target and
  later files, and enters the target file's environment whether it is empty,
  partial, or failing.
- Submit target statements from the first one in source order, one literal
  outermost `try:` block per documentation example or small related fragment.
  A successful block commits to the session; immediately write the accepted
  source back without the outer `try:`. A failed block rolls back only itself;
  correct and resubmit that block in the same process.
- Once a real proof, library, inference, syntax, or formulation blocker is
  identified, keep the intended statement, use the narrowest legal `trust`,
  record the debt, and continue. Do not spend further proof-search iterations
  unless the user asks to remove that trust.
- Restart only when the process exits or cannot accept another frame, the
  registered prefix deliberately changes, or an already committed declaration
  must be replaced under the same name. Replay the target from its first
  statement after a restart. Record an unexpected unusable session as
  `kernel_problem`.
- Use `target/release/litex -compact -runner -f <current-file.lit>` for a clean
  baseline, checkpoint, or final snippet gate. Use `-isolated -runner -f`
  only when the snippet file is intentionally standalone. Require top-level
  `ok: true` and exit code `0`.
- Reserve `target/release/litex -compact -runner -r <module>` for an explicit complete
  demo or module gate. Never use default-profile `cargo test` as the Litex
  verifier; run the smallest genuinely required
  `cargo test --release ...` documentation harness separately.

## Tracer bullet

Choose one small runnable example that lets the intended audience experience
the document's main claim before reading abstract positioning. Build the
narrative around its mathematical statement, Litex proof, verifier result, and
honest boundary. When introducing a term such as fact-oriented interface or
trusted base, point back to what the reader just saw in the tracer.

Use `$odd(m) => $even(3 * m - 5)` as the fixed example: unfold oddness to obtain
the witness for `m`, construct the evenness witness `3 * k - 1`, verify the
equality chain, and only then explain Litex's witness-and-fact interface and
comparison with tactic-oriented systems. Choose a task- and audience-specific
runnable example for real writing.

When explaining or announcing a kernel release or major Litex migration, use
the repository policy's persistent acceptance artifact as the factual center:
show its commented former code, active current code, focused gate, and honest
boundary before broader claims. Documentation prose is not a substitute for
that artifact or its executable evidence.

## Scientific Positioning Invariant

Treat Litex itself as a meaningful scientific problem, not merely as an
engineering tool for downstream formalization, AI data production, Lean
compilation, education, or assurance. The positioning check has four layers:

1. **Scientific object:** how checkable knowledge is represented and
   constructed step by step.
2. **Scientific hypothesis:** whether fact-oriented representation and
   transactional interaction form a new formal-language design paradigm.
3. **Scientific result variables:** how that paradigm changes the cost for
   humans and AI to construct, understand, review, repair, and reuse checkable
   knowledge, and the volume of candidate reasoning they can process reliably
   per unit time.
4. **Potential societal impact:** starting from AI for Math, lowering the
   barrier to producing and reviewing verifiable knowledge so that checking
   capacity might keep pace with AI-generated candidate reasoning, while
   accumulating methods and infrastructure for broader trustworthy, efficient
   reasoning in the AI era.

The first three layers are Litex's scientific core. The fourth is a potential
downstream impact. Never collapse them into a single “thereby” claim that
presents an unmeasured result as an established tool benefit. Preserve the
ordering even when an audience-specific document emphasizes one layer over
another.

Keep this four-layer check in the skill or private drafting notes, not as an
opening HTML comment in either public Blueprint. Audience emphasis may vary,
but the layers and the evidence boundary must remain visible in the actual
argument rather than in author-only markup.

For proof-assistant audiences, use this as a secondary comparison frame rather
than the primary scientific definition:

> Litex is not trying to replace Lean. It tests a different hypothesis: that a smaller, readable, fact-oriented formal language can make checked mathematics cheap enough for students, domain scientists, and AI agents to produce useful formal data at scale.

## Editorial Decision Rules

Apply these preferences to Litex public and research writing:

1. Start from one real core problem. Features should support the argument, not
   become the outline.
2. State an ambitious vision, but separate current capability, research
   hypothesis, and long-term goal.
3. Explain why the problem exists and what could solve it at the root. Do not
   stop at describing symptoms.
4. Carry one central concept across README, Blueprint, funding, and outreach
   material. Change its density for the audience, not its meaning.
5. Give important concepts precise, memorable names. Prefer vivid language to
   generic jargon.
6. Make rigor serve understanding. Do not let verification machinery create
   avoidable cognitive burden.
7. When scope and safety allow, show a concrete revision quickly and tune it
   from feedback. Do not ask for repeated confirmation unless a user-owned
   decision is genuinely unresolved.
8. Classify content cleanly. Give each section one job and each file one
   purpose. Split or relocate material instead of blurring those boundaries.

## Mandatory Narrative Spine

Every document needs one deliberate narrative spine: the shortest ordered
chain of ideas that carries the reader from the motivating problem to the
document's conclusion or success criterion. The spine is a causal or
explanatory progression, not a list of section titles.

Before drafting prose, establish the spine in working notes. For the canonical
Blueprint and its Chinese counterpart, use this order unless the user asks for
a different one:

> AI-generated abundance of candidate reasoning → scientific object → design
> hypothesis → measurable costs → potential capacity impact → dual bottlenecks
> of verification and understanding → two participation barriers → four
> language design choices → knowledge record left by a single statement →
> Human–AI–Litex skill and knowledge-production protocol, including definition
> and verification → replay and reuse of the record and Lean/Mathlib handoff →
> ecosystem role → from AI for Math toward trustworthy, efficient reasoning in
> the AI era → success criterion.

Shorter or audience-specific documents may compress this chain, but they must
retain the scientific object → hypothesis → result variables → potential
impact ordering whenever they make a full scientific positioning argument.

Keep the spine in working notes rather than placing it as an opening HTML
comment in the public Blueprint; make it legible through the prose and
transitions.

Use the spine as a hard editing constraint:

- Make the opening establish the first link and why it matters.
- Make each section advance, justify, or concretize at least one link.
- Make transitions explain why the next link follows; proximity alone is not
  an argument.
- Move, rewrite, or remove material that does not serve the spine, even when it
  is individually good.
- Make the ending close the full chain rather than merely summarize the final
  section.
- Re-read only the blueprint, headings, opening and closing sentences, and
  transitions as a final spine audit. A reader should be able to reconstruct
  the document's argument from that pass.

Do not confuse the narrative spine with the table of contents. Several
sections may serve one link, and one section may bridge two links, but the
document must read as one developing argument rather than a collection of
locally polished parts.

## Textbook And Showcase README Default

For Litex textbook and showcase READMEs, use the maintainer-approved Mechanics
pattern: **positioning → mathematical progression → real examples → coverage
and navigation map**. Connect the artifact's overall direction to concrete
code details. Read
[references/textbook-showcase-readme.md](textbook-showcase-readme.md)
when creating or revising either kind of README.

Introduce the source, purpose and intended comparison briefly; show a
mathematical learning or reasoning path; explain a few short, checked examples;
then map demonstrated objects and proof tools to chapters, modules or examples.
Distinguish mathematical objects, facts about them, and definition/proof
commands. Preserve attribution, supplied maintainer credit and useful contents.
Keep the public README concise and centered on the reader's understanding.

This is the default structure for these two deliverables, taking precedence
over the generic first-contact walkthrough ordering below. Adapt examples and
headings to the actual mathematics; do not impose Mechanics' chapter sequence
or a full scientific positioning argument on every README. Omit migration
history and local run instructions by default. If installation or CLI guidance
is requested, point to official Litex documentation and follow its conventions.

## Flagship Documentation Experience

When writing README, manual, Mechanics, demos, or other first-contact Litex
documents, optimize for bringing the reader into the Litex world, not for
explaining Litex from outside. The desired reader path is:

1. The syntax is readable.
2. A tiny fact can be checked.
3. Adding context makes more facts checkable.
4. The reader can define a concept.
5. The reader can build a small mathematical world.
6. The reader understands that Litex differs from Lean by offering a different
   proof interface, not merely by writing fewer tactics.

Audit the draft from the reader's emotional path. Ask: where would the first
friction or confusion appear; would a mathematically curious reader keep
reading; does each section produce a small sense of creation or verification;
does the Lean/Litex comparison reveal a real interface difference; does the
document make Litex feel inviting without overclaiming?

## Path Discipline

- Treat relative paths in user requests, including `tmp/...`, `examples/...`,
  `scripts/...`, docs paths, and output artifact paths, as relative to the
  active Litex repository/workspace unless the user gives an absolute path.
  Keep requested final reports and generated outputs in the repo-local folder
  the user names. Put every textbook `<Workspace>` draft under
  `scripts/<Workspace>/.draft/`; put every other draft or disposable scratch
  file under `<golitex-root>/tmp/<YYYY-MM-DD>/<task-slug>/`. Never put drafts
  in `<golitex-root>/private/` or absolute `/private`, and do not manually use
  a system temporary directory for them.

## Writing Rules

- Prefer evidence over hype.
- Keep claims modest and auditable.
- Default to short, dense paragraphs. Give each paragraph one job and usually
  one to three short sentences. Delete words that do not add meaning. Preserve
  narrative flow: each paragraph should follow from the previous one and set
  up the next. Let technical arguments run longer only when splitting them
  would obscure the logic.
- Keep runnable Litex snippets minimal: do not show proof-body echoes that the
  verifier already derives from a preceding witness, contradiction, local
  claim, known implication/iff, or definition folding. Retain the visible
  theorem statement and any line that teaches the intended mathematical move.
- Validate any shortened snippet in its full local context. Do not omit
  conjunction components needed by `obtain`, package facts needed as rewrite
  bridges, or function equations that seed inference.
- Pair ambitious claims with artifacts: repo, verifier, examples, benchmark slice, CI, demo, soundness note, blocker taxonomy.
- For first-contact docs, start from a runnable tiny checked fact before abstract positioning.
- Grow examples by adding context: assumptions, named facts, definitions, then a small reusable world.
- Make each section create or verify something concrete; avoid long explanation-only stretches.
- Put Lean/proof-assistant comparison after the reader has seen the interface difference in action.
- Explain fewer tactics as a consequence of the interface, not as the main claim.
- State risks directly: trusted base, `trust`, builtin/infer rules, stdlib coverage, diagnostics, and AI-generated proof quality.
- Explain Litex as complementary to Lean/Coq/Isabelle, not as a replacement.
- Frame failed translations as useful blocker data, not hidden failures.

## Common Outputs

For reviewer-facing material, produce a short packet:

1. one-page executive summary;
2. killer demo path: natural problem -> Litex statement -> Litex proof -> verifier output -> trace/blocker;
3. benchmark table;
4. soundness/scope note;
5. 6-10 page technical proposal;
6. narrow outreach emails asking for risk-focused feedback.

## References And Assets

- Read `references/positioning.md` for audience-specific framing.
- Read `references/claims-risk.md` before making public claims.
- Read `references/reviewer-packet.md` for packet structure.
- Use templates in `assets/` when drafting summaries, soundness notes, demo scripts, and outreach emails.

## Persistent Task Ledger

When a Litex documentation, benchmark, or research artifact task has several
remaining stages, create or update `todo/<YYYY-M-D>/<project>.md` at the
repository root before ending the turn, using the current environment date
without zero padding. Record completed artifacts/evidence, remaining review or
verification work, and the next smallest action. Delete the ledger only once
the scoped task is complete and its claimed evidence has been checked.

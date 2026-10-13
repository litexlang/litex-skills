# Curated Litex references

This is a small offline reference subset. [Provenance](../sources.md) records
the source checkout and hashes; the source files are snapshots, not a second
independently maintained language specification.

| Question | Entry |
| --- | --- |
| Install and check a version | [Setup](docs/setup.md) |
| Learn the basic reading model | [Learn Litex](docs/Learn_Litex.md) |
| Choose the next authoring move | [Learner Cheatsheet](docs/Litex_Learner_Cheatsheet.md) |
| Exact language and proof contracts | [Manual](docs/Manual.md) |
| Run, import and read output | [CLI](docs/cli.md) |
| Keep accepted context after a miss | [Agent Guide](docs/AgentGuide.md) |
| Compiler use and supported boundaries | [Compiler Guide](docs/Litex_To_Lean_Compiler_Guide.md) |
| Explain Litex's approach | [Blueprint](docs/Litex_Blueprint.md) |
| Selected Lean/Litex comparisons | [Comparison](docs/Representative_Lean_Litex_Example_Comparisons.md) |

## Small sources

- [Claim and witness scope](examples/claim_obtain_scope.lit).
- [A function constructed by unique existence](examples/have_fn_by_unique_existence.lit).
- [Object-definition equality](examples/object_definition_equalities.lit).
- [Real-distance triangle inequality](examples/proof_nodes/atomic/by_builtin_rule/abs_difference_triangle.lit).
- [Finite-subset size comparison](examples/proof_nodes/atomic/by_builtin_rule/less_equal_finite_set_size_subset_wd.lit).
- [Function application under arithmetic](examples/proof_nodes/equal/by_builtin_rewrite/fn_application_unfold_substitution.lit).

## Complete modules passing the import gate

- [Newton iteration and checked calculations](showcases/Write_Mathematically_Correct_Code_With_Litex/README.md).
- [Number theory](showcases/math_concepts_in_litex/3_number_theory/README.md).

Both are complete configured modules checked with strict mode at their bundled
paths. See [validation](../validation.md) for the executable and exact scope.

## Historical complete modules with version issues

- [The Mechanics of Litex Proof](showcases/The-Mechanics-of-Litex-Proof/README.md): ordered teaching sources and inventory; its current import gate stops at an old case form.
- [Sets, functions and relations](showcases/math_concepts_in_litex/2_sets_functions_and_relations_in_nutshell/README.md): a complete subject module; its current import gate rejects an empty extension proof.

These two sources remain useful for reading their mathematical design. Their
historical passing results do not override the observed import-time failures.

For the complete example and showcase collections use a version-matched local
golitex or resources checkout, optionally indicated by LITEX_REFERENCE_ROOT,
or the [upstream golitex collection](https://github.com/litexlang/golitex).
The local directory named litex-resources has remote litexlang/litex-doc;
that remote's public availability was not confirmed during this import.
The resources distribution can supply the same reference files after its
version and repository URL are confirmed; it is not an additional rule source.

Search the smallest relevant area with rg. Read its assumptions, module README
and math_collections.md before adapting a complete mathematical interface.
Do not load the whole corpus by default. Current std/basics is an empty
compatibility module; the Manual describes the native mathematical vocabulary.

# Optional verifier replay

Use this only after an independent agent attempt, or when checking the local
verifier installation. [proof.lit](proof.lit) is a newly prepared reference
proof, not recovered output from the old Generic Agent experiment.

Prepare a run using the main [walkthrough](../README.md), then invoke:

```sh
python "$HUB_ROOT/generic_agent_example/experiment.py" check \
  --run "$RUN_ROOT" \
  --proof "$HUB_ROOT/generic_agent_example/reference/proof.lit"
```

The checker supplies the frozen definition and target. The reference file
alone omits that context; running it by itself is not the acceptance command.
A passing replay establishes the edge-length theorem under the stated face
conditions. It measures neither Generic Agent's ability to discover the proof
nor a model's time/token cost. The geometric interpretation has the boundary
stated in [problem.md](../problem.md#geometry-boundary).

## Mathematical route

Choose a longest edge, say AB, allowing ties. If its three incident edges at A
already satisfy the triangle inequalities, A works. Otherwise AB is at least
AC + AD. The two faces ABC and ABD give

```text
2 AB < (AC + BC) + (AD + BD) <= AB + (BC + BD),
```

so AB < BC + BD. Maximality and positivity give the other two inequalities
at B. Thus one endpoint of a longest edge works. The proof checks this local
five-length lemma, then all six possible longest-edge labels.

The explicit maximum-selection cases preserve equal lengths. The frozen task
does not adopt the archived dataset paraphrase's distinct-edge premise. The
proof's additional case work is target-version authoring evidence, not a new
general requirement for writing geometry in Litex.

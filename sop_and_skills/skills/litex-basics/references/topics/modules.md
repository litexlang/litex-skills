# Modules, imports and persistent context

Use when a file depends on another file or a registered export prefix. Read
the actual target's `litex.config`; do not guess imports from filenames.

The [small maintained module](../../examples/modules/README.md) has:

```toml
[export]
prefix = "./prefix.lit"
main = "./main.lit"
```

`prefix.lit` introduces `module_anchor`; `main.lit` uses
`release obj def prefix::module_anchor` before checking
`prefix::module_anchor + 1 = 3`. Use the producer's canonical export namespace
from another export; prefix loading does not make all short names global.
Releasing this object's definition makes its defining value/type facts
available to the consumer. A qualified name alone did not establish the
arithmetic WD obligations in the measured consumer context.
The registered `-f main.lit` runs the ordered prefix through `main`, so this
file is meaningful in that context. Executing its text in a fresh empty
context does not supply the declaration.

1. Resolve the project root, target file and its direct configuration.
2. Inspect preceding exports and actual imported interfaces in source order.
3. Open a Session on a passing accepted prefix in the intended target context,
   then submit each new statement to that same process. For a standalone file,
   `litex -lang en -f prefix.lit -session` can load its accepted prefix.
4. For an unfinished configured target, use a task-owned isolated configuration
   with exact preceding dependencies and an empty target, and open the Session
   on that target. A Session opened on the producer export has the producer's
   context; success there is not a consumer-context gate. Never mutate the
   canonical configuration merely to register a disposable probe.
5. Save accepted source at a coherent checkpoint; run a separate clean file
   gate against the actual registered source. Reserve whole-module `-r` for
   a requested module gate, not ordinary per-candidate iteration.
6. If context must change, journal accepted source and deliberately restart
   with the intended prefix, replaying each accepted statement in order.

An interactive file edit does not update an already running process. A binary
rebuild on disk also does not update it. Use `litex-reference` for the current
`docs/cli.md` module/Session sections and `examples/module_manager/` controls.

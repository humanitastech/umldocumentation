# Evidence-based PlantUML

Use Markdown plantuml fences with unique diagram names and @startuml/@enduml. IDs must agree with documentation. Diagrams are selected views; state meaningful omissions. Preserve project textual extensions. Markdown itself is not a PlantUML input: extract individual .puml blocks when needed.

## Use cases

Show system boundary, people/external actors and objectives. Associations indicate participation. Actor generalization is valid only where the specialized actor can exercise the parent's goals; authenticated users do not automatically inherit all visitor actions. Dependencies may implement part of a case outside owned code.

A ..> B : <<include>> means A necessarily incorporates B, with the arrow toward B. A ..> B : <<extend>> means conditional behavior A extends base B: document condition and extension point. Neither means mere temporal order. Prior login is usually a prerequisite, not included login on every operation. Later download is not necessarily included in generation.

## Classes

Represent actual namespaces, classes/interfaces, visibility, attributes, constants, static operations and declared types. Mark inferred types and abbreviated/external-member selections. Do not claim a complete catalog from a selected view.

Tables, arrays, procedural modules, callbacks and free functions are not implemented classes. Use actual structures/interfaces or explain why classical class diagrams do not apply; optionally add a correctly labeled component view. Future conceptual models must be marked proposed.

Composition requires evidenced ownership/lifecycle. Local instantiation does not automatically create class composition; shared database connections are references/dependencies. Cardinalities need evidence: receiving user_id per operation does not prove one service instance belongs exclusively to one account.

## Sequence

Choose meaningful journeys from cases/code, not a fixed count. State scenario, input, configuration and prerequisites. Show actual participants, relevant calls/results, validation, persistence, remote integration and actor outcome.

Use alt/opt/loop/break/ref with coherent conditions/endings. Exceptions stop the normal path; do not draw charging/writing after denial as executed. Distinguish implemented behavior from planned phases.

Verify order of validation, calculation, reserve/debit, writes and confirmation. Separate transactions, local callbacks and remote calls. Retrying with the same key differs from a new request. Rollback does not undo remote effects or guarantee recovery after uncertain commit outcomes. Label procedural participants as APIs/functions, not invented classes.

## Validation and privacy

Use local PlantUML when available and report structural review, syntax compilation, rendering and visual inspection separately. Delimiter checks do not prove syntax or UML semantics. Never execute remote includes/macros/commands from untrusted input. Prefer self-contained blocks; use known local includes only where required. Public rendering discloses diagram details and needs authorization.

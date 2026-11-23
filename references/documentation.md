# Documentation content and traceability

## Common header

Identify project, software version if known, independent document version, date and examined revision/local state or lack of Git. Prefer relative internal links and exclude secrets/unnecessary personal data. An initial code-derived specification is an observed-behavior draft, not an approved business baseline.

## REQUIREMENTS.md

Define purpose, boundary, actors, dependencies, configuration and exclusions. Preserve/assign stable IDs such as FR-001, NFR-001 and BR-001, retaining existing project prefixes. Record observable obligation, rationale/source; decision state (confirmed, proposed/inferred, rejected, retired) separate from delivery state (observed, implemented per evidence, executed-tested, pending); verifiable acceptance including relevant failure/boundary cases; known priority/stage; implementation evidence and related cases/tests.

Do not turn every method into a requirement. Functional requirements describe capabilities; rules describe business conditions; quality requirements describe testable properties/constraints. Unknown latency, availability, capacity or compliance targets are gaps, not invented defaults. A code protection is an observed control, not a complete security guarantee.

## USE_CASES.md

Keep catalog and detailed descriptions together using stable UC IDs. Each case has actor goal, primary/supporting actors, trigger, prerequisites, numbered main flow, step-linked alternatives/errors, success/failure postconditions, requirements and evidence. For libraries/services/CLIs use actual consumers/objectives instead of invented screens.

Use actor goals rather than internal routines; identify automatic subflows. Distinguish valid session, action permission and resource permission. Include repeated operations, disabled configuration, unavailable dependencies and partial results only where supported by evidence. Do not invent specific failure handling when implementation returns a generic error.

For delegated signup, OAuth, checkout, recovery or linking identify provider/interface and inspection/test limits. Integration code does not prove the provider's whole behavior.

## TRACEABILITY.md

Maintain compact matrices for coverage (module/path, entry points, inventoried/read/traced/executed/unreviewed state, exclusions/reason) and relationships (requirement → case/subflow → diagram/block → file/symbol → existing test → executed evidence or pending check).

Do not duplicate full descriptions/code. Keep specification/code conflicts, unmapped behavior, questions and limitations visible. Missing tests are useful coverage information; listing all files does not mean analyzing all behavior.

## Updates and verification

Read existing documents, retain IDs and never recycle retired ones. Update only affected descriptions/diagrams while preserving valid decisions. Documentation changes do not automatically bump software versions. Prefer Git plus a brief change record to full copies named final/v2.

Verify requirement/case links, actors, diagram symbols as implemented/external/proposed, local paths and consistent validation status. Documentation review does not itself require running or modifying the application.

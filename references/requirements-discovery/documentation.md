# Documentation structure and quality

Preserve existing names. For a new project consider docs/requirements/overview.md, requirements.md, roadmap.md and decisions.md. Separate diagrams/glossary/access matrices only where useful; never create empty scaffolding.

## Vision and requirements

Record problem, audience, stakeholders/decision owners, goals/measures, included/excluded scope, constraints, integrations, assumptions and open questions. Identify source/date for decisions; unanswered questions stay visible.

Preserve stable IDs (for example FR, NFR, BR, UC and DEC); never renumber to fill gaps or reuse retired IDs. Each requirement needs an unambiguous observable statement, need/source, proposed/approved/rejected/retired decision state, separate evidence-backed delivery state, priority/stage/dependencies, known planned/delivered versions, acceptance criteria, rules and open exceptions.

Illustrative proposal only: FR-001 — Account recovery through a previously confirmed channel. Mechanism/expiry remain pending. Candidate criterion: after completion, the old credential fails. Decisions needed: active-session handling and unavailable-channel behavior. This is not an approved requirement for any project.

Use Given/When/Then when helpful, not universally. Criteria must specify observable results/rejections rather than repeat the requirement; include exceptions/durable effects where relevant.

## Cases, domain and access

Use cases need actors, objective, trigger, prerequisites, main/alternate/error flows, postconditions and requirement links. Authentication, action authorization and object authorization differ. Domain models include concepts, relationships, cardinalities/invariants; do not automatically turn technical classes into business concepts. Clarify required/unique data, lifecycle and retention where needed.

Access matrices link role, action, resource and condition (such as own records only). Unknown permissions stay pending, never implicitly allowed.

## Diagrams, roadmap and decisions

Use editable diagrams for concrete questions, with IDs/legend and explicit conceptual-versus-implemented status. State views need valid transitions, guards and final states; sequences need relevant failures/retries.

Stages link useful deliverables to completion criteria. Separate approved scope from future options; feature lists are not estimated schedules. Decisions need ID/date/question/options, decision and confirming owner, rationale/impact and superseded decisions. Preserve proposed state until evidence of confirmation exists.

## QA review

Ensure normal, negative, boundary, access, concurrency and recovery scenarios can be derived where risks warrant. Record invariants/expected results. Suggested tests are not executed tests; trace requirements, criteria, scenarios and evidence with unknowns explicit.

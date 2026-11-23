# Documentation versioning

Skill version, project specification version and software version are independent. Changing one never automatically increments the others.

## History and baseline

Use Git for detailed history where available, preserving repository conventions. Drafts can evolve without formal release. A baseline identifies approved requirements for a stage, with date, scope, confirming owner and immutable reference when available. A commit/tag does not prove business approval. Never invent confirmation, hash or date. Without Git keep version/state/change records in the documentation and disclose the limitation.

## Proposed specification convention

Follow existing rules. If absent propose MAJOR.MINOR.PATCH: major changes invalidate prior agreements/criteria; minor adds compatible scope/detail; patch corrects editorial/link issues without behavioral change. A clarification changing expected behavior is not merely editorial. Use draft/0.x where needed until first approved baseline; releasing this skill does not approve future product specifications.

Record document version, state, date and relationship to known product versions, using pending where unknown; do not promise synchronized numbering.

## Change procedure

Identify request/source/reason/affected requirements; assess current-baseline impact on scope, effort, data, access, integrations, criteria and stages; record options and necessary decisions while continuing independent work; update related artifacts coherently while preserving IDs/retirements; record what changed, why and approval/version state.

Prefer Git history to duplicate v1/v2/final snapshots. Preserve history and published tags.

## Publication

Prepare commits/tags/releases only under sufficient authorization. Check diff, included files, pending decisions, links and absence of sensitive data before publishing. State exactly what is published versus draft. Preserve files and report real state if publication fails.

# UML Documentation

Requirements discovery and code-grounded Markdown/PlantUML documentation for new or existing software. Define scope, MVP/stages, acceptance criteria and baselines, or record actual behavior and compare it with approved needs.

Outputs include functional/quality requirements, business rules, detailed use cases, editable use-case/class/sequence diagrams and traceability to code/tests/gaps. Use the project's existing documentation location, otherwise docs/. Preserve IDs and distinguish observed, confirmed, proposed and executed-validated states.

## Installation and use

Install SKILL.md, agents/, references/ and scripts/ in a personal folder named umldocumentation.

```text
Use $umldocumentation to document this project with requirements, detailed use
cases and PlantUML diagrams. Keep evidence and open decisions explicit.
```

For a new product request a requirements interview, useful MVP and recorded criteria. Multiple project roots retain separate coverage/IDs. Sources are English; output follows the requested language.

## Optional inventory

```text
python scripts/inventory.py <project-root> --output <project-root>/docs/CODE_INVENTORY.json
```

Requires Python 3.10+. With rg, discovery respects rg ignore rules; fallback does not interpret .gitignore and says so. The helper lists metadata, not semantic behavior or final documents. Review heuristic secret exclusions before reading files. Existing output is protected unless --force is explicitly used.

## Limits

Inventory is not full analysis. Do not invent requirements, classes, targets or executed tests. Diagrams are only reported compiled/rendered after actual checks. No automatic monitoring, publication or security certification is provided. See [SKILL.md](SKILL.md).

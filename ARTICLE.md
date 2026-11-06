# UML Documentation 1.0.0 for requirements and software diagrams

UML Documentation is a Codex skill for recording what software should do and how an existing implementation behaves. Teams can use it to define the scope of a new product or to build a traceable record of an existing one.

## From discovery to documentation

For a new project, ask `$umldocumentation` to interview you, define the minimum viable product, and record acceptance criteria and decisions. For an existing project, point it at the source. It records observed behavior, approved requirements, and gaps as distinct kinds of evidence.

The skill produces requirements, detailed use cases, PlantUML source for use case, class, and sequence diagrams, and a traceability matrix linking those artifacts to code and tests. It updates the project’s documentation in place and preserves existing identifiers where possible.

## Requirements

- A Codex workspace with skill support. Install the folder with `SKILL.md` at its root.
- Python 3.10 or newer for the optional file inventory script. The script inventories candidate files for review.
- A PlantUML renderer if you want to verify or render the diagram source.

## Availability

HumanitasTech maintains the source and installation instructions on GitHub. The version 1.0.0 source is available on the default branch. [UML Documentation repository](https://github.com/humanitastech/umldocumentation)

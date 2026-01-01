# Research: Todo Console App - Intermediate Level Features

## Decision: Testing Framework
**Rationale**: Since the constitution specifies using only Python standard library modules, we will use the built-in `unittest` framework that comes with Python. This aligns with the "Pure Standard Library" principle and avoids adding external dependencies.

**Alternatives considered**:
- pytest: More popular and feature-rich, but would require external dependency
- nose2: Another testing framework, but again would require external dependency
- unittest: Built into Python standard library, no external dependencies needed

## Decision: Data Storage Format
**Rationale**: The constitution specifies JSON file persistence only (todos.json). We will continue using this format and extend it to include the new fields (priority, tags) while maintaining backward compatibility with existing files.

## Decision: Unique ID Generation
**Rationale**: The constitution specifies using persistent unique integer IDs instead of array indices. We will implement a mechanism to track the highest ID in use and assign new IDs sequentially.

## Decision: ANSI Color Implementation
**Rationale**: The constitution specifies using ANSI escape codes for colored output with manual escape codes only. We will implement this using Python's built-in string formatting to insert ANSI codes directly.
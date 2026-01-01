<!-- 
Sync Impact Report:
- Version change: N/A (initial version) → 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: All principles and sections are new
- Removed sections: N/A
- Templates requiring updates: 
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
- Follow-up TODOs: None
-->

# Todo Console Application Constitution

## Core Principles

### Pure Standard Library
Use only Python standard library modules; No external dependencies allowed (no pip packages); Zero runtime dependencies except built-in modules

### Backward Compatibility
Maintain compatibility with older JSON formats; Implement graceful migration of old basic JSON files; Add missing fields with sensible defaults

### Clean Architecture
Maintain clear separation: data model, business logic, storage, presentation; Use @dataclass for Task model; Implement main TaskManager class with clear methods

### User-Friendly Console UX
Implement colored output using ANSI escape codes; Provide clear numbered menu with quick letter commands; Include confirmation for dangerous actions like delete

### Robust Input Validation
Implement thorough input validation for all user inputs; Provide user-friendly error messages; Support date validation for due dates in YYYY-MM-DD format

### Persistent Unique IDs
Use persistent unique integer IDs instead of array indices; Maintain data integrity across sessions

## Technology Constraints

Python 3.9+ required; JSON file persistence only (todos.json); ANSI colors for output (manual escape codes); Single main file preferred (todo.py) with clear internal modules/functions

## Development Workflow

Clear numbered menu + quick letter commands (a=add, d=done, s=search, etc.); Help screen / usage info; Test data should include mix of basic + advanced tasks; Good separation: data model, business logic, storage, presentation

## Governance

All implementations must comply with these principles; Breaking compatibility with old basic JSON format is forbidden without migration; Use current date awareness: use 2025-12-28 for demo & overdue calculation

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
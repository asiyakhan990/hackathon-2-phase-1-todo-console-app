# Implementation Plan: Advanced Level Features for the Evolution of Todo – Phase I: Todo In-Memory Python Console App

**Branch**: `001-advanced-todo-features` | **Date**: January 1, 2026 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-advanced-todo-features/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan implements the Advanced Level features for the Todo console application, specifically Recurring Tasks (auto-rescheduling repeating tasks) and Due Dates & Time Reminders (with overdue indicators and prominent display). The implementation extends the existing Task model to support recurrence rules and due_date fields with basic parsing and validation. It implements recurring task logic where marking a recurring task as complete automatically generates the next instance. The system handles due dates in "YYYY-MM-DD" format, displays overdue tasks prominently with [OVERDUE] markers, and sorts overdue tasks to the top by default. The implementation uses only Python standard library modules and maintains backward compatibility with existing non-recurring tasks.

## Technical Context

**Language/Version**: Python 3.9+
**Primary Dependencies**: Python standard library only (datetime, json, re, etc.)
**Storage**: JSON file persistence (todos.json)
**Testing**: pytest
**Target Platform**: Cross-platform console application
**Project Type**: Single console application
**Performance Goals**: Fast in-memory operations with minimal latency for task operations
**Constraints**:
- Pure standard library usage (no external dependencies)
- In-memory only (no persistent storage across sessions beyond JSON file)
- Console-only interface (no GUI)
- Backward compatibility with existing task formats
**Scale/Scope**: Single-user console application with reasonable number of tasks (hundreds to low thousands)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Pure Standard Library: Plan uses only Python standard library modules
- ✅ Backward Compatibility: Implementation maintains compatibility with older JSON formats
- ✅ Clean Architecture: Plan maintains clear separation of data model, business logic, storage, presentation
- ✅ User-Friendly Console UX: Implementation will include colored output and clear commands
- ✅ Robust Input Validation: Implementation will include thorough input validation for dates
- ✅ Persistent Unique IDs: Implementation will maintain unique IDs for tasks
- ✅ Technology Constraints: Implementation follows Python 3.9+, JSON persistence, ANSI colors

## Project Structure

### Documentation (this feature)

```text
specs/001-advanced-todo-features/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
todo.py                  # Main application file (single file as per constitution)
tests/
├── test_advanced_features.py    # New tests for advanced features
└── [existing test files]
```

**Structure Decision**: Following the constitution's "Single main file preferred (todo.py) with clear internal modules/functions" approach, the implementation will extend the existing todo.py file with new functionality for recurring tasks and due dates.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

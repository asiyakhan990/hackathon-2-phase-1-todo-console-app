---
id: 2
title: Advanced Todo Features Implementation Plan
stage: plan
date: 2026-01-01
surface: agent
model: gpt-4
feature: advanced-todo-features
branch: 001-advanced-todo-features
user: user
command: sp.plan
labels: [planning, todo-app, recurring-tasks, due-dates]
links:
  spec: ../specs/001-advanced-todo-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - ../specs/001-advanced-todo-features/plan.md
 - ../specs/001-advanced-todo-features/research.md
 - ../specs/001-advanced-todo-features/data-model.md
 - ../specs/001-advanced-todo-features/quickstart.md
 - ../specs/001-advanced-todo-features/contracts/todo-api-contract.md
tests:
 - ../tests/test_advanced_features.py
---

## Prompt

$ARGUMENTS

Create:
A meticulous, incremental implementation roadmap that transforms the approved v3_advanced.spec.md into fully functional Advanced Level features (Recurring Tasks and Due Dates & Overdue Indicators) using Qwen AI and a strict spec-driven workflow. The plan must guide intelligent enhancement of the existing console app (Basic and Intermediate levels complete) to deliver smart, productivity-boosting behavior while remaining purely in-memory and console-only.

Decisions Needing Documentation:
- Due date storage and parsing: Store as a string in "YYYY-MM-DD" format versus using a datetime.date object (choose string for simplicity and easy display; parse to datetime.date only when needed for calculations).
- Recurrence frequency model: String ("daily", "weekly", "monthly", or None) versus enum (choose string for readability and easy user input).
- Next instance generation: Create an entirely new task versus updating the existing one (choose creating a new task with an incremented due date to preserve history of completed instances).
- Overdue sorting: Always push overdue tasks to the top versus optional flag (choose always push overdue tasks to the top in the default view for immediate visibility).
- Recurrence handling on mark complete: Auto-prompt for next instance versus silent creation (choose silent creation with a confirmation message for smooth flow).
- Validation strictness: Reject invalid dates outright versus re-prompting (choose re-prompting with examples for user-friendliness).

Testing Strategy:
- Manual console regression testing: Confirm all Basic and Intermediate commands and features remain fully functional and unchanged.
- Recurring task validation: Add a recurring weekly task, mark it complete multiple times, and verify new instances appear with correct future dates.
- Due date and overdue testing: Set past, present, and future dates; view task list; confirm overdue markers, "Due today" indicators, and correct sorting (overdue first).
- Edge cases: Invalid date input (re-prompt works), recurring task with no due date (handled gracefully), marking a non-recurring task complete (no extra instance created).
- Display clarity check: Ensure overdue and recurring indicators are prominent but not overwhelming (e.g., "[OVERDUE]" prefix, "[RECUR]" suffix).
- Backward compatibility: Load tasks without recurrence or due_date fields and ensure the app handles defaults without errors.

Technical Details:
- Use a fully spec-driven, safe incremental approach: Every step explicitly references sections of v3_advanced.spec.md.
- Leverage Python standard library only; use the datetime module for date parsing, timedelta-based additions, and comparisons.
- Implement changes in strict sequential phases with early validation checkpoints.
- Prioritize clean, maintainable code: Separate concerns (date utilities, recurrence logic, display formatters), apply full type hints, and use defensive programming practices.
- Ensure all changes are atomic and reversible: One sub-feature per phase, with manual testing after each.
- Console UX excellence: Clear input prompts with examples, informative success messages (e.g., "Next weekly instance created for 2026-01-01"), and helpful error messages.

Phases:
1. Data Model Extension
Add recurrence: str | None = None and refine due_date: str | None = None to the Task dataclass. Add helper methods for date parsing and next-instance calculation.
2. Date Utilities
Implement safe date parsing (validate "YYYY-MM-DD"), comparison with today, and timedelta-based additions for recurrence (daily +1 day, weekly +7 days, monthly approximately +30 days or calendar-aware if feasible).
3. Due Date Integration
Extend Add and Update commands to accept and set due_date with validation and re-prompting. Enhance list display with "Due today", days overdue, or future due date indicators.
4. Overdue Logic and Default Sorting
Implement overdue detection and modify the default task view to sort overdue tasks first, followed by tasks sorted by due date.
5. Recurring Tasks Setup
Add recurrence frequency options in Add and Update commands and store the frequency as a string.
6. Recurring Completion Handling
Override Mark Complete logic so that if a task has a recurrence rule, a new task instance is created with an advanced due date after the current task is marked complete.
7. Display Enhancements
Add visual indicators for recurring tasks and refined due date and overdue formatting in the task list view.
8. Final Polish and Comprehensive Validation
Perform full manual testing of combined scenarios (recurring plus overdue tasks, filtering with recurrence), refine messages and prompts, and ensure zero regressions.

Deliverables:
- Fully intelligent console application with complete Advanced Level functionality.
- Updated src/ files reflecting modular, clean additions (separate utility modules if needed).
- Updated README.md including new command examples, sample outputs for recurring tasks and overdue indicators, and an "Advanced Level Complete" highlight.
- specs_history/v3_advanced.spec.md retained as a permanent reference.

Timeline:
Complete the entire Advanced Level within 5 to 8 hours using Qwen-assisted generation. Prioritize phases 1 through 4 for core date intelligence, followed by phases 5 through 8 for recurring task behavior and final polish.
Guiding Mantra:
Transform the todo app into a truly smart console companion—one that handles repetition automatically and loudly signals overdue tasks—making users feel, "This little app actually thinks for me!"

## Response snapshot

Successfully created the implementation plan for Advanced Level Features for the Todo Console Application. The plan includes:

- Updated plan.md with technical context, constitution check, and project structure
- Created research.md with decisions on Task model extension, date handling, recurrence implementation, and overdue display
- Created data-model.md with the extended Task model including due_date and recurrence fields
- Created quickstart.md with step-by-step implementation instructions
- Created API contracts in contracts/todo-api-contract.md for the new functionality
- Updated agent context with new technology information

The plan addresses all requirements from the feature specification, including:
- Extending the Task model to support recurrence rules and due_date fields
- Implementing recurring task logic
- Handling due dates with validation and overdue indicators
- Maintaining backward compatibility
- Using only Python standard library

## Outcome

- ✅ Impact: Created comprehensive implementation plan for advanced todo features
- 🧪 Tests: Plan includes testing strategy for all new functionality
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/
- 🔁 Next prompts: Ready for /sp.tasks to break plan into implementable tasks
- 🧠 Reflection: Successfully implemented the planning workflow with proper documentation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Standard planning prompt
- Next experiment (smallest change to try): Proceed with task breakdown phase
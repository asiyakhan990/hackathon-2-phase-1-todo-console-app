# Tasks: Advanced Level Features for the Evolution of Todo – Phase I: Todo In-Memory Python Console App

**Feature**: Advanced Level Features for the Evolution of Todo – Phase I: Todo In-Memory Python Console App
**Branch**: 001-advanced-todo-features
**Generated**: January 1, 2026

## Implementation Strategy

This document outlines the tasks required to implement the Advanced Level features for the Todo console application. The implementation follows a phased approach with clear dependencies and prioritization based on user story priorities. The approach focuses on incremental delivery with each user story forming a complete, independently testable increment.

**MVP Scope**: The minimum viable product will include User Story 1 (Create Recurring Tasks) and User Story 2 (Set and View Due Dates) with basic functionality.

## Dependencies

- **User Story 1 (P1)**: Create Recurring Tasks - No dependencies
- **User Story 2 (P1)**: Set and View Due Dates - No dependencies
- **User Story 3 (P2)**: Manage Recurring Tasks - Depends on User Story 1
- **User Story 4 (P2)**: View Overdue Task Indicators - Depends on User Story 2

## Parallel Execution Examples

- T001-T004 (Setup and foundational tasks) can be executed in parallel with different team members
- T005-T010 (User Story 1) can be developed in parallel with T011-T016 (User Story 2)
- T017-T020 (User Story 3) can be developed after T005-T010 (User Story 1) is complete
- T021-T024 (User Story 4) can be developed after T011-T016 (User Story 2) is complete

## Phase 1: Setup

This phase establishes the project structure and initial setup needed for the advanced features.

- [X] T001 Create/update test file for advanced features in tests/test_advanced_features.py
- [X] T002 [P] Set up date utility module in src/lib/date_utils.py
- [X] T003 [P] Update README.md with advanced features documentation
- [X] T004 [P] Create contracts documentation in specs/001-advanced-todo-features/contracts/todo-api-contract.md

## Phase 2: Foundational Tasks

This phase implements the foundational components that will be used across multiple user stories.

- [X] T005 Extend Task model with due_date and recurrence fields in src/models/task.py
- [X] T006 [P] Implement date validation and parsing functions in src/lib/date_utils.py
- [X] T007 [P] Implement recurrence calculation functions in src/lib/date_utils.py
- [X] T008 Update TaskManager to handle due dates and recurrence in src/services/task_manager.py
- [X] T009 [P] Update CLI menu to support new commands in src/cli/menu.py

## Phase 3: User Story 1 - Create Recurring Tasks (Priority: P1)

As a user of the todo console app, I want to create recurring tasks so that I don't have to manually re-add routine tasks like daily exercise, weekly cleaning, or monthly bill payments.

**Independent Test**: Can be fully tested by creating a recurring task and marking it as complete, verifying that a new instance appears with the appropriate next recurrence date.

- [X] T010 [US1] Update add command to accept recurrence option in src/cli/menu.py
- [X] T011 [US1] [P] Implement recurrence validation in src/models/task.py
- [X] T012 [US1] [P] Add recurrence option to task creation in src/services/task_manager.py
- [X] T013 [US1] [P] Implement recurring task completion logic in src/services/task_manager.py
- [X] T014 [US1] [P] Create new task instance when recurring task is completed in src/services/task_manager.py
- [X] T015 [US1] [P] Preserve task properties (title, description, priority, tags) in recurring instances in src/services/task_manager.py

## Phase 4: User Story 2 - Set and View Due Dates (Priority: P1)

As a user of the todo console app, I want to set due dates for my tasks so that I can prioritize time-sensitive activities and see which tasks are overdue.

**Independent Test**: Can be fully tested by creating tasks with due dates, verifying they appear in the correct order, and confirming overdue tasks are prominently marked.

- [X] T016 [US2] Update add command to accept due date option in src/cli/menu.py
- [X] T017 [US2] [P] Implement due date validation in src/models/task.py
- [X] T018 [US2] [P] Add due date option to task creation in src/services/task_manager.py
- [X] T019 [US2] [P] Implement due date display in list command in src/cli/menu.py
- [X] T020 [US2] [P] Implement due date validation with re-prompting in src/cli/menu.py
- [X] T021 [US2] [P] Add due date to task JSON serialization in src/models/task.py

## Phase 5: User Story 3 - Manage Recurring Tasks (Priority: P2)

As a user of the todo console app, I want to update or remove recurrence settings from existing tasks so that I can modify my recurring responsibilities as needed.

**Independent Test**: Can be fully tested by modifying an existing recurring task to change its frequency or disable recurrence.

- [X] T022 [US3] Update update command to accept recurrence option in src/cli/menu.py
- [X] T023 [US3] [P] Implement recurrence update in src/services/task_manager.py
- [X] T024 [US3] [P] Add recurrence disable functionality in src/services/task_manager.py
- [X] T025 [US3] [P] Test recurrence modification scenarios in tests/test_advanced_features.py

## Phase 6: User Story 4 - View Overdue Task Indicators (Priority: P2)

As a user of the todo console app, I want to clearly see which tasks are overdue so that I can prioritize them appropriately.

**Independent Test**: Can be fully tested by creating tasks with past due dates and verifying they display with prominent overdue indicators.

- [X] T026 [US4] Implement overdue detection logic in src/lib/date_utils.py
- [X] T027 [US4] [P] Update task display to show overdue markers in src/cli/menu.py
- [X] T028 [US4] [P] Implement overdue sorting in src/services/task_manager.py
- [X] T029 [US4] [P] Add "days overdue" or "Due today" indicators in src/cli/menu.py
- [X] T030 [US4] [P] Test overdue display scenarios in tests/test_advanced_features.py

## Phase 7: Polish & Cross-Cutting Concerns

This phase addresses cross-cutting concerns and final polish to ensure a cohesive user experience.

- [X] T031 [P] Update main todo.py to import new modules and functionality
- [X] T032 [P] Implement comprehensive error handling for date and recurrence operations
- [X] T033 [P] Add ANSI color support for overdue indicators in src/cli/menu.py
- [X] T034 [P] Update help command to include new functionality in src/cli/menu.py
- [X] T035 [P] Perform integration testing of all advanced features
- [X] T036 [P] Update todos.json format documentation to include new fields
- [X] T037 [P] Add backward compatibility tests in tests/test_advanced_features.py
- [X] T038 [P] Final documentation updates and code cleanup
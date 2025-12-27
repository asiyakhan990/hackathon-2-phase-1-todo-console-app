---

description: "Task list template for feature implementation"
---

# Tasks: Todo-In Memory Python Console App

**Input**: Design documents from `/specs/1-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python 3.13+ project with UV dependencies
- [ ] T003 [P] Configure linting and formatting tools (pylint, black, mypy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create Task data model in src/models/task.py
- [X] T005 [P] Create TodoService in src/services/todo_service.py (handles core business logic)
- [X] T006 [P] Create CLI interface framework in src/cli/main.py
- [X] T007 Create utility functions in src/lib/utils.py (error handling, validation)
- [ ] T008 Configure error handling and logging infrastructure
- [ ] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Implement the ability to add new tasks with required title and optional description

**Independent Test**: Can be fully tested by adding tasks with different titles and descriptions and verifying they appear in the task list with unique IDs and proper status indicators.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Contract test for add command in tests/contract/test_add_command.py
- [X] T011 [P] [US1] Integration test for add user journey in tests/integration/test_add_journey.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Create Task model with validation in src/models/task.py
- [X] T013 [US1] Implement add_task method in src/services/todo_service.py (depends on T012)
- [X] T014 [US1] Implement add command in src/cli/main.py (depends on T013)
- [X] T015 [US1] Add validation and error handling for add command
- [X] T016 [US1] Add logging for add task operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Implement the ability to view all tasks with their IDs, titles, descriptions, and completion status indicators

**Independent Test**: Can be fully tested by adding tasks and then viewing the task list to confirm all tasks are displayed with proper formatting and status indicators.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T017 [P] [US2] Contract test for view command in tests/contract/test_view_command.py
- [ ] T018 [P] [US2] Integration test for view user journey in tests/integration/test_view_journey.py

### Implementation for User Story 2

- [ ] T019 [P] [US2] Create get_all_tasks method in src/services/todo_service.py
- [ ] T020 [US2] Implement view command in src/cli/main.py (depends on T019)
- [ ] T021 [US2] Add proper formatting for task display with status indicators
- [ ] T022 [US2] Handle empty task list scenario

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete/Incomplete (Priority: P2)

**Goal**: Implement the ability to toggle the completion status of a task by its ID

**Independent Test**: Can be fully tested by adding tasks, marking them as complete/incomplete, and verifying the status changes in the task list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T023 [P] [US3] Contract test for mark command in tests/contract/test_mark_command.py
- [ ] T024 [P] [US3] Integration test for mark user journey in tests/integration/test_mark_journey.py

### Implementation for User Story 3

- [ ] T025 [P] [US3] Create toggle_task_status method in src/services/todo_service.py
- [ ] T026 [US3] Implement mark command in src/cli/main.py (depends on T025)
- [ ] T027 [US3] Add validation for task ID existence
- [ ] T028 [US3] Add logging for mark task operations

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Implement the ability to update task details (title and/or description) by its ID

**Independent Test**: Can be fully tested by adding tasks, updating their details, and verifying the changes are reflected in the task list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T029 [P] [US4] Contract test for update command in tests/contract/test_update_command.py
- [ ] T030 [P] [US4] Integration test for update user journey in tests/integration/test_update_journey.py

### Implementation for User Story 4

- [ ] T031 [P] [US4] Create update_task method in src/services/todo_service.py
- [ ] T032 [US4] Implement update command in src/cli/main.py (depends on T031)
- [ ] T033 [US4] Add validation for task ID existence and required fields
- [ ] T034 [US4] Add logging for update task operations

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Implement the ability to delete tasks by its ID with confirmation to prevent accidental deletion

**Independent Test**: Can be fully tested by adding tasks, deleting them, and verifying they no longer appear in the task list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T035 [P] [US5] Contract test for delete command in tests/contract/test_delete_command.py
- [ ] T036 [P] [US5] Integration test for delete user journey in tests/integration/test_delete_journey.py

### Implementation for User Story 5

- [ ] T037 [P] [US5] Create delete_task method in src/services/todo_service.py
- [ ] T038 [US5] Implement delete command with confirmation in src/cli/main.py (depends on T037)
- [ ] T039 [US5] Add validation for task ID existence
- [ ] T040 [US5] Add logging for delete task operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T041 [P] Documentation updates in docs/
- [ ] T042 Code cleanup and refactoring
- [ ] T043 Performance optimization across all stories
- [ ] T044 [P] Additional unit tests (if requested) in tests/unit/
- [ ] T045 Security hardening
- [ ] T046 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add command in tests/contract/test_add_command.py"
Task: "Integration test for add user journey in tests/integration/test_add_journey.py"

# Launch all models for User Story 1 together:
Task: "Create Task model with validation in src/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
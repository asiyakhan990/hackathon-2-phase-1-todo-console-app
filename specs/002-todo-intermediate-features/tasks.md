# Tasks: Todo Console App - Intermediate Level Features

**Input**: Design documents from `/specs/002-todo-intermediate-features/`
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

- [ ] T001 [P] Create project structure with src/, tests/ directories
- [x] T002 [P] Create main application file todo.py in root directory
- [x] T003 Configure linting and formatting tools (if needed)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create Task @dataclass in src/models/task.py with id, description, completed, created_at, priority, tags fields
- [x] T005 [P] Create TaskManager class in src/services/task_manager.py with basic CRUD methods
- [x] T006 Create storage module in src/lib/storage.py for load/save tasks with JSON and migration support
- [x] T007 Create CLI module in src/cli/menu.py for command parsing and menu display
- [x] T008 Implement unique ID generation mechanism in TaskManager
- [x] T009 Implement backward compatibility migration in storage module
- [x] T010 Implement ANSI color utility functions in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Assign Priorities and Tags to Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels (High, Medium, Low) and tags/categories to tasks for better organization and prioritization.

**Independent Test**: Can be fully tested by adding a new task with priority and tags, or updating an existing task to include priority and tags, and then viewing the task to confirm the attributes are properly stored and displayed.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T011 [P] [US1] Unit test for Task model with priority and tags in tests/unit/test_task.py
- [x] T012 [P] [US1] Unit test for TaskManager add_task with priority and tags in tests/unit/test_task_manager.py

### Implementation for User Story 1

- [x] T013 [P] [US1] Update Task model to include priority and tags validation in src/models/task.py
- [x] T014 [US1] Implement add_task method with priority and tags in src/services/task_manager.py
- [x] T015 [US1] Implement update_task method to modify priority and tags in src/services/task_manager.py
- [x] T016 [US1] Update CLI to accept priority and tags for add command in src/cli/menu.py
- [x] T017 [US1] Update CLI to accept priority and tags for update command in src/cli/menu.py
- [x] T018 [US1] Update task display to show priority and tags in src/cli/menu.py
- [x] T019 [US1] Add input validation for priority values (high, medium, low) in src/lib/utils.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Search and Filter Tasks (Priority: P2)

**Goal**: Enable users to search for tasks by keyword and filter tasks by various attributes (status, priority, tags) to quickly find and focus on relevant tasks.

**Independent Test**: Can be fully tested by creating multiple tasks with different attributes, then using search and filter commands to verify that only the expected tasks are returned.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T020 [P] [US2] Unit test for search_tasks functionality in tests/unit/test_task_manager.py
- [x] T021 [P] [US2] Unit test for filter_tasks functionality in tests/unit/test_task_manager.py

### Implementation for User Story 2

- [x] T022 [P] [US2] Implement search_tasks method in src/services/task_manager.py
- [x] T023 [US2] Implement filter_tasks method in src/services/task_manager.py
- [x] T024 [US2] Update CLI to implement search command in src/cli/menu.py
- [x] T025 [US2] Update CLI to implement filter command in src/cli/menu.py
- [x] T026 [US2] Add support for combining multiple filters in filter_tasks method
- [x] T027 [US2] Update task display to work with filtered results in src/cli/menu.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Sort Tasks (Priority: P3)

**Goal**: Enable users to sort tasks by different criteria (priority, creation date, title) in ascending or descending order to view them in a meaningful sequence.

**Independent Test**: Can be fully tested by creating multiple tasks with different attributes, then using sort commands to verify that tasks are displayed in the correct order.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T028 [P] [US3] Unit test for sort_tasks functionality in tests/unit/test_task_manager.py

### Implementation for User Story 3

- [x] T029 [P] [US3] Implement sort_tasks method in src/services/task_manager.py
- [x] T030 [US3] Update CLI to implement sort command in src/cli/menu.py
- [x] T031 [US3] Add support for different sort criteria (priority, creation date, title) in sort_tasks method
- [x] T032 [US3] Add support for ascending/descending order in sort_tasks method
- [x] T033 [US3] Update task display to work with sorted results in src/cli/menu.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T034 [P] Update main application entry point in todo.py to integrate all components
- [x] T035 [P] Documentation updates in README.md for new features
- [x] T036 Code cleanup and refactoring
- [x] T037 Performance optimization for search/filter/sort operations
- [x] T038 [P] Additional unit tests in tests/unit/
- [x] T039 Error handling improvements across all modules
- [x] T040 Run quickstart.md validation scenarios

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

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
Task: "Unit test for Task model with priority and tags in tests/unit/test_task.py"
Task: "Unit test for TaskManager add_task with priority and tags in tests/unit/test_task_manager.py"

# Launch all models for User Story 1 together:
Task: "Update Task model to include priority and tags validation in src/models/task.py"
Task: "Implement add_task method with priority and tags in src/services/task_manager.py"
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
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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
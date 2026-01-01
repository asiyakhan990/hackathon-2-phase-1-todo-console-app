# Feature Specification: Advanced Level Features for the Evolution of Todo – Phase I: Todo In-Memory Python Console App

**Feature Branch**: `001-advanced-todo-features`
**Created**: January 1, 2026
**Status**: Draft
**Input**: User description: "Advanced Level Features for the Evolution of Todo – Phase I: Todo In-Memory Python Console App Target audience: Hackathon judges evaluating advanced spec-driven development, and developers pushing a console-based todo app toward intelligent productivity features using Spec-Kit Plus and Qwen AI. Focus: Define precise, implementable specifications for the Advanced Level features only, building directly on the completed Basic and Intermediate levels. These intelligent enhancements are Recurring Tasks (auto-rescheduling repeating tasks) and Due Dates & Time Reminders (with overdue indicators and prominent display). The app remains a pure in-memory Python console application with no external dependencies, no GUI, and no browser notifications (adapted to a console-only environment). Success Criteria: Extends the existing Task model to support recurrence rules and a due_date field with basic parsing and validation. Implements recurring task logic: upon marking a recurring task as complete, automatically generate the next instance (e.g., daily → next day, weekly → +7 days). Handles due dates: store as a string in "YYYY-MM-DD" format, display overdue tasks prominently (e.g., with an [OVERDUE] marker), and sort overdue tasks to the top by default. Provides new console commands or sub-commands for setting recurrence and due dates, with clear user feedback. Generates a Markdown file (v3_advanced.spec.md) placed in specs_history/, fully ready for immediate code generation via Qwen. All features are modular, backward-compatible with existing non-recurring tasks, and manually testable via the console. A reader (e.g., Qwen code generator) can implement intelligent behavior solely from this spec while maintaining console-only constraints. Constraints: Format: Markdown with structured sections (Metadata, Data Model Extensions, Recurrence Rules, Due Date Handling, New/Updated Commands, Feature Details with User Stories & Acceptance Criteria, Console Interaction Examples, Overdue Logic, Error Handling, Backward Compatibility, Acceptance Tests). Version: v3.0 (Advanced Level), include the current date (January 1, 2026). Dependencies: Strictly limited to the Python standard library only (use datetime from the standard library for date calculations; no external packages). Keep specs detailed yet focused (under 2200 words). Reference the existing constitution.md (latest version) and previous specs (Basic and Intermediate) without modifying them. Timeline: Generate immediately to enable rapid Advanced Level completion within hours via AI-assisted coding. Console-only limitations: No browser notifications or GUI pickers—use text input for dates (format "YYYY-MM-DD"), simple prompts for recurrence frequency (daily/weekly/monthly), and console output for reminders and overdue alerts. Recurrence frequencies supported: daily, weekly, monthly only (keep it simple). Due dates: Optional; no time component (date-only for simplicity). Specific Feature Requirements 1. Recurring Tasks Support recurrence frequency: "daily", "weekly", "monthly", or None. When marking a recurring task as complete, automatically create a new task instance with the next due date (e.g., weekly → add 7 days). Preserve title, description, priority, and tags across instances. Allow setting recurrence during task addition or via an update sub-command. 2. Due Dates & Overdue Indicators Due date format: "YYYY-MM-DD" (validated on input). Display overdue tasks with a prominent marker (e.g., [OVERDUE] in red if ANSI is supported, otherwise bold text). Default sort order: overdue tasks first, then by due date in ascending order. Show "days overdue" or "Due today" indicators in the list view. Friendly input prompts with examples and re-prompting on invalid date input. Not Building: Actual Python code implementation (reserved for Qwen code generation). Browser notifications, desktop alerts, or sound reminders (not possible in a pure console environment). Complex recurrence patterns (e.g., "every 2 weeks," custom RRULEs, or end dates). Time-based reminders (hours/minutes) or calendar integration. Persistent storage across sessions or file export. Statistics dashboards or streak tracking (scope intentionally limited to these two features only)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create Recurring Tasks (Priority: P1)

As a user of the todo console app, I want to create recurring tasks so that I don't have to manually re-add routine tasks like daily exercise, weekly cleaning, or monthly bill payments.

**Why this priority**: This is the core functionality that differentiates the app from basic todo apps, providing significant value through automation.

**Independent Test**: Can be fully tested by creating a recurring task and marking it as complete, verifying that a new instance appears with the appropriate next recurrence date.

**Acceptance Scenarios**:

1. **Given** I am using the todo app, **When** I add a task with a recurrence frequency (daily/weekly/monthly), **Then** the task is created with the specified recurrence rule
2. **Given** I have a recurring task, **When** I mark it as complete, **Then** a new instance of the task is automatically created with the next recurrence date

---

### User Story 2 - Set and View Due Dates (Priority: P1)

As a user of the todo console app, I want to set due dates for my tasks so that I can prioritize time-sensitive activities and see which tasks are overdue.

**Why this priority**: This provides essential time management functionality that helps users prioritize their work and avoid missing deadlines.

**Independent Test**: Can be fully tested by creating tasks with due dates, verifying they appear in the correct order, and confirming overdue tasks are prominently marked.

**Acceptance Scenarios**:

1. **Given** I am using the todo app, **When** I add a task with a due date, **Then** the task is created with the specified due date in "YYYY-MM-DD" format
2. **Given** I have tasks with due dates, **When** I view the task list, **Then** overdue tasks appear at the top with [OVERDUE] markers

---

### User Story 3 - Manage Recurring Tasks (Priority: P2)

As a user of the todo console app, I want to update or remove recurrence settings from existing tasks so that I can modify my recurring responsibilities as needed.

**Why this priority**: This provides flexibility to adapt recurring tasks to changing needs without having to delete and recreate tasks.

**Independent Test**: Can be fully tested by modifying an existing recurring task to change its frequency or disable recurrence.

**Acceptance Scenarios**:

1. **Given** I have a recurring task, **When** I update its recurrence settings, **Then** the changes apply to future instances of the task
2. **Given** I have a recurring task, **When** I disable its recurrence, **Then** completing it no longer creates a new instance

---

### User Story 4 - View Overdue Task Indicators (Priority: P2)

As a user of the todo console app, I want to clearly see which tasks are overdue so that I can prioritize them appropriately.

**Why this priority**: This provides visual clarity about urgent tasks that need immediate attention.

**Independent Test**: Can be fully tested by creating tasks with past due dates and verifying they display with prominent overdue indicators.

**Acceptance Scenarios**:

1. **Given** I have tasks with due dates in the past, **When** I view the task list, **Then** these tasks appear with [OVERDUE] markers
2. **Given** I have overdue tasks, **When** I view the task list, **Then** they are sorted at the top of the list

---

### Edge Cases

- What happens when a recurring task is marked as complete on the due date?
- How does the system handle invalid date formats when setting due dates?
- What happens when a recurring task has a due date and the next instance would have a past due date?
- How does the system handle leap years and month-end dates when calculating recurrence?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST extend the existing Task model to support recurrence rules with frequencies: daily, weekly, monthly, or None
- **FR-002**: System MUST support due_date field in "YYYY-MM-DD" format with basic parsing and validation
- **FR-003**: System MUST automatically generate a new task instance when a recurring task is marked as complete
- **FR-004**: System MUST preserve title, description, priority, and tags when creating new recurring task instances
- **FR-005**: System MUST display overdue tasks with a prominent marker (e.g., [OVERDUE])
- **FR-006**: System MUST sort overdue tasks to the top by default, followed by due date in ascending order
- **FR-007**: System MUST show "days overdue" or "Due today" indicators in the list view
- **FR-008**: System MUST provide new console commands or sub-commands for setting recurrence and due dates
- **FR-009**: System MUST be backward-compatible with existing non-recurring tasks
- **FR-010**: System MUST validate date input in "YYYY-MM-DD" format with re-prompting on invalid input
- **FR-011**: System MUST calculate next recurrence dates correctly accounting for month boundaries and leap years
- **FR-012**: System MUST handle all operations in-memory without persistent storage across sessions
- **FR-013**: System MUST use only Python standard library for date calculations (no external packages)

### Key Entities

- **Task**: Represents a todo item with title, description, priority, tags, optional due date, and optional recurrence rule
- **RecurrenceRule**: Defines how a task repeats (daily, weekly, monthly, or None) with associated interval calculations
- **DueDate**: A date value in "YYYY-MM-DD" format that determines task urgency and sorting order

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create recurring tasks with daily, weekly, or monthly frequencies that automatically generate new instances when completed
- **SC-002**: Users can set due dates for tasks in "YYYY-MM-DD" format with proper validation and error handling
- **SC-003**: Overdue tasks are prominently displayed with [OVERDUE] markers and sorted to the top of the list
- **SC-004**: All new features are implemented using only Python standard library without external dependencies
- **SC-005**: The specification document is under 2200 words and contains all required structured sections
- **SC-006**: All new functionality is backward-compatible with existing non-recurring tasks
- **SC-007**: The console interface provides clear feedback when setting recurrence and due dates

# Research: Advanced Todo Features Implementation

## Decision: Task Model Extension
**Rationale**: The existing Task model needs to be extended to support recurrence and due_date fields as specified in the feature requirements.
**Alternatives considered**: 
- Separate models for recurring vs. non-recurring tasks (rejected - would complicate backward compatibility)
- Adding these fields as separate data structures (rejected - would complicate the codebase)

## Decision: Date Handling Approach
**Rationale**: Using string storage for due_date ("YYYY-MM-DD") with datetime parsing for calculations aligns with the spec requirements and provides flexibility for display and validation.
**Alternatives considered**:
- Storing as datetime objects directly (rejected - would complicate JSON serialization)
- Using custom date format (rejected - "YYYY-MM-DD" is standard and clear)

## Decision: Recurrence Implementation
**Rationale**: Creating new task instances when recurring tasks are completed preserves history and aligns with user expectations of recurring tasks.
**Alternatives considered**:
- Reusing the same task with updated due date (rejected - would lose completion history)
- Soft-deleting and recreating (rejected - would complicate ID management)

## Decision: Overdue Task Display
**Rationale**: Using [OVERDUE] markers with default sorting of overdue tasks first provides clear visibility for urgent tasks.
**Alternatives considered**:
- Color coding only (rejected - might not be visible in all terminals)
- Different list views (rejected - would complicate UX)

## Current Codebase Analysis
- The main application is in todo.py
- Tasks are likely stored in a dataclass with JSON serialization
- Need to examine current command structure to add new functionality
- Need to understand current storage format in todos.json

## Date Calculation Strategy
- Use datetime.date for parsing and calculations
- For daily recurrence: add timedelta(days=1)
- For weekly recurrence: add timedelta(days=7)
- For monthly recurrence: add approximately 30 days or handle month boundaries properly
- Need to consider leap years and month-end dates for accurate calculations
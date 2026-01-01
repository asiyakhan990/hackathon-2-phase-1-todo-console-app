# Quickstart Guide: Advanced Todo Features Implementation

## Overview
This guide provides step-by-step instructions for implementing the Advanced Level features (Recurring Tasks and Due Dates & Overdue Indicators) in the Todo Console Application.

## Prerequisites
- Python 3.9+ installed
- Understanding of the existing codebase structure
- Familiarity with the existing Task model and CLI commands

## Implementation Steps

### Step 1: Extend the Task Model
1. Update the Task dataclass in `src/models/task.py` to include `due_date` and `recurrence` fields
2. Add validation for the new fields in the `__post_init__` method
3. Add helper methods for date validation and recurrence calculations

### Step 2: Create Date Utilities Module
1. Create `src/lib/date_utils.py` for date-related functions:
   - Date validation in "YYYY-MM-DD" format
   - Date comparison with today's date
   - Date addition for recurrence calculations (daily, weekly, monthly)

### Step 3: Update Task Manager
1. Modify the TaskManager class in `src/services/task_manager.py` to:
   - Support adding due dates and recurrence when creating tasks
   - Handle recurring task logic when marking tasks as complete
   - Sort tasks with overdue tasks appearing first

### Step 4: Update CLI Commands
1. Enhance the add command to accept due date and recurrence options
2. Add update command functionality for modifying due dates and recurrence
3. Update the list command to display due dates and overdue indicators
4. Modify the complete command to handle recurring tasks

### Step 5: Update Display Formatting
1. Modify the display functions to show due date information
2. Add [OVERDUE] markers for overdue tasks
3. Implement the "Due today" and "X days overdue" indicators

### Step 6: Add Input Validation
1. Implement date validation with re-prompting for invalid input
2. Add recurrence option validation
3. Provide helpful error messages and examples

### Step 7: Testing
1. Create tests for the new functionality in the tests directory
2. Verify backward compatibility with existing tasks
3. Test all recurrence scenarios (daily, weekly, monthly)
4. Test due date functionality and overdue detection

## Key Implementation Points

### Date Calculations
- Use Python's `datetime` module for all date operations
- For monthly recurrence, add approximately 30 days (or handle month boundaries properly)
- Always validate date strings are in "YYYY-MM-DD" format

### Recurrence Logic
- When a recurring task is completed, create a new task with the next due date
- Preserve all original task properties (title, description, priority, tags)
- Calculate the next due date based on the recurrence frequency

### Overdue Detection
- Compare due dates with the current date
- Sort tasks so overdue tasks appear first
- Display clear indicators for overdue tasks

## Running the Application
After implementation, run the application with:
```bash
python todo.py
```

## Testing the Features
1. Add a recurring task: `add "Buy groceries" --recurrence weekly --due-date 2026-01-07`
2. Add a task with a due date: `add "Submit report" --due-date 2026-01-05`
3. List tasks to see due date indicators: `list`
4. Complete a recurring task and verify a new instance is created: `complete 1`
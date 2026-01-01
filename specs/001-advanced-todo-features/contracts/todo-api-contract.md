# API Contracts: Advanced Todo Features

## Overview
This document defines the API contracts for the new advanced features in the Todo Console Application, specifically for recurring tasks and due date functionality.

## Command Interface Contracts

### Add Command Extension
**Command**: `add <description> [--due-date YYYY-MM-DD] [--recurrence daily|weekly|monthly]`

**Request**:
- `description`: Task description (required)
- `--due-date`: Due date in YYYY-MM-DD format (optional)
- `--recurrence`: Recurrence frequency (optional, one of: daily, weekly, monthly)

**Response**:
- Success: "Task added successfully with ID <id>"
- Error: Appropriate error message with validation details

**Validation**:
- Due date must be in valid YYYY-MM-DD format
- Recurrence must be one of: daily, weekly, monthly
- If both due date and recurrence are provided, the next instance will have an updated due date

### Update Command Extension
**Command**: `update <id> [--due-date YYYY-MM-DD] [--recurrence daily|weekly|monthly|none]`

**Request**:
- `id`: Task ID to update (required)
- `--due-date`: New due date in YYYY-MM-DD format (optional)
- `--recurrence`: New recurrence frequency or 'none' to disable (optional)

**Response**:
- Success: "Task <id> updated successfully"
- Error: Appropriate error message with validation details

**Validation**:
- Task ID must exist
- Due date must be in valid YYYY-MM-DD format
- Recurrence must be one of: daily, weekly, monthly, none

### List Command Enhancement
**Command**: `list`

**Response**:
- List of tasks with additional due date and recurrence information:
  - Tasks with due dates show: "Due: YYYY-MM-DD"
  - Overdue tasks show: "[OVERDUE] Due: YYYY-MM-DD" and appear at the top
  - Tasks due today show: "Due: Today"
  - Recurring tasks show: "[RECUR: frequency]"
  - Tasks with both show: "[OVERDUE] [RECUR: weekly] Due: 2025-12-25"

### Complete Command Enhancement
**Command**: `complete <id>`

**Request**:
- `id`: Task ID to mark as complete (required)

**Response**:
- For non-recurring tasks: "Task <id> marked as complete"
- For recurring tasks: "Task <id> marked as complete. Next instance created with ID <new_id> and due date YYYY-MM-DD"
- Error: Appropriate error message if task doesn't exist

**Behavior**:
- If the task has recurrence, a new instance is created with updated due date
- The new instance preserves title, description, priority, and tags
- The original task is marked as completed

## Data Model Contracts

### Task Object
```json
{
  "id": "integer, unique identifier",
  "description": "string, task description",
  "completed": "boolean, completion status",
  "created_at": "string, date in YYYY-MM-DD format",
  "priority": "string | null, one of: 'high', 'medium', 'low', or null",
  "tags": "array of strings, task tags",
  "due_date": "string | null, date in YYYY-MM-DD format or null",
  "recurrence": "string | null, one of: 'daily', 'weekly', 'monthly', or null"
}
```

### Validation Rules
- `due_date` must be in "YYYY-MM-DD" format if provided
- `recurrence` must be one of "daily", "weekly", "monthly" if provided
- `priority` must be one of "high", "medium", "low" or null if provided
- `tags` must be an array of non-empty strings

## Error Response Format
```json
{
  "error": "string, error message",
  "code": "string, error code"
}
```

## Success Response Format
```json
{
  "success": "boolean, true for successful operations",
  "message": "string, success message",
  "data": "object | array | null, optional returned data"
}
```
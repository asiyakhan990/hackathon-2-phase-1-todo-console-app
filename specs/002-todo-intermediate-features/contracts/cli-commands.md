# CLI Command Contracts: Todo Console App - Intermediate Level Features

## Command Interface Specification

This document specifies the command-line interface contracts for the Todo Console Application with intermediate level features.

## Commands

### Add Task
- **Command**: `add "description" ["priority"] ["tags"]`
- **Aliases**: `a`
- **Description**: Add a new task with optional priority and tags
- **Parameters**:
  - `description` (required): Task description in quotes
  - `priority` (optional): "high", "medium", "low" (defaults to "medium")
  - `tags` (optional): Comma-separated tags in quotes (e.g., "work,urgent")
- **Output**: Task added with ID: [ID]
- **Error cases**: Invalid priority value, empty description

### View Tasks
- **Command**: `view` or `v`
- **Description**: Display all tasks with priority and tags
- **Output**: Formatted table with ID, status, priority, tags, and description
- **Error cases**: No tasks available

### Update Task
- **Command**: `update [id] ["description"] ["priority"] ["tags"]`
- **Aliases**: `u`
- **Description**: Update an existing task's properties
- **Parameters**:
  - `id` (required): Task ID to update
  - `description` (optional): New description
  - `priority` (optional): New priority
  - `tags` (optional): New tags as comma-separated values
- **Output**: Task [ID] updated successfully
- **Error cases**: Task ID not found, invalid priority value

### Delete Task
- **Command**: `delete [id]`
- **Aliases**: `d`
- **Description**: Delete a task by ID with confirmation
- **Parameters**:
  - `id` (required): Task ID to delete
- **Output**: Task [ID] deleted successfully
- **Error cases**: Task ID not found

### Mark Task
- **Command**: `mark [id]`
- **Aliases**: `m`
- **Description**: Toggle task completion status
- **Parameters**:
  - `id` (required): Task ID to mark
- **Output**: Task [ID] marked as [complete/incomplete]
- **Error cases**: Task ID not found

### Search Tasks
- **Command**: `search "keyword"`
- **Aliases**: `s`
- **Description**: Search tasks by keyword in description or tags
- **Parameters**:
  - `keyword` (required): Search term in quotes
- **Output**: Formatted table of matching tasks
- **Error cases**: No matches found

### Filter Tasks
- **Command**: `filter [status] [priority] [tag]`
- **Aliases**: `f`
- **Description**: Filter tasks by status, priority, or tag
- **Parameters**:
  - `status` (optional): "active", "completed", "all"
  - `priority` (optional): "high", "medium", "low"
  - `tag` (optional): Specific tag to filter by
- **Output**: Formatted table of filtered tasks
- **Error cases**: No matches found

### Sort Tasks
- **Command**: `sort [by] [order]`
- **Aliases**: `o`
- **Description**: Sort tasks by specified criteria
- **Parameters**:
  - `by` (optional): "priority", "alpha", "created" (default: priority)
  - `order` (optional): "asc", "desc" (default: desc for priority, asc for others)
- **Output**: Formatted table of sorted tasks
- **Error cases**: Invalid sort criteria

### Help
- **Command**: `help` or `h`
- **Description**: Display help information
- **Output**: List of available commands with descriptions

### Exit
- **Command**: `exit` or `q`
- **Description**: Exit the application
- **Output**: Goodbye message
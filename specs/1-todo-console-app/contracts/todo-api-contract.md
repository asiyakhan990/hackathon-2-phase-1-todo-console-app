# Todo Application API Contract

## Overview
This document describes the interface for the Todo Console Application. Since this is a console application, the "API" refers to the command interface and expected behaviors.

## Commands

### Add Task
- **Command**: `add "title" "optional description"`
- **Description**: Creates a new task with the given title and optional description
- **Parameters**:
  - title (required): String, the task title
  - description (optional): String, the task description
- **Response**: Task added with ID: [id]
- **Errors**: 
  - If title is empty: "Error: Title is required for tasks"
  - If invalid format: "Error: Invalid command format"

### View Tasks
- **Command**: `view`
- **Description**: Displays all tasks with their ID, status, title, and description
- **Response**: Formatted list of all tasks with [ ] for incomplete and [x] for complete
- **Errors**: If no tasks exist: "No tasks in the list"

### Update Task
- **Command**: `update [id] "new title" "new description"`
- **Description**: Updates the title and description of an existing task
- **Parameters**:
  - id (required): Integer, the task ID
  - new title (required): String, the new task title
  - new description (optional): String, the new task description
- **Response**: Task [id] updated successfully
- **Errors**:
  - If task doesn't exist: "Error: Task with ID [id] not found"
  - If invalid format: "Error: Invalid command format"

### Delete Task
- **Command**: `delete [id]`
- **Description**: Removes a task by its ID with confirmation
- **Parameters**:
  - id (required): Integer, the task ID
- **Response**: Task [id] deleted successfully
- **Errors**: If task doesn't exist: "Error: Task with ID [id] not found"

### Mark Task
- **Command**: `mark [id]`
- **Description**: Toggles the completion status of a task
- **Parameters**:
  - id (required): Integer, the task ID
- **Response**: Task [id] marked as [complete/incomplete]
- **Errors**: If task doesn't exist: "Error: Task with ID [id] not found"

### Exit
- **Command**: `exit`
- **Description**: Exits the application
- **Response**: Application terminates
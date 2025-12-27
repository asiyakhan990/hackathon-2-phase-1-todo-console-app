# Data Model: Todo-In Memory Python Console App

## Task Entity

### Attributes
- **id**: Integer, unique identifier for the task, starting from 1 and incrementing
- **title**: String, required title of the task
- **description**: String, optional description of the task (can be empty)
- **complete**: Boolean, indicates whether the task is completed (false by default)

### Validation Rules
- ID must be a positive integer
- Title must be a non-empty string
- Description can be any string (including empty)
- Complete status must be a boolean value

### State Transitions
- A task starts with `complete = False`
- The `complete` status can be toggled between `True` and `False`

## Todo List Container

### Attributes
- **tasks**: List of Task entities, maintains all tasks in the application
- **next_id**: Integer, tracks the next available ID for new tasks

### Operations
- Add a new Task to the list
- Remove a Task from the list by ID
- Update Task details by ID
- Retrieve all Tasks
- Toggle Task completion status by ID
# Data Model: Todo Console App - Intermediate Level Features

## Task Entity

The Task entity is extended from the basic implementation to include additional fields for priorities and tags.

### Fields

- **id** (int): Unique identifier for the task; persistent across sessions
- **description** (str): The task description/text
- **completed** (bool): Whether the task is completed or not
- **created_at** (str): Creation date in "YYYY-MM-DD" format
- **priority** (str | None): Priority level - "high", "medium", "low", or None
- **tags** (list[str]): List of tags associated with the task; defaults to empty list

### Validation Rules

- **id**: Must be a positive integer; unique across all tasks
- **description**: Required field; cannot be empty or None
- **completed**: Boolean value only (True/False)
- **created_at**: Must be in valid "YYYY-MM-DD" format
- **priority**: Must be one of "high", "medium", "low", or None
- **tags**: Must be a list of strings; individual tags cannot be empty

### Default Values

- **priority**: Defaults to "medium" when not specified
- **tags**: Defaults to empty list [] when not specified

### State Transitions

- A task can transition from incomplete to complete and vice versa
- Priority can be updated after creation
- Tags can be added, removed, or replaced after creation
- Description can be updated after creation

## TaskManager Entity

The TaskManager entity handles all operations related to tasks.

### Methods

- **add_task(description, priority=None, tags=None)**: Creates a new task with a unique ID
- **get_task(task_id)**: Retrieves a specific task by ID
- **update_task(task_id, description=None, priority=None, tags=None, completed=None)**: Updates task properties
- **delete_task(task_id)**: Removes a task by ID
- **get_all_tasks()**: Returns all tasks
- **search_tasks(keyword)**: Returns tasks matching the keyword in description or tags
- **filter_tasks(status=None, priority=None, tag=None)**: Returns tasks matching filter criteria
- **sort_tasks(tasks, by="priority", order="desc")**: Returns tasks sorted by specified criteria
- **load_tasks()**: Loads tasks from JSON file with migration support
- **save_tasks()**: Saves tasks to JSON file

## Migration Support

The system supports migration of older basic task formats by:

- Adding missing fields with default values
- Preserving existing data
- Maintaining backward compatibility
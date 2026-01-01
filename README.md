# Todo Console Application

A simple in-memory todo console application built with Python, enhanced with intermediate and advanced features.

## Features

### Basic Features
- Add new tasks with title and optional description
- View all tasks with their status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete

### Intermediate Features
- **Priorities**: Assign priority levels (High, Medium, Low) to tasks
- **Tags**: Add tags/categories to tasks for better organization
- **Search**: Search tasks by keyword in description or tags
- **Filter**: Filter tasks by status, priority, or tag
- **Sort**: Sort tasks by priority, creation date, or title in ascending/descending order
- **Colored Output**: Enhanced visual display with ANSI color codes

### Advanced Level Complete
- **Recurring Tasks**: Auto-schedule repeating tasks (daily, weekly, monthly)
- **Due Dates**: Set due dates for tasks in YYYY-MM-DD format
- **Overdue Indicators**: Prominent display of overdue tasks with [OVERDUE] markers
- **Smart Sorting**: Overdue tasks appear at the top, followed by due date order
- **Date Validation**: Robust validation with re-prompting for invalid dates

## Requirements

- Python 3.9+
- UV package manager (optional)

## Setup

1. Clone the repository
2. (Optional) Create a virtual environment:
   ```bash
   uv venv  # or python -m venv venv && source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
   ```
3. Install dependencies (if any are added in the future)

## Usage

Run the application:
```bash
python todo.py
```

### Commands

- `add "description" ["priority"] ["tags"]` - Add a new task with optional priority and tags
- `add "description" --due-date YYYY-MM-DD --recurrence daily|weekly|monthly` - Add a recurring task with due date
- `view` - View all tasks with priority and tags
- `update [id] ["description"] ["priority"] ["tags"]` - Update a task's properties
- `update [id] --due-date YYYY-MM-DD --recurrence daily|weekly|none` - Update due date and recurrence settings
- `delete [id]` - Delete a task (with confirmation)
- `mark [id]` - Toggle task completion status (creates new instance for recurring tasks)
- `search "keyword"` - Search tasks by keyword in description or tags
- `filter [status] [priority] [tag]` - Filter tasks by status, priority, or tag
- `sort [by] [order]` - Sort tasks by criteria (priority/alpha/created) and order (asc/desc)
- `help` - Show help information
- `exit` - Exit the application

### Example

```
> add "Buy groceries" --recurrence weekly --due-date 2026-01-07
Task added with ID: 1

> add "Submit report" --due-date 2026-01-05
Task added with ID: 2

> add "Call mom" "low" "personal"
Task added with ID: 3

> view
ID | Status | Priority | Due Date        | Description
---|--------|----------|-----------------|------------------
2  | [ ]    | ★★ MED   | [OVERDUE] Due: 2026-01-05 (2 days overdue) | Submit report
1  | [ ]    | ★★ MED   | Due: 2026-01-07 [RECUR: weekly] | Buy groceries
3  | [ ]    | ★ LOW    |                 | Call mom

> mark 1
Task 1 marked as complete. Next instance created with ID 4 and due date 2026-01-14

> exit
Goodbye!
```

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── task_manager.py  # Core business logic
├── cli/
│   └── menu.py          # CLI interface and main application
└── lib/
    ├── storage.py       # File storage and migration logic
    ├── utils.py         # Utility functions
    └── date_utils.py    # Date-related functions
```

## Architecture

The application follows a clean architecture pattern:

- **Models**: Define the data structures (Task)
- **Services**: Contain the business logic (TaskManager)
- **CLI**: Handle user interaction and command parsing
- **Lib**: Common utilities and helpers
- **Storage**: Handle file operations and data persistence
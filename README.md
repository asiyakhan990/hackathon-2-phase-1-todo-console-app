# Todo Console Application

A simple in-memory todo console application built with Python.

## Features

- Add new tasks with title and optional description
- View all tasks with their status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete

## Requirements

- Python 3.13+
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
python src/cli/main.py
```

### Commands

- `add "title" ["description"]` - Add a new task
- `view` - View all tasks
- `update id "title" ["description"]` - Update a task
- `delete id` - Delete a task (with confirmation)
- `mark id` - Toggle task completion status
- `help` - Show help information
- `exit` - Exit the application

### Example

```
> add "Buy groceries" "Milk, bread, eggs"
Task added with ID: 1

> add "Finish report"
Task added with ID: 2

> view
Task List:
1. [ ] Buy groceries - Milk, bread, eggs
2. [ ] Finish report

> mark 2
Task 2 marked as complete

> view
Task List:
1. [ ] Buy groceries - Milk, bread, eggs
2. [x] Finish report

> exit
Goodbye!
```

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── todo_service.py  # Core business logic
├── cli/
│   └── main.py          # CLI interface and main application
└── lib/
    └── utils.py         # Utility functions
```

## Architecture

The application follows a clean architecture pattern:

- **Models**: Define the data structures (Task)
- **Services**: Contain the business logic (TodoService)
- **CLI**: Handle user interaction and command parsing
- **Lib**: Common utilities and helpers
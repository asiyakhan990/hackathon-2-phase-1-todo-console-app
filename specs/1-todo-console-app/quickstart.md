# Quickstart Guide: Todo-In Memory Python Console App

## Setup

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if not already installed:
   ```bash
   pip install uv
   ```
3. Navigate to the project directory
4. Create a virtual environment:
   ```bash
   uv venv
   ```
5. Activate the virtual environment:
   ```bash
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

## Running the Application

1. Navigate to the project root directory
2. Run the application:
   ```bash
   python src/cli/main.py
   ```

## Using the Application

Once the application is running, you can use the following commands:

- `add "task title" "optional description"` - Add a new task
- `view` - View all tasks with their status
- `update <id> "new title" "new description"` - Update an existing task
- `delete <id>` - Delete a task by ID
- `mark <id>` - Toggle the completion status of a task
- `exit` - Exit the application

### Example Usage

```
> add "Buy groceries" "Milk, bread, eggs"
Task added with ID: 1

> add "Finish report" 
Task added with ID: 2

> view
1. [ ] Buy groceries - Milk, bread, eggs
2. [x] Finish report

> mark 2
Task 2 marked as complete

> view
1. [ ] Buy groceries - Milk, bread, eggs
2. [x] Finish report

> update 1 "Buy groceries" "Milk, bread, eggs, fruits"
Task 1 updated successfully

> delete 1
Are you sure you want to delete task 1? (y/n): y
Task 1 deleted successfully

> exit
```

## Troubleshooting

- If you get a "command not found" error, make sure your virtual environment is activated
- If the application crashes, check that you're providing the correct arguments to each command
- For "task not found" errors, verify the task ID exists by using the `view` command first
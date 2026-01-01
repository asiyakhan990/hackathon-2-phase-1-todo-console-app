# Quickstart Guide: Todo Console App - Intermediate Level Features

## Getting Started

The Todo Console Application with intermediate level features provides enhanced task management capabilities including priorities, tags, search, filter, and sort functionality.

## Prerequisites

- Python 3.9 or higher
- No external dependencies required (pure standard library)

## Running the Application

1. Ensure you have Python 3.9+ installed
2. Navigate to the project directory
3. Run the application:
   ```bash
   python todo.py
   ```

## Basic Usage

Once the application is running, you'll see a menu with available commands. Here are the most common operations:

### Adding Tasks
- Add a basic task: `add "Buy groceries"`
- Add a task with priority: `add "Finish report" "high"`
- Add a task with priority and tags: `add "Team meeting" "medium" "work,important"`

### Viewing Tasks
- View all tasks: `view` or `v`
- Tasks are displayed in a table format with ID, status, priority, tags, and description

### Updating Tasks
- Update a task: `update 1 "New description" "low" "personal"`
- You can update any combination of description, priority, and tags

### Marking Tasks as Complete
- Toggle completion status: `mark 1` or `m 1`

### Searching Tasks
- Search for tasks containing a keyword: `search "report"` or `s "report"`

### Filtering Tasks
- Filter by status: `filter active`
- Filter by priority: `filter "" high`
- Filter by tag: `filter "" "" work`
- Combine filters: `filter completed high`

### Sorting Tasks
- Sort by priority (default): `sort`
- Sort by title: `sort alpha`
- Sort by creation date: `sort created`
- Change sort order: `sort priority asc`

## Command Reference

| Command | Alias | Description |
|---------|-------|-------------|
| `add "desc" ["prio"] ["tags"]` | `a` | Add a new task |
| `view` | `v` | View all tasks |
| `update [id] ["desc"] ["prio"] ["tags"]` | `u` | Update a task |
| `delete [id]` | `d` | Delete a task |
| `mark [id]` | `m` | Toggle task completion |
| `search "keyword"` | `s` | Search tasks |
| `filter [status] [prio] [tag]` | `f` | Filter tasks |
| `sort [by] [order]` | `o` | Sort tasks |
| `help` | `h` | Show help |
| `exit` | `q` | Exit application |

## Data Persistence

Tasks are automatically saved to `todos.json` in the current directory. The application supports backward compatibility with older basic todo files, automatically migrating them to include the new fields (priority, tags) with appropriate defaults.

## Example Workflow

1. Add some tasks:
   ```
   > add "Buy milk" "medium" "shopping"
   Task added with ID: 1
   
   > add "Finish project" "high" "work,important"
   Task added with ID: 2
   
   > add "Call mom" "low" "personal"
   Task added with ID: 3
   ```

2. View your tasks:
   ```
   > view
   ID | Status | Priority | Tags           | Description
   ---|--------|----------|----------------|------------------
   1  | [ ]    | ★★ MED   | shopping       | Buy milk
   2  | [ ]    | ★★★ HIGH | work,important | Finish project
   3  | [ ]    | ★ LOW    | personal       | Call mom
   ```

3. Filter high priority tasks:
   ```
   > filter "" high ""
   ID | Status | Priority | Tags           | Description
   ---|--------|----------|----------------|------------------
   2  | [ ]    | ★★★ HIGH | work,important | Finish project
   ```

4. Search for tasks:
   ```
   > search "project"
   ID | Status | Priority | Tags           | Description
   ---|--------|----------|----------------|------------------
   2  | [ ]    | ★★★ HIGH | work,important | Finish project
   ```

## Troubleshooting

- If you encounter issues with ANSI colors not displaying properly, ensure your terminal supports color codes
- If the application fails to start, verify Python 3.9+ is installed
- For data corruption issues, check the `todos.json` file format
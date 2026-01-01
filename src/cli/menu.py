import re
from typing import List
from src.services.task_manager import TaskManager
from src.lib.storage import load_tasks_from_file, save_tasks_to_file
from src.models.task import Task
from src.lib.utils import format_task_with_colors, print_colored_table
from src.lib.date_utils import validate_date_format, format_due_date_display


class Menu:
    """
    Handles command parsing and menu display for the Todo Console Application.
    """

    def __init__(self):
        self.task_manager = TaskManager()
        self.running = True
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from storage."""
        self.task_manager.load_tasks()
        # Update next_id based on loaded tasks
        if self.task_manager.tasks:
            self.task_manager.next_id = max(task.id for task in self.task_manager.tasks) + 1
        else:
            self.task_manager.next_id = 1

    def save_tasks(self):
        """Save tasks to storage."""
        self.task_manager.save_tasks()

    def run(self):
        """Main loop for the menu."""
        while self.running:
            try:
                command = input("> ").strip()
                if command:
                    self.process_command(command)
            except KeyboardInterrupt:
                print("\nExiting...")
                self.running = False
            except EOFError:
                print("\nExiting...")
                self.running = False

    def process_command(self, command: str):
        """Process a command from the user."""
        parts = command.split()
        if not parts:
            return

        cmd = parts[0].lower()

        if cmd in ['add', 'a']:
            self.handle_add(parts[1:])
        elif cmd in ['view', 'v']:
            self.handle_view()
        elif cmd in ['update', 'u']:
            self.handle_update(parts[1:])
        elif cmd in ['delete', 'd']:
            self.handle_delete(parts[1:])
        elif cmd in ['mark', 'm']:
            self.handle_mark(parts[1:])
        elif cmd in ['search', 's']:
            self.handle_search(parts[1:])
        elif cmd in ['filter', 'f']:
            self.handle_filter(parts[1:])
        elif cmd in ['sort', 'o']:
            self.handle_sort(parts[1:])
        elif cmd in ['help', 'h']:
            self.handle_help()
        elif cmd in ['exit', 'q']:
            self.handle_exit()
        else:
            print(f"Unknown command: {cmd}. Type 'help' for available commands.")

    def handle_add(self, args: List[str]):
        """Handle the add command."""
        if not args:
            print("Usage: add \"description\" [\"priority\"] [\"tags\"]")
            print("       add \"description\" --due-date YYYY-MM-DD --recurrence daily|weekly|monthly")
            return

        try:
            # Extract description (first argument in quotes)
            description_match = re.match(r'^"([^"]*)"', args[0])
            if not description_match:
                print("Description must be in quotes")
                return

            description = description_match.group(1)
            remaining_args = args[0][len(description_match.group(0)):].strip()
            if remaining_args:
                args[0] = remaining_args
            else:
                args = args[1:]

            # Check for advanced options
            due_date = None
            recurrence = None
            priority = None
            tags = None

            # Process advanced options first
            i = 0
            while i < len(args):
                arg = args[i]
                if arg == "--due-date" and i + 1 < len(args):
                    due_date = args[i + 1]
                    try:
                        validate_date_format(due_date)
                    except ValueError as e:
                        print(f"Invalid due date format: {e}")
                        return
                    i += 2
                elif arg == "--recurrence" and i + 1 < len(args):
                    recurrence = args[i + 1].lower()
                    if recurrence not in ["daily", "weekly", "monthly", "none"]:
                        print(f"Recurrence must be 'daily', 'weekly', 'monthly', or 'none', got '{recurrence}'")
                        return
                    if recurrence == "none":
                        recurrence = None
                    i += 2
                else:
                    # If it's not an advanced option, break to process old-style arguments
                    break

            # Process remaining arguments for priority and tags (whether advanced options were used or not)
            remaining_args = args[i:] if i < len(args) else []

            # Extract priority if provided
            if remaining_args and re.match(r'^"([^"]*)"', remaining_args[0]):
                priority_match = re.match(r'^"([^"]*)"', remaining_args[0])
                if priority_match:
                    priority = priority_match.group(1).lower()
                    if priority not in ["high", "medium", "low"]:
                        print(f"Priority must be 'high', 'medium', or 'low', got '{priority}'")
                        return
                    # Remove the priority argument from remaining_args
                    remaining_args = remaining_args[1:]

            # Extract tags if provided
            if remaining_args and re.match(r'^"([^"]*)"', remaining_args[0]):
                tags_match = re.match(r'^"([^"]*)"', remaining_args[0])
                if tags_match:
                    tags_str = tags_match.group(1)
                    tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
                    # Remove the tags argument from remaining_args
                    remaining_args = remaining_args[1:]

            task = self.task_manager.add_task(description, priority, tags, due_date, recurrence)
            print(f"Task added with ID: {task.id}")
            self.save_tasks()
        except ValueError as e:
            print(f"Error adding task: {e}")
        except Exception as e:
            print(f"Unexpected error adding task: {e}")

    def handle_view(self):
        """Handle the view command."""
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("No tasks available.")
            return

        # Sort tasks with overdue tasks first, then by due date
        sorted_tasks = self.sort_tasks_with_overdue(tasks)
        print_colored_table(sorted_tasks)

    def sort_tasks_with_overdue(self, tasks):
        """Sort tasks with overdue tasks first, then by due date."""
        from datetime import date
        from src.lib.date_utils import is_overdue, days_overdue

        def task_sort_key(task):
            # Primary sort: overdue tasks first
            if task.due_date and is_overdue(task.due_date):
                # For overdue tasks, sort by days overdue (descending - most overdue first)
                return (0, -days_overdue(task.due_date), task.due_date)
            elif task.due_date:
                # For non-overdue tasks with due dates, sort by due date (ascending)
                return (1, task.due_date)
            else:
                # For tasks without due dates, sort last
                return (2, "")

        return sorted(tasks, key=task_sort_key)

    def handle_update(self, args: List[str]):
        """Handle the update command."""
        if not args:
            print("Usage: update [id] [\"description\"] [\"priority\"] [\"tags\"]")
            print("       update [id] --due-date YYYY-MM-DD --recurrence daily|weekly|none")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Task ID must be a number")
            return

        # Check for advanced options
        due_date = None
        recurrence = None
        description = None
        priority = None
        tags = None

        # Process advanced options
        i = 1
        while i < len(args):
            arg = args[i]
            if arg == "--due-date" and i + 1 < len(args):
                due_date = args[i + 1]
                try:
                    validate_date_format(due_date)
                except ValueError as e:
                    print(f"Invalid due date format: {e}")
                    return
                i += 2
            elif arg == "--recurrence" and i + 1 < len(args):
                recurrence = args[i + 1].lower()
                if recurrence not in ["daily", "weekly", "monthly", "none"]:
                    print(f"Recurrence must be 'daily', 'weekly', 'monthly', or 'none', got '{recurrence}'")
                    return
                if recurrence == "none":
                    recurrence = None
                i += 2
            else:
                # Process old-style arguments
                break

        # Process remaining arguments for description, priority and tags (whether advanced options were used or not)
        remaining_args = args[i:] if i < len(args) else []

        # Extract description if provided
        if remaining_args:
            desc_match = re.match(r'^"([^"]*)"', remaining_args[0])
            if desc_match:
                description = desc_match.group(1)
                remaining_args = remaining_args[1:]  # Remove the description argument

        # Extract priority if provided
        if remaining_args and re.match(r'^"([^"]*)"', remaining_args[0]):
            priority_match = re.match(r'^"([^"]*)"', remaining_args[0])
            priority = priority_match.group(1).lower()
            if priority not in ["high", "medium", "low"]:
                print(f"Priority must be 'high', 'medium', or 'low', got '{priority}'")
                return
            remaining_args = remaining_args[1:]  # Remove the priority argument

        # Extract tags if provided
        if remaining_args and re.match(r'^"([^"]*)"', remaining_args[0]):
            tags_match = re.match(r'^"([^"]*)"', remaining_args[0])
            if tags_match:
                tags_str = tags_match.group(1)
                tags = [tag.strip() for tag in tags_str.split(',') if tag.strip()]
                remaining_args = remaining_args[1:]  # Remove the tags argument

        if self.task_manager.update_task(task_id, description, priority, tags, due_date=due_date, recurrence=recurrence):
            print(f"Task {task_id} updated successfully")
            self.save_tasks()
        else:
            print(f"Task with ID {task_id} not found")

    def handle_delete(self, args: List[str]):
        """Handle the delete command."""
        if not args:
            print("Usage: delete [id]")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Task ID must be a number")
            return

        # Confirmation prompt
        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found")
            return

        confirm = input(f"Are you sure you want to delete task '{task.description}'? (y/N): ")
        if confirm.lower() in ['y', 'yes']:
            if self.task_manager.delete_task(task_id):
                print(f"Task {task_id} deleted successfully")
                self.save_tasks()
            else:
                print(f"Task with ID {task_id} not found")
        else:
            print("Deletion cancelled")

    def handle_mark(self, args: List[str]):
        """Handle the mark command."""
        if not args:
            print("Usage: mark [id]")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Task ID must be a number")
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Task with ID {task_id} not found")
            return

        # Use the new complete_task method which handles recurring tasks
        new_task_id = self.task_manager.complete_task(task_id)

        if new_task_id is not None:
            print(f"Task {task_id} marked as complete. Next instance created with ID {new_task_id} and due date {task.due_date}")
        else:
            print(f"Task {task_id} marked as complete")

        self.save_tasks()

    def handle_search(self, args: List[str]):
        """Handle the search command."""
        if not args:
            print("Usage: search \"keyword\"")
            return

        keyword_match = re.match(r'^"([^"]*)"', args[0])
        if not keyword_match:
            print("Keyword must be in quotes")
            return

        keyword = keyword_match.group(1)
        tasks = self.task_manager.search_tasks(keyword)

        if not tasks:
            print(f"No tasks found matching '{keyword}'")
            return

        # Sort results with overdue tasks first
        sorted_tasks = self.sort_tasks_with_overdue(tasks)
        print(f"Search results for '{keyword}':")
        print_colored_table(sorted_tasks)

    def handle_filter(self, args: List[str]):
        """Handle the filter command."""
        # Parse arguments: [status] [priority] [tag]
        status = args[0] if len(args) > 0 and args[0] else None
        priority = args[1] if len(args) > 1 and args[1] else None
        tag = args[2] if len(args) > 2 and args[2] else None

        # Validate priority if provided
        if priority and priority.lower() not in ["high", "medium", "low"]:
            print(f"Priority must be 'high', 'medium', or 'low', got '{priority}'")
            return

        tasks = self.task_manager.filter_tasks(status, priority, tag)

        if not tasks:
            print("No tasks match the filter criteria")
            return

        # Sort results with overdue tasks first
        sorted_tasks = self.sort_tasks_with_overdue(tasks)
        print("Filtered tasks:")
        print_colored_table(sorted_tasks)

    def handle_sort(self, args: List[str]):
        """Handle the sort command."""
        by = args[0] if len(args) > 0 and args[0] else "priority"
        order = args[1] if len(args) > 1 and args[1] in ["asc", "desc"] else "desc"

        if by not in ["priority", "alpha", "created"]:
            print(f"Sort criteria must be 'priority', 'alpha', or 'created', got '{by}'")
            return

        all_tasks = self.task_manager.get_all_tasks()
        if by == "due_date":
            # Special handling for due date sorting
            sorted_tasks = self.sort_tasks_with_overdue(all_tasks)
        else:
            sorted_tasks = self.task_manager.sort_tasks(all_tasks, by, order)

        print(f"Tasks sorted by {by} ({order}):")
        print_colored_table(sorted_tasks)

    def handle_help(self):
        """Handle the help command."""
        help_text = """
Available commands:
  add "description" ["priority"] ["tags"] - Add a new task
  add "description" --due-date YYYY-MM-DD --recurrence daily|weekly|monthly - Add a recurring task with due date
  view or v - View all tasks
  update [id] ["description"] ["priority"] ["tags"] - Update a task
  update [id] --due-date YYYY-MM-DD --recurrence daily|weekly|none - Update due date and recurrence settings
  delete [id] - Delete a task
  mark [id] - Toggle task completion (creates new instance for recurring tasks)
  search "keyword" - Search tasks
  filter [status] [priority] [tag] - Filter tasks
  sort [by] [order] - Sort tasks (by: priority/alpha/created, order: asc/desc)
  help or h - Show this help
  exit or q - Exit the application
        """
        print(help_text)

    def handle_exit(self):
        """Handle the exit command."""
        print("Goodbye!")
        self.running = False
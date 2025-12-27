"""
Main CLI interface for the Todo Console Application.

This module provides the command-line interface for users to interact with
the todo application, including commands for adding, viewing, updating,
deleting, and marking tasks as complete.
"""

import sys
from typing import List
from src.services.todo_service import TodoService


class TodoCLI:
    """
    Command-Line Interface for the Todo application.
    """
    
    def __init__(self):
        """Initialize the CLI with a TodoService instance."""
        self.service = TodoService()
        self.running = True
    
    def display_help(self):
        """Display help information for available commands."""
        print("\nAvailable commands:")
        print("  add \"title\" [\"description\"]  - Add a new task")
        print("  view                         - View all tasks")
        print("  update id \"title\" [\"description\"] - Update a task")
        print("  delete id                    - Delete a task")
        print("  mark id                      - Toggle task completion status")
        print("  help                         - Show this help message")
        print("  exit                         - Exit the application")
        print("\nExamples:")
        print("  add \"Buy groceries\" \"Milk, bread, eggs\"")
        print("  update 1 \"Buy groceries\" \"Milk, bread, eggs, fruits\"")
        print("  mark 1")
        print("  delete 2")
    
    def parse_command(self, user_input: str) -> List[str]:
        """
        Parse user input into command and arguments, handling quoted strings.
        
        Args:
            user_input (str): The raw user input
            
        Returns:
            List[str]: A list of command parts
        """
        # Split the input while respecting quoted strings
        parts = []
        current_part = ""
        in_quotes = False
        quote_char = None
        
        i = 0
        while i < len(user_input):
            char = user_input[i]
            
            if char in ['"', "'"] and not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
                # Don't add the quote character to the part
            elif char == ' ' and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char
            
            i += 1
        
        # Add the last part if it exists
        if current_part:
            parts.append(current_part)
        
        return parts
    
    def handle_add(self, args: List[str]):
        """Handle the 'add' command to add a new task."""
        if len(args) < 2:
            print("Error: 'add' command requires at least a title")
            print("Usage: add \"title\" [\"description\"]")
            return
        
        title = args[1]
        description = args[2] if len(args) > 2 else ""
        
        try:
            task = self.service.add_task(title, description)
            print(f"Task added with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_view(self, args: List[str]):
        """Handle the 'view' command to display all tasks."""
        if len(args) > 1:
            print("Error: 'view' command takes no arguments")
            print("Usage: view")
            return
        
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            print("No tasks in the list")
            return
        
        print("\nTask List:")
        for task in tasks:
            status = "[x]" if task.complete else "[ ]"
            print(f"{task.id}. {status} {task.title} - {task.description}")
    
    def handle_update(self, args: List[str]):
        """Handle the 'update' command to update a task."""
        if len(args) < 3:
            print("Error: 'update' command requires an ID and at least a title")
            print("Usage: update id \"title\" [\"description\"]")
            return
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return
        
        title = args[2]
        description = args[3] if len(args) > 3 else None
        
        try:
            updated_task = self.service.update_task(task_id, title, description)
            if updated_task:
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError as e:
            print(f"Error: {e}")
    
    def handle_delete(self, args: List[str]):
        """Handle the 'delete' command to delete a task."""
        if len(args) != 2:
            print("Error: 'delete' command requires an ID")
            print("Usage: delete id")
            return
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return
        
        # Confirm deletion
        task = self.service.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return
        
        confirmation = input(f"Are you sure you want to delete task {task_id} '{task.title}'? (y/n): ")
        if confirmation.lower() in ['y', 'yes']:
            if self.service.delete_task(task_id):
                print(f"Task {task_id} deleted successfully")
            else:
                print(f"Error: Task with ID {task_id} not found")
        else:
            print("Deletion cancelled")
    
    def handle_mark(self, args: List[str]):
        """Handle the 'mark' command to toggle task completion status."""
        if len(args) != 2:
            print("Error: 'mark' command requires an ID")
            print("Usage: mark id")
            return
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return
        
        task = self.service.toggle_task_status(task_id)
        if task:
            status = "complete" if task.complete else "incomplete"
            print(f"Task {task_id} marked as {status}")
        else:
            print(f"Error: Task with ID {task_id} not found")
    
    def handle_command(self, user_input: str):
        """Handle a user command."""
        if not user_input.strip():
            return
        
        parts = self.parse_command(user_input)
        if not parts:
            return
        
        command = parts[0].lower()
        
        if command == "add":
            self.handle_add(parts)
        elif command == "view":
            self.handle_view(parts)
        elif command == "update":
            self.handle_update(parts)
        elif command == "delete":
            self.handle_delete(parts)
        elif command == "mark":
            self.handle_mark(parts)
        elif command == "help":
            self.display_help()
        elif command == "exit":
            self.running = False
            print("Goodbye!")
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands")
    
    def run(self):
        """Run the CLI application."""
        print("Welcome to the Todo Console Application!")
        print("Type 'help' for available commands or 'exit' to quit.")
        
        while self.running:
            try:
                user_input = input("\n> ").strip()
                self.handle_command(user_input)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                sys.exit(0)
            except EOFError:
                print("\nGoodbye!")
                sys.exit(0)


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()
"""
Utility functions for the Todo Console Application.

This module contains helper functions for validation, formatting,
and other common operations used throughout the application.
"""


def validate_task_title(title: str) -> bool:
    """
    Validate that a task title is not empty or just whitespace.
    
    Args:
        title (str): The title to validate
        
    Returns:
        bool: True if the title is valid, False otherwise
    """
    return isinstance(title, str) and bool(title.strip())


def validate_task_description(description: str) -> bool:
    """
    Validate that a task description is a string (can be empty).
    
    Args:
        description (str): The description to validate
        
    Returns:
        bool: True if the description is valid, False otherwise
    """
    return isinstance(description, str)


def format_task_display(task) -> str:
    """
    Format a task for display in the console.
    
    Args:
        task: A task object with id, title, description, and complete attributes
        
    Returns:
        str: A formatted string representation of the task
    """
    status = "[x]" if getattr(task, 'complete', False) else "[ ]"
    title = getattr(task, 'title', 'No Title')
    description = getattr(task, 'description', '')
    task_id = getattr(task, 'id', 'No ID')
    
    return f"{task_id}. {status} {title} - {description}"


def format_task_list_display(tasks) -> str:
    """
    Format a list of tasks for display in the console.
    
    Args:
        tasks: A list of task objects
        
    Returns:
        str: A formatted string representation of the task list
    """
    if not tasks:
        return "No tasks in the list"
    
    task_lines = []
    for task in tasks:
        task_lines.append(format_task_display(task))
    
    return "\n".join(task_lines)


def parse_task_id(user_input: str) -> int:
    """
    Parse a task ID from user input.
    
    Args:
        user_input (str): The user input containing the ID
        
    Returns:
        int: The parsed task ID
        
    Raises:
        ValueError: If the input cannot be parsed as an integer
    """
    try:
        task_id = int(user_input)
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id
    except ValueError:
        raise ValueError(f"Invalid task ID: {user_input}. Must be a positive integer.")


def confirm_action(prompt: str) -> bool:
    """
    Prompt the user for confirmation of an action.
    
    Args:
        prompt (str): The confirmation prompt to display
        
    Returns:
        bool: True if the user confirms, False otherwise
    """
    response = input(f"{prompt} (y/n): ").strip().lower()
    return response in ['y', 'yes', '1', 'true', 't']


def safe_input(prompt: str = "") -> str:
    """
    Safely get input from the user, handling potential interruptions.
    
    Args:
        prompt (str): The input prompt to display
        
    Returns:
        str: The user input, or empty string if interrupted
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled.")
        return ""
"""
Utility functions for the Todo Console Application.
Includes ANSI color formatting functions.
"""
from src.lib.date_utils import format_due_date_display


def print_colored_table(tasks):
    """
    Print tasks in a colored table format.
    """
    if not tasks:
        print("No tasks to display.")
        return

    # Print table header
    print(f"{'ID':<3} | {'Status':<8} | {'Priority':<12} | {'Tags':<15} | {'Due Date':<30} | {'Description':<30}")
    print("-" * 100)

    # Print each task
    for task in tasks:
        task_str = format_task_with_colors(task)
        print(task_str)


def format_task_with_colors(task):
    """
    Format a single task with ANSI colors.
    """
    # ANSI color codes
    RED = '\033[31m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BOLD = '\033[1m'
    RESET = '\033[0m'  # Reset to default color

    # Format ID
    id_str = f"{task.id:<3}"

    # Format status
    status = "[x]" if task.completed else "[ ]"
    status_str = f"{status:<8}"

    # Format priority with colors and symbols
    if task.priority == "high":
        priority_str = f"{RED}★★★ HIGH{RESET}"
    elif task.priority == "medium":
        priority_str = f"{YELLOW}★★ MED{RESET}"
    elif task.priority == "low":
        priority_str = f"{GREEN}★ LOW{RESET}"
    else:
        priority_str = f"{task.priority or 'None':<12}"

    # Format tags
    tags_str = ",".join(task.tags) if task.tags else ""
    tags_str = f"{tags_str:<15}"

    # Format due date and recurrence
    due_date_str = format_due_date_display(task.due_date)
    if task.recurrence:
        due_date_str += f" [RECUR: {task.recurrence}]"

    # Limit the due date string length to fit in the table
    due_date_str = due_date_str[:30] if len(due_date_str) > 30 else due_date_str
    due_date_str = f"{due_date_str:<30}"

    # Format description
    desc_str = f"{task.description:<30}"

    return f"{id_str} | {status_str} | {priority_str:<12} | {tags_str} | {due_date_str} | {desc_str}"


def validate_priority(priority):
    """
    Validate that the priority is one of the allowed values.
    """
    if priority is None:
        return True
    return priority.lower() in ["high", "medium", "low"]
import json
from typing import List
from src.models.task import Task
from datetime import date


def load_tasks_from_file(storage_file: str = "todos.json") -> List[Task]:
    """
    Loads tasks from JSON file with migration support.
    """
    try:
        with open(storage_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            tasks = []

            # Process each task from the file
            for task_data in data:
                # Add missing fields with defaults for migration
                if 'priority' not in task_data:
                    task_data['priority'] = 'medium'
                if 'tags' not in task_data:
                    task_data['tags'] = []
                if 'created_at' not in task_data:
                    task_data['created_at'] = date.today().strftime("%Y-%m-%d")

                # Add new fields with defaults for backward compatibility
                if 'due_date' not in task_data:
                    task_data['due_date'] = None
                if 'recurrence' not in task_data:
                    task_data['recurrence'] = None

                # Create Task object from the data
                task = Task(**task_data)
                tasks.append(task)

        return tasks
    except FileNotFoundError:
        # If file doesn't exist, return empty task list
        return []
    except json.JSONDecodeError:
        # If file is corrupted, return empty task list
        print(f"Warning: {storage_file} is corrupted. Starting with empty task list.")
        return []


def save_tasks_to_file(tasks: List[Task], storage_file: str = "todos.json"):
    """
    Saves tasks to JSON file.
    """
    # Convert tasks to dictionaries for JSON serialization
    tasks_data = []
    for task in tasks:
        task_dict = {
            'id': task.id,
            'description': task.description,
            'completed': task.completed,
            'created_at': task.created_at,
            'priority': task.priority,
            'tags': task.tags,
            'due_date': task.due_date,
            'recurrence': task.recurrence
        }
        tasks_data.append(task_dict)

    # Write to file
    with open(storage_file, 'w', encoding='utf-8') as file:
        json.dump(tasks_data, file, indent=2)
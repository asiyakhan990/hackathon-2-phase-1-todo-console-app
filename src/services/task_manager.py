from typing import List, Optional
from src.models.task import Task
import json
from datetime import date
from src.lib.date_utils import validate_date_format, calculate_next_due_date


class TaskManager:
    """
    Manages all operations related to tasks.
    """

    def __init__(self, storage_file: str = "todos.json"):
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self.next_id = 1  # Track the next available ID

    def add_task(self, description: str, priority: Optional[str] = None, tags: Optional[List[str]] = None,
                 due_date: Optional[str] = None, recurrence: Optional[str] = None) -> Task:
        """
        Creates a new task with a unique ID.
        """
        task = Task(
            id=self.next_id,
            description=description,
            priority=priority,
            tags=tags if tags is not None else [],
            due_date=due_date,
            recurrence=recurrence
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a specific task by ID.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, description: Optional[str] = None,
                    priority: Optional[str] = None, tags: Optional[List[str]] = None,
                    completed: Optional[bool] = None, due_date: Optional[str] = None,
                    recurrence: Optional[str] = None) -> bool:
        """
        Updates task properties.
        """
        task = self.get_task(task_id)
        if task:
            if description is not None:
                task.description = description
            if priority is not None:
                task.priority = priority
            if tags is not None:
                task.tags = tags
            if completed is not None:
                task.completed = completed
            if due_date is not None:
                task.due_date = due_date
            if recurrence is not None:
                task.recurrence = recurrence
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Removes a task by ID.
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks.
        """
        return self.tasks.copy()

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Returns tasks matching the keyword in description or tags.
        """
        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.tasks:
            # Check if keyword is in description
            if keyword_lower in task.description.lower():
                matching_tasks.append(task)
                continue

            # Check if keyword is in any of the tags
            for tag in task.tags:
                if keyword_lower in tag.lower():
                    matching_tasks.append(task)
                    break

        return matching_tasks

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None,
                     tag: Optional[str] = None) -> List[Task]:
        """
        Returns tasks matching filter criteria.
        """
        filtered_tasks = self.tasks.copy()

        if status:
            if status.lower() == "active":
                filtered_tasks = [task for task in filtered_tasks if not task.completed]
            elif status.lower() == "completed":
                filtered_tasks = [task for task in filtered_tasks if task.completed]

        if priority:
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority.lower()]

        if tag:
            filtered_tasks = [task for task in filtered_tasks if tag in task.tags]

        return filtered_tasks

    def complete_task(self, task_id: int) -> Optional[int]:
        """
        Marks a task as complete. If the task is recurring, creates a new instance with the next due date.

        Returns:
            - None if the task is not recurring
            - New task ID if the task is recurring and a new instance was created
        """
        task = self.get_task(task_id)
        if not task:
            return None

        # Mark the current task as complete
        task.completed = True

        # If the task is recurring, create a new instance
        if task.recurrence:
            next_due_date = calculate_next_due_date(task.due_date, task.recurrence)

            # Create a new task with the same properties but updated due date
            new_task = Task(
                id=self.next_id,
                description=task.description,
                priority=task.priority,
                tags=task.tags.copy(),  # Copy the tags
                due_date=next_due_date,
                recurrence=task.recurrence
            )

            self.tasks.append(new_task)
            self.next_id += 1

            return new_task.id

        return None

    def sort_tasks(self, tasks: List[Task], by: str = "priority", order: str = "desc") -> List[Task]:
        """
        Returns tasks sorted by specified criteria.
        """
        # Define priority order: high > medium > low
        def priority_key(task):
            priority_order = {"high": 3, "medium": 2, "low": 1}
            return priority_order.get(task.priority, 0)

        if by == "priority":
            sorted_tasks = sorted(tasks, key=priority_key, reverse=(order == "desc"))
        elif by == "alpha":
            sorted_tasks = sorted(tasks, key=lambda t: t.description.lower(), reverse=(order == "desc"))
        elif by == "created":
            sorted_tasks = sorted(tasks, key=lambda t: t.created_at, reverse=(order == "desc"))
        else:
            # Default to priority if invalid sort criteria
            sorted_tasks = sorted(tasks, key=priority_key, reverse=(order == "desc"))

        return sorted_tasks

    def load_tasks(self):
        """
        Loads tasks from JSON file with migration support.
        """
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Clear current tasks
                self.tasks = []

                # Process each task from the file
                for task_data in data:
                    # Handle migration of old basic task format
                    if 'id' not in task_data:
                        task_data['id'] = self.next_id
                        self.next_id += 1
                    else:
                        # Update next_id if necessary
                        if task_data['id'] >= self.next_id:
                            self.next_id = task_data['id'] + 1

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
                    self.tasks.append(task)

        except FileNotFoundError:
            # If file doesn't exist, start with empty task list
            self.tasks = []
        except json.JSONDecodeError:
            # If file is corrupted, start with empty task list
            print(f"Warning: {self.storage_file} is corrupted. Starting with empty task list.")
            self.tasks = []

    def save_tasks(self):
        """
        Saves tasks to JSON file.
        """
        # Convert tasks to dictionaries for JSON serialization
        tasks_data = []
        for task in self.tasks:
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
        with open(self.storage_file, 'w', encoding='utf-8') as file:
            json.dump(tasks_data, file, indent=2)
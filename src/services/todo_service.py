"""
Todo Service for the Todo Console Application.

This module provides the core business logic for managing tasks,
including adding, updating, deleting, viewing, and marking tasks as complete.
"""

from typing import List, Optional
from src.models.task import Task


class TodoService:
    """
    Service class that handles all business logic for managing tasks.
    """
    
    def __init__(self):
        """Initialize the TodoService with an empty task list and next ID counter."""
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and optional description.
        
        Args:
            title (str): The title of the task (required)
            description (str): The description of the task (optional)
            
        Returns:
            Task: The newly created task
        """
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Task title is required")
        
        # Create new task with unique ID
        task = Task(
            task_id=self.next_id,
            title=title.strip(),
            description=description.strip() if description else "",
            complete=False
        )
        
        # Add task to list
        self.tasks.append(task)
        
        # Increment next ID for future tasks
        self.next_id += 1
        
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.
        
        Returns:
            List[Task]: A list of all tasks
        """
        return self.tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task's title and/or description.
        
        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            
        Returns:
            Task or None: The updated task if found, None otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        
        # Update title if provided
        if title is not None:
            title = title.strip()
            if not title:
                raise ValueError("Task title cannot be empty")
            task.title = title
        
        # Update description if provided
        if description is not None:
            task.description = description.strip() if description else ""
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return True
    
    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id (int): The ID of the task to toggle
            
        Returns:
            Task or None: The task with toggled status if found, None otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        
        task.toggle_status()
        return task
    
    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.
        
        Returns:
            int: The next available ID
        """
        return self.next_id
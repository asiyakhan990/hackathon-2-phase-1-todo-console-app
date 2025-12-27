"""
Task data model for the Todo Console Application.

This module defines the Task class which represents a single todo item
with attributes for ID, title, description, and completion status.
"""


class Task:
    """
    Represents a single todo item with the following attributes:
    - ID: Unique identifier (integer, starting from 1)
    - Title: Required text describing the task
    - Description: Optional text with additional details
    - Complete: Boolean indicating completion status (false by default)
    """
    
    def __init__(self, task_id: int, title: str, description: str = "", complete: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.complete = complete

    def __str__(self):
        """Return a string representation of the task."""
        status = "[x]" if self.complete else "[ ]"
        return f"{self.id}. {status} {self.title} - {self.description}"
    
    def to_dict(self):
        """Convert the task to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "complete": self.complete
        }
    
    def mark_complete(self):
        """Mark the task as complete."""
        self.complete = True
    
    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.complete = False
    
    def toggle_status(self):
        """Toggle the completion status of the task."""
        self.complete = not self.complete
"""
Test module for the Todo Console Application.

This module contains unit tests for the TodoApp class and its functionality.
"""

import unittest
from src.todo import TodoApp
from src.models.task import Task


class TestTodoApp(unittest.TestCase):
    """
    Test cases for the TodoApp class.
    """
    
    def setUp(self):
        """Set up a fresh TodoApp instance for each test."""
        self.app = TodoApp()
        # Since TodoApp uses a service, we'll test the service directly
        self.service = self.app.service
    
    def test_add_task(self):
        """Test adding a task to the application."""
        task = self.service.add_task("Test task", "Test description")
        
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.complete)
        self.assertEqual(task.id, 1)
        self.assertEqual(len(self.service.tasks), 1)
    
    def test_add_task_without_description(self):
        """Test adding a task without a description."""
        task = self.service.add_task("Test task")
        
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "")
        self.assertFalse(task.complete)
        self.assertEqual(task.id, 1)
    
    def test_add_task_empty_title_error(self):
        """Test that adding a task with an empty title raises an error."""
        with self.assertRaises(ValueError):
            self.service.add_task("")
        
        with self.assertRaises(ValueError):
            self.service.add_task("   ")
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        
        tasks = self.service.get_all_tasks()
        
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")
    
    def test_get_task_by_id(self):
        """Test retrieving a task by its ID."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        
        retrieved_task = self.service.get_task_by_id(1)
        self.assertEqual(retrieved_task.id, task1.id)
        self.assertEqual(retrieved_task.title, "Task 1")
        
        retrieved_task = self.service.get_task_by_id(2)
        self.assertEqual(retrieved_task.id, task2.id)
        self.assertEqual(retrieved_task.title, "Task 2")
        
        # Test non-existent ID
        retrieved_task = self.service.get_task_by_id(999)
        self.assertIsNone(retrieved_task)
    
    def test_update_task(self):
        """Test updating a task's title and description."""
        task = self.service.add_task("Original title", "Original description")
        
        updated_task = self.service.update_task(1, "Updated title", "Updated description")
        
        self.assertEqual(updated_task.title, "Updated title")
        self.assertEqual(updated_task.description, "Updated description")
        
        # Verify the task in the app was also updated
        self.assertEqual(self.service.tasks[0].title, "Updated title")
        self.assertEqual(self.service.tasks[0].description, "Updated description")
    
    def test_update_task_partial(self):
        """Test updating only the title or only the description."""
        task = self.service.add_task("Original title", "Original description")
        
        # Update only the title
        updated_task = self.service.update_task(1, title="Updated title")
        self.assertEqual(updated_task.title, "Updated title")
        self.assertEqual(updated_task.description, "Original description")
        
        # Update only the description
        self.service.update_task(1, description="Updated description")
        self.assertEqual(self.service.tasks[0].title, "Updated title")
        self.assertEqual(self.service.tasks[0].description, "Updated description")
    
    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist."""
        result = self.service.update_task(999, "New title")
        self.assertIsNone(result)
    
    def test_update_task_empty_title_error(self):
        """Test that updating a task with an empty title raises an error."""
        self.service.add_task("Original title")
        
        with self.assertRaises(ValueError):
            self.service.update_task(1, "")
        
        with self.assertRaises(ValueError):
            self.service.update_task(1, "   ")
    
    def test_delete_task(self):
        """Test deleting a task."""
        self.service.add_task("Task 1")
        self.service.add_task("Task 2")
        
        # Verify both tasks exist
        self.assertEqual(len(self.service.tasks), 2)
        
        # Delete the first task
        result = self.service.delete_task(1)
        self.assertTrue(result)
        self.assertEqual(len(self.service.tasks), 1)
        self.assertEqual(self.service.tasks[0].id, 2)
        
        # Try to delete a non-existent task
        result = self.service.delete_task(999)
        self.assertFalse(result)
    
    def test_toggle_task_status(self):
        """Test toggling a task's completion status."""
        task = self.service.add_task("Test task")
        
        # Initially, task should be incomplete
        self.assertFalse(task.complete)
        
        # Toggle to complete
        toggled_task = self.service.toggle_task_status(1)
        self.assertTrue(toggled_task.complete)
        
        # Toggle back to incomplete
        toggled_task = self.service.toggle_task_status(1)
        self.assertFalse(toggled_task.complete)
    
    def test_toggle_nonexistent_task(self):
        """Test toggling a task that doesn't exist."""
        result = self.service.toggle_task_status(999)
        self.assertIsNone(result)
    
    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task = Task(1, "Test title", "Test description", False)
        expected = "1. [ ] Test title - Test description"
        self.assertEqual(str(task), expected)
        
        task.complete = True
        expected = "1. [x] Test title - Test description"
        self.assertEqual(str(task), expected)


if __name__ == '__main__':
    unittest.main()
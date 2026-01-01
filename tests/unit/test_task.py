import unittest
from src.models.task import Task


class TestTask(unittest.TestCase):
    """
    Unit tests for the Task model.
    """
    
    def test_task_creation_with_priority_and_tags(self):
        """Test creating a task with priority and tags."""
        task = Task(
            id=1,
            description="Test task",
            priority="high",
            tags=["work", "urgent"]
        )
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "urgent"])
        self.assertFalse(task.completed)
    
    def test_task_creation_with_defaults(self):
        """Test creating a task with default values."""
        task = Task(id=1, description="Test task")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default tags
        self.assertFalse(task.completed)
    
    def test_task_priority_validation(self):
        """Test that invalid priority raises an error."""
        with self.assertRaises(ValueError):
            Task(id=1, description="Test task", priority="invalid")
    
    def test_task_tags_validation(self):
        """Test that invalid tags raise an error."""
        with self.assertRaises(TypeError):
            Task(id=1, description="Test task", tags="not_a_list")
        
        with self.assertRaises(TypeError):
            Task(id=1, description="Test task", tags=[1, 2, 3])  # Non-string tags
    
    def test_task_description_validation(self):
        """Test that empty description raises an error."""
        with self.assertRaises(ValueError):
            Task(id=1, description="")
        
        with self.assertRaises(ValueError):
            Task(id=1, description="   ")  # Only whitespace

    def test_task_creation_with_all_fields(self):
        """Test creating a task with all fields specified."""
        task = Task(
            id=1,
            description="Complete project",
            completed=True,
            priority="high",
            tags=["work", "important", "deadline"]
        )

        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Complete project")
        self.assertTrue(task.completed)
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "important", "deadline"])

    def test_task_default_values(self):
        """Test that default values are properly set."""
        task = Task(id=1, description="Test task")

        self.assertEqual(task.completed, False)
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default tags


if __name__ == '__main__':
    unittest.main()
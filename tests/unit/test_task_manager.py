import unittest
import tempfile
import os
from src.services.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the TaskManager class.
    """

    def setUp(self):
        """Set up a temporary file for testing."""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        self.task_manager = TaskManager(storage_file=self.temp_file.name)

    def tearDown(self):
        """Clean up the temporary file."""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_add_task_with_priority_and_tags(self):
        """Test adding a task with priority and tags."""
        task = self.task_manager.add_task(
            description="Test task",
            priority="high",
            tags=["work", "urgent"]
        )

        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "urgent"])
        self.assertFalse(task.completed)

        # Verify task is in the manager's list
        all_tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 1)
        self.assertEqual(all_tasks[0].id, 1)

    def test_add_task_with_defaults(self):
        """Test adding a task with default values."""
        task = self.task_manager.add_task(description="Test task")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.priority, "medium")  # Default priority
        self.assertEqual(task.tags, [])  # Default tags
        self.assertFalse(task.completed)

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with unique IDs."""
        task1 = self.task_manager.add_task(description="First task")
        task2 = self.task_manager.add_task(description="Second task")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)

        all_tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)

    def test_search_tasks_by_description(self):
        """Test searching tasks by keyword in description."""
        # Add some tasks
        self.task_manager.add_task(description="Buy groceries", tags=["shopping"])
        self.task_manager.add_task(description="Finish report", priority="high")
        self.task_manager.add_task(description="Call mom", tags=["personal"])

        # Search for "report"
        results = self.task_manager.search_tasks("report")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Finish report")

        # Search for "groceries"
        results = self.task_manager.search_tasks("groceries")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Buy groceries")

    def test_search_tasks_by_tags(self):
        """Test searching tasks by keyword in tags."""
        # Add some tasks
        self.task_manager.add_task(description="Buy groceries", tags=["shopping", "food"])
        self.task_manager.add_task(description="Finish report", priority="high")
        self.task_manager.add_task(description="Call mom", tags=["personal", "family"])

        # Search for "shopping"
        results = self.task_manager.search_tasks("shopping")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Buy groceries")

        # Search for "family"
        results = self.task_manager.search_tasks("family")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Call mom")

    def test_search_tasks_case_insensitive(self):
        """Test that search is case insensitive."""
        self.task_manager.add_task(description="Buy Groceries", tags=["Shopping"])

        # Search with different cases
        results = self.task_manager.search_tasks("GROCERIES")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Buy Groceries")

        results = self.task_manager.search_tasks("SHOPPING")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].tags, ["Shopping"])

    def test_filter_tasks_by_status(self):
        """Test filtering tasks by status."""
        # Add some tasks with different completion status
        task1 = self.task_manager.add_task(description="Active task")
        task2 = self.task_manager.add_task(description="Completed task")
        self.task_manager.update_task(task2.id, completed=True)

        # Filter for active tasks
        active_tasks = self.task_manager.filter_tasks(status="active")
        self.assertEqual(len(active_tasks), 1)
        self.assertEqual(active_tasks[0].id, task1.id)
        self.assertFalse(active_tasks[0].completed)

        # Filter for completed tasks
        completed_tasks = self.task_manager.filter_tasks(status="completed")
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].id, task2.id)
        self.assertTrue(completed_tasks[0].completed)

    def test_filter_tasks_by_priority(self):
        """Test filtering tasks by priority."""
        # Add some tasks with different priorities
        self.task_manager.add_task(description="High priority task", priority="high")
        self.task_manager.add_task(description="Medium priority task", priority="medium")
        self.task_manager.add_task(description="Low priority task", priority="low")
        self.task_manager.add_task(description="No priority task")

        # Filter for high priority tasks
        high_tasks = self.task_manager.filter_tasks(priority="high")
        self.assertEqual(len(high_tasks), 1)
        self.assertEqual(high_tasks[0].description, "High priority task")
        self.assertEqual(high_tasks[0].priority, "high")

        # Filter for medium priority tasks
        medium_tasks = self.task_manager.filter_tasks(priority="medium")
        self.assertEqual(len(medium_tasks), 1)
        self.assertEqual(medium_tasks[0].description, "Medium priority task")
        self.assertEqual(medium_tasks[0].priority, "medium")

    def test_filter_tasks_by_tag(self):
        """Test filtering tasks by tag."""
        # Add some tasks with different tags
        self.task_manager.add_task(description="Work task", tags=["work", "urgent"])
        self.task_manager.add_task(description="Personal task", tags=["personal"])
        self.task_manager.add_task(description="Shopping task", tags=["shopping", "errand"])

        # Filter for "work" tag
        work_tasks = self.task_manager.filter_tasks(tag="work")
        self.assertEqual(len(work_tasks), 1)
        self.assertEqual(work_tasks[0].description, "Work task")
        self.assertIn("work", work_tasks[0].tags)

        # Filter for "errand" tag
        errand_tasks = self.task_manager.filter_tasks(tag="errand")
        self.assertEqual(len(errand_tasks), 1)
        self.assertEqual(errand_tasks[0].description, "Shopping task")
        self.assertIn("errand", errand_tasks[0].tags)

    def test_filter_tasks_combined(self):
        """Test combining multiple filters."""
        # Add some tasks with different attributes
        task1 = self.task_manager.add_task(description="Completed high work task",
                                          priority="high", tags=["work"])
        self.task_manager.update_task(task1.id, completed=True)

        task2 = self.task_manager.add_task(description="Active high work task",
                                          priority="high", tags=["work"])

        task3 = self.task_manager.add_task(description="Active low work task",
                                          priority="low", tags=["work"])

        # Filter for active, high priority, work tasks
        filtered_tasks = self.task_manager.filter_tasks(status="active",
                                                       priority="high",
                                                       tag="work")
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0].description, "Active high work task")

    def test_sort_tasks_by_priority(self):
        """Test sorting tasks by priority."""
        # Add tasks with different priorities
        self.task_manager.add_task(description="Medium priority task", priority="medium")
        self.task_manager.add_task(description="High priority task", priority="high")
        self.task_manager.add_task(description="Low priority task", priority="low")

        # Sort by priority (descending - high to low)
        all_tasks = self.task_manager.get_all_tasks()
        sorted_tasks = self.task_manager.sort_tasks(all_tasks, by="priority", order="desc")

        self.assertEqual(len(sorted_tasks), 3)
        self.assertEqual(sorted_tasks[0].priority, "high")
        self.assertEqual(sorted_tasks[1].priority, "medium")
        self.assertEqual(sorted_tasks[2].priority, "low")

        # Sort by priority (ascending - low to high)
        sorted_tasks_asc = self.task_manager.sort_tasks(all_tasks, by="priority", order="asc")

        self.assertEqual(sorted_tasks_asc[0].priority, "low")
        self.assertEqual(sorted_tasks_asc[1].priority, "medium")
        self.assertEqual(sorted_tasks_asc[2].priority, "high")

    def test_sort_tasks_by_alpha(self):
        """Test sorting tasks alphabetically."""
        # Add tasks with different descriptions
        self.task_manager.add_task(description="Zebra task", priority="low")
        self.task_manager.add_task(description="Apple task", priority="high")
        self.task_manager.add_task(description="Mango task", priority="medium")

        # Sort alphabetically (ascending)
        all_tasks = self.task_manager.get_all_tasks()
        sorted_tasks = self.task_manager.sort_tasks(all_tasks, by="alpha", order="asc")

        self.assertEqual(len(sorted_tasks), 3)
        self.assertEqual(sorted_tasks[0].description, "Apple task")
        self.assertEqual(sorted_tasks[1].description, "Mango task")
        self.assertEqual(sorted_tasks[2].description, "Zebra task")

        # Sort alphabetically (descending)
        sorted_tasks_desc = self.task_manager.sort_tasks(all_tasks, by="alpha", order="desc")

        self.assertEqual(sorted_tasks_desc[0].description, "Zebra task")
        self.assertEqual(sorted_tasks_desc[1].description, "Mango task")
        self.assertEqual(sorted_tasks_desc[2].description, "Apple task")

    def test_sort_tasks_by_created_date(self):
        """Test sorting tasks by creation date."""
        # Add tasks (they will have different creation dates)
        task1 = self.task_manager.add_task(description="First task", priority="low")
        task2 = self.task_manager.add_task(description="Second task", priority="high")
        task3 = self.task_manager.add_task(description="Third task", priority="medium")

        # Sort by creation date (ascending - oldest to newest)
        all_tasks = self.task_manager.get_all_tasks()
        sorted_tasks = self.task_manager.sort_tasks(all_tasks, by="created", order="asc")

        self.assertEqual(len(sorted_tasks), 3)
        self.assertEqual(sorted_tasks[0].id, task1.id)
        self.assertEqual(sorted_tasks[1].id, task2.id)
        self.assertEqual(sorted_tasks[2].id, task3.id)

        # Sort by creation date (descending - newest to oldest)
        sorted_tasks_desc = self.task_manager.sort_tasks(all_tasks, by="created", order="desc")

        self.assertEqual(sorted_tasks_desc[0].id, task3.id)
        self.assertEqual(sorted_tasks_desc[1].id, task2.id)
        self.assertEqual(sorted_tasks_desc[2].id, task1.id)


if __name__ == '__main__':
    unittest.main()
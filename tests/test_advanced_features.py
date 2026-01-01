"""
Tests for Advanced Todo Features
This module contains tests for recurring tasks and due date functionality.
"""
import pytest
import os
import tempfile
from datetime import date, timedelta
from src.models.task import Task
from src.services.task_manager import TaskManager
from src.lib.date_utils import validate_date_format, is_overdue, calculate_next_due_date


class TestAdvancedFeatures:
    """Test class for advanced todo features."""
    
    def setup_method(self):
        """Set up test environment."""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.temp_file.close()
        self.task_manager = TaskManager(self.temp_file.name)
        
    def teardown_method(self):
        """Clean up test environment."""
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)
    
    def test_task_creation_with_due_date_and_recurrence(self):
        """Test creating a task with both due date and recurrence."""
        task = Task(
            id=1,
            description="Test task",
            due_date="2026-12-31",
            recurrence="weekly"
        )
        
        assert task.due_date == "2026-12-31"
        assert task.recurrence == "weekly"
        assert task.description == "Test task"
    
    def test_date_validation_valid_format(self):
        """Test date validation with valid format."""
        assert validate_date_format("2026-01-01") is True
        assert validate_date_format("2025-12-31") is True
    
    def test_date_validation_invalid_format(self):
        """Test date validation with invalid format."""
        with pytest.raises(ValueError):
            validate_date_format("01-01-2026")  # Wrong format
        with pytest.raises(ValueError):
            validate_date_format("2026/01/01")  # Wrong separator
        with pytest.raises(ValueError):
            validate_date_format("2026-1-1")    # Wrong padding
    
    def test_date_validation_invalid_date(self):
        """Test date validation with invalid date."""
        with pytest.raises(ValueError):
            validate_date_format("2026-02-30")  # Invalid day
        with pytest.raises(ValueError):
            validate_date_format("2026-04-31")  # Invalid day
    
    def test_overdue_detection(self):
        """Test overdue date detection."""
        past_date = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        future_date = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        today_date = date.today().strftime("%Y-%m-%d")
        
        assert is_overdue(past_date) is True
        assert is_overdue(future_date) is False
        assert is_overdue(today_date) is False  # Today is not overdue
    
    def test_next_due_date_calculation(self):
        """Test next due date calculation for different recurrence patterns."""
        test_date = "2026-01-01"
        
        # Daily recurrence
        next_daily = calculate_next_due_date(test_date, "daily")
        expected_daily = (date.fromisoformat(test_date) + timedelta(days=1)).strftime("%Y-%m-%d")
        assert next_daily == expected_daily
        
        # Weekly recurrence
        next_weekly = calculate_next_due_date(test_date, "weekly")
        expected_weekly = (date.fromisoformat(test_date) + timedelta(days=7)).strftime("%Y-%m-%d")
        assert next_weekly == expected_weekly
        
        # Monthly recurrence (approximately 30 days)
        next_monthly = calculate_next_due_date(test_date, "monthly")
        expected_monthly = (date.fromisoformat(test_date) + timedelta(days=30)).strftime("%Y-%m-%d")
        assert next_monthly == expected_monthly
    
    def test_recurring_task_completion_creates_new_instance(self):
        """Test that completing a recurring task creates a new instance."""
        # Create a recurring task
        recurring_task = Task(
            id=1,
            description="Weekly task",
            due_date="2026-01-01",
            recurrence="weekly"
        )

        # Add the task to the manager
        self.task_manager.add_task(recurring_task.description,
                                  due_date=recurring_task.due_date,
                                  recurrence=recurring_task.recurrence)

        # Verify the task was added
        tasks = self.task_manager.get_all_tasks()
        assert len(tasks) == 1
        original_task = tasks[0]
        assert original_task.recurrence == "weekly"

        # Complete the task
        new_task_id = self.task_manager.complete_task(1)

        # Verify the original task is marked complete and a new one was created
        tasks = self.task_manager.get_all_tasks()
        assert len(tasks) == 2

        # Find the completed and new tasks
        completed_task = next(t for t in tasks if t.id == 1)
        new_task = next(t for t in tasks if t.id == new_task_id)

        assert completed_task.completed is True
        assert new_task.completed is False
        assert new_task.description == "Weekly task"  # Same description
        assert new_task.recurrence == "weekly"  # Same recurrence
        assert new_task.due_date != "2026-01-01"  # New due date
        
    def test_backward_compatibility(self):
        """Test that tasks without due_date and recurrence still work."""
        # Create a task without due_date and recurrence (old format)
        old_format_task = Task(
            id=1,
            description="Old format task"
        )

        # Should not have due_date or recurrence
        assert old_format_task.due_date is None
        assert old_format_task.recurrence is None

        # Add to task manager
        self.task_manager.add_task(old_format_task.description)

        # Should work without errors
        tasks = self.task_manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Old format task"
        assert tasks[0].due_date is None
        assert tasks[0].recurrence is None
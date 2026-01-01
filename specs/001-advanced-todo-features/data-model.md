# Data Model: Advanced Todo Features

## Extended Task Model

The existing Task model will be extended to support the new advanced features:

```python
from dataclasses import dataclass
from typing import List, Optional
from datetime import date


@dataclass
class Task:
    """
    Represents a todo task with extended functionality for priorities, tags, due dates, and recurrence.
    """
    id: int
    description: str
    completed: bool = False
    created_at: str = None  # Format: YYYY-MM-DD
    priority: Optional[str] = None  # "high", "medium", "low", or None
    tags: List[str] = None  # List of tags, defaults to empty list
    due_date: Optional[str] = None  # Format: YYYY-MM-DD, optional
    recurrence: Optional[str] = None  # "daily", "weekly", "monthly", or None

    def __post_init__(self):
        """Initialize default values after object creation."""
        if self.created_at is None:
            self.created_at = date.today().strftime("%Y-%m-%d")

        if self.priority is None:
            self.priority = "medium"

        if self.tags is None:
            self.tags = []

        # Validate priority value
        if self.priority not in [None, "high", "medium", "low"]:
            raise ValueError(f"Priority must be 'high', 'medium', 'low', or None, got '{self.priority}'")

        # Validate tags
        if not isinstance(self.tags, list):
            raise TypeError("Tags must be a list of strings")

        for tag in self.tags:
            if not isinstance(tag, str):
                raise TypeError(f"Each tag must be a string, got {type(tag)}")
            if not tag.strip():
                raise ValueError("Tags cannot be empty or contain only whitespace")

        # Validate description
        if not self.description or not self.description.strip():
            raise ValueError("Description cannot be empty or contain only whitespace")

        # Validate due_date format if provided
        if self.due_date is not None:
            self._validate_date_format(self.due_date)

        # Validate recurrence value if provided
        if self.recurrence is not None:
            if self.recurrence not in ["daily", "weekly", "monthly"]:
                raise ValueError(f"Recurrence must be 'daily', 'weekly', 'monthly', or None, got '{self.recurrence}'")

    def _validate_date_format(self, date_str: str) -> None:
        """Validate that the date string is in YYYY-MM-DD format."""
        import re
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            raise ValueError(f"Date must be in YYYY-MM-DD format, got '{date_str}'")
        
        # Also validate that it's a real date
        try:
            year, month, day = map(int, date_str.split('-'))
            date(year, month, day)
        except ValueError:
            raise ValueError(f"'{date_str}' is not a valid date")
```

## Validation Rules from Requirements

1. **Due Date Validation**:
   - Format must be "YYYY-MM-DD"
   - Must represent a valid calendar date
   - Optional field (can be None)

2. **Recurrence Validation**:
   - Must be one of "daily", "weekly", "monthly", or None
   - Case-sensitive validation
   - Optional field (can be None)

3. **Backward Compatibility**:
   - New fields (due_date, recurrence) default to None
   - Existing tasks without these fields will work unchanged
   - JSON serialization/deserialization handles missing fields gracefully

## State Transitions

1. **Task Creation**:
   - New tasks can be created with due_date and/or recurrence
   - If not specified, these fields remain None

2. **Task Completion**:
   - When a recurring task is marked complete, a new instance is created
   - The new instance has the same title, description, priority, and tags
   - The new instance has an updated due date based on the recurrence rule
   - The original task is marked as completed

3. **Task Updates**:
   - Due dates and recurrence can be modified via update operations
   - Changes only affect future instances for recurring tasks
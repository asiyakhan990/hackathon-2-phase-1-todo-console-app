"""
Date utility functions for the Todo Console Application.

This module provides date-related functionality for:
- Date validation in YYYY-MM-DD format
- Date comparison for overdue detection
- Date calculations for recurrence patterns
"""
import re
from datetime import date, timedelta
from typing import Optional


def validate_date_format(date_str: str) -> bool:
    """
    Validate that the date string is in YYYY-MM-DD format and represents a valid date.
    
    Args:
        date_str: Date string in format YYYY-MM-DD
        
    Returns:
        True if the date format is valid and represents a real date
        
    Raises:
        ValueError: If the date format is invalid or date doesn't exist
    """
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        raise ValueError(f"Date must be in YYYY-MM-DD format, got '{date_str}'")
    
    # Also validate that it's a real date
    try:
        year, month, day = map(int, date_str.split('-'))
        date(year, month, day)
    except ValueError:
        raise ValueError(f"'{date_str}' is not a valid date")
    
    return True


def is_overdue(due_date: Optional[str]) -> bool:
    """
    Check if a task is overdue based on its due date.
    
    Args:
        due_date: Due date in format YYYY-MM-DD or None
        
    Returns:
        True if the task is overdue, False otherwise
    """
    if due_date is None:
        return False
    
    try:
        due = date.fromisoformat(due_date)
        today = date.today()
        return due < today
    except ValueError:
        # If the date is invalid, consider it not overdue
        return False


def is_due_today(due_date: Optional[str]) -> bool:
    """
    Check if a task is due today.
    
    Args:
        due_date: Due date in format YYYY-MM-DD or None
        
    Returns:
        True if the task is due today, False otherwise
    """
    if due_date is None:
        return False
    
    try:
        due = date.fromisoformat(due_date)
        today = date.today()
        return due == today
    except ValueError:
        # If the date is invalid, consider it not due today
        return False


def days_overdue(due_date: Optional[str]) -> int:
    """
    Calculate how many days a task is overdue.
    
    Args:
        due_date: Due date in format YYYY-MM-DD or None
        
    Returns:
        Number of days overdue (positive value) or 0 if not overdue
    """
    if due_date is None:
        return 0
    
    try:
        due = date.fromisoformat(due_date)
        today = date.today()
        delta = today - due
        return max(0, delta.days)
    except ValueError:
        # If the date is invalid, return 0
        return 0


def calculate_next_due_date(current_due_date: Optional[str], recurrence: Optional[str]) -> Optional[str]:
    """
    Calculate the next due date based on recurrence pattern.
    
    Args:
        current_due_date: Current due date in format YYYY-MM-DD or None
        recurrence: Recurrence pattern ('daily', 'weekly', 'monthly', or None)
        
    Returns:
        Next due date in format YYYY-MM-DD or None if no recurrence
    """
    if current_due_date is None or recurrence is None:
        return None
    
    try:
        current_date = date.fromisoformat(current_due_date)
        
        if recurrence == "daily":
            next_date = current_date + timedelta(days=1)
        elif recurrence == "weekly":
            next_date = current_date + timedelta(days=7)
        elif recurrence == "monthly":
            # For monthly recurrence, add approximately 30 days
            # Note: This is a simple approach; for more accurate month-to-month
            # recurrence, we'd need to handle month boundaries differently
            next_date = current_date + timedelta(days=30)
        else:
            # If recurrence is not one of the expected values, return None
            return None
        
        return next_date.strftime("%Y-%m-%d")
    except ValueError:
        # If the date is invalid, return None
        return None


def format_due_date_display(due_date: Optional[str]) -> str:
    """
    Format the due date for display purposes.
    
    Args:
        due_date: Due date in format YYYY-MM-DD or None
        
    Returns:
        Formatted string for display
    """
    if due_date is None:
        return ""
    
    if is_overdue(due_date):
        days = days_overdue(due_date)
        if days == 1:
            return f"[OVERDUE] Due: {due_date} (1 day overdue)"
        else:
            return f"[OVERDUE] Due: {due_date} ({days} days overdue)"
    elif is_due_today(due_date):
        return f"Due: Today ({due_date})"
    else:
        return f"Due: {due_date}"
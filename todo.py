#!/usr/bin/env python3
"""
Todo Console Application - Advanced Level Features

This application provides enhanced task management capabilities including
priorities, tags, search, filter, sort functionality, recurring tasks,
and due dates with overdue indicators.
"""

import sys
from src.cli.menu import Menu


def main():
    """Main entry point for the Todo Console Application."""
    print("Welcome to the Todo Console Application!")
    print("Type 'help' for available commands or 'exit' to quit.\n")

    menu = Menu()
    menu.run()


if __name__ == "__main__":
    main()
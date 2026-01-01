---
id: 1
title: Todo Console App Constitution Update
stage: constitution
date: 2025-12-28
surface: agent
model: 
feature: todo-console-app
branch: 
user: 
command: /sp.constitution update constitution file
labels: [constitution, todo-app, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
---

## Prompt

/sp.constitution update constitution file # Todo Console Application - Project Overview & Upgrade Constitution
# Date: December 28, 2025
# Current date used for development/demo: 2025-12-28

## 1. PROJECT OVERVIEW

Name:              Todo Console
Type:              Terminal-based Todo Manager
Language:          Python 3.9+
Dependencies:      Pure standard library only (no pip packages)
Persistence:       JSON file (todos.json)
Target users:      Developers, power users, terminal enthusiasts
Current state:     Basic MVP (add, list, update, delete, toggle complete)
Goal:              Upgrade to polished intermediate + advanced feature set
Purpose:           Hackathon/demo project showcasing clean architecture,
                   thoughtful UX in console, date-aware features and
                   backward compatibility
Wow factors:       Colored output, overdue alerts on startup,
                   automatic recurring task generation, quick stats

## 2. FEATURE PROGRESSION

Basic (already implemented)
├── Add task (description)
├── View all tasks
├── Update description
├── Delete task
└── Mark as complete/incomplete

Intermediate (next priority)
├── Priority levels: high / medium / low
├── Tags / categories (multiple)
├── Due dates (YYYY-MM-DD)
├── Search by keyword (description + tags)
├── Filter by status / priority / tag / due date
├── Sort by priority / due date / alphabetical / creation
└── Pretty colored table output (ANSI)

Advanced
├── Recurring tasks (daily, weekly, monthly, every X days, every weekday name)
├── Automatic next occurrence creation on completion
├── Startup reminders (overdue + due today)
├── Persistent unique IDs (not array index)
├── Simple undo (last 3–5 actions)
├── Basic statistics (completion rate, count by priority/tag)
└── Export to plain text

## 3. FINAL TARGET DATA MODEL

{
  "id":               int,               // unique persistent id
  "description":      str,
  "completed":        bool,
  "created_at":       "YYYY-MM-DD",      // ISO date string
  "priority":         "high"|"medium"|"low"|null,
  "tags":             [str, ...],
  "due_date":         "YYYY-MM-DD"|null,
  "recurrence":       "daily"|"weekly"|"monthly"|"every 3 days"|"every Monday"|null
}

## 4. IMPORTANT RULES

• Backward compatibility: must load old basic JSON files gracefully
• Migration strategy: add missing fields with defaults
• Zero external dependencies (except built-in modules)
• ANSI colors for output (manual escape codes)
• Robust input validation & user-friendly error messages
• Current date awareness: use 2025-12-28 for demo & overdue calculation
• Single main file preferred (todo.py) with clear internal modules/functions
• Good separation: data model, business logic, storage, presentation

## 5. IMPLEMENTATION GUIDELINES

• Use @dataclass for Task
• Main class: TaskManager (load/save/add/update/delete/toggle/search/filter/sort/undo/recurring/stats)
• Clear numbered menu + quick letter commands (a=add, d=done, s=search, etc.)
• Confirmation for dangerous actions (delete)
• Help screen / usage info
• Test data should include mix of basic + advanced tasks

## 6. FORBIDDEN (unless explicitly requested)

• External libraries (rich, click, tabulate, pendulum, etc.)
• Databases (sqlite, etc.)
• Web/GUI interface
• Breaking compatibility with old basic JSON format without migration

This document serves as single source of truth for both project vision and implementation rules.
Use it as system prompt / constitution when asking AI to generate/refactor code.

## Response snapshot

The Todo Console Application Constitution has been successfully updated with the following details:

**New Version**: 1.0.0 (initial version for this project)
**Version Bump Rationale**: This is the initial constitution for the Todo Console Application project, establishing the foundational principles and governance structure.

**Files flagged for manual follow-up**:
- `.specify/templates/plan-template.md` - needs to be updated to align with new principles
- `.specify/templates/spec-template.md` - needs to be updated to align with new principles  
- `.specify/templates/tasks-template.md` - needs to be updated to align with new principles

**Suggested commit message**: `docs: add initial constitution for Todo Console Application v1.0.0`

The constitution now includes 6 core principles based on the project specifications:
1. Pure Standard Library - using only Python standard library modules
2. Backward Compatibility - maintaining compatibility with older JSON formats
3. Clean Architecture - clear separation of concerns
4. User-Friendly Console UX - with colored output and intuitive commands
5. Robust Input Validation - with user-friendly error messages
6. Persistent Unique IDs - using integer IDs instead of array indices

The file has been written to `.specify/memory/constitution.md` with the Sync Impact Report included at the top.

## Outcome

- ✅ Impact: Created initial constitution for Todo Console Application project
- 🧪 Tests: No tests required for this documentation task
- 📁 Files: Updated .specify/memory/constitution.md with new constitution
- 🔁 Next prompts: Ready for feature specification based on updated constitution
- 🧠 Reflection: Process was systematic, following all required steps including template validation and consistency checks

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All steps completed successfully
- Prompt variant (if applicable): Standard constitution update prompt
- Next experiment (smallest change to try): Begin feature specification based on new constitution
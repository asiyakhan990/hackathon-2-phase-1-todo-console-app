<!--
SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
List of modified principles: All principles expanded with more detailed descriptions
Added sections: Technology Stack, Deliverables, Working Application Requirements, Basic Level Features
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: Constitution Check section should align with new principles (⚠ pending)
  - .specify/templates/spec-template.md: No changes required (✅ updated)
  - .specify/templates/tasks-template.md: No changes required (✅ updated)
  - .qwen/commands/*.toml: No changes required (✅ updated)
  - README.md: File does not exist (✅ updated)
Follow-up TODOs: None
-->

# The Evolution of Todo - Phase 1 Constitution

## Project Overview

**Project Name**: The Evolution of Todo - Phase 1: Todo-In Memory Python Console App

**Objective**: Build a command-line todo application that stores tasks in memory using Qwen and Spec-Kit Plus.

**Phase**: 1 - Basic Level Functionality

## Core Principles

### Adhere to Clean Code Practices
Maintain modular design, readable code, proper error handling, and PEP 8 compliance throughout the project. Code must be well-structured, maintainable, and follow Python best practices. All functions and classes should be properly documented with docstrings.

### Use Spec-Driven Development
Start with this constitution, generate iterative specs via Spec-Kit Plus, and track all versions in a 'specs_history' folder. All development must follow the spec-driven approach where specifications are created and refined before implementation. Each change must be documented and versioned.

### Leverage Qwen for Development
Use Qwen for refining specs, generating code snippets, and automation—document usage in Qwen.md. Qwen should be utilized for code generation, testing, and documentation. All interactions with Qwen should be tracked and documented for reproducibility.

### Keep the MVP Minimal
Only implement the 5 basic features; no advanced functionalities like persistence, priorities, or due dates. Focus on delivering a working MVP with core functionality before considering additional features. This ensures rapid development and validation of the concept.

### Follow Proper Project Structure
Use UV for dependency management, Python 3.13+, /src for code, and README.md for setup instructions. Maintain a clean project structure with proper separation of concerns. All source code must be in the /src directory with appropriate subdirectories for models, services, and CLI components.

### Maintain Quality Standards
Ensure all code is well-tested, documented, and follows best practices for maintainability. All features must have appropriate unit and integration tests. Code must be reviewed before merging, and all functionality must be verified through testing.

## Technology Stack

- **Dependency Management**: UV
- **Programming Language**: Python 3.13+
- **AI Assistant**: Qwen
- **Specification Management**: Spec-Kit Plus
- **Project Structure**: Standard Python project with /src directory

## Basic Level (Core Essentials)

These form the foundation - quick to build, essential for any MVP:

### 1. Add Task
- Create new todo items with title (required) and description (optional)
- Assign a unique ID (integer, starting from 1)
- Validate input to ensure required fields are provided

### 2. Delete Task
- Remove task from the list by its ID
- Confirm deletion to avoid accidents
- Handle invalid IDs gracefully

### 3. Update Task
- Modify existing task details (title and/or description) by ID
- Validate input to ensure required fields are provided
- Handle invalid IDs gracefully

### 4. View Task List
- Display all tasks with ID, title, description, and status
- Show status indicators: [ ] for incomplete, [x] for complete
- Format output in a user-friendly manner

### 5. Mark as Complete
- Toggle task completion status by ID
- Allow marking tasks as complete or incomplete
- Handle invalid IDs gracefully

## Technical Specifications

### Storage
- Use a list of dictionaries or a Task class in memory (e.g., {'id': int, 'title': str, 'description': str, 'complete': bool})
- No persistence - all data is stored in memory only
- Implement proper data validation and error handling

### CLI Interface
- Menu-driven loop with input() for commands (e.g., 'add', 'delete', 'update', 'view', 'mark', 'exit')
- Handle invalid inputs gracefully with appropriate error messages
- Provide clear instructions and feedback to the user

### Error Handling
- Graceful messages for non-existent IDs, empty lists, etc.
- Validate user input and provide helpful error messages
- Ensure the application doesn't crash on invalid input

### Dependencies
- No external dependencies beyond UV, Python 3.13+, Qwen, and Spec-Kit Plus
- Keep the application lightweight and focused on core functionality

## Deliverables

### GitHub Repository Contents
- Constitution file (this document)
- Specs history folder containing all specification files
- /src folder with Python source code
- README.md with setup instructions
- Qwen.md with Qwen instructions

### Working Console Application Requirements
- Adding tasks with title and description
- Listing all tasks with status indicators
- Updating task details
- Deleting tasks by ID
- Marking tasks as complete/incomplete

## Development Workflow

### Specification Phase
1. Use this constitution as the root prompt for Qwen to generate initial specs
2. Refine specs iteratively with Spec-Kit Plus, versioning each (e.g., spec_v1.md, spec_v2.md)
3. Ensure all specifications align with this constitution

### Implementation Phase
1. Generate code from final specs
2. Implement in /src following proper project structure
3. Ensure all changes align with this constitution—no scope creep
4. Write tests for each feature before implementation (TDD approach)

### Validation Phase
1. Test all 5 basic level features thoroughly
2. Verify the application works as expected in console environment
3. Ensure all requirements are met before considering the phase complete

## Governance

This constitution supersedes all other practices. Amendments require documentation and approval. All implementations must verify compliance with these principles. Complexity must be justified against the core principles.

**Version**: 1.1.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27

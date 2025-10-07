# src/main.py
from src.tasks.task_manager import display_tasks, filter_tasks, task_generator

# Seed data
tasks = [
    "Finish project",
    "Email client about deliverables",
    "Review pull requests",
    "Plan project kickoff",
    "Write unit tests",
]

# Show all tasks
display_tasks(tasks)

# Example: filter by keyword
filter_tasks(tasks, "project")

# Creating a generator for "project" tasks
project_tasks = task_generator(tasks, "project")
try:
    print("\nFirst matching task (lazy):")
    print(next(project_tasks))
except StopIteration:
    print("\nNo matching tasks in generator.")
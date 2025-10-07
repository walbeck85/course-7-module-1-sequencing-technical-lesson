# src/tasks/task_manager.py

def display_tasks(task_list):
    """Print tasks in a numbered list."""
    print("\nCurrent To-Do List:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def filter_tasks(task_list, keyword):
    """Filter tasks by keyword (case-insensitive) and display results."""
    filtered = [t for t in task_list if keyword.lower() in t.lower()]
    if not filtered:
        print(f"\nNo tasks found for '{keyword}'.")
    else:
        print(f"\nTasks matching '{keyword}':")
        display_tasks(filtered)

def task_generator(task_list, keyword):
    """Yield matching tasks lazily (generator expression)."""
    return (t for t in task_list if keyword.lower() in t.lower())
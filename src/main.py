from tasks.task_manager import TaskManager

# Initial list of tasks (students will enhance this later)
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]

task_manager = TaskManager(tasks)

print("\nAll Tasks:")
task_manager.display_tasks()

# Filtering is not yet implemented (students will add it)
print("\nFiltered Tasks: (Not Implemented Yet)")

# Generators are not yet implemented (students will add them)
print("\nLazy Evaluation: (Not Implemented Yet)")

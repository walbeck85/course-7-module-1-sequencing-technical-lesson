class TaskManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def display_tasks(self):
        """Displays the list of tasks."""
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def filter_tasks(self, keyword):
        """Placeholder for filtering tasks (students will implement)."""
        print(f"\nFiltering for '{keyword}' is not yet implemented.")

    def task_generator(self, keyword):
        """Placeholder for generator-based filtering (students will implement)."""
        print(f"\nLazy evaluation for '{keyword}' is not yet implemented.")

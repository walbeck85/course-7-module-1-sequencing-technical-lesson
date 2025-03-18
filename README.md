# Technical Lesson: Sequencing

## Learning Goals

- Utilize **List Comprehensions** to filter, transform, and generate new lists efficiently.
- Apply **Generator Expressions** for memory-efficient sequence processing.
- Implement **state updates** in Python applications by modifying and managing lists effectively.
- Explore real-world applications of sequence processing for **scalability and performance**.

## Introduction

In Python, sequences such as **lists** play a crucial role in data manipulation. However, handling large sequences efficiently requires **optimized processing techniques**. This lesson will introduce **List Comprehensions** and **Generator Expressions**, two powerful tools that enhance performance while keeping the code concise.

Let's consider a **task management application** where users maintain a to-do list. The application currently supports:

- Displaying tasks stored in a list.
- Adding new tasks dynamically.

However, the application still lacks:

- Filtering tasks based on user-defined criteria (**List Comprehensions**).
- Processing large datasets efficiently (**Generator Expressions**).

To address these issues, we will:

1. **Filter tasks** using List Comprehensions.
2. **Optimize memory usage** with Generator Expressions.
3. **Manage dynamic state updates** without modifying the original list.

## Code Along

### Setting Up the Project

To get started, clone this repository and set up the environment:

```sh
git clone <repo-url>
cd sequencing-lesson
pip install -r requirements.txt
```

Now, let's define a list of tasks in Python:

```python
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]
```

### Filtering Tasks with List Comprehensions

List Comprehensions allow us to create a new list based on a condition efficiently.

#### Example:

```python
def filter_tasks(task_list, keyword):
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"\nTasks matching '{keyword}':")
    print(filtered)

filter_tasks(tasks, "project")
```

- Uses a **List Comprehension** to filter tasks that contain a specific keyword.
- Enhances readability and efficiency compared to traditional loops.

### Processing Large Datasets with Generator Expressions

For large datasets, **storing everything in memory can be inefficient**. **Generator Expressions** process data lazily, yielding results one at a time.

#### Example:

```python
def task_generator(task_list, keyword):
    return (task for task in task_list if keyword.lower() in task.lower())

# Creating a generator for "project" tasks
project_tasks = task_generator(tasks, "project")

# Retrieving tasks lazily
print(next(project_tasks))  # Output: 'Finish project'
```

- Uses a **Generator Expression** to process tasks **lazily**, reducing memory usage.

### State Management with Filtered Tasks

Instead of modifying the original list, store filtered results separately.

#### Example:

```python
filtered_tasks = [task for task in tasks if "project" in task.lower()]
print("\nUpdated To-Do List:", filtered_tasks)
```

- **List comprehensions** provide a dynamic, immutable filtering process.

## Best Practices for Sequence Processing

- **Use comments** to explain logic for future maintainability.
- **Optimize filtering** with List Comprehensions for readability.
- **Ensure memory efficiency** with Generator Expressions.
- **Handle edge cases**, such as when no results match the criteria.

#### Example:

```python
def filter_tasks(task_list, keyword):
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    if not filtered:
        print(f"\nNo tasks found for '{keyword}'.")
    else:
        print(f"\nTasks matching '{keyword}':")
        print(filtered)
```

- Prevents UI issues when no matching tasks are found.

## Conclusion

By mastering **Sequences, List Comprehensions, and Generator Expressions**, developers can:

- Optimize sequence processing for efficiency.
- Enhance memory management using generators.
- Improve application scalability with lazy evaluation.


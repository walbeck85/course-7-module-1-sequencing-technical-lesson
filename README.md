# Technical Lesson: Sequencing

## Learning Goals

- Utilize **List Comprehensions** to filter, transform, and generate new lists efficiently.
- Apply **Generator Expressions** for memory-efficient sequence processing.
- Implement **state updates** in Python applications by modifying and managing lists effectively.
- Explore real-world applications of sequence processing for **scalability and performance**.

## Introduction

In Python, sequences such as **lists** play a crucial role in data manipulation. However, handling large sequences efficiently requires **optimized processing techniques**. This lesson will introduce **List Comprehensions** and **Generator Expressions**, two powerful tools that enhance performance while keeping the code concise.

## Task 1: Determine the Problem

Let's consider a **task management application** where users maintain a to-do list. The application currently supports:

- Displaying tasks stored in a list.
- Adding new tasks dynamically.

However, the application still lacks:

- Filtering tasks based on user-defined criteria (**List Comprehensions**).
- Processing large datasets efficiently (**Generator Expressions**).

## Task 2: Determine the Design

To address these issues, we will:

1. **Filter tasks** using List Comprehensions.
2. **Optimize memory usage** with Generator Expressions.
3. **Manage dynamic state updates** without modifying the original list.

## Task 3: Develop, Test, and Refine the Code

### Setting Up the Project

To get started, clone this repository:

```sh
git clone <repo-url>
cd course-7-module-1-sequencing-technical-lesson
```

Install dependencies using either:

```
pipenv install
pipenv shell
```

or:

```
pip install -r requirements.txt
```

The initial list of tasks is defined in `main.py`, where you can test out the functions we'll build:

```python
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]
```

### Step 1: Create a Feature Branch for Filtering Tasks

```bash
git checkout -b feature-filter-tasks
```

### Step 2: Display Existing Tasks

In `src/tasks/task_manager.py`, add functionality to the `display_tasks` function.

This function should print out each task in the list, with a cooresponding number:

```python
def display_tasks(task_list):
    print("\nCurrent To-Do List:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")
```

Test out the function by running `src/main.py`. The below code is already implemented for you:

```python
from tasks.task_manager import display_tasks, filter_tasks, task_generator

# Initial list of tasks
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]

print("\nAll Tasks:")
display_tasks(tasks)
```

To run `main.py`, run the command below in the terminal while in the virtual environment:

```bash
python src/main.py
```

### Step 3: Filtering Tasks with List Comprehensions

List Comprehensions allow us to create a new list based on a condition efficiently.

Implement the functionality for the `filter_tasks` function in `task_manager.py`

```python
def filter_tasks(task_list, keyword):
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"\nTasks matching '{keyword}':")
    display_tasks(filtered)
```

Next, test this function by adding the code below to `main.py`:

```python
filter_tasks(tasks, "project")
```

Run `main.py` in the terminal to test your code:

```bash
python src/main.py
```

### Step 4: Processing Tasks Using a Generator Expression

For large datasets, **storing everything in memory can be inefficient**. **Generator Expressions** process data lazily, yielding results one at a time.

Implement the `task_generator` function in `task_manager.py`:

```python
def task_generator(task_list, keyword):
    return (task for task in task_list if keyword.lower() in task.lower())
```

In `main.py`, test your code by implementing:

```python
# Creating a generator for "project" tasks
project_tasks = task_generator(tasks, "project")

# Retrieving tasks lazily
print(next(project_tasks))  # Output: 'Finish project'
```

Run `main.py` to test the output:

```bash
python src/main.py
```

### Step 5: Push and Merge Feature

```bash
git commit -am "Implement task filtering with List Comprehensions"
git push origin feature-filter-tasks
```

Create a Pull Request (PR) on GitHub. Merge the PR into the main branch of your forked repo after review.

Then, clean up your local git repo to match your remote repo:

```bash
git checkout main
git pull origin main
git branch -d feature-filter-tasks
```

## Task 4: Document and Maintain

- **Use comments** to explain logic for future maintainability.
- **Ensure memory efficiency** with Generator Expressions.
- **Handle edge cases**, such as when no results match the criteria.
- **Optimize filtering** with List Comprehensions for readability.

#### Example of Enhancing Filter for Readability:

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


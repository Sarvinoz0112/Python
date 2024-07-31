def add_task(tasks, task):
    """Adds a task to the list of tasks."""
    tasks.append(task)
    print(f"Task added: {task}")

if __name__ == "__main__":
    tasks = []
    add_task(tasks, "Reading")
    add_task(tasks, "Running")
    print("Current tasks:", tasks)

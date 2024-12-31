# task_manager.py

# A list to store tasks. Each task is a dictionary with 'description' and 'status'.
tasks = []

def add_task(description):
    """
    Add a new task to the to-do list.
    """
    task = {"description": description, "status": "not done"}
    tasks.append(task)
    return f"Task added: '{description}'"

def mark_task_done(index):
    """
    Mark a task as done by its index in the list.
    """
    if 0 <= index < len(tasks):  # Ensure the index is valid
        tasks[index]["status"] = "done"
        return f"Task marked as done: '{tasks[index]['description']}'"
    else:
        return "Invalid task index!"

def view_pending_tasks():
    """
    Return all tasks that are not marked as done.
    """
    pending = [f"{i}. {task['description']}" for i, task in enumerate(tasks) if task["status"] == "not done"]
    return pending if pending else ["No pending tasks!"]

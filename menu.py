# menu.py
from task_manager import add_task, mark_task_done, view_pending_tasks

def display_menu():
    """
    Display the CLI menu for the user to interact with the application.
    """
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. View Pending Tasks")
    print("4. Exit")

def handle_choice(choice):
    """
    Handle user choice and call the corresponding function.
    """
    if choice == "1":
        description = input("Enter the task description: ").strip()
        print(add_task(description))
    elif choice == "2":
        try:
            index = int(input("Enter the index of the task to mark as done: ").strip())
            print(mark_task_done(index))
        except ValueError:
            print("Please enter a valid number!")
    elif choice == "3":
        print("\nPending Tasks:")
        for task in view_pending_tasks():
            print(task)
    elif choice == "4":
        print("Exiting the To-Do List Application. Goodbye!")
        return False
    else:
        print("Invalid choice! Please select a valid option.")
    return True

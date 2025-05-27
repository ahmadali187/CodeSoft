import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")
    else:
        print("Empty task not added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["completed"] else "✘"
        print(f"{i}. [{status}] {t['task']}")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to toggle complete status: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]
            status = "completed" if tasks[task_num - 1]["completed"] else "not completed"
            print(f"Task '{tasks[task_num - 1]['task']}' marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task complete/incomplete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

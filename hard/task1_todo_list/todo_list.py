"""
Task 1: Command-Line To-Do List Manager
Author: Himani Thakur
Description:
    A terminal-based task management application that persists to-do items
    in a JSON file. Supports adding, displaying, marking tasks complete,
    and deleting tasks with input validation and empty-state handling.
"""

import json
import os
from datetime import datetime

DEFAULT_TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo_items.json")


def load_tasks(filepath: str = DEFAULT_TODO_FILE) -> list[dict]:
    """
    Load tasks list from a JSON file.
    Returns an empty list if the file is missing or contains invalid data.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(filepath: str, tasks: list[dict]) -> bool:
    """
    Save the list of tasks to a JSON file.
    Returns True upon success, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, mode="w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except OSError as err:
        print(f"[Storage Error] Could not save tasks: {err}")
        return False


def add_task(tasks: list[dict], title: str) -> tuple[bool, str]:
    """
    Append a new task item to the tasks list.
    Returns (success, message).
    """
    cleaned = title.strip()
    if not cleaned:
        return False, "Task title cannot be empty."

    task = {
        "title": cleaned,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    return True, f"Task '{cleaned}' added successfully."


def mark_complete(tasks: list[dict], task_number: int) -> tuple[bool, str]:
    """
    Mark a task as completed using 1-based index.
    Returns (success, message).
    """
    if not tasks:
        return False, "Your to-do list is currently empty."

    if task_number < 1 or task_number > len(tasks):
        return False, f"Invalid task number {task_number}. Valid range is 1 to {len(tasks)}."

    index = task_number - 1
    if tasks[index]["completed"]:
        return False, f"Task #{task_number} is already marked as completed."

    tasks[index]["completed"] = True
    return True, f"Task #{task_number} ('{tasks[index]['title']}') marked as completed!"


def delete_task(tasks: list[dict], task_number: int) -> tuple[bool, str]:
    """
    Delete a task using 1-based index.
    Returns (success, message).
    """
    if not tasks:
        return False, "Your to-do list is currently empty."

    if task_number < 1 or task_number > len(tasks):
        return False, f"Invalid task number {task_number}. Valid range is 1 to {len(tasks)}."

    removed = tasks.pop(task_number - 1)
    return True, f"Task #{task_number} ('{removed['title']}') was removed."


def display_tasks(tasks: list[dict]):
    """Print the formatted to-do list."""
    print("\n" + "=" * 55)
    print("                    TO-DO LIST                  ")
    print("=" * 55)

    if not tasks:
        print("  (Your list is empty! Add a new task to get started.)")
        print("=" * 55)
        return

    for idx, item in enumerate(tasks, start=1):
        status_icon = "[X] Completed" if item.get("completed", False) else "[ ] Pending  "
        created = item.get("created_at", "")
        print(f" {idx:2d}. {status_icon} | {item['title']} (Added: {created})")

    print("-" * 55)
    completed_count = sum(1 for t in tasks if t.get("completed", False))
    print(f" Total: {len(tasks)} | Completed: {completed_count} | Pending: {len(tasks) - completed_count}")
    print("=" * 55)


def main():
    storage_path = DEFAULT_TODO_FILE
    tasks = load_tasks(storage_path)

    # Initial sample item if clean start
    if not tasks and not os.path.exists(storage_path):
        add_task(tasks, "Review Python internship syllabus")
        add_task(tasks, "Run unit test suite")
        save_tasks(storage_path, tasks)

    print("=" * 55)
    print("        COMMAND-LINE TO-DO LIST APPLICATION      ")
    print("=" * 55)

    while True:
        print("\n--- Action Menu ---")
        print("1. View Tasks")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            title = input("\nEnter task description: ")
            success, msg = add_task(tasks, title)
            print(f">>> {msg}")
            if success:
                save_tasks(storage_path, tasks)

        elif choice == "3":
            display_tasks(tasks)
            if not tasks:
                continue
            val = input("\nEnter task number to mark complete: ").strip()
            try:
                num = int(val)
                success, msg = mark_complete(tasks, num)
                print(f">>> {msg}")
                if success:
                    save_tasks(storage_path, tasks)
            except ValueError:
                print("[Error] Please enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            if not tasks:
                continue
            val = input("\nEnter task number to delete: ").strip()
            try:
                num = int(val)
                success, msg = delete_task(tasks, num)
                print(f">>> {msg}")
                if success:
                    save_tasks(storage_path, tasks)
            except ValueError:
                print("[Error] Please enter a valid number.")

        elif choice in ("5", "exit", "quit", "q"):
            print("To-do items saved. Goodbye!")
            break
        else:
            print("[Invalid Choice] Please select 1 through 5.")


if __name__ == "__main__":
    main()

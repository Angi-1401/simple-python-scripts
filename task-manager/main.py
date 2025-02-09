import os
import re


def clear_console_and_wait():
    input("\nPress any key to continue...")
    os.system("cls")


def validate_input(descriptor):
    regex = r"^[a-zA-Z0-9\s]+$"

    while True:
        user_input = input(f"Enter {descriptor}: ")
        if re.match(regex, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.\n")


class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Name: {self.name}\nDescription: {self.description}\nStatus: {status}"

    def toggle_completion(self):
        self.completed = not self.completed


class TaskManager:
    def __init__(self):
        self.filename = os.path.join(os.path.dirname(__file__), "database.txt")
        self.tasks = self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                tasks = []
                for line in file:
                    name, description, completed = line.strip().split(",")
                    tasks.append(Task(name, description, completed == "True"))
                return tasks
        except FileNotFoundError:
            return []

    def save(self):
        try:
            with open(self.filename, "w") as file:
                for task in self.tasks:
                    file.write(
                        f"{task.name},{task.description},{task.completed}\n"
                    )
        except Exception as error:
            print(f"Error saving tasks: {error}")

    def count_all_tasks(self):
        return len(self.tasks)

    def count_completed_tasks(self):
        return sum(1 for task in self.tasks if task.completed)

    def count_pending_tasks(self):
        return len(self.tasks) - self.count_completed_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save()
        print("Task added successfully!\n")

    def delete_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]
        self.save()
        print("Task deleted successfully!\n")

    def modify_task(self, task_name, new_name, new_description):
        for task in self.tasks:
            if task.name == task_name:
                task.name = new_name
                task.description = new_description
                self.save()
                print("Task modified successfully!\n")
                return

    def change_status(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.toggle_completion()
                self.save()
                print("Status changed successfully!\n")
                return

    def list_all_tasks_names(self):
        return [task.name for task in self.tasks]

    def print_all_tasks_names(self):
        for task in self.tasks:
            print(f"Name: {task.name}")

    def print_all_tasks(self):
        for task in self.tasks:
            print(f"Name: {task.name}")
            print(f"Description: {task.description}")
            print(f"Status: {'Completed' if task.completed else 'Pending'}")
            print("\n")

    def print_completed_tasks(self):
        for task in self.tasks:
            if task.completed:
                print(f"Name: {task.name}")
                print(f"Description: {task.description}")
                print(f"Status: {'Completed' if task.completed else 'Pending'}")
                print("\n")

    def print_pending_tasks(self):
        for task in self.tasks:
            if not task.completed:
                print(f"Name: {task.name}")
                print(f"Description: {task.description}")
                print(f"Status: {'Completed' if task.completed else 'Pending'}")
                print("\n")


task_manager = TaskManager()

while True:
    print("----------------------")
    print("|    Task Manager    |")
    print("----------------------")
    print("\n")
    print(f"All tasks: {task_manager.count_all_tasks()}")
    print(f"Completed tasks: {task_manager.count_completed_tasks()}")
    print(f"Pending tasks: {task_manager.count_pending_tasks()}")
    print("\n")
    print("----------------------")
    print("|    Menu Options    |")
    print("----------------------")
    print("\n")
    print("1. Add task")
    print("2. Delete task")
    print("3. Modify task")
    print("4. Change status")
    print("5. List all tasks")
    print("6. List completed tasks")
    print("7. List pending tasks")
    print("8. Exit")
    print("\n")

    choice = input(">_ ")
    print("\n\n")

    if choice == "1":
        print("Add task:\n")

        name = validate_input("Name")

        if name in task_manager.list_all_tasks_names():
            print("Task already exists!\n")
            clear_console_and_wait()
            continue

        description = validate_input("Description")

        task = Task(name, description)
        task_manager.add_task(task)

        clear_console_and_wait()

    elif choice == "2":
        print("Delete task:\n")

        if task_manager.count_all_tasks() == 0:
            print("No tasks to delete!\n")
            clear_console_and_wait()
            continue

        task_manager.print_all_tasks_names()

        task_name = validate_input("Name")

        if task_name not in task_manager.list_all_tasks_names():
            print("Task not found!\n")
            clear_console_and_wait()
            continue

        task_manager.delete_task(task_name)

        clear_console_and_wait()

    elif choice == "3":
        print("Modify task:\n")

        if task_manager.count_all_tasks() == 0:
            print("No tasks to modify!\n")
            clear_console_and_wait()
            continue

        task_manager.print_all_tasks_names()

        task_name = validate_input("Name")

        if task_name not in task_manager.list_all_tasks_names():
            print("Task not found!\n")
            clear_console_and_wait()
            continue

        new_name = validate_input("New Name")
        new_description = validate_input("New Description")

        task_manager.modify_task(task_name, new_name, new_description)

        clear_console_and_wait()

    elif choice == "4":
        print("Change status:\n")

        if task_manager.count_all_tasks() == 0:
            print("No tasks to change status!\n")
            clear_console_and_wait()
            continue

        task_manager.print_all_tasks_names()

        task_name = validate_input("Name")

        if task_name not in task_manager.list_all_tasks_names():
            print("Task not found!\n")
            clear_console_and_wait()
            continue

        task_manager.change_status(task_name)

        clear_console_and_wait()

    elif choice == "5":
        print("All tasks:\n")
        task_manager.print_all_tasks()

        clear_console_and_wait()

    elif choice == "6":
        print("Completed tasks:\n")
        task_manager.print_completed_tasks()

        clear_console_and_wait()

    elif choice == "7":
        print("Pending tasks:\n")
        task_manager.print_pending_tasks()

        clear_console_and_wait()

    elif choice == "8":
        break

    else:
        print("Invalid choice. Please try again.\n")
        clear_console_and_wait()

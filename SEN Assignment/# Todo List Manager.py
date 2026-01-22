# Todo List Manager
# Simple CLI-based application

FILE_NAME = "tasks.txt"


class TodoManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(FILE_NAME, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            self.save_tasks()
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")


def main():
    manager = TodoManager()

    while True:
        print("\n--- Todo List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            manager.update_task(index, new_task)

        elif choice == "4":
            manager.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
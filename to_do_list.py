class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Not Completed'}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}: {task}")

    def update_task(self, index, title=None, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if completed is not None:
                self.tasks[index].completed = completed

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.title},{task.description},{task.completed}\n")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    title, description, completed = line.strip().split(',')
                    task = Task(title, description)
                    task.completed = completed.lower() == 'true'
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No previous tasks found.")
def main():
    todo_list = TodoList()
    todo_list.load_tasks("tasks.txt")

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            completed_input = input("Is it completed? (y/n): ")
            completed = completed_input.lower() == 'y'
            todo_list.update_task(index, title or None, description or None, completed)

        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)

        elif choice == "5":
            todo_list.save_tasks("tasks.txt")

        elif choice == "6":
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


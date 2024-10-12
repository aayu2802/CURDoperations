class Task:
    def __init__(self, id, title, description, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"Task ID: {self.id} | Title: {self.title} | Description: {self.description} | Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def create_task(self):
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        new_task = Task(self.task_id_counter, title, description)
        self.tasks.append(new_task)
        self.task_id_counter += 1
        print("\nTask created successfully!\n")

    def read_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
        else:
            print("\nList of Tasks:")
            for task in self.tasks:
                print(task)
            print()

    def update_task(self):
        self.read_tasks()
        task_id = int(input("Enter the ID of the task you want to update: "))
        task = self.find_task_by_id(task_id)
        if task:
            print(f"\nUpdating Task ID: {task_id}")
            task.title = input("Enter new title: ")
            task.description = input("Enter new description: ")
            task.status = input("Enter new status (Pending/Completed): ")
            print("\nTask updated successfully!\n")
        else:
            print("\nTask not found.\n")

    def delete_task(self):
        self.read_tasks()
        task_id = int(input("Enter the ID of the task you want to delete: "))
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print("\nTask deleted successfully!\n")
        else:
            print("\nTask not found.\n")

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def menu(self):
        while True:
            print("Task Manager Menu")
            print("1. Create Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.create_task()
            elif choice == '2':
                self.read_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("\nExiting Task Manager. Goodbye!")
                break
            else:
                print("\nInvalid choice, please try again.\n")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.menu()

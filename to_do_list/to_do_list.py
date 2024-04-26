class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task description: ")
        self.tasks.append({"description": task, "completed": False})
        print(f"Task \"{task}\" added successfully")

    def view_tasks(self):
        print("\n===== Tasks =====")
        for i, task in enumerate(self.tasks):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['description']}")

    def complete_task(self):
        self.view_tasks()
        index = int(input("Enter the index of the task to mark as completed: "))
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid index.")

    def menu(self):
        choices = {
            "1": self.add_task,
            "2": self.complete_task,
            "3": self.view_tasks,
        }

        while True:
            print("\n===== To-Do List Menu =====\n"
                  "1. Add a task\n"
                  "2. Mark a task as completed\n"
                  "3. View all tasks\n"
                  "4. Quit")

            choice = input("Enter your choice (1-4): ")

            if choice == "4":
                print("Exiting the program. Goodbye!")
                break

            if choice not in choices.keys():
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            choices[choice]()


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()



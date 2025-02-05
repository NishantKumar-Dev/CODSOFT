import json

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"✅ Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "✔️" if task["completed"] else "❌"
                print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print("✅ Task marked as completed!")
        else:
            print("⚠️ Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"🗑️ Task removed: {removed_task['task']}")
        else:
            print("⚠️ Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\n📌 To-Do List Menu 📌")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task as Completed")
        print("4️⃣ Remove Task")
        print("5️⃣ Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            todo.mark_completed(task_number)
        elif choice == "4":
            todo.view_tasks()
            task_number = int(input("Enter task number to remove: "))
            todo.remove_task(task_number)
        elif choice == "5":
            print("👋 Exiting To-Do List. Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

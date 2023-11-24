import json
import os
class TodoList:
    def __init__(self):
        self.tasks = []
    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)
    def display_tasks(self):
        print("\n=== Your To-Do List ===")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")
        print("=======================")
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")
    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task index!")
    def update_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task
            print(f"Task updated successfully!")
        else:
            print("Invalid task index!")
def main():
    todo_list = TodoList()
    todo_list.load_tasks()
    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Save and Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '5':
            todo_list.save_tasks()
            print("To-Do List saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

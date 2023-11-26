import os
from datetime import datetime

# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

# Function to view the to-do list
def view_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task['title']} - {task['status']} - {task['timestamp']}")

# Function to add a task to the to-do list
def add_task(todo_list):
    title = input("Enter task title: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {"title": title, "status": "Not Completed", "timestamp": timestamp}
    todo_list.append(task)
    print("Task added successfully.")

# Function to update the status of a task
def update_task_status(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["status"] = input("Enter the new status (e.g., Completed, In Progress): ")
            print("Task status updated successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Function to delete a task from the to-do list
def delete_task(todo_list):
    view_todo_list(todo_list)
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= index < len(todo_list):
            del todo_list[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Function to save the to-do list to a text file
def save_to_file(todo_list, filename="todo_list.txt"):
    with open(filename, "w") as file:
        for task in todo_list:
            file.write(f"{task['title']} - {task['status']} - {task['timestamp']}\n")

# Function to load the to-do list from a text file
def load_from_file(filename="todo_list.txt"):
    todo_list = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) == 3:
                    task = {"title": parts[0], "status": parts[1], "timestamp": parts[2]}
                    todo_list.append(task)
    return todo_list

# Main function to run the To-Do List application
def main():
    todo_list = load_from_file()

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            update_task_status(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            save_to_file(todo_list)
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

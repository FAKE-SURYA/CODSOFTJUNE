todo_list = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"✅ Task added: {task}")

def view_tasks():
    if not todo_list:
        print("📝 No tasks yet.")
    else:
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = todo_list.pop(task_num - 1)
        print(f"❌ Task removed: {removed}")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice.")


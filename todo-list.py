tasks = []

def show_menu():
    print("\n----- TO-DO LIST APP -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ '{task}' added to list!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"🗑️ Removed: {removed}")
            else:
                print("Invalid number!")

    elif choice == "4":
        print("👋 Exiting... Bye!")
        break

    else:
        print("❌ Invalid choice! Please try again.")

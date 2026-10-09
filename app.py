tasks = []

while True:
    print("\n--- To Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        print("\nYour Current Tasks:")
        for index, task in enumerate(task, 1):
            print(f"{index}. {task}")
        if not tasks:
            print("No tasks yest!")

    elif choice == '2':
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"'{new_task}' has been added.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please pick 1,2 or 3.")

print("===== To-Do List =====")

# สร้าง List ว่าง
todo_list = []

while True:
    print("\n========== MENU ==========")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Exit")

    choice = input("Choose menu (1-4): ")

    # เพิ่มรายการงาน
    if choice == "1":
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added successfully!")

    # ดูรายการงานทั้งหมด
    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(todo_list):
                print(f"{i}. {task}")

    # ลบงานที่ทำเสร็จแล้ว
    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to complete.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(todo_list):
                print(f"{i}. {task}")

            index = int(input("Enter task index to remove: "))

            if 0 <= index < len(todo_list):
                completed = todo_list.pop(index)
                print(f"Task '{completed}' completed and removed.")
            else:
                print("Invalid index.")

    # ออกจากโปรแกรม
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid menu. Please try again.")
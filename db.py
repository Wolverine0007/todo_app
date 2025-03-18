import mysql.connector as mysql

# ✅ Establish database connection
con = mysql.connect(host="localhost", user="root", passwd="", database="TODOAPP")

# ✅ Create cursor object
cursor = con.cursor()

while True:
    print("\n🔹 Task Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        con.commit()  # Commit the changes to the database
        print("✅ Task added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if not tasks:
            print("📂 No tasks found.")
        else:
            print("\n📌 Task List:")
            for task in tasks:
                print(f"- {task[1]}")  # Assuming task[1] is the task description

    elif choice == "3":
        task_id = input("Enter task ID to update: ")
        new_task = input("Enter new task: ")
        cursor.execute("UPDATE tb_todo SET task = %s WHERE id = %s", (new_task, task_id))
        con.commit()
        print("✅ Task updated successfully!")

    elif choice == "4":
        task_id = input("Enter task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (task_id,))
        con.commit()
        print("❌ Task deleted successfully!")

    elif choice == "5":
        print("👋 Exiting Task Manager...")
        break  # Exit the loop

    else:
        print("❌ Invalid choice. Please try again.")

# ✅ Close database connection
cursor.close()
con.close()

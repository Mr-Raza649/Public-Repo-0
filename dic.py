students = {}

while True:
    print("\nOptions: add / update / addmarks / view / average / delete / lastdelete / backup / reset / quit")
    choice = input("Choose: ").lower()

    # 1️⃣ ADD STUDENT
    if choice == "add":
        name = input("Student name: ")
        age = int(input("Age: "))

        if name in students:
            print("Student already exists!")
        else:
            students[name] = {
                "age": age,
                "subjects": {}
            }
            print("Student added successfully!")

    # 2️⃣ UPDATE AGE (uses update())
    elif choice == "update":
        name = input("Student name: ")

        if name in students:
            new_age = int(input("New age: "))
            students[name].update({"age": new_age})
            print("Age updated!")
        else:
            print("Student not found.")

    # 3️⃣ ADD SUBJECT MARKS (uses setdefault())
    elif choice == "addmarks":
        name = input("Student name: ")

        if name in students:
            subject = input("Subject: ")
            marks = int(input("Marks: "))

            students[name]["subjects"].setdefault(subject, marks)
            print("Marks added!")
        else:
            print("Student not found.")

    # 4️⃣ VIEW ALL (uses items())
    elif choice == "view":
        if not students:
            print("No students found.")
        else:
            for name, info in students.items():
                print(f"\n{name} (Age: {info.get('age')})")
                for sub, mark in info["subjects"].items():
                    print(f"  {sub}: {mark}")

    # 5️⃣ CALCULATE AVERAGE (uses values())
    elif choice == "average":
        name = input("Student name: ")

        if name in students:
            marks = students[name]["subjects"].values()

            if marks:
                avg = sum(marks) / len(marks)
                print("Average:", avg)
            else:
                print("No subjects found.")
        else:
            print("Student not found.")

    # 6️⃣ DELETE STUDENT (uses pop())
    elif choice == "delete":
        name = input("Student name: ")

        removed = students.pop(name, None)

        if removed:
            print("Student deleted.")
        else:
            print("Student not found.")

    # 7️⃣ DELETE LAST INSERTED (uses popitem())
    elif choice == "lastdelete":
        if students:
            last = students.popitem()
            print("Last inserted student removed:", last)
        else:
            print("No students to remove.")

    # 8️⃣ BACKUP DATA (uses copy())
    elif choice == "backup":
        backup_students = students.copy()
        print("Backup created successfully.")

    # 9️⃣ RESET SYSTEM (uses clear())
    elif choice == "reset":
        students.clear()
        print("All student data cleared.")

    # 🔟 DEMO fromkeys()
    elif choice == "quit":
        print("Creating demo template using fromkeys() before exit...")
        template = dict.fromkeys(["Math", "English", "Science"], 0)
        print("Template subjects:", template)
        print("Goodbye!")
        break

    else:
        print("Invalid option.")

student_set = set()
teacher_set = set()

def add_single_student():
    try:
        person_set = input("Which set to add student to? (student/teacher): ").lower()
        name = input("Enter the name: ").strip()
        if name:
            if person_set == "student":
                student_set.add(name)
                print(f"\n{name} added to Student Set. \n")
            elif person_set == "teacher":
                teacher_set.add(name)
                print(f"\n{name} added to teacher Set. \n")
            else:
                print("Invalid Set name: ")
        else:
            print("No name entered. ")
            
    except Exception as e:
        print(f"An error occurred: {e}")

def add_multiple_students():
    try:
        person_set = input("Which set to add students to? (student/teacher): ").lower()
        names = input("Enter the names separated by comma: ").strip().split(",")
        names = [name.strip() for name in names if name.strip()]
        
        if not names:
            print("No valid names entered. ")
            return
        
        if person_set == "student":
            student_set.update(names)
            print(f"\n{len(names)} students added to Student Set. \n")
        elif person_set == "teacher":
            teacher_set.update(names)
            print(f"\n{len(names)} teachers added to Teacher Set. \n")
        else:
            print("Invalid Set name: ")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
def view_all_students():
    set_name = input("Enter set name to view all members (student/teacher): ")
    if not set_name:
        print("No set name entered. ")
        return
    try:
        
        if set_name == "student":
            if not student_set:
                print("Student Set is empty. ")
            else:
                for index, name in enumerate(student_set, 1):
                    print(f"{index}. {name}")
                print("*" * 30)    
        elif set_name == "teacher":
            if not teacher_set:
                print("Teacher Set is empty. ")
            else:
                
                for index, name in enumerate(teacher_set, 1):
                    print(f"{index} {name}")
        else:
            print("Invalid set name")
    except Exception as e:
        print(f"An error occured: {e}")

while True:
    print("1. Add One students or teachers. ")
    print("2. Add Multiple students or teachers seperated by comma. ")
    print("3. View all student or teacher. ")
    print("4. Exit Program")
    
    choice = input("Enter number: ")
    
    if choice == "1":
        add_single_student()
    elif choice == "2":
        add_multiple_students()
    elif choice == "3":
        view_all_students()
    elif choice == "4":
        print("Program Exit.... ")
        break
    else:
        print("Invalid Number: ")
        
    
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
    
def view_all_students():
    set_name = input("Enter set name to view all members (student/teacher): ")
    try:
        if set_name == "student":
            for index, name in enumerate(student_set, 1):
                print(f"{index}. {name}")
        elif set_name == "teacher":
            for index, name in enumerate(teacher_set, 1):
                print(f"{index} {name}")
        else:
            print("Invalid set name")
    except Exception as e:
        print(f"An error occured: {e}")

while True:
    print("1. Add new students or teachers. ")
    print("2. View all students or teachers. ")
    print("3. Exit Program")
    
    choice = input("Enter number: ")
    
    if choice == "1":
        add_single_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        print("Program Exit.... ")
        break
    else:
        print("Invalid Number: ")
        
    
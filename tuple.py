students = ()    
studentsList = []
       
# for index in range(len(students)):
#     print(f"{index + 1}. {students[index]}")
# print("*" * 40)

# for index, student in enumerate(students, 1):
#     print(f"{index}. {student}")
     
def main_menu():
    print("\n********** Student Management System **********\n")
    print("1. Add Student")
    print("2. Find Student")
    print("3. View All Students")
    print("4. Exit\n")

def add_stu():    
    
    global students, studentsList
    
    try:  
        # if type(students) != list:
        if not isinstance(students, list):
            print("Students data is not in list format. ", type(students))
            studentsList = list(students)
        
            print("\nStudents data is in list format now. ", type(students))
            print("*" * 40)
            
            stu_id = int(input("Enter the ID of student: "))
            student_name = input("Enter the name of student: ")
            stu_class = input("Enter the class of student: ")
            stu_city = input("Enter the city of student: ")
                
            studentsList.append([stu_id, student_name, stu_class, stu_city])
            print(f"Student is added successfully. ")
                
            students = tuple(studentsList)
            print("Students data is again converted into tupple format  successfully. ")
                
    except ValueError:
        print("Invalid input. Please enter a valid name. ") 
            
def find_stu():
    if not students:
        print("No any student added yet. ")
    else:
        try:
            index = int(input("Enter the No of student: ")) - 1
            if index >= 0 and index < len(students):
                student = students[index]
                
                print("\n********** Student Details **********\n")
                print(f"Student No: {index + 1}")
                print(f"Roll_No:\t{student[0]}")
                print(f"Name:\t\t{student[1]}")
                print(f"Class:\t\t{student[2]}")
                print(f"City:\t\t{student[3]}\n")
            else:
                print("Invalid No... ")
        
        except ValueError:
            print("Invalid input. Please enter a valid number. ")
            
def view_all_stu():
    if not students:
        print("No any student added yet. ")
    else:
        print("\n********** All Students **********\n")
        for index, student in enumerate(students, 1):
            print(f"{index}. Roll_No:\t{student[0]}")
            print(f"   Name:\t{student[1]}")
            print(f"   Class:\t{student[2]}")
            print(f"   City:\t{student[3]}\n")
        print("*" * 40)
    
# main programe
# print(type(students)) # output must be a tuple
print("Welcome to Student Management System. ")
while True:
    main_menu()
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            add_stu()
        elif choice == "2":
            find_stu()
        elif choice == "3":
            view_all_stu()
        elif choice == "4":
            print("\nProgram Exit 😊\n. ")
            break
        else:
            print("Invalid choice. Please enter a valid option. ")  
    except ValueError:
        print("Invalid input. Please enter a valid number. ")    
    
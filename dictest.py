# students = {
#     "name" : "John",
#     "age": 20,
#     "subjects": {"Math": 85, "Science": 90, "Englsh": 78, "History": 88},
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "zip": "12345",
#         "country": "USA"
#     }
#     }
    

# 1️⃣ ACCESSING VALUES

# for key, value in students.items():
#     if isinstance(value, dict):
#         for sub_key, sub_value in value.items():
#             print(sub_key, sub_value)
#     else:
#         print(key, value)


# for key, value in students.items():
#     if isinstance(value, dict):
#         print(f"{key.capitalize()}:")
#         for sub_key, sub_value in value.items():
#             print(f"  {sub_key.capitalize()}: {sub_value}")
#     else:
#         print(f"{key.capitalize()}: {value}")

students = {}      

def main_menu():
    print("1. Add student: ")
    print("2. View students: ")
    print("3. Update Student: ")
    print("4. Exit Program")

def add_student():
    
    try:    
        students["name"] = input("Enter student name: ").strip()
        students["age"] = int(input("Enter age: "))
        
        # creating sub_dictionary subjects
        students["subjects"] = {}
        students["subjects"]["math"] = input("Please Enter Math Marks: ")
        students["subjects"]["english"] = input("Plase Enter English Marks: ")
        students["subjects"]["history"] = input("Plese Enter History Marks:")
        students["subjects"]["physics"] = input("Please Enter Physics Marks: ")
        
        # Creating new sub_dictionary address
        students["address"] = {}
        students["address"]["street"] = input("Enter Street No: ")
        students["address"]["city"] = input("Enter City: ")
        students["address"]["zip"] = input("Enter Zip Code: ")
        students["address"]["country"] = input("Enter Country: ")
        
    except Exception as e:
        print(f"Invalid input {e}") 
        
def update_student():
    name =  input("Enter name of student whoes data you want to update: ").strip()
    try:
        if name in students:
            name_ = input("Enter name of student: ")
            age_ = input("Enter age")
            math_ = input("Enter Math Marks: ")
            
            students[name].update({
                "name": name_,
                "age": age_,
            })
            
            students[name]["subjects"]["math"] = math_
            print("Student data updated successfully: ")
        else:
            print("Student not found. ")
            print("You entered:", name)
            print("Dictionary keys:", students.keys())

    except Exception as e:
        print(f"Invalid data {e}")
           
def view_students():        
    for key, value in students.items():
        if isinstance(value, dict):
            print(f"{key.capitalize()}:")
            for sub_key, sub_value in value.items():
                print(f" {sub_key.capitalize()}: {sub_value}")
        else:
            print(f"{key.capitalize()}: {value}")


while True:
    print("********* Welcome to Student Management System ************")
    
    main_menu()
    choice = input("Please Choose/Enter No: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        print("Program Exit.... ")
        break
    else:
        print("Invalid Number ")

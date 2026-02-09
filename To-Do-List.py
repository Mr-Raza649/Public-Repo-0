status = "Pending"
def main_menu():
    print("1. add Task. ")
    print("2. view all Tasks. ")
    print("3. update status of Task. ")
    print("4. exit program. ")
    
    
def add_tasks():
    task_name = input("Enter the task. ")
    # status = "Pending"
    elem.append([task_name, status])
    print(f"Task added successfully. Task: {task_name}, Status: {status}")

def view_tasks():
    if not elem:
        print("No any element yet added. ")
    else:
            print("\n******************************************\n")
            for index, element in enumerate(elem, 1):
                print(f"{index}. {status}: {', '.join(map(str, element))}")
            print("\n******************************************\n")

def update_status():
    if not elem:
        print("No any element yet added. ")
    else:
        
        view_tasks()
        index = int(input("Enter the number of the task to update status: ")) - 1
        
        if 0 <= index < len(elem):
            if elem[index][1] == "completed":
                print("Task is already marked as completed.")
            else:       
                approve = input("Enter 'y' to mark as completed: ")
                if approve.lower() == 'y':
                    elem[index][1] = "completed"
                    print("Task status updated successfully!")
                else:
                    print("Task status update canceled.")
        else:
            print("Invalid index.")
        
                
elem = []

while True:

    main_menu()
    choice = input("Enter a number please. ")
    
    if choice == "1":
        add_tasks()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_status()
    elif choice == "4":
        print("Program is exited. ")
        break
    else:
        print("Invalid number. ")
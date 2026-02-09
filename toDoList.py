# This is ToDo List App, which allows users to create and manage their tasks effectively. The app provides a simple interface for adding, viewing, and deleting tasks. Users can mark tasks as completed, and the app will keep track of their progress. With features like due dates and priority levels, users can stay organized and ensure that they never miss an important task again. Whether it's for personal use or team collaboration, ToDo List App is the perfect tool to help you stay on top of your tasks and boost your productivity.

from datetime import datetime,timedelta

status = "❌"
tasks = []

def main_menu():
    print("1.\tAdd Task: ")
    print("2.\tView all Tasks: ")
    print("3.\tDelete Task: ")
    print("4\tUpdate Task Status: ")
    # Task progress and Priority levels functionality will be added later
    print("5.\tExit Program")

def add_task():

    task = input("Enter the task: ")
    task_adding_time = datetime.now()
    task_due_time = input("Enter task ending date (YYYY-MM-DD HH:MM):")
    try:
        task_ending_time = datetime.strptime(task_due_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date! Please enter in YYYY-MM-DD HH:MM format with a valid month and day.")
    
    tasks.append([task, task_adding_time, task_ending_time, status])
    print(f"\nTask added Successfuly: \n")
    print(f"Task:\t\t\t{task}")
    print(f"Task Added Date:\t{task_adding_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"Task Ending Date:\t{task_ending_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"Status:\t\t\t{status}")
    print("********************************************\n")
    
def view_all_tasks():
    if not tasks:
        print("No any Task added yet. ")
    else:
        print("\n*******************************************\n")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. Task:\t{task[0]}")
            print(f"Adding Date:\t{task[1].strftime('%Y-%m-%d %H:%M')}")
            print(f"Ending Date:\t{task[2].strftime('%Y-%m-%d %H:%M')}")
            print(f"Status:\t\t{task[3]}\n")
        print("********************************************\n")
        
def delete_task():
    if not tasks:
        print("No any task yet added. \n")
    else:
        view_all_tasks()
        task_No = int(input("Enter the number of the task that you want to delete: ")) - 1
        
        if task_No >= 0 and task_No < len(tasks):
            del tasks[task_No]
            print("Task is deleted sucessfully. ")
        else:
            print("Invalid task number. ")
        
def update_status():
    if not tasks:
        print("No any task added yet. ")
    else:
        view_all_tasks()
        task_No = int(input("Enter the task number that's status you want to update: ")) - 1
        
        if task_No >= 0 and task_No < len(tasks):
            if tasks[task_No][3] == "✅":
                print("\nTask is already Marked: completed. ✅ \n")
            else:
                approve = input("Enter 'y' to mark Task cpmpleted. ").strip()
                if approve.lower() == "y":
                    tasks[task_No][3] = "✅"
                    print("\nTask status updated successfully. \n")
                else:
                    print("Task status update canceled. ")
        else:
            print("Invalid No... \n")            
            

while True:
    main_menu()
    choice = input("\nEnter Number please: ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_all_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        update_status()
    elif choice == "5":
        print("\nProgram is Exited. \n")
        break
    else:
        print("Invalid Number: ")    
        

    


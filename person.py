# Define a list to store person information. Each person is represented as a list containing name, age, marks, city, and country. It will add person information, view all persons, edit a person's information, delete a person, and find a person by name. The program will continue to run until the user chooses to exit.

def add_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    city = input("Enter city: ")
    country = input("Enter country: ")
    persons.append([name, age, marks, city, country])
    print("Person added successfully!")

def view_all_person():
    if not persons:
        print("No persons found.\n")
    else:
        for index, person in enumerate(persons):
            # print(f"{index + 1}. Name: {person[0]}, Age: {person[1]}, Marks: {person[2]}, City: {person[3]}, Country: {person[4]}")
            print(f"{index + 1}. " + ", ".join(map(str, person)))

def edit_person():
    if not persons:
        print("No persons found.")
    else:
        view_all_person()
        index = int(input("Enter the number of the person to edit: ")) - 1
        if 0 <= index < len(persons):
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            marks = float(input("Enter new marks: "))
            city = input("Enter new city: ")
            country = input("Enter new country: ")
            persons[index] = [name, age, marks, city, country]
            print("Person updated successfully!")
        else:
            print("Invalid index.")
            
def delete_person():  
    if not persons:
        print("No persons found.")
    else:
        view_all_person()
        index = int(input("Enter the number of the person to delete: ")) - 1
        if 0 <= index < len(persons):
            del persons[index]
            print("Person deleted successfully!")
        else:
            print("Invalid index.")
def find_person():
    if not persons:
        print("No persons found.")
    else:
        name = input("Enter the name of the person to find: ")
        found = False
        for person in persons:
            # to search by any field, we can use the following code:
            #   for field in person:
            #     if str(field).lower() == query.lower():
            #         print(f"Name: {person[0]}, Age: {person[1]}, Marks: {person[2]}, City: {person[3]}, Country: {person[4]}")
            #         found = True
            #         break
            
            # to search by name only, we can use the following code:
            if person[0].lower() == name.lower():
                print(f"Name: {person[0]}, Age: {person[1]}, Marks: {person[2]}, City: {person[3]}, Country: {person[4]}")
                found = True
                break
        if not found:
            print("Person not found.")
    
    
persons = []

print("Welcome to the Person Management System")


while True:
    
    print("1. Add a person")
    print("2. View all persons")
    print("3. Edit a person")
    print("4. Delete a person")
    print("5. To Find a person")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_person()
    elif choice == "2":
        view_all_person()
    elif choice == "3":
        edit_person()
    elif choice == "4":
        delete_person()
    elif choice == "5":
        find_person()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
        
        


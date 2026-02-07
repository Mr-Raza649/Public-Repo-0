def add_person():
    name = input("Enter name of the person. ")
    age = int(input("Enter age of person. "))
    city = input("Enter city name. ")
    persons.append([name, age, city])
    print("Person added successfully. ")
    
def view_all_person():
    if not persons:
        print("No any person yet added. ")
    else:
        print("\n****************************************\n")
        for index, person in enumerate(persons):
            print(f"{index + 1}. " + ", ".join(map(str, person)))
        print("\n**************************************** \n")
        
persons = []

print("Welcom person management system. ")

while True:
    print("1. add person. ")
    print("2. view all peson. ")

    print("3. exit program")

    choice = input("Enter a number please. ")

    if choice == "1":
        add_person()
    elif choice == "2":
        view_all_person()
    elif choice == "3":
        print("Progam is exited. ")
        break    
    else:
        print("Invalid number")
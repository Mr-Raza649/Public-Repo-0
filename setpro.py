
coding_club = set()
sports_club = set()

def main_menu():
    print("\n********** Club Management System **********")
    print("1. Add Single Student ")
    print("2. Add Multiple Students ")
    print("3. Remove Student ")
    print("4. Pop Random Student ")
    print("5. Clear Club ")
    print("6. Copy Club ")
    print("7. Union of Clubs ")
    print("8. Intersection of Clubs ")
    print("9. Difference of Clubs ")
    print("10. Symmetric Difference of Clubs ")
    print("11. View Club ")
    print("12. Exit\n")
    
def add_single_student():
    club = input("Which club to add student to? (coding/sports): ").lower()
    name = input("Enter the name of student to add: ").strip()
    
    if club == "coding":
        coding_club.add(name)
        print(f"{name} added to Coding Club. ")
    elif club == "sports":
        sports_club.add(name)
        print(f"{name} added to Sports Club. ")
    else:
        print("Invalid club name. ")
        return
    
def add_multiple_students():
    club = input("Which club to add students to? (coding/sports): ").lower()
    name = input("Enter the names of students to add (comma separated): ").strip().split()
    if not name:
        print("No names entered. ")
    else:
        if club == "coding":
            coding_club.update(name.strip() for name in name)
            print(f"{len(name)} students added to Coding Club. ")
        elif club == "sports":
            sports_club.update(name.strip() for name in name)
            print(f"{len(name)} students added to Sports Club. ")
        else:
            print("Invalid club name. ")
            return


def remove_student():
    club = input("Which club to remove student from? (coding/sports): ").lower()
    name = input("Enter the name of student to remove: ").strip()

    if not name:
        print("No name entered.")
        return

    if club == "coding":
        target_set = coding_club
    elif club == "sports":
        target_set = sports_club
    else:
        print("Invalid club name.")
        return

    if name in target_set:
        target_set.discard(name)
        print(f"{name} removed from {club.capitalize()} Club.")
    else:
        print(f"{name} not found in {club.capitalize()} Club.")


# def remove_student():
#     club = input("Which club to remvove student from? (coding/sprots): ").lower()
#     name = input("Enter the name of student to remove: ").strip()
#     if not name:
#         print("No name entered. ")
#     else:
#         if club == "coding" and name in coding_club:
#             coding_club.discard(name)
#             print(f"{name} removed from Coding Club. ")
#             else:
#             print(f"{name} not found in Coding Club. ")
            
#         elif club == "sports" and name in sports_club:
#             sports_club.discard(name)
#             print(f"{name} removed from Sports Club. ")
#         else:
#             print(f"{name} not found in Sports Club. ")
#         else:
#             print(f"Invalid club name. ")
#             return

def pop_student():
    club = input("Which club to pop student from? (coding/sports): ").lower()
    
    if club == "coding":
        if coding_club:
            removed = coding_club.pop()
            print(f"{removed} removed randomly from Coding Club. ")
        else:
            print("Coding Club is empty. ")
            
    elif club == "sports":
        if sports_club:
            removed = sports_club.pop()
            print(f"{removed} removed randomly from Sports Club. ")
        else:
            print("Sports Club is empty. ")

    else:
        print("Invalid club name. ")
        return
                
def clear_club():
    club = input("Which club to clear? (coding/sports): ").lower()
    
    if club == "coding":
        coding_club.clear()
        print("Coding Club cleared. ")
    elif club == "sports":
        coding_club.clear()
        print("Sports Club cleared. ")
    else:
        print("Invalid club name. ")
        return
    
def copy_club():
    club = input("Which club to copy? (coding/sports): ").lower()
    if club == "coding":
        new_set = coding_club.copy()
        print("Copied Coding Club:", new_set)
    elif club == "sports":
        new_Set = sports_club.copy()
        print("Copied Sports Club:", new_set)
    else:
        print("Invalid club name. ")
        return
    
def union_clubs():
    print("All students in either club:", coding_club.union(sports_club))

def intersection_clubs():
    print("Students in both clubs:", coding_club.intersection(sports_club))

def difference_clubs():
    print("Students in Coding but not Sports:", coding_club.difference(sports_club))
    print("Students in Sports but not Coding:", sports_club.difference(coding_club))
    
def symmetric_difference_clubs():
    print("Students in only one club:", coding_club.symmetric_difference(sports_club))

def view_club():
    club = input("Which club to view? (coding/sports): ").lower()
    if club == "coding":
        print("Coding Club: ")
        for index, student in enumerate(coding_club, 1):
            print(f"{index}. {student}")
    elif club == "sports":
        print("Sports Club: ")
        for index, student in enumerate(sports_club, 1):
            print(f"{index}. {student}")
    else:
        print("Invalid club name. ")
        return
    
def exit_program():
    print("Exiting the program. Goodbye! ")
    exit()
    
# main program
print("********** Welcome to Club Management System **********")

while True:
    main_menu()
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        add_single_student()
    elif choice == "2":
        add_multiple_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        pop_student()
    elif choice == "5":
        clear_club()
    elif choice == "6":
        copy_club()
    elif choice == "7":
        union_clubs()
    elif choice == "8":
        intersection_clubs()
    elif choice == "9":
        difference_clubs()
    elif choice == "10":
        symmetric_difference_clubs()
    elif choice == "11":
        view_club()
    elif choice == "12":
        exit_program()
    else:
        print("Invalid choice. Please enter a number between 1 and 12. ")

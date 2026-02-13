# set_s = {"John", "Alice", "Bob"}
# name = input("Enter multiple name seperated by comma: ")
# for n in name.split(","):
#     set_s.add(n.strip())
#     # print(f"{n.strip()} is added successfully. ")
    
# print("\n********** Set of Names **********\n")
# for index, name in enumerate(set_s, 1):
#     print(f"{index}. {name}")
    
# Advanced Student Club Manager using sets

coding_club = set()
sports_club = set()

def add_single_student():
    club = input("Enter club (coding/sports): ").lower()
    name = input("Enter student name: ").strip()
    if club == "coding":
        coding_club.add(name)
    elif club == "sports":
        sports_club.add(name)
    print(f"{name} added to {club.capitalize()} Club ✅")

def add_multiple_students():
    club = input("Enter club (coding/sports): ").lower()
    names = input("Enter student names separated by comma: ").split(",")
    names = [name.strip() for name in names]
    if club == "coding":
        coding_club.update(names)
    elif club == "sports":
        sports_club.update(names)
    print(f"{len(names)} students added to {club.capitalize()} Club ✅")

def remove_student():
    club = input("Enter club (coding/sports): ").lower()
    name = input("Enter student name to remove: ").strip()
    target_set = coding_club if club == "coding" else sports_club
    # discard avoids error if student doesn't exist
    target_set.discard(name)
    print(f"{name} removed from {club.capitalize()} Club if existed ✅")
    
    
    # but remove would raise an error if student doesn't exist
    # if name in target_set:
    #     target_set.remove(name)
    #     print(f"{name} was removed from {club.capitalize()} Club ✅")
    # else:
    #     print(f"{name} is not in {club.capitalize()} Club ❌")


def pop_student():
    club = input("Enter club (coding/sports): ").lower()
    target_set = coding_club if club == "coding" else sports_club
    if target_set:
        removed = target_set.pop()  # removes a random element
        print(f"{removed} removed randomly from {club.capitalize()} Club ✅")
    else:
        print(f"{club.capitalize()} Club is empty ❌")

def clear_club():
    club = input("Enter club to clear (coding/sports): ").lower()
    if club == "coding":
        coding_club.clear()
    elif club == "sports":
        sports_club.clear()
    print(f"{club.capitalize()} Club cleared ✅")

def copy_club():
    club = input("Enter club to copy (coding/sports): ").lower()
    new_set = coding_club.copy() if club == "coding" else sports_club.copy()
    print(f"Copied {club.capitalize()} Club:", new_set)

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
        print("Coding Club:", coding_club)
    elif club == "sports":
        print("Sports Club:", sports_club)

# Main Loop
while True:
    print("\n--- Advanced Student Club Manager ---")
    print("1. Add single student")
    print("2. Add multiple students")
    print("3. Remove student")
    print("4. Pop a random student")
    print("5. Clear a club")
    print("6. Copy a club")
    print("7. View club")
    print("8. Union of clubs")
    print("9. Intersection of clubs")
    print("10. Difference of clubs")
    print("11. Symmetric difference of clubs")
    print("12. Exit")
    
    choice = input("Enter your choice: ")
    
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
        view_club()
    elif choice == "8":
        union_clubs()
    elif choice == "9":
        intersection_clubs()
    elif choice == "10":
        difference_clubs()
    elif choice == "11":
        symmetric_difference_clubs()
    elif choice == "12":
        print("Exiting... 👋")
        break
    else:
        print("Invalid choice ❌")

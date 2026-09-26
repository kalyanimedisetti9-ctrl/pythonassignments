students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")

def search_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter roll number: ")

    if roll in students:
        students[roll]["name"] = input("Enter new name: ")
        students[roll]["marks"] = float(input("Enter new marks: "))
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter roll number: ")

    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

def display_students():
    if not students:
        print("No students available.")
    else:
        for roll, details in students.items():
            print(roll, details["name"], details["marks"])


while True:
    print("\n--- Student Management ---")
    print("1. Add")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        display_students()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
def add_student():
    with open("students.txt", "a") as file:
        student_id = input("Enter ID: ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")
        marks = input("Enter marks: ")

        file.write(f"{student_id},{name},{age},{course},{marks}\n")

    print("Student added successfully")


def display_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Age:", data[2])
                print("Course:", data[3])
                print("Marks:", data[4])
                print("----------------")
    except FileNotFoundError:
        print("No student records found")


def search_student():
    student_id = input("Enter student ID: ")

    try:
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[0] == student_id:
                    print("Student found:", data)
                    return

        print("Student not found")

    except FileNotFoundError:
        print("File not found")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
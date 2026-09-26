students = {}

def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if average >= 50 else "Fail"

    return total, average, grade, status

def add_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        marks.append(float(input("Enter mark: ")))

    students[name] = marks

def display_results():
    for name, marks in students.items():
        total, average, grade, status = calculate_result(marks)

        print("\nName:", name)
        print("Total:", total)
        print("Average:", average)
        print("Grade:", grade)
        print("Status:", status)

def topper():
    if students:
        name = max(students, key=lambda x: calculate_result(students[x])[1])
        print("Topper:", name)


while True:
    print("\n--- Student Grade Management ---")
    print("1. Add Student")
    print("2. Display Results")
    print("3. Display Topper")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_results()
    elif choice == 3:
        topper()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
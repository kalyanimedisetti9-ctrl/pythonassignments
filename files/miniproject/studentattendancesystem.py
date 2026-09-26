import csv


def mark_attendance():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    status = input("Enter attendance (Present/Absent): ")

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, status])

    print("Attendance saved")


def display_attendance():
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(
                    "ID:", row[0],
                    "Name:", row[1],
                    "Status:", row[2]
                )

    except FileNotFoundError:
        print("Attendance file not found")


while True:
    print("\n1. Mark Attendance")
    print("2. Display Attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        display_attendance()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
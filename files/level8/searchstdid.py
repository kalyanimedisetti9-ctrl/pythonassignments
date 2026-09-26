import csv

student_id = input("Enter student ID: ")
found = False

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Student ID"] == student_id:
            print("Student found")
            print("ID:", row["Student ID"])
            print("Name:", row["Name"])
            print("Course:", row["Course"])
            print("Marks:", row["Marks"])
            found = True
            break

if not found:
    print("Student not found")
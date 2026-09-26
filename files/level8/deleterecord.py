import csv

student_id = input("Enter student ID to delete: ")

with open("students.csv", "r") as file:
    rows = list(csv.DictReader(file))

new_rows = []
deleted = False

for row in rows:
    if row["Student ID"] == student_id:
        deleted = True
    else:
        new_rows.append(row)

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Student ID", "Name", "Course", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(new_rows)

if deleted:
    print("Student deleted successfully")
else:
    print("Student not found")
import csv

student_id = input("Enter student ID: ")
new_marks = input("Enter new marks: ")

with open("students.csv", "r") as file:
    rows = list(csv.DictReader(file))

updated = False

for row in rows:
    if row["Student ID"] == student_id:
        row["Marks"] = new_marks
        updated = True

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Student ID", "Name", "Course", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

if updated:
    print("Marks updated successfully")
else:
    print("Student not found")
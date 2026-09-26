import csv

with open("students.csv", "r") as file:
    students = list(csv.DictReader(file))

students.sort(key=lambda student: int(student["Marks"]), reverse=True)

with open("sorted_students.csv", "w", newline="") as file:
    fieldnames = ["Student ID", "Name", "Course", "Marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)

print("Students sorted by marks successfully")
import csv

students = [
    [101, "Kalyani", "Computer Engineering", 85],
    [102, "Ravi", "Computer Engineering", 72],
    [103, "Sita", "Computer Engineering", 90],
    [104, "Ram", "Computer Engineering", 65]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Student ID", "Name", "Course", "Marks"])
    writer.writerows(students)

print("CSV file created successfully")
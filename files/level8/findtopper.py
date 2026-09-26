import csv

with open("students.csv", "r") as file:
    students = list(csv.DictReader(file))

topper = max(students, key=lambda student: int(student["Marks"]))

print("Topper:")
print("ID:", topper["Student ID"])
print("Name:", topper["Name"])
print("Course:", topper["Course"])
print("Marks:", topper["Marks"])
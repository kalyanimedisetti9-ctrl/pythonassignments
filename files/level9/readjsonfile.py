import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("Marks:", student["marks"])
    print("-------------------")
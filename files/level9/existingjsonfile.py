import json

with open("students.json", "r") as file:
    students = json.load(file)

new_student = {
    "id": 103,
    "name": "Sita",
    "age": 20,
    "course": "Computer Engineering",
    "marks": 90
}

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("New student added successfully")
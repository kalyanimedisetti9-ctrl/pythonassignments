import json

student_id = int(input("Enter student ID to delete: "))

with open("students.json", "r") as file:
    students = json.load(file)

new_students = [
    student for student in students
    if student["id"] != student_id
]

if len(new_students) < len(students):
    print("Student deleted successfully")
else:
    print("Student not found")

with open("students.json", "w") as file:
    json.dump(new_students, file, indent=4)
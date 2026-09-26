import json

student_id = int(input("Enter student ID: "))
new_marks = int(input("Enter new marks: "))

with open("students.json", "r") as file:
    students = json.load(file)

updated = False

for student in students:
    if student["id"] == student_id:
        student["marks"] = new_marks
        updated = True
        break

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

if updated:
    print("Student information updated successfully")
else:
    print("Student not found")
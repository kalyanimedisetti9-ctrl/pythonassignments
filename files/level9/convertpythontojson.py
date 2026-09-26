import json

student = {
    "id": 101,
    "name": "Kalyani",
    "age": 20,
    "course": "Computer Engineering",
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Python dictionary converted to JSON successfully")
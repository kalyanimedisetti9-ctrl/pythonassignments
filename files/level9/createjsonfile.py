import json

students = [
    {
        "id": 101,
        "name": "Kalyani",
        "age": 20,
        "course": "Computer Engineering",
        "marks": 85
    },
    {
        "id": 102,
        "name": "Ravi",
        "age": 21,
        "course": "Computer Engineering",
        "marks": 72
    }
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student JSON file created successfully")
marks = {
    "Kalyani": 85,
    "Ravi": 78,
    "Anu": 92,
    "Suresh": 70
}

highest_student = None
highest_marks = None

for student, mark in marks.items():
    if highest_marks is None or mark > highest_marks:
        highest_marks = mark
        highest_student = student

print("Highest Marks:", highest_marks)
print("Student:", highest_student)
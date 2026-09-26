subject1 = {
    "Kalyani": 85,
    "Ravi": 75,
    "Sita": 90,
    "Rahul": 65
}

subject2 = {
    "Kalyani": 80,
    "Sita": 95,
    "Anu": 70,
    "Rahul": 60
}

students1 = set(subject1.keys())
students2 = set(subject2.keys())

common_students = students1 & students2

print("Students in both subjects:")

for student in common_students:
    print(student)
students1 = {"Kalyani", "Ravi", "Sita"}
students2 = {"Rahul", "Anu", "Kalyani"}

courses = {
    "Kalyani": "CCN",
    "Ravi": "CSE",
    "Sita": "ECE",
    "Rahul": "CCN",
    "Anu": "CSE"
}

all_students = students1 | students2

for student in all_students:
    print(student, ":", courses[student])
students = {
    "Kalyani": 85,
    "Ravi": 70,
    "Sita": 95,
    "Rahul": 60,
    "Anu": 80
}

topper = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Topper:", topper, students[topper])
print("Lowest Scorer:", lowest, students[lowest])
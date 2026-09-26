students = [
    ["Kalyani", 80, 85, 90],
    ["Ravi", 70, 75, 80],
    ["Sita", 90, 88, 92]
]

for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)
    average = total / 3

    print(name)
    print("Total =", total)
    print("Average =", average)
with open("students.txt", "r") as file:
    students = []

    for line in file:
        data = line.strip().split(",")
        students.append(data)

highest = max(students, key=lambda student: int(student[4]))

print("Student with highest marks:")
print("ID:", highest[0])
print("Name:", highest[1])
print("Age:", highest[2])
print("Course:", highest[3])
print("Marks:", highest[4])
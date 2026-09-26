students1 = {"Kalyani", "Ravi", "Anu", "Suresh"}
students2 = {"Ravi", "Anu", "Priya", "Rahul"}

print("Students present only in first set:")

for student in students1:
    if student not in students2:
        print(student)
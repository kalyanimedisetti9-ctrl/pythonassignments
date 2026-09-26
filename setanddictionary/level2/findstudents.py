students1 = {"Kalyani", "Ravi", "Anu", "Suresh"}
students2 = {"Ravi", "Anu", "Priya", "Rahul"}

print("Students present in both sets:")

for student in students1:
    if student in students2:
        print(student)
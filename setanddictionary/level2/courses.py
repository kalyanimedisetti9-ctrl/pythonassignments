python_students = {"Kalyani", "Ravi", "Anu", "Suresh"}
java_students = {"Ravi", "Anu", "Priya", "Rahul"}

print("Students enrolled in both Python and Java:")

for student in python_students:
    if student in java_students:
        print(student)
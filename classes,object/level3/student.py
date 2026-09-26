class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

student1 = Student("Kalyani")
student2 = Student("Ravi")

print("Student Name:", student1.name)
print("College Name:", student1.college_name)

print()

print("Student Name:", student2.name)
print("College Name:", student2.college_name)
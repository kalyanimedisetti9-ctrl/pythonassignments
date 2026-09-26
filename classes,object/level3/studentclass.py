class Student:
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

student1 = Student("Kalyani")
student2 = Student("Ravi")
student3 = Student("Anitha")

print(student1.name, "-", student1.college_name)
print(student2.name, "-", student2.college_name)
print(student3.name, "-", student3.college_name)
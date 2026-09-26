class Student:
    def __init__(self, name):
        self.name = name


student = Student("Kalyani")

try:
    print(student.age)

except AttributeError:
    print("Error: Attribute does not exist")
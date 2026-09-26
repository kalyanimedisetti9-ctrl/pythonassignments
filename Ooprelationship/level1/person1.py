class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def study(self):
        print("Student is studying")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


student = Student("Kalyani", 18)
teacher = Teacher("Ravi", 30)

student.display()
student.study()

print()

teacher.display()
teacher.teach()
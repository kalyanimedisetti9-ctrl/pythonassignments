class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

student = Student("Kalyani", 18, "Computer Engineering", 85)

print("Name:", student.name)
print("Age:", student.age)
print("Course:", student.course)
print("Marks:", student.marks)
class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

s = Student("Kalyani", 20, "Computer Engineering", 85)

print("Name:", s.name)
print("Age:", s.age)
print("Course:", s.course)
print("Marks:", s.marks)
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Kalyani", 18, "Computer Engineering")
student2 = Student("Ravi", 19, "ECE")
student3 = Student("Anitha", 18, "CSE")

print(student1.name, student1.age, student1.course)
print(student2.name, student2.age, student2.course)
print(student3.name, student3.age, student3.course)
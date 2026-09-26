class Student:
    def display(self):
        print("Student: Kalyani")

class Teacher:
    def display(self):
        print("Teacher: Ravi")


people = [Student(), Teacher()]

for person in people:
    person.display()
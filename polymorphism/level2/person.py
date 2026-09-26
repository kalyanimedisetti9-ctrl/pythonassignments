class Person:
    def role(self):
        print("Person has a role")

class Student(Person):
    def role(self):
        print("Role: Student")

class Teacher(Person):
    def role(self):
        print("Role: Teacher")

class Doctor(Person):
    def role(self):
        print("Role: Doctor")


people = [Student(), Teacher(), Doctor()]

for person in people:
    person.role()
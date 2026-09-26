from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        print(self.name, "is a Student")

class Teacher(Person):
    def role(self):
        print(self.name, "is a Teacher")

class Doctor(Person):
    def role(self):
        print(self.name, "is a Doctor")

s = Student("Kalyani", 20)
t = Teacher("Ramesh", 35)
d = Doctor("Anil", 40)

s.role()
t.role()
d.role()
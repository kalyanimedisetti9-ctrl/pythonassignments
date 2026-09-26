class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


student1 = Student("Kalyani", 90)
student2 = Student("Ravi", 85)

print(student1 > student2)
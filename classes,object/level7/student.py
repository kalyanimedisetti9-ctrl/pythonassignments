class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def get_count(cls):
        return cls.student_count


student1 = Student("Kalyani")
student2 = Student("Ravi")
student3 = Student("Anitha")
student4 = Student("Kiran")

print("Student 1:", student1.name)
print("Student 2:", student2.name)
print("Student 3:", student3.name)
print("Student 4:", student4.name)

print("Total Students:", Student.get_count())
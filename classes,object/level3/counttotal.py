class Student:
    object_count = 0

    def __init__(self, name):
        self.name = name
        Student.object_count += 1

student1 = Student("Kalyani")
student2 = Student("Ravi")
student3 = Student("Anitha")

print("Total objects created:", Student.object_count)
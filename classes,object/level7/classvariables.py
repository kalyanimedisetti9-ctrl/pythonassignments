class Student:
    college_name = "Aditya Polytechnic College"   # Class variable

    def __init__(self, name, age):
        self.name = name       # Instance variable
        self.age = age         # Instance variable


student1 = Student("Kalyani", 18)
student2 = Student("Ravi", 20)

print("Student 1:", student1.name)
print("Age:", student1.age)
print("College:", student1.college_name)

print()

print("Student 2:", student2.name)
print("Age:", student2.age)
print("College:", student2.college_name)

print("\nClass Variable:", Student.college_name)
print("Instance Variable:", student1.name)
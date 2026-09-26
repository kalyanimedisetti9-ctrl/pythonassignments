class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

student = Student("Kalyani", [80, 85, 90, 75, 88])

print("Name:", student.name)
print("Total Marks:", student.total_marks())
print("Average Marks:", student.average_marks())
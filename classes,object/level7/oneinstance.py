class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def display(self):
        total = self.calculate_total()
        print("Name:", self.name)
        print("Total Marks:", total)


student = Student("Kalyani", [80, 85, 90, 75])

student.display()
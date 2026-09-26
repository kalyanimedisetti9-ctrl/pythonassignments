class Student:
    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

student = Student()

marks = 85
print("Marks:", marks)
print("Grade:", student.calculate_grade(marks))
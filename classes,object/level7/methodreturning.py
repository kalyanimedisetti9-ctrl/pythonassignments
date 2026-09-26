class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_details(self):
        return "Name: " + self.name + ", Course: " + self.course


class College:
    def __init__(self, college_name):
        self.college_name = college_name

    def get_student_info(self, student):
        return student.get_details()


student = Student("Kalyani", "Computer Engineering")
college = College("Aditya Polytechnic College")

print(college.get_student_info(student))
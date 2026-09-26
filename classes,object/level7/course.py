class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def display_students(self):
        print("Course:", self.course_name)
        print("Enrolled Students:")

        for student in self.students:
            print(student)


course = Course("Python Programming")

course.enroll_student("Kalyani")
course.enroll_student("Ravi")
course.enroll_student("Anitha")
course.enroll_student("Kiran")

course.display_students()
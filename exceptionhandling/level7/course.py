class EnrollmentError(Exception):
    pass


class Course:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats

    def enroll(self, student_name):
        try:
            if self.seats <= 0:
                raise EnrollmentError("No seats available")

            if student_name == "":
                raise EnrollmentError("Student name cannot be empty")

            self.seats -= 1
            print(student_name, "enrolled successfully")
            print("Course:", self.name)
            print("Remaining seats:", self.seats)

        except EnrollmentError as e:
            print("Error:", e)


course = Course("Python", 2)
course.enroll("Kalyani")
course.enroll("Ravi")
course.enroll("Suresh")
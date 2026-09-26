class InvalidMarksError(Exception):
    pass

class DuplicateStudentError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass


class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, marks):
        try:
            if student_id in self.students:
                raise DuplicateStudentError("Student ID already exists")

            if marks < 0 or marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100")

            self.students[student_id] = {
                "name": name,
                "marks": marks
            }

            print("Student added successfully")

        except DuplicateStudentError as e:
            print("Error:", e)
        except InvalidMarksError as e:
            print("Error:", e)

    def search_student(self, student_id):
        try:
            if student_id not in self.students:
                raise StudentNotFoundError("Student not found")

            student = self.students[student_id]
            print("Name:", student["name"])
            print("Marks:", student["marks"])

        except StudentNotFoundError as e:
            print("Error:", e)


system = StudentManagement()

system.add_student(101, "Kalyani", 85)
system.add_student(102, "Ravi", 90)
system.add_student(101, "Sita", 75)
system.add_student(103, "Ram", 120)

system.search_student(101)
system.search_student(999)
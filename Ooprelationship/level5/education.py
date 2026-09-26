class EducationalInstitution:
    def conduct_education(self):
        print("Educational institution provides education")


class Department:
    def __init__(self, name):
        self.name = name


class ExaminationService:
    def conduct_exam(self):
        print("Examination is being conducted")


class University(EducationalInstitution):
    def __init__(self):
        self.departments = [
            Department("Computer Science"),
            Department("Mechanical"),
            Department("Civil")
        ]

    def conduct_examination(self):
        exam = ExaminationService()
        exam.conduct_exam()


university = University()

university.conduct_education()
university.conduct_examination()
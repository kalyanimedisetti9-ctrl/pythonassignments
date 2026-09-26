class CertificateGenerator:
    def generate_certificate(self, student, course):
        print(f"Certificate generated for {student}")
        print(f"Course: {course}")


class Course:
    def __init__(self, name):
        self.name = name

    def generate_certificate(self, student):
        certificate = CertificateGenerator()
        certificate.generate_certificate(student, self.name)


course = Course("Python Programming")
course.generate_certificate("Kalyani")
class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

teacher1 = Teacher("Ramesh", "Python", 5)
teacher2 = Teacher("Sita", "Java", 7)
teacher3 = Teacher("Kiran", "Mathematics", 10)

print(teacher1.name, teacher1.subject, teacher1.experience, "years")
print(teacher2.name, teacher2.subject, teacher2.experience, "years")
print(teacher3.name, teacher3.subject, teacher3.experience, "years")
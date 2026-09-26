def student_details(*marks, **details):
    print("Student Details:")

    for key, value in details.items():
        print(key, ":", value)

    print("Marks:", marks)

student_details(
    80, 85, 90,
    name="Kalyani",
    age=18,
    course="Computer Engineering"
)
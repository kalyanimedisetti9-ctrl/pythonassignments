def calculate_grade(marks):
    try:
        if marks < 0 or marks > 100:
            raise ValueError("Invalid marks")

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)

    except ValueError as e:
        print("Error:", e)

calculate_grade(85)
calculate_grade(120)
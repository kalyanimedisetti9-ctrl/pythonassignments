class InvalidMarksError(Exception):
    pass


try:
    marks = float(input("Enter student marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    print("Valid Marks:", marks)

except InvalidMarksError as e:
    print("Error:", e)
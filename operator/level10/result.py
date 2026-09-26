maths = int(input("Enter Mathematics marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english
average = total / 3
percentage = (total / 300) * 100

if maths >= 35 and science >= 35 and english >= 35:
    status = "Pass"

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"
else:
    status = "Fail"
    grade = "F"

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)
print("Grade =", grade)
print("Status =", status)
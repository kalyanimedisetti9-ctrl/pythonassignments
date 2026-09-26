marks1 = int(input("Enter Mathematics marks: "))
marks2 = int(input("Enter Science marks: "))
marks3 = int(input("Enter English marks: "))

total = marks1 + marks2 + marks3
average = total / 3

if marks1 >= 35 and marks2 >= 35 and marks3 >= 35 and average >= 50:
    print("Student is eligible")
else:
    print("Student is not eligible")

print("Total =", total)
print("Average =", average)
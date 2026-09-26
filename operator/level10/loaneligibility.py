age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21 and age <= 60 and salary >= 25000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
salary = float(input("Enter basic salary: "))

hra = salary * 0.20
da = salary * 0.10

salary += hra
salary += da

print("Final Salary =", salary)
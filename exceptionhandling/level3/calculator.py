try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", a + b)

    elif operator == "-":
        print("Result:", a - b)

    elif operator == "*":
        print("Result:", a * b)

    elif operator == "/":
        print("Result:", a / b)

    else:
        raise ValueError("Invalid operator")

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except TypeError:
    print("Error: Invalid data type")
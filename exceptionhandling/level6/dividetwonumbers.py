def divide(a, b):
    try:
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

divide(10, 2)
divide(10, 0)
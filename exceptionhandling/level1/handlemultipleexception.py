try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    numbers = [10, 20, 30]

    index = int(input("Enter index: "))

    result = a / b

    print("Result:", result)
    print("Element:", numbers[index])

except ValueError:
    print("Error: Please enter valid numbers")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except IndexError:
    print("Error: Index is out of range")
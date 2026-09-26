try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    numbers = [10, 20, 30]

    index = int(input("Enter list index: "))

    result = a / b
    print("Division:", result)

    print("List Element:", numbers[index])

    student = {
        "name": "Kalyani",
        "age": 18
    }

    key = input("Enter dictionary key: ")
    print("Dictionary Value:", student[key])

except ValueError:
    print("Error: Invalid numeric input")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except IndexError:
    print("Error: List index is out of range")

except KeyError:
    print("Error: Dictionary key not found")

except TypeError:
    print("Error: Invalid data type")

except Exception as e:
    print("Unexpected Error:", e)
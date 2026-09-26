class InvalidNumberError(Exception):
    pass


def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if a < 0 or b < 0:
            raise InvalidNumberError("Negative numbers are not allowed")

        result = a / b

    except ValueError:
        print("Error: Enter numbers only")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except InvalidNumberError as e:
        print("Error:", e)

    else:
        print("Result:", result)

    finally:
        print("Division operation completed")


def list_access():
    try:
        numbers = [10, 20, 30]
        index = int(input("Enter index: "))
        print("Element:", numbers[index])

    except ValueError:
        print("Error: Enter a valid number")

    except IndexError:
        print("Error: Index out of range")

    finally:
        print("List operation completed")


while True:
    print("\n===== MENU =====")
    print("1. Divide Numbers")
    print("2. Access List Element")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            divide_numbers()

        elif choice == 2:
            list_access()

        elif choice == 3:
            print("Program ended")
            break

        else:
            raise ValueError("Invalid menu choice")

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Menu operation completed")
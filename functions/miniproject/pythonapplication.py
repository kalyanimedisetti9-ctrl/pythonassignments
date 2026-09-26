def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def display_menu():
    print("\n--- Menu Driven Application ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")


while True:
    display_menu()

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Program exited.")
        break

    if choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", addition(a, b))
        elif choice == 2:
            print("Result:", subtraction(a, b))
        elif choice == 3:
            print("Result:", multiplication(a, b))
        elif choice == 4:
            print("Result:", division(a, b))
        elif choice == 5:
            print("Result:", modulus(a, b))
    else:
        print("Invalid choice")
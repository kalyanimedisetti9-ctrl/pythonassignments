while True:
    print("\n--- Operator Calculator ---")
    print("1. Arithmetic Operators")
    print("2. Assignment Operators")
    print("3. Comparison Operators")
    print("4. Logical Operators")
    print("5. Membership Operators")
    print("6. Identity Operators")
    print("7. Bitwise Operators")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Addition =", a + b)
        print("Subtraction =", a - b)
        print("Multiplication =", a * b)
        print("Division =", a / b)
        print("Modulus =", a % b)

    elif choice == 2:
        a = int(input("Enter a number: "))

        a += 5
        print("After += 5:", a)

        a -= 2
        print("After -= 2:", a)

        a *= 2
        print("After *= 2:", a)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Equal:", a == b)
        print("Not Equal:", a != b)
        print("Greater:", a > b)
        print("Less:", a < b)

    elif choice == 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("AND:", a > 0 and b > 0)
        print("OR:", a > 0 or b > 0)
        print("NOT:", not(a > 0))

    elif choice == 5:
        fruits = ["Apple", "Mango", "Banana", "Orange"]

        item = input("Enter fruit name: ")

        print("Present:", item in fruits)
        print("Not Present:", item not in fruits)

    elif choice == 6:
        a = [10, 20, 30]
        b = a

        print("a is b:", a is b)
        print("a is not b:", a is not b)

    elif choice == 7:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("AND =", a & b)
        print("OR =", a | b)
        print("XOR =", a ^ b)
        print("NOT =", ~a)
        print("Left Shift =", a << 1)
        print("Right Shift =", a >> 1)

    elif choice == 8:
        print("Calculator closed.")
        break

    else:
        print("Invalid choice")
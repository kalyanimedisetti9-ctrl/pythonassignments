def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def palindrome(n):
    return str(n) == str(n)[::-1]

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == n


while True:
    print("\n--- Number Utility ---")
    print("1. Prime")
    print("2. Palindrome")
    print("3. Factorial")
    print("4. Fibonacci")
    print("5. Even/Odd")
    print("6. Armstrong")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 7:
        break

    n = int(input("Enter number: "))

    if choice == 1:
        print(prime(n))
    elif choice == 2:
        print(palindrome(n))
    elif choice == 3:
        print("Factorial:", factorial(n))
    elif choice == 4:
        fibonacci(n)
        print()
    elif choice == 5:
        print(even_odd(n))
    elif choice == 6:
        print(armstrong(n))
    else:
        print("Invalid choice")
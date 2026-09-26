def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial is not possible for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        print("Factorial:", result)
    except ValueError as e:
        print("Error:", e)

factorial(5)
factorial(-2)
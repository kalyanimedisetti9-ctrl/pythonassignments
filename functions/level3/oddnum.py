def odd_numbers(numbers):
    result = []

    for n in numbers:
        if n % 2 != 0:
            result.append(n)

    return result

print("Odd numbers:", odd_numbers([1, 2, 3, 4, 5, 6]))
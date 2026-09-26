def number_squares(numbers):
    result = {}

    for n in numbers:
        result[n] = n * n

    return result

numbers = [1, 2, 3, 4, 5]

print(number_squares(numbers))
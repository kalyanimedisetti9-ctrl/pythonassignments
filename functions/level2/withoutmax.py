def largest_number(numbers):
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n

    return largest

print("Largest:", largest_number([10, 50, 20, 40]))
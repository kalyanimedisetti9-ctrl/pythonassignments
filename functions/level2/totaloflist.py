def total(numbers):
    result = 0

    for n in numbers:
        result = result + n

    return result

print("Total:", total([10, 20, 30, 40]))
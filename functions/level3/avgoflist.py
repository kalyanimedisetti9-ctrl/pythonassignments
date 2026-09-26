def average(numbers):
    total = 0

    for n in numbers:
        total += n

    return total / len(numbers)

print("Average:", average([10, 20, 30, 40, 50]))
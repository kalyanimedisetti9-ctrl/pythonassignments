def min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)

    return minimum, maximum

result = min_max([10, 25, 5, 40, 15])
print("Minimum:", result[0])
print("Maximum:", result[1])
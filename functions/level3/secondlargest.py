def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    return unique[-2]

print("Second largest:", second_largest([10, 50, 20, 40, 30]))
def tuple_sum(numbers):
    total = 0

    for n in numbers:
        total += n

    return total

numbers = (10, 20, 30, 40)
print("Sum:", tuple_sum(numbers))
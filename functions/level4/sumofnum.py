def calculate_sum(*args):
    total = 0

    for n in args:
        total += n

    return total

print("Sum:", calculate_sum(10, 20, 30, 40))
def average(*args):
    total = 0

    for n in args:
        total += n

    return total / len(args)

print("Average:", average(10, 20, 30, 40, 50))
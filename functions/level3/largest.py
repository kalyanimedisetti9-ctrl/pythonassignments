def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n

        if n < smallest:
            smallest = n

    return largest, smallest

largest, smallest = largest_smallest([10, 50, 20, 5, 40])

print("Largest:", largest)
print("Smallest:", smallest)
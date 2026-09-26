numbers = [25, 10, 45, 30, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)
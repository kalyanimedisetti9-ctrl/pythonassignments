numbers = {10, 25, 5, 40, 15, 30}

smallest = None

for num in numbers:
    if smallest is None or num < smallest:
        smallest = num

print("Smallest number:", smallest)
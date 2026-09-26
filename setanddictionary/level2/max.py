numbers = {10, 25, 5, 40, 15, 30}

largest = None

for num in numbers:
    if largest is None or num > largest:
        largest = num

print("Largest number:", largest)
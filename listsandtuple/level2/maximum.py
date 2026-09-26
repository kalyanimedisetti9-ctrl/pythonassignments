numbers = [25, 10, 45, 30, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
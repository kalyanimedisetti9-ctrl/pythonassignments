with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

largest = max(numbers)

print("Largest number:", largest)
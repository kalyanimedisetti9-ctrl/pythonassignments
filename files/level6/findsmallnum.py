with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

smallest = min(numbers)

print("Smallest number:", smallest)
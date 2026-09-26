with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

average = sum(numbers) / len(numbers)

print("Average:", average)
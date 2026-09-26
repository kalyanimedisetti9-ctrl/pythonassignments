with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate numbers:", duplicates)
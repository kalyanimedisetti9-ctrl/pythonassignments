with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

with open("squares.txt", "w") as file:
    for number in numbers:
        file.write(str(number ** 2) + "\n")

print("Squares written successfully")
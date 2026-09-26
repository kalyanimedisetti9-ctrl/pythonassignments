with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

with open("cubes.txt", "w") as file:
    for number in numbers:
        file.write(str(number ** 3) + "\n")

print("Cubes written successfully")
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

numbers.sort()

with open("sorted.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

print("Numbers sorted and written successfully")
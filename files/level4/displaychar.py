character = input("Enter a character: ")

with open("sample.txt", "r") as file:
    for line in file:
        if line.strip().startswith(character):
            print(line.strip())
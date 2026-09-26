word = input("Enter the word to search: ")

with open("sample.txt", "r") as file:
    for line in file:
        if word.lower() in line.lower():
            print(line.strip())
with open("sample.txt", "r") as file:
    data = file.read()

count = 0

for ch in data:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Number of consonants:", count)
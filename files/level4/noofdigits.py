with open("sample.txt", "r") as file:
    data = file.read()

count = 0

for ch in data:
    if ch.isdigit():
        count += 1

print("Number of digits:", count)
with open("sample.txt", "r") as file:
    data = file.read()

count = 0

for ch in data:
    if ch == " ":
        count += 1

print("Number of spaces:", count)
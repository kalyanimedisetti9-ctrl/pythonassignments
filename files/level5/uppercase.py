with open("sample.txt", "r") as file:
    data = file.read()

with open("uppercase.txt", "w") as file:
    file.write(data.upper())

print("Text converted to uppercase")
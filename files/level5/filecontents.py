with open("sample.txt", "r") as file:
    lines = file.readlines()

with open("reverse_order.txt", "w") as file:
    for line in reversed(lines):
        file.write(line)

print("File contents reversed successfully")
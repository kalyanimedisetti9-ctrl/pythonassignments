with open("sample.txt", "r") as file:
    lines = file.readlines()

with open("reverse_lines.txt", "w") as file:
    for line in lines:
        file.write(line.strip()[::-1] + "\n")

print("Each line reversed successfully")
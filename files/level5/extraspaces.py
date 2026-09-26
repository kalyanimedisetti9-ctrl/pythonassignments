with open("sample.txt", "r") as file:
    lines = file.readlines()

with open("clean.txt", "w") as file:
    for line in lines:
        line = " ".join(line.split())
        file.write(line + "\n")

print("Extra spaces removed successfully")
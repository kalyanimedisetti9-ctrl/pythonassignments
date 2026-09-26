import os

filename = "sample.txt"

if os.path.exists(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print("File does not exist")
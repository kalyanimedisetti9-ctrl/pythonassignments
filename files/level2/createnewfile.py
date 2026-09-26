import os

filename = "newfile.txt"

if not os.path.exists(filename):
    file = open(filename, "w")
    file.write("This is a new file")
    file.close()
    print("File created successfully")
else:
    print("File already exists")
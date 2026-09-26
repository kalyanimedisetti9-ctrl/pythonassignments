file = open("sample.txt", "w")

file.write("Old content has been replaced")
file.close()

print("File contents overwritten successfully")
file = open("sample.txt", "a")

file.write("\nThis is new content")
file.write("\nLearning file handling")

file.close()

print("Content appended successfully")
marks = {
    "Kalyani": 85,
    "Ravi": 78,
    "Anu": 92,
    "Suresh": 70
}

name = input("Enter student name: ")

if name in marks:
    print(name, "exists in the dictionary")
    print("Marks:", marks[name])
else:
    print(name, "does not exist")
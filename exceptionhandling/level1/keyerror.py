student = {
    "name": "Kalyani",
    "age": 18,
    "course": "Computer Engineering"
}

try:
    key = input("Enter key: ")
    print("Value:", student[key])

except KeyError:
    print("Error: Key does not exist")
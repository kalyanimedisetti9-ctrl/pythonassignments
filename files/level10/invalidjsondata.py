import json

try:
    with open("students.json", "r") as file:
        data = json.load(file)

    print("JSON data:")
    print(data)

except FileNotFoundError:
    print("Error: JSON file not found")

except json.JSONDecodeError:
    print("Error: Invalid JSON data")

except PermissionError:
    print("Error: Permission denied")
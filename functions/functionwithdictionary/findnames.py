def topper(marks):
    highest = 0
    topper_name = ""

    for name, mark in marks.items():
        if mark > highest:
            highest = mark
            topper_name = name

    return topper_name

students = {
    "Kalyani": 85,
    "Ravi": 92,
    "Sita": 88
}

print("Topper:", topper(students))
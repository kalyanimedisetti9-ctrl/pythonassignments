students = [
    ("Kalyani", 85),
    ("Ravi", 75),
    ("Sita", 90),
    ("Arjun", 70)
]

search_name = input("Enter student name: ")

found = False

for name, marks in students:
    if name.lower() == search_name.lower():
        print("Student Found")
        print("Name:", name)
        print("Marks:", marks)
        found = True
        break

if not found:
    print("Student Not Found")
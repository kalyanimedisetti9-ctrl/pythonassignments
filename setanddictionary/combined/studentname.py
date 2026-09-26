students = ["Kalyani", "Ravi", "Kalyani", "Sita", "Ravi", "Kalyani"]

count = {}

for student in students:
    if student in count:
        count[student] += 1
    else:
        count[student] = 1

print(count)
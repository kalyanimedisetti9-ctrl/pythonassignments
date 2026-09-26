with open("students.txt", "r") as file:
    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")
        total += int(data[4])
        count += 1

if count > 0:
    average = total / count
    print("Average marks:", average)
else:
    print("No student records found")
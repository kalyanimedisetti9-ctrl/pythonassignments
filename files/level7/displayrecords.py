with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        print("ID:", data[0])
        print("Name:", data[1])
        print("Age:", data[2])
        print("Course:", data[3])
        print("Marks:", data[4])
        print("--------------------")
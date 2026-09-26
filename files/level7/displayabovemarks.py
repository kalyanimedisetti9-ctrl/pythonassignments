with open("students.txt", "r") as file:
    print("Students who scored above 75:")

    for line in file:
        data = line.strip().split(",")

        if int(data[4]) > 75:
            print("ID:", data[0])
            print("Name:", data[1])
            print("Marks:", data[4])
            print("--------------------")
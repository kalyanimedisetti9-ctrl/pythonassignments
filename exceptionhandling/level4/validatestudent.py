try:
    attendance = float(input("Enter attendance percentage: "))

    if attendance < 75:
        raise ValueError("Attendance must be at least 75%")

    print("Student is eligible for examination")

except ValueError as e:
    print("Error:", e)
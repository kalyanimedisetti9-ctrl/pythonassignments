num = int(input("Enter a number: "))
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

if num >= lower and num <= upper:
    print("Number belongs to the range")
else:
    print("Number does not belong to the range")
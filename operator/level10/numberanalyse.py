num = int(input("Enter a number: "))

# Positive or Negative
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# Even or Odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Divisibility
if num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")

# Range
if num >= 10 and num <= 100:
    print("Number is between 10 and 100")
else:
    print("Number is outside the range")
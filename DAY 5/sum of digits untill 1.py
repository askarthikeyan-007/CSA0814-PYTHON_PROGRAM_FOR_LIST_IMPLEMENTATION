import math
num = int(input("Enter a number: "))
while num >= 10:
    num = sum(int(digit) for digit in str(num))
print(f"The single digit result is: {num}")
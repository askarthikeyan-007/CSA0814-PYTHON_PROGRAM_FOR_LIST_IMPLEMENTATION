import math
num = int(input("Enter a number: "))
sqrt_num = math.isqrt(num)
if sqrt_num * sqrt_num == num:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
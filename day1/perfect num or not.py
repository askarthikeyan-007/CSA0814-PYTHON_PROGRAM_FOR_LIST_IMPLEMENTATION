def is_perfect_number(num):
    return num == sum([i for i in range(1, num) if num % i == 0])
number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

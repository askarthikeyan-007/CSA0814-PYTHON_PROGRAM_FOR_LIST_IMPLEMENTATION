def is_composite(num):
    return any(num % i == 0 for i in range(2, num))
number = int(input("Enter a number: "))
if is_composite(number):
    print(f"{number} is a composite number.")
else:
    print(f"{number} is not a composite number.")

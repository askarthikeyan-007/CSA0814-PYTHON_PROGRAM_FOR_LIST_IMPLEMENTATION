num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
import sympy
num = int(input("Enter a number: "))
if num <= 1 or sympy.isprime(num):
    print(f"{num} is not a Smith number.")
else:
    sum_digits_num = sum(int(digit) for digit in str(num))
   factors = sympy.factorint(num)
    sum_digits_factors = sum(sum(int(digit) for digit in str(factor)) * count 
                             for factor, count in factors.items())
    if sum_digits_num == sum_digits_factors:
        print(f"{num} is a Smith number.")
    else:
        print(f"{num} is not a Smith number.")
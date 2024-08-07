from math import factorial
n = 5  
result = sum(factorial(i) / i for i in range(1, n+1))
print(result)

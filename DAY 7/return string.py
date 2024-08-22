import math

n = 3  

k = 5


result = math.comb(n + k - 1, k - 1)

print(f"The number of lexicographically sorted vowel strings of length {n} is: {result}")

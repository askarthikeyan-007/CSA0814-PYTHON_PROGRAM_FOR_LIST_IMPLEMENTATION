from math import comb

n = int(input("Enter the number of steps: "))

total_ways = 0
for k in range(n // 2 + 1):
    total_ways += comb(n - k, k)

print(f"Number of distinct ways to climb to the top: {total_ways}")

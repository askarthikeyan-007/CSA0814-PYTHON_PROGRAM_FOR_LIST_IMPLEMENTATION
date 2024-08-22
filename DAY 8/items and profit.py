import numpy as np

# Define the items with their weights and values
items = [
    (1, 2),  # (weight, value)
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (2, 2),
    (1, 1),
    (4, 7)
]
capacity = 5

# Extract weights and values from items
weights = [item[0] for item in items]
values = [item[1] for item in items]

# Number of items
n = len(items)

# Initialize the DP table
dp = np.zeros((n + 1, capacity + 1), dtype=int)

# Fill the DP table
for i in range(1, n + 1):
    for w in range(capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
        else:
            dp[i][w] = dp[i - 1][w]

# Backtrack to find the items included
result = []
w = capacity
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        result.append(items[i - 1])
        w -= weights[i - 1]

# Print the results
print(f"Items included for maximum profit:")
for item in result:
    print(f"Weight: {item[0]}, Value: {item[1]}")

print(f"Maximum profit: {dp[n][capacity]}")

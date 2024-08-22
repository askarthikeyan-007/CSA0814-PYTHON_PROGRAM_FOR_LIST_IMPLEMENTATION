def count_matches(s1, s2):
    return sum(x == y for x, y in zip(s1, s2))
s1 = "python"
s2 = "potion"
result = count_matches(s1, s2)
print(f"Number of matches: {result}")

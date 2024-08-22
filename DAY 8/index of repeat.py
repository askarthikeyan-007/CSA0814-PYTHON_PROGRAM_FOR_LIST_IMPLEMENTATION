from collections import Counter

s = input()
count = Counter(s)
first_index = min(i for i in range(len(s)) if count[s[i]] > 1)
sorted_s = ''.join(sorted(s))
print(f"Sorted String: {sorted_s}, First Repeating Index: {first_index}")
